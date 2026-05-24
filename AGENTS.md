# Auto Learn Agent Guide

本仓库是个人学习 Agent 的知识索引项目。遇到问题时，按以下顺序检索。

## 仓库路径

- **WSL**：`/mnt/d/code/gitreps/auto_learn`（请用此路径打开工作区）
- **Windows**：`D:\code\gitreps\auto-learn`（联接，与上为同一仓库）
- 远程仓库：`https://github.com/fooSynaptic/auto-learn.git`
- 旧目录 `exam` 已删除；题解在 `legacy/`，工具在 `tool-list/`

## 四清单

| 清单 | 路径 | 用途 |
|------|------|------|
| tool-list | `catalog/tool-list.yaml` | 可复用工具、模板、库 |
| solved-list | `catalog/solved-list.yaml` | 已有题解与实现 |
| reading-list | `catalog/reading-list.yaml` | 阅读记忆（含 Chrome 导入） |
| problem-list | `catalog/problem-list.yaml` | 待解决问题 backlog |

## 检索协议

1. **tool-list**：按 tags、name、entry 匹配可复用方案
2. **solved-list**：按 title、topics、summary 匹配历史解法
3. **reading-list**：补概念、找来源文档
4. **problem-list**：仍无法解决则创建/更新 `status: open`

## problem 类型

- `algorithm` — 算法与数据结构
- `debug` — 调试与报错
- `system-design` — 系统设计与架构
- `reading-derived` — 从 Chrome 阅读自动转化

## Chrome 索引维护

```bash
# 从 Chrome Profile 导入书签/历史/会话（只读）
python3 scripts/import_chrome_sources.py

# 分类 reading 条目
python3 scripts/classify_reading_items.py

# 将 algorithm/debug/system-design 类 reading 转为 problem
python3 scripts/reading_to_problem.py

# 从 legacy 代码扫描 solved/tool 索引
python3 scripts/sync_catalog_from_legacy.py
```

默认 Chrome Profile：

`/mnt/c/Users/ordinar/AppData/Local/Google/Chrome/User Data/Default`

## 状态流转

```
problem open → wip → solved（写入 solved-list，移出 problem-list）
                      ↘ 可泛化 → tool-list
reading inbox → active → done/archived
```

## Agent 约束

- 优先读 `catalog/*.yaml`，不要全仓库盲目 grep
- 不修改 Chrome 原始 Profile 文件
- 自动生成的问题保留 `source: chrome` 和原 URL
- 解决后更新 `related` 交叉引用
