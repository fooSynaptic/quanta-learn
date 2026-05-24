# Auto Learn

个人学习 Agent 项目：用四清单索引题解、工具、阅读记忆与待解决问题。

## 目录位置

| 环境 | 路径 |
|------|------|
| Windows（资源管理器 / Cursor） | `D:\code\gitreps\auto-learn` |
| WSL / Linux | `/mnt/d/code/gitreps/auto_learn` |

> 物理目录名为 `auto_learn`（WSL 兼容）；Windows 下 `auto-learn` 为指向它的联接。原 `exam` 目录已移除。

## 四清单

| 清单 | 路径 |
|------|------|
| tool-list | `catalog/tool-list.yaml` |
| solved-list | `catalog/solved-list.yaml` |
| reading-list | `catalog/reading-list.yaml` |
| problem-list | `catalog/problem-list.yaml` |

## 工作流

```
新问题 → tool-list → solved-list → reading-list → problem-list(open)
```

详见 [AGENTS.md](AGENTS.md)、[DESIGN.md](DESIGN.md)。

## Chrome 索引

```bash
python3 scripts/import_chrome_sources.py
python3 scripts/classify_reading_items.py
python3 scripts/reading_to_problem.py
python3 scripts/sync_catalog_from_legacy.py
```

## 依赖

Python 3.10+，`pip install -r requirements.txt`
