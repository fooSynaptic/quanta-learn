#!/usr/bin/env python3
"""Classify reading-list items into reading/algorithm/debug/system-design."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from _catalog_utils import CATALOG_DIR, load_yaml, save_yaml, today  # noqa: E402

READING_CATALOG = CATALOG_DIR / "reading-list.yaml"

RULES: list[tuple[str, list[str]]] = [
    (
        "algorithm",
        [
            r"leetcode",
            r"lintcode",
            r"nowcoder",
            r"algorithm",
            r"dynamic.?program",
            r"graph",
            r"tree",
            r"sort",
            r"binary.?search",
            r"剑指",
            r"刷题",
        ],
    ),
    (
        "debug",
        [
            r"debug",
            r"stack.?overflow",
            r"error",
            r"exception",
            r"traceback",
            r"bug",
            r"issue",
            r"github\.com/.+/issues",
            r"segmentation fault",
            r"内存泄漏",
            r"调试",
        ],
    ),
    (
        "system-design",
        [
            r"system.?design",
            r"architecture",
            r"distributed",
            r"microservice",
            r"scalability",
            r"cap theorem",
            r"raft",
            r"kafka",
            r"redis",
            r"负载均衡",
            r"系统设计",
            r"高并发",
            r"数据库",
        ],
    ),
    (
        "reading",
        [
            r"blog",
            r"medium",
            r"arxiv",
            r"paper",
            r"course",
            r"tutorial",
            r"docs?",
            r"wiki",
            r"阅读",
            r"笔记",
            r"教程",
        ],
    ),
]


def classify_text(text: str) -> str:
    text = text.lower()
    scores = {name: 0 for name, _ in RULES}
    for name, patterns in RULES:
        for pattern in patterns:
            if re.search(pattern, text, re.IGNORECASE):
                scores[name] += 1
    best = max(scores.items(), key=lambda kv: kv[1])
    if best[1] == 0:
        return "unknown"
    return best[0]


def classify_item(item: dict) -> str:
    haystack = " ".join(
        [
            item.get("title", ""),
            item.get("url", ""),
            item.get("source_path", ""),
            " ".join(item.get("tags", [])),
        ]
    )
    return classify_text(haystack)


def main() -> None:
    items = load_yaml(READING_CATALOG)
    changed = 0
    for item in items:
        category = classify_item(item)
        if item.get("category") != category:
            item["category"] = category
            item["updated_at"] = today()
            changed += 1
        if category != "reading" and category != "unknown":
            tags = set(item.get("tags", []))
            tags.add(category)
            item["tags"] = sorted(tags)

    save_yaml(READING_CATALOG, items)
    print(f"Classified {len(items)} reading items ({changed} updated)")


if __name__ == "__main__":
    main()
