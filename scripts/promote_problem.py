#!/usr/bin/env python3
"""Promote a problem-list entry to solved-list after resolution."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from _catalog_utils import CATALOG_DIR, load_yaml, save_yaml, slugify, today  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Promote problem to solved-list")
    parser.add_argument("problem_id", help="Problem id, e.g. prob-chrome-...")
    parser.add_argument("solution_path", help="Relative path to solution file")
    parser.add_argument("--title", default="", help="Optional solved title")
    args = parser.parse_args()

    problems = load_yaml(CATALOG_DIR / "problem-list.yaml")
    solved = load_yaml(CATALOG_DIR / "solved-list.yaml")

    problem = next((p for p in problems if p.get("id") == args.problem_id), None)
    if not problem:
        raise SystemExit(f"Problem not found: {args.problem_id}")

    stem = Path(args.solution_path).stem
    solved_id = f"solved-{slugify(stem)}"
    solved_entry = {
        "id": solved_id,
        "title": args.title or problem.get("title", solved_id),
        "paths": [args.solution_path],
        "language": Path(args.solution_path).suffix.lstrip("."),
        "topics": problem.get("tags", []),
        "source": problem.get("source", "manual"),
        "quality": "runnable",
        "summary": problem.get("notes", ""),
        "variants": [],
        "related": {
            "tools": problem.get("related", {}).get("tools", []),
            "reading": problem.get("related", {}).get("reading", []),
        },
        "created_at": today(),
        "updated_at": today(),
    }

    solved.append(solved_entry)
    problems = [p for p in problems if p.get("id") != args.problem_id]

    save_yaml(CATALOG_DIR / "solved-list.yaml", sorted(solved, key=lambda x: x["id"]))
    save_yaml(CATALOG_DIR / "problem-list.yaml", problems)

    print(f"Promoted {args.problem_id} -> {solved_id}")


if __name__ == "__main__":
    main()
