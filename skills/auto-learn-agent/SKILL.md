---
name: auto-learn-agent
description: Accelerate reading-list digestion for quanta-learn. Ingest Lark/Chrome sources, tag and redact Chrome items, match tool-list and solved-list, park short-term blockers in problem-list, and maintain related cross-references.
---

# Quanta Learn Agent

Primary goal: **run the long-horizon learning loop**, not only answer one-off questions.

Canonical flow: [docs/images/learning-core-flow.svg](../../docs/images/learning-core-flow.svg).

## Default workflow (reading digestion)

1. List `<CATALOG_READING>` items with `status: inbox` or `active`.
2. Match `<CATALOG_TOOL>` then `<CATALOG_SOLVED>` using tags, category, title, topics.
3. If sufficient → set `related`, `status: done`, optional `summary`.
4. If reusable → propose / refresh solved and tool entries.
5. If blocked soon → ensure a problem exists with `blocked` / `deferred` and link `related`.

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
Chrome ingest must redact secrets/home paths and honor the local blocklist.

## After solving

- Update reading `related.solved` / `related.tools`
- Add or refresh solved-list; propose tool-list if reusable
