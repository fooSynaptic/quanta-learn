---
name: auto-learn-agent
description: Personal learning agent for auto-learn. Search tool-list first, then solved-list, reading-list, and problem-list. Maintain Chrome reading imports and problem state transitions.
---

# Auto Learn Agent

Use this skill when working inside the `auto-learn` repository.

## Layout

- `tool-list/` — reusable tools (sorting, SVM, union-find, …)
- `legacy/` — historical one-off solutions (`legacy/Coding/`, …)
- `catalog/` — YAML indexes (Agent reads these first)

## Search order

1. `catalog/tool-list.yaml`
2. `catalog/solved-list.yaml`
3. `catalog/reading-list.yaml`
4. `catalog/problem-list.yaml`

## When user asks a new question

- Match reusable tools under `tool-list/` before one-off solutions in `legacy/`
- If still unresolved, add to problem-list with `status: open`

## Chrome pipeline

```bash
python3 scripts/import_chrome_sources.py
python3 scripts/classify_reading_items.py
python3 scripts/reading_to_problem.py
python3 scripts/sync_catalog_from_legacy.py
```

Never write to the Chrome profile.

## After solving

- Move problem to solved-list (often under `legacy/`)
- Propose tool-list entry if reusable
