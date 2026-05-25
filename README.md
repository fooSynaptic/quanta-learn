# Quanta Learn

**四清单索引框架**：自动汇总学习材料（如 Chrome 书签），用 reading 指标管理 backlog，并复用 tool-list / solved-list 加速消化。

**仓库**：[github.com/fooSynaptic/quanta-learn](https://github.com/fooSynaptic/quanta-learn)

## 能做什么

- **四清单**：`tool-list` → `solved-list` → `reading-list` → `problem-list`
- **浏览器取材**：只读导入书签 / 历史 / 会话 → `reading-list` 索引
- **本地看板**：`python3 dashboard/server.py` → http://127.0.0.1:8765/

## 快速开始

```bash
git clone https://github.com/fooSynaptic/quanta-learn.git
cd quanta-learn

pip install -r requirements.txt
bash scripts/init_local_catalog.sh
```

## 文档

| 文档 | 内容 |
|------|------|
| [DESIGN.md](DESIGN.md) | 消化闭环、数据流、路线图 |
| [AGENTS.md](AGENTS.md) | Agent 协议 |
| [docs/UI-DESIGN.md](docs/UI-DESIGN.md) | Dashboard 设计 |
| [docs/TODO.md](docs/TODO.md) | 开发待办 |
| [catalog/README.md](catalog/README.md) | 本地索引初始化 |

## 维护命令

```bash
export CHROME_USER_DATA_DIR="<your-browser-profile-dir>"
python3 scripts/import_chrome_sources.py
python3 scripts/classify_reading_items.py
python3 scripts/reading_to_problem.py
python3 scripts/sync_catalog_from_legacy.py
python3 scripts/build_dashboard_stats.py
```

## 依赖

Python 3.10+，`pip install -r requirements.txt`
