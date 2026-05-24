#!/usr/bin/env python3
"""Scan legacy code directories and build solved-list / tool-list catalogs."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from _catalog_utils import (  # noqa: E402
    CATALOG_DIR,
    ROOT,
    infer_language,
    infer_topics_from_name,
    load_yaml,
    merge_by_key,
    save_yaml,
    slugify,
    today,
)

SOLVED_SCAN_DIRS = [
    "Coding",
    "interviewProblem",
    "jianzhiOffer/problems",
    "Sorting",
    "DP",
    "machine_learning",
    "csCourses",
    "recursion",
    "recursion/py_version",
    "linklist",
    "trees",
    "searching",
    "greedy",
    "heapsort",
    "fastsort",
    "datastruct",
    "cppGround",
    "steps",
    "num_reverse",
    "maxaverage",
    "max_container",
    "math",
    "order_Linklist",
    "recur_list",
    "rebptree",
]

CODE_EXTENSIONS = {".py", ".c", ".cpp"}

TOOL_DEFINITIONS = [
    {
        "id": "tool-smo-svm",
        "name": "SMOSVM",
        "kind": "library",
        "paths": ["machine_learning/svm/smo_svm.py"],
        "entry": "SMOSVM.fit / predict / decision_function",
        "tags": ["ml", "svm", "smo", "optimization"],
        "deps": ["numpy"],
        "doc": "machine_learning/svm/README.md",
        "related": {"reading": [], "solved": ["solved-smo-svm"]},
    },
    {
        "id": "tool-sorting-suite",
        "name": "SortingSuite",
        "kind": "library",
        "paths": [
            "Sorting/main.py",
            "Sorting/bubble_sort.py",
            "Sorting/fast_sort.py",
            "Sorting/heapSort.py",
            "Sorting/insert_sort.py",
            "Sorting/merge_sort.py",
            "Sorting/select_sort.py",
        ],
        "entry": "Sorting/main.py",
        "tags": ["sorting", "algorithm"],
        "deps": [],
        "doc": "Sorting/main.py",
        "related": {"reading": [], "solved": []},
    },
    {
        "id": "tool-union-find",
        "name": "UnionFind",
        "kind": "library",
        "paths": ["csCourses/AlgorithmsFourthEdith/unionFind.py"],
        "entry": "UnionFind class",
        "tags": ["union-find", "graph", "disjoint-set"],
        "deps": [],
        "doc": "csCourses/AlgorithmsFourthEdith/unionFind.py",
        "related": {"reading": [], "solved": []},
    },
    {
        "id": "tool-linked-list",
        "name": "MyLinkedList",
        "kind": "library",
        "paths": ["linklist/MyLinkedList.py"],
        "entry": "MyLinkedList",
        "tags": ["linked-list", "data-structure"],
        "deps": [],
        "doc": "linklist/MyLinkedList.py",
        "related": {"reading": [], "solved": []},
    },
    {
        "id": "tool-stack",
        "name": "LinkedStack",
        "kind": "library",
        "paths": [
            "csCourses/AlgorithmsFourthEdith/LinkedStack.py",
            "csCourses/AlgorithmsFourthEdith/reSizedArrayStack.py",
        ],
        "entry": "LinkedStack / ArrayStack",
        "tags": ["stack", "data-structure"],
        "deps": [],
        "doc": "csCourses/AlgorithmsFourthEdith/LinkedStack.py",
        "related": {"reading": [], "solved": []},
    },
]


def source_from_path(rel: str) -> str:
    if rel.startswith("Coding/"):
        return "leetcode"
    if rel.startswith("interviewProblem/"):
        return "company"
    if rel.startswith("jianzhiOffer/"):
        return "offer"
    if rel.startswith("machine_learning/"):
        return "ml"
    if rel.startswith("csCourses/"):
        return "course"
    if rel.startswith("Sorting/"):
        return "algorithm"
    return "legacy"


def title_from_stem(stem: str) -> str:
    return stem.replace("_", " ").replace("-", " ").strip().title()


def build_solved_items() -> list[dict]:
    by_stem: dict[str, dict] = {}

    for rel_dir in SOLVED_SCAN_DIRS:
        base = ROOT / rel_dir
        if not base.exists():
            continue
        for path in sorted(base.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in CODE_EXTENSIONS:
                continue
            rel = path.relative_to(ROOT).as_posix()
            stem = path.stem
            item_id = f"solved-{slugify(stem)}"
            topics = infer_topics_from_name(stem)
            entry = {
                "id": item_id,
                "title": title_from_stem(stem),
                "paths": [rel],
                "language": infer_language(path),
                "topics": topics,
                "source": source_from_path(rel),
                "quality": "runnable",
                "summary": "",
                "variants": [],
                "related": {"tools": [], "reading": []},
                "created_at": today(),
                "updated_at": today(),
            }
            if stem in by_stem:
                by_stem[stem]["paths"].append(rel)
                by_stem[stem]["variants"] = sorted(set(by_stem[stem]["paths"][1:]))
                by_stem[stem]["topics"] = sorted(set(by_stem[stem]["topics"] + topics))
            else:
                by_stem[stem] = entry

    return sorted(by_stem.values(), key=lambda x: x["id"])


def build_tool_items() -> list[dict]:
    items = []
    for tool in TOOL_DEFINITIONS:
        item = dict(tool)
        item.setdefault("created_at", today())
        item.setdefault("updated_at", today())
        items.append(item)
    return items


def main() -> None:
    solved_path = CATALOG_DIR / "solved-list.yaml"
    tool_path = CATALOG_DIR / "tool-list.yaml"

    solved_items = build_solved_items()
    tool_items = build_tool_items()

    solved_items = merge_by_key(load_yaml(solved_path), solved_items, "id")
    tool_items = merge_by_key(load_yaml(tool_path), tool_items, "id")

    save_yaml(solved_path, solved_items)
    save_yaml(tool_path, tool_items)

    print(f"Wrote {len(solved_items)} solved entries -> {solved_path}")
    print(f"Wrote {len(tool_items)} tool entries -> {tool_path}")


if __name__ == "__main__":
    main()
