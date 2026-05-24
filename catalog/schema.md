# Catalog Schema

统一索引字段定义，供 Agent 与维护脚本使用。

## 通用字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | string | 全局唯一，前缀见下 |
| `title` | string | 人类可读标题 |
| `tags` | string[] | 检索标签 |
| `created_at` | date | 创建日期 YYYY-MM-DD |
| `updated_at` | date | 最近更新 |
| `related` | object | 交叉引用 |

## ID 前缀

- `read-*` — reading-list
- `prob-*` — problem-list
- `solved-*` — solved-list
- `tool-*` — tool-list

## reading-list

```yaml
- id: read-example
  title: "文章标题"
  url: "https://..."
  status: inbox | active | done | archived
  source: chrome-bookmark | chrome-history | chrome-session | manual
  source_path: ""           # Chrome 文件夹路径或 session 来源
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
  title: "问题标题"
  kind: algorithm | debug | system-design | reading-derived
  source: chrome | leetcode | offer | company | manual
  source_ref: ""            # URL 或题号
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
  title: "题目标题"
  paths:
    - Coding/example.py
  language: python | c | cpp
  topics: []
  source: leetcode | offer | company to | course | ml
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
