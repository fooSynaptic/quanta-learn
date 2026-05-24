---
name: auto-learn-agent
description: Personal learning agent for auto-learn. Search tool-list first, then solved-list, reading-list, and problem-list. Maintain Chrome reading imports and problem state transitions.
---

# Auto Learn Agent

Use this skill when working inside the `auto-learn` repository.

## Search order

1. `catalog/tool-list.yaml`
2. `catalog/solved-list.yaml`
3. `catalog/reading-list.yaml`
4. `catalog/problem-list.yaml`

## When user asks a new question

- Match reusable tools before one-off solutions
- If no tool fits, search solved-list for similar patterns
- If concept gap exists, search reading-list
- If still unresolved, add to problem-list with `status: open`

## Chrome pipeline

Run in order when refreshing browser memory:

```bash
python3 scripts/import_chrome_sources.py
python3 scripts/classify_reading_items.py
python3 scripts/reading_to_problem.py
```

Never write to the Chrome profile; only read/copy into `reading-list/sources/chrome/`.

## Problem kinds

- algorithm
- debug
- system-design
- reading-derived

## After solving

- Move problem to solved-list
- Link related reading/tools
- Propose tool-list entry if reusable
