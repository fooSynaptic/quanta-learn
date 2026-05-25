---
name: auto-learn-agent
description: Accelerate reading-list digestion for quanta-learn. Auto-import learning materials, match tool-list and solved-list using reading metrics, convert actionable items to problems, and maintain related cross-references.
---

# Quanta Learn Agent

Primary goal: **digest the reading-list backlog**, not only answer one-off questions.

## Default workflow (reading digestion)

1. List `<CATALOG_READING>` items with `status: inbox` or `active`.
2. Match `<CATALOG_TOOL>` then `<CATALOG_SOLVED>` using tags, category, title, topics.
3. If sufficient → set `related`, `status: done`, optional `summary`.
4. If needs work and category is algorithm/debug/system-design → ensure problem exists (`reading_to_problem.py`), solve, then update solved/tool and `related`.

## Secondary workflow (new question)

Search order: tool-list → solved-list → reading-list → problem-list.

## Ingest pipeline

```bash
export CHROME_USER_DATA_DIR="<your-browser-profile-dir>"
python3 scripts/import_chrome_sources.py
python3 scripts/classify_reading_items.py
python3 scripts/reading_to_problem.py
python3 scripts/sync_catalog_from_legacy.py
```

Never write to the browser profile. Do not commit local catalog YAML or reading snapshots.

## After solving

- Update reading `related.solved` / `related.tools`
- Add or refresh solved-list; propose tool-list if reusable
