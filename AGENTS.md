# Quanta Learn — Agent 指南

默认任务：**消化 reading-list backlog** — 自动取材后的学习材料在 `<CATALOG_READING>` 中；用 **tool-list**、**solved-list** 与 reading 上的**指标**匹配复用，必要时转入 problem-list。设计见 [DESIGN.md](DESIGN.md)。

## 四清单

| 清单 | 占位符 | Agent 怎么用 |
|------|--------|----------------|
| reading-list | `<CATALOG_READING>` | **主队列**：按 `status`、`category`、`last_seen` 决定下一篇；消化后更新 `related`、`summary` |
| tool-list | `<CATALOG_TOOL>` | 消化/解题时**先**按 tags、name、entry 匹配 |
| solved-list | `<CATALOG_SOLVED>` | **再**按 topics、summary 匹配 |
| problem-list | `<CATALOG_PROBLEM>` | reading 无法仅靠复用解决时创建或推进 `wip` |

初始化：`bash scripts/init_local_catalog.sh`。字段见 [catalog/schema.md](catalog/schema.md)。

## 消化 reading（优先）

![阅读消化闭环](docs/images/reading-digestion-loop.svg)

1. 筛选 `status: inbox` 或 `active` 的条目。
2. 用 `tags`、`category`、`title`、`url` 检索 `<CATALOG_TOOL>`、`<CATALOG_SOLVED>`。
3. **命中且足够** → 填写 `related.tools` / `related.solved`，`status: done`（或 `archived`），可选 `summary`。
4. **需动手** 且 `category` 为 algorithm / debug / system-design → 确保存在对应 problem（可提示用户跑 `reading_to_problem.py`），解题后回写 related。
5. 解决后：写入 solved；可复用则登记 tool — 便于同主题 reading 下次直接命中。

## 解答新问题（用户直接提问时）

![检索顺序](docs/images/agent-resolve-workflow.svg)

tool-list → solved-list → reading-list（补材料来源）→ problem-list（`open`）

## reading 指标速查

| 字段 | 用途 |
|------|------|
| `status` | inbox / active / done / archived |
| `category` | classify 结果；决定是否转 problem |
| `tags` | 与 tool/solved 对齐 |
| `related.*` | 命中后必维护，避免重复劳动 |
| `last_seen` | 可优先处理近期再次访问的 URL |

## 维护流水线

```bash
export CHROME_USER_DATA_DIR="<your-browser-profile-dir>"
python3 scripts/import_chrome_sources.py
python3 scripts/classify_reading_items.py
python3 scripts/reading_to_problem.py
python3 scripts/sync_catalog_from_legacy.py
```

## 状态流转

![状态流转](docs/images/status-transitions.svg)

## 约束

- 读本地 `catalog/*.yaml`；公开仓仅有 `*.yaml.example`
- 不提交 catalog 实文件、阅读快照、自动 problem 正文
- **Git 提交**：禁止 `Co-authored-by: Cursor` 及任何 AI/Bot 共同作者（`.cursor/rules/no-co-author-in-commits.mdc`）
- 只读浏览器 Profile；保留 `source` 与 URL
- Skill：`skills/auto-learn-agent/SKILL.md`
