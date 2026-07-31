# tool-list

可复用求解工具与算法实现的**物理目录**。索引元数据在 [`../catalog/tool-list.yaml`](../catalog/tool-list.yaml)。

从 reading → solved 沉淀出来、可再次调用的入口落在这里；按**主题子域**与 reading/solved 对齐。

## 递进关系

```text
reading-list/<domain>/  →  solved-list/<domain>/  →  tool-list/<domain>/
```

## 目录结构

```text
tool-list/
├── README.md
├── runners/               # 统一运行入口（待扩展）
├── rlhf-book/             # 主题域：RLHF Book 可复用工具
├── ml/
│   └── svm/               # SMO 线性 SVM
└── algorithms/
    ├── sorting/           # 排序算法套件
    ├── linked-list/       # 链表工具
    ├── cs-courses/        # 课程配套（并查集、栈等）
    ├── heapsort/
    ├── fastsort/
    ├── greedy/
    ├── datastruct/
    ├── c-classic/         # C/C++ classics (ex fooSynaptic/C-algorithm)
    └── cpp/               # C++ 基础练习
```

## 与仓库根目录的关系

- **根目录**只保留：`catalog/`、`reading-list/`、`problem-list/`、`solved-list/`、`tool-list/`、`legacy/`、`scripts/`
- **题解代码**在 `legacy/`（如 `legacy/Coding/`）或 `solved-list/<domain>/`
- **可复用工具**在 `tool-list/`（本目录）

## 维护

```bash
python3 scripts/sync_catalog_from_legacy.py
```
