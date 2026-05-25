#!/usr/bin/env python3
"""Aggregate catalog YAML into dashboard/stats.json and queues.json."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from _catalog_utils import CATALOG_DIR, load_yaml  # noqa: E402

DASHBOARD_DIR = ROOT / "dashboard"
READING_PATH = CATALOG_DIR / "reading-list.yaml"
PROBLEM_PATH = CATALOG_DIR / "problem-list.yaml"
SOLVED_PATH = CATALOG_DIR / "solved-list.yaml"
TOOL_PATH = CATALOG_DIR / "tool-list.yaml"

READING_PENDING = {"inbox", "active"}
READING_DONE = {"done", "archived"}
PROBLEM_OPEN = {"open", "wip", "blocked", "deferred"}


def _has_match(item: dict[str, Any]) -> bool:
    rel = item.get("related") or {}
    return bool(rel.get("tools") or rel.get("solved"))


def _short_path(source_path: str, max_len: int = 48) -> str:
    if not source_path:
        return ""
    parts = [p for p in source_path.split("/") if p and p not in ("bookmark_bar", "书签栏", "other", "其他书签")]
    text = " / ".join(parts[-3:]) if parts else source_path
    return text if len(text) <= max_len else "…" + text[-(max_len - 1) :]


def _summarize_reading(item: dict[str, Any]) -> dict[str, Any]:
    url = item.get("url") or ""
    domain = ""
    if url.startswith("http"):
        domain = urlparse(url).netloc or ""
    rel = item.get("related") or {}
    path_short = _short_path(item.get("source_path", ""))
    url_display = url
    if len(url_display) > 72:
        url_display = url_display[:69] + "…"
    return {
        "id": item.get("id", ""),
        "title": item.get("title", "") or "(无标题)",
        "status": item.get("status", "inbox"),
        "category": item.get("category", "unknown"),
        "source": item.get("source", ""),
        "domain": domain,
        "url_preview": url_display,
        "path_short": path_short,
        "has_tool_match": bool(rel.get("tools")),
        "has_solved_match": bool(rel.get("solved")),
        "updated_at": item.get("updated_at", ""),
        "last_seen": item.get("last_seen", ""),
    }


def _summarize_problem(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": item.get("id", ""),
        "title": item.get("title", ""),
        "status": item.get("status", "open"),
        "kind": item.get("kind", ""),
        "source": item.get("source", ""),
        "priority": item.get("priority", "medium"),
        "updated_at": item.get("updated_at", ""),
    }


def _summarize_solved(item: dict[str, Any]) -> dict[str, Any]:
    paths = item.get("paths") or []
    path_preview = paths[0] if paths else ""
    return {
        "id": item.get("id", ""),
        "title": item.get("title", ""),
        "topics": item.get("topics", []),
        "language": item.get("language", ""),
        "quality": item.get("quality", ""),
        "source": item.get("source", ""),
        "summary": (item.get("summary") or "")[:200],
        "path_preview": path_preview,
        "path_count": len(paths),
        "updated_at": item.get("updated_at", ""),
    }


def compute_stats(
    reading: list[dict[str, Any]],
    problems: list[dict[str, Any]],
    solved: list[dict[str, Any]],
    tools: list[dict[str, Any]],
) -> dict[str, Any]:
    r_total = len(reading)
    r_done = sum(1 for i in reading if i.get("status") in READING_DONE)
    r_pending = sum(1 for i in reading if i.get("status") in READING_PENDING)
    r_matched = sum(1 for i in reading if i.get("status") in READING_DONE and _has_match(i))

    p_total = len(problems)
    p_solved = sum(1 for i in problems if i.get("status") == "solved")
    p_open = sum(1 for i in problems if i.get("status") in PROBLEM_OPEN)

    by_category: dict[str, int] = {}
    for i in reading:
        c = i.get("category") or "unknown"
        by_category[c] = by_category.get(c, 0) + 1

    return {
        "reading_total": r_total,
        "reading_pending": r_pending,
        "reading_done": r_done,
        "reading_digest_rate": round(r_done / r_total, 4) if r_total else 0,
        "reading_matched": r_matched,
        "reading_match_rate": round(r_matched / r_done, 4) if r_done else 0,
        "reading_by_category": by_category,
        "problem_total": p_total,
        "problem_open": p_open,
        "problem_solved": p_solved,
        "problem_resolve_rate": round(p_solved / p_total, 4) if p_total else 0,
        "solved_count": len(solved),
        "tool_count": len(tools),
    }


def build_reading_queues(reading: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    buckets: dict[str, list[dict[str, Any]]] = {
        "inbox": [],
        "active": [],
        "done": [],
        "archived": [],
    }
    for item in reading:
        st = item.get("status", "inbox")
        if st not in buckets:
            st = "inbox"
        buckets[st].append(_summarize_reading(item))

    def sort_inbox(x: dict[str, Any]) -> str:
        return x.get("last_seen") or x.get("updated_at") or ""

    def sort_other(x: dict[str, Any]) -> str:
        return x.get("updated_at") or ""

    buckets["inbox"].sort(key=sort_inbox, reverse=True)
    for k in ("active", "done", "archived"):
        buckets[k].sort(key=sort_other, reverse=True)
    return buckets


def build_problem_queues(problems: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    open_items = []
    solved_items = []
    for item in problems:
        s = _summarize_problem(item)
        if item.get("status") == "solved":
            solved_items.append(s)
        else:
            open_items.append(s)
    open_items.sort(key=lambda x: x.get("updated_at", ""), reverse=True)
    solved_items.sort(key=lambda x: x.get("updated_at", ""), reverse=True)
    return {"open": open_items, "solved": solved_items}


def main() -> None:
    reading = load_yaml(READING_PATH)
    problems = load_yaml(PROBLEM_PATH)
    solved = load_yaml(SOLVED_PATH)
    tools = load_yaml(TOOL_PATH)

    stats = compute_stats(reading, problems, solved, tools)
    payload = {
        "stats": stats,
        "reading_queues": build_reading_queues(reading),
        "problem_queues": build_problem_queues(problems),
        "solved_list": [_summarize_solved(i) for i in solved],
    }

    DASHBOARD_DIR.mkdir(parents=True, exist_ok=True)
    out = DASHBOARD_DIR / "data.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(stats, ensure_ascii=False, indent=2))
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
