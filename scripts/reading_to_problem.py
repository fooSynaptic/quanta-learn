#!/usr/bin/env python3
"""Convert classified reading items into problem-list entries."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from _catalog_utils import (  # noqa: E402
    CATALOG_DIR,
    load_yaml,
    merge_by_key,
    save_yaml,
    slugify,
    today,
)

READING_CATALOG = CATALOG_DIR / "reading-list.yaml"
PROBLEM_CATALOG = CATALOG_DIR / "problem-list.yaml"

KIND_TO_DIR = {
    "algorithm": "algorithm",
    "debug": "debug",
    "system-design": "system-design",
}

PROBLEM_CATEGORIES = {"algorithm", "debug", "system-design"}


def problem_id_for_reading(item: dict) -> str:
    return f"prob-chrome-{slugify(item.get('title') or item.get('url', 'item'))[:40]}"


def write_problem_markdown(problem: dict) -> Path:
    kind = problem.get("kind", "algorithm")
    subdir = KIND_TO_DIR.get(kind, "generated-from-reading")
    rel_dir = ROOT / "problem-list" / subdir
    rel_dir.mkdir(parents=True, exist_ok=True)
    path = rel_dir / f"{problem['id']}.md"
    if path.exists():
        return path

    content = f"""---
id: {problem['id']}
kind: {kind}
source: chrome
status: open
created_at: {problem.get('created_at', today())}
---

# {problem['title']}

- Source URL: {problem.get('source_ref', '')}
- Origin: {problem.get('notes', '')}

## Goal

Turn this reading item into an actionable learning task.

## Next Steps

- [ ] Read and summarize the source
- [ ] Search tool-list for reusable helpers
- [ ] Search solved-list for similar patterns
- [ ] Implement or document the solution
"""
    path.write_text(content, encoding="utf-8")
    return path


def reading_to_problem(item: dict) -> dict | None:
    category = item.get("category", "unknown")
    if category not in PROBLEM_CATEGORIES:
        return None

    problem_id = problem_id_for_reading(item)
    return {
        "id": problem_id,
        "title": item.get("title", problem_id),
        "kind": category,
        "source": "chrome",
        "source_ref": item.get("url", ""),
        "status": "open",
        "priority": "medium",
        "tags": sorted(set(item.get("tags", []) + [category, "chrome-import"])),
        "created_at": today(),
        "updated_at": today(),
        "notes": f"Auto-generated from reading item {item.get('id')} ({item.get('source')})",
        "related": {
            "reading": [item.get("id", "")],
            "tools": [],
            "solved_similar": [],
        },
    }


def main() -> None:
    reading_items = load_yaml(READING_CATALOG)
    existing_problems = load_yaml(PROBLEM_CATALOG)

    generated: list[dict] = []
    for item in reading_items:
        problem = reading_to_problem(item)
        if not problem:
            continue
        path = write_problem_markdown(problem)
        problem["path"] = path.relative_to(ROOT).as_posix()
        generated.append(problem)

        rel = item.setdefault("related", {})
        probs = set(rel.get("problems", []))
        probs.add(problem["id"])
        rel["problems"] = sorted(probs)
        item["updated_at"] = today()

    merged_problems = merge_by_key(existing_problems, generated, "id")
    save_yaml(PROBLEM_CATALOG, merged_problems)
    save_yaml(READING_CATALOG, reading_items)

    print(f"Generated {len(generated)} problems -> {PROBLEM_CATALOG}")
    print(f"Catalog total problems: {len(merged_problems)}")


if __name__ == "__main__":
    main()
