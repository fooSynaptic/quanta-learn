# solved-list

历史题解与实验排障归档的**物理目录**。索引元数据在本地 [`../catalog/solved-list.yaml`](../catalog/solved-list.yaml)（不进公开仓）。

## 当前焦点：RLHF Book

本目录当前底本面向 [*Reinforcement Learning from Human Feedback*](https://github.com/natolambert/rlhf-book)（rlhf-book）一书配套的 **实验跑通** 与 **实现排障**：

- 章节实验代码/配置跑不通、结果对不上预期时的复现与修复记录
- 训练脚本、依赖、数据管线、评测指标等实现层面的问题与解法
- 可复用的排障结论（便于下次 digest reading / 解答同类问题直接命中）

后续条目按章节或问题主题落在本目录下；索引字段遵循 [`catalog/schema.md`](../catalog/schema.md) 的 `solved-*` 约定（`topics` / `summary` / `quality` 等）。

## 目录结构

```text
solved-list/
├── README.md          # 本说明（底本）
└── notes/             # 短笔记 / 排障备忘（可扩展）
```

## 与四清单的关系

| 清单 | 关系 |
|------|------|
| **reading-list** | 消化 RLHF 书章与实验说明时，优先用本目录已有题解匹配 |
| **tool-list** | 可泛化的脚本/入口登记到 tool；具体「这一次怎么修通」留在 solved |
| **problem-list** | 尚无法只靠复用解决的动手项，解决后回写本目录 |

检索顺序（解答新问题时）：`tool-list` → **`solved-list`** → `reading-list` → `problem-list`。详见 [DESIGN.md](../DESIGN.md)、[AGENTS.md](../AGENTS.md)。

## 维护

```bash
python3 scripts/sync_catalog_from_legacy.py
```
