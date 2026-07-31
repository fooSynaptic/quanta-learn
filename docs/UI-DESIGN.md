# Dashboard UI

Local panel for the four lists. Run `python3 dashboard/server.py` → http://127.0.0.1:8765/

## Goals

- Show reading backlog health (inbox / active / done)
- Surface tool and solved coverage
- Keep open problems visible without mixing them into solved archives

## Tabs

| Tab | Source |
|-----|--------|
| Reading | reading-list catalog |
| Problems | problem-list catalog |
| Solved | solved-list catalog |
| Tools | tool-list catalog |

`problem.status=solved` closes a todo; **solved-list** is the solution archive. Keep them separate; detail views may link `related.solved`.

## Stats

| Metric | Meaning |
|--------|---------|
| `reading_inbox` / `reading_active` / `reading_done` | reading backlog |
| `problem_open` / `problem_wip` | open work |
| `solved_count` | solved-list size |
| `tool_count` | tool-list size |

Built by `scripts/build_dashboard_stats.py`.

## Layout

```text
Header: Quanta Learn
Tabs: Reading | Problems | Solved | Tools
Main: filterable table / cards for the active tab
Detail: fields + related links
```

## Domains

Topic folders (for example `rlhf-book`) appear as paths under each list; the UI should treat them as ordinary catalog entries once indexed.

## Non-goals (v1)

- Editing catalogs in the browser
- Auth / multi-user
