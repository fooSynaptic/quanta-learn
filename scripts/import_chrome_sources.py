#!/usr/bin/env python3
"""Read Chrome bookmarks/history/sessions (read-only) and merge into reading-list."""

from __future__ import annotations

import json
import shutil
import sqlite3
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from _catalog_utils import (  # noqa: E402
    CATALOG_DIR,
    merge_by_key,
    load_yaml,
    save_yaml,
    slugify,
    today,
)

DEFAULT_CHROME_PROFILE = Path(
    "/mnt/c/Users/ordinar/AppData/Local/Google/Chrome/User Data/Default"
)
OUTPUT_DIR = ROOT / "reading-list" / "sources" / "chrome"
READING_CATALOG = CATALOG_DIR / "reading-list.yaml"


def copy_readonly(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def parse_bookmarks(node: dict[str, Any], folder_path: str = "") -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    name = node.get("name", "")
    current_path = f"{folder_path}/{name}".strip("/")

    if node.get("type") == "url" and node.get("url"):
        url = node["url"]
        item_id = f"read-{slugify(url)[:48]}"
        items.append(
            {
                "id": item_id,
                "title": name or url,
                "url": url,
                "status": "inbox",
                "source": "chrome-bookmark",
                "source_path": current_path,
                "captured_at": today(),
                "last_seen": today(),
                "category": "unknown",
                "tags": [part.lower() for part in current_path.split("/") if part][:5],
                "summary": "",
                "related": {"tools": [], "solved": [], "problems": []},
            }
        )

    for child in node.get("children", []) or []:
        items.extend(parse_bookmarks(child, current_path))

    return items


def load_bookmarks(profile: Path) -> list[dict[str, Any]]:
    bookmarks_file = profile / "Bookmarks"
    if not bookmarks_file.exists():
        print(f"Bookmarks not found: {bookmarks_file}")
        return []

    snapshot = OUTPUT_DIR / f"bookmarks-{today()}.json"
    copy_readonly(bookmarks_file, snapshot)

    data = json.loads(snapshot.read_text(encoding="utf-8"))
    roots = data.get("roots", {})
    items: list[dict[str, Any]] = []
    for root_name in ("bookmark_bar", "other", "synced"):
        root = roots.get(root_name)
        if root:
            items.extend(parse_bookmarks(root, root_name))
    return items


def load_history(profile: Path, limit: int = 200) -> list[dict[str, Any]]:
    history_file = profile / "History"
    if not history_file.exists():
        print(f"History not found: {history_file}")
        return []

    snapshot = OUTPUT_DIR / f"history-copy-{today()}.db"
    copy_readonly(history_file, snapshot)

    conn = sqlite3.connect(f"file:{snapshot}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    try:
        rows = conn.execute(
            """
            SELECT url, title, visit_count, last_visit_time
            FROM urls
            WHERE url LIKE 'http%'
            ORDER BY last_visit_time DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
    finally:
        conn.close()

    items: list[dict[str, Any]] = []
    for row in rows:
        url = row["url"]
        title = row["title"] or url
        item_id = f"read-{slugify(url)[:48]}"
        items.append(
            {
                "id": item_id,
                "title": title,
                "url": url,
                "status": "inbox",
                "source": "chrome-history",
                "source_path": "history",
                "captured_at": today(),
                "last_seen": today(),
                "category": "unknown",
                "tags": ["chrome-history"],
                "summary": "",
                "related": {"tools": [], "solved": [], "problems": []},
                "visit_count": row["visit_count"],
            }
        )
    return items


def load_sessions(profile: Path) -> list[dict[str, Any]]:
    sessions_dir = profile / "Sessions"
    if not sessions_dir.exists():
        print(f"Sessions not found: {sessions_dir}")
        return []

    items: list[dict[str, Any]] = []
    for session_file in sorted(sessions_dir.glob("Session_*"))[:3]:
        snapshot = OUTPUT_DIR / f"{session_file.name}-{today()}.bin"
        try:
            copy_readonly(session_file, snapshot)
        except OSError as exc:
            print(f"Skip session file (locked or unreadable): {session_file.name} ({exc})")
            continue
        raw = snapshot.read_bytes()
        # Session files are binary; extract http(s) URLs as lightweight signal.
        text = raw.decode("latin-1", errors="ignore")
        urls = sorted(set(part for part in text.split("\x00") if part.startswith("http")))
        for url in urls[:50]:
            item_id = f"read-{slugify(url)[:48]}"
            items.append(
                {
                    "id": item_id,
                    "title": url,
                    "url": url,
                    "status": "inbox",
                    "source": "chrome-session",
                    "source_path": session_file.name,
                    "captured_at": today(),
                    "last_seen": today(),
                    "category": "unknown",
                    "tags": ["chrome-session"],
                    "summary": "",
                    "related": {"tools": [], "solved": [], "problems": []},
                }
            )
    return items


def dedupe_by_url(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_url: dict[str, dict[str, Any]] = {}
    priority = {
        "chrome-bookmark": 3,
        "chrome-history": 2,
        "chrome-session": 1,
    }
    for item in items:
        url = item.get("url")
        if not url:
            continue
        existing = by_url.get(url)
        if not existing:
            by_url[url] = item
            continue
        if priority.get(item.get("source", ""), 0) > priority.get(existing.get("source", ""), 0):
            merged = {**existing, **item}
            merged["tags"] = sorted(set(existing.get("tags", []) + item.get("tags", [])))
            by_url[url] = merged
        else:
            existing["tags"] = sorted(set(existing.get("tags", []) + item.get("tags", [])))
            existing["last_seen"] = today()
    return sorted(by_url.values(), key=lambda x: x.get("title", ""))


def main() -> None:
    profile = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_CHROME_PROFILE
    if not profile.exists():
        raise SystemExit(f"Chrome profile not found: {profile}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    bookmark_items = load_bookmarks(profile)
    history_items = load_history(profile)
    session_items = load_sessions(profile)

    incoming = dedupe_by_url(bookmark_items + history_items + session_items)
    existing = load_yaml(READING_CATALOG)
    merged = merge_by_key(existing, incoming, "id")

    save_yaml(READING_CATALOG, merged)

    manifest = {
        "imported_at": datetime.now().isoformat(timespec="seconds"),
        "profile": str(profile),
        "counts": {
            "bookmarks": len(bookmark_items),
            "history": len(history_items),
            "sessions": len(session_items),
            "merged_unique": len(incoming),
            "catalog_total": len(merged),
        },
    }
    (OUTPUT_DIR / f"manifest-{today()}.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
