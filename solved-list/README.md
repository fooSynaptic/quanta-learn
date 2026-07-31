# solved-list

历史题解与实验排障的**沉淀层**。索引元数据在本地 [`../catalog/solved-list.yaml`](../catalog/solved-list.yaml)（不进公开仓）。

## 递进关系

材料先在 `reading-list/<domain>/` 消化；动手跑通、修通实现后，按**同一子域名**落入本目录：

```text
reading-list/<domain>/  →  solved-list/<domain>/  →  tool-list/<domain>/
```

根 README 只描述清单职责与目录约定，**不**把某一本书写成整个 solved-list 的「当前焦点」。

## 目录结构

```text
solved-list/
├── README.md           # 本说明
├── notes/              # 短备忘（未成域时）
└── <domain>/           # 按主题的题解域
    └── rlhf-book/      # 示例：RLHF Book 实验与实现排障
```

## 与四清单

| 清单 | 关系 |
|------|------|
| **reading-list** | 同名 `<domain>` 是阅读来源 |
| **tool-list** | 可泛化部分上移到 `tool-list/<domain>/`；「这一次怎么修通」留在本域 |
| **problem-list** | 尚无法复用解决的动手项，解决后回写本目录对应域 |

检索顺序：`tool-list` → **`solved-list`** → `reading-list` → `problem-list`。见 [DESIGN.md](../DESIGN.md)。

## 维护

```bash
python3 scripts/sync_catalog_from_legacy.py
```
