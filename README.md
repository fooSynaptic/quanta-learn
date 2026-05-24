# Auto Learn

个人学习 Agent 项目：四清单索引 + 可复用工具 + 历史题解。

**仓库**：https://github.com/fooSynaptic/auto-learn

## 目录位置

| 环境 | 路径 |
|------|------|
| Windows | `D:\code\gitreps\auto-learn` |
| WSL | `/mnt/d/code/gitreps/auto_learn` |

## 仓库结构（根目录）

```text
auto-learn/
├── catalog/           # 索引层（Agent 主读）
├── reading-list/      # Chrome / 阅读记忆
├── problem-list/      # 待解决问题
├── solved-list/       # 已解决索引与笔记
├── tool-list/         # 可复用工具实现（排序、SVM、并查集…）
├── legacy/            # 历史题解（Coding、面经、Offer…）
├── scripts/           # 维护脚本
├── AGENTS.md
├── DESIGN.md
└── README.md
```

根目录**不再**平铺 `Sorting/`、`Coding/` 等文件夹；算法工具在 `tool-list/`，题解在 `legacy/`。

## 公开 vs 本地

| 进入 GitHub（框架） | 仅本机（私密） |
|--------------------|----------------|
| `scripts/`、`skills/`、`catalog/schema.md`、`*.yaml.example` | `catalog/*.yaml`（四清单索引） |
| `tool-list/` 工具代码、`legacy/` 题解、`DESIGN.md` | `reading-list/sources/`（Chrome 快照） |
| 目录骨架（`.gitkeep`） | `problem-list/**/*.md`（自动生成条目） |

克隆后初始化本地索引见 [catalog/README.md](catalog/README.md)。

## 四清单（本地 `catalog/*.yaml`）

| 清单 | 本地文件 |
|------|----------|
| tool-list | `catalog/tool-list.yaml` |
| solved-list | `catalog/solved-list.yaml` |
| reading-list | `catalog/reading-list.yaml` |
| problem-list | `catalog/problem-list.yaml` |

## 工作流

```
新问题 → tool-list → solved-list → reading-list → problem-list(open)
```

## 维护命令

```bash
python3 scripts/import_chrome_sources.py
python3 scripts/classify_reading_items.py
python3 scripts/reading_to_problem.py
python3 scripts/sync_catalog_from_legacy.py
```

## 依赖

Python 3.10+，`pip install -r requirements.txt`
