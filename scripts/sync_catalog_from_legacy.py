#!/usr/bin/env python3
"""Scan legacy/ and tool-list/ directories to rebuild solved-list and tool-list catalogs."""

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

# Solved one-off problem code lives under legacy/
SOLVED_SCAN_DIRS = [
    "legacy/Coding",
    "legacy/interviewProblem",
    "legacy/jianzhiOffer/problems",
    "legacy/DP",
    "legacy/recursion",
    "legacy/recursion/py_version",
    "legacy/trees",
    "legacy/searching",
    "legacy/steps",
    "legacy/num_reverse",
    "legacy/maxaverage",
    "legacy/max_container",
    "legacy/math",
    "legacy/order_Linklist",
    "legacy/recur_list",
    "legacy/rebptree",
]

CODE_EXTENSIONS = {".py", ".c", ".cpp"}

TOOL_DEFINITIONS = [
    {
        "id": "tool-smo-svm",
        "name": "SMOSVM",
        "kind": "library",
        "paths": ["tool-list/ml/svm/smo_svm.py"],
        "entry": "SMOSVM.fit / predict / decision_function",
        "tags": ["ml", "svm", "smo", "optimization"],
        "deps": ["numpy"],
        "doc": "tool-list/ml/svm/README.md",
        "related": {"reading": [], "solved": ["solved-smo-svm"]},
    },
    {
        "id": "tool-sorting-suite",
        "name": "SortingSuite",
        "kind": "library",
        "paths": [
            "tool-list/algorithms/sorting/main.py",
            "tool-list/algorithms/sorting/bubble_sort.py",
            "tool-list/algorithms/sorting/fast_sort.py",
            "tool-list/algorithms/sorting/heapSort.py",
            "tool-list/algorithms/sorting/insert_sort.py",
            "tool-list/algorithms/sorting/merge_sort.py",
            "tool-list/algorithms/sorting/select_sort.py",
        ],
        "entry": "tool-list/algorithms/sorting/main.py",
        "tags": ["sorting", "algorithm"],
        "deps": [],
        "doc": "tool-list/algorithms/sorting/main.py",
        "related": {"reading": [], "solved": []},
    },
    {
        "id": "tool-union-find",
        "name": "UnionFind",
        "kind": "library",
        "paths": [
            "tool-list/algorithms/cs-courses/AlgorithmsFourthEdith/unionFind.py"
        ],
        "entry": "UnionFind class",
        "tags": ["union-find", "graph", "disjoint-set"],
        "deps": [],
        "doc": "tool-list/algorithms/cs-courses/AlgorithmsFourthEdith/unionFind.py",
        "related": {"reading": [], "solved": []},
    },
    {
        "id": "tool-linked-list",
        "name": "MyLinkedList",
        "kind": "library",
        "paths": ["tool-list/algorithms/linked-list/MyLinkedList.py"],
        "entry": "MyLinkedList",
        "tags": ["linked-list", "data-structure"],
        "deps": [],
        "doc": "tool-list/algorithms/linked-list/MyLinkedList.py",
        "related": {"reading": [], "solved": []},
    },
    {
        "id": "tool-stack",
        "name": "LinkedStack",
        "kind": "library",
        "paths": [
            "tool-list/algorithms/cs-courses/AlgorithmsFourthEdith/LinkedStack.py",
            "tool-list/algorithms/cs-courses/AlgorithmsFourthEdith/reSizedArrayStack.py",
        ],
        "entry": "LinkedStack / ArrayStack",
        "tags": ["stack", "data-structure"],
        "deps": [],
        "doc": "tool-list/algorithms/cs-courses/AlgorithmsFourthEdith/LinkedStack.py",
        "related": {"reading": [], "solved": []},
    },
    {
        "id": "tool-heapsort-c",
        "name": "HeapSortC",
        "kind": "library",
        "paths": [
            "tool-list/algorithms/heapsort/heapmax.c",
            "tool-list/algorithms/heapsort/arrtoheap.c",
            "tool-list/algorithms/heapsort/inittree.c",
        ],
        "entry": "heap C implementations",
        "tags": ["heap", "sorting", "c"],
        "deps": [],
        "doc": "tool-list/algorithms/heapsort/",
        "related": {"reading": [], "solved": []},
    },
    {
        "id": "tool-greedy-c",
        "name": "GreedyC",
        "kind": "library",
        "paths": ["tool-list/algorithms/greedy/greedy.c"],
        "entry": "greedy.c",
        "tags": ["greedy", "c"],
        "deps": [],
        "doc": "tool-list/algorithms/greedy/greedy.c",
        "related": {"reading": [], "solved": []},
    },
]


def source_from_path(rel: str) -> str:
    if rel.startswith("legacy/Coding/"):
        return "leetcode"
    if rel.startswith("legacy/interviewProblem/"):
        return "company"
    if rel.startswith("legacy/jianzhiOffer/"):
        return "offer"
    if "tool-list/ml/" in rel:
        return "ml"
    if "tool-list/algorithms/" in rel:
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

    # Full replace for solved paths after directory migration
    save_yaml(solved_path, solved_items)
    tool_items = merge_by_key(load_yaml(tool_path), tool_items, "id")
    save_yaml(tool_path, tool_items)

    print(f"Wrote {len(solved_items)} solved entries -> {solved_path}")
    print(f"Wrote {len(tool_items)} tool entries -> {tool_path}")


if __name__ == "__main__":
    main()
