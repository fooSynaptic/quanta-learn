# Catalog Schema

Fields shared by Agent workflows and maintenance scripts.

## Common

| Field | Type | Notes |
|-------|------|-------|
| `id` | string | unique; prefixes below |
| `title` | string | display title |
| `tags` | string[] | search tags |
| `created_at` | date | YYYY-MM-DD |
| `updated_at` | date | last update |
| `related` | object | cross refs |

## ID prefixes

- `read-*` — reading-list
- `prob-*` — problem-list
- `solved-*` — solved-list
- `tool-*` — tool-list

## reading-list

```yaml
- id: read-example
  title: "Title"
  url: "https://..."
  status: inbox | active | done | archived
  source: chrome-bookmark | chrome-history | chrome-session | manual
  source_path: ""
  captured_at: 2026-05-24
  last_seen: 2026-05-24
  category: reading | algorithm | debug | system-design | unknown
  summary: ""
  related:
    tools: []
    solved: []
    problems: []
```

## problem-list

```yaml
- id: prob-example
  title: "Title"
  kind: algorithm | debug | system-design | reading-derived
  source: chrome | leetcode | offer | company | manual
  source_ref: ""
  status: open | wip | blocked | deferred | solved
  priority: low | medium | high
  tags: []
  created_at: 2026-05-24
  notes: ""
  related:
    reading: []
    tools: []
    solved_similar: []
  path: problem-list/algorithm/example.md
```

## solved-list

```yaml
- id: solved-example
  title: "Title"
  paths:
    - Coding/example.py
  language: python | c | cpp
  topics: []
  source: leetcode | offer | company | course | ml
  quality: draft | runnable | reviewed
  summary: ""
  variants: []
  related:
    tools: []
    reading: []
```

## tool-list

```yaml
- id: tool-example
  name: ToolName
  kind: library | cli | template
  paths: []
  entry: "Class.method"
  tags: []
  deps: []
  doc: ""
  related:
    reading: []
    solved: []
```
