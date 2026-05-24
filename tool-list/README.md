# tool-list

可复用求解工具与算法实现的**物理目录**。索引元数据在 [`../catalog/tool-list.yaml`](../catalog/tool-list.yaml)。

## 目录结构

```text
tool-list/
├── README.md
├── registry.yaml          # 与 catalog 同步的简要注册表
├── runners/               # 统一运行入口（待扩展）
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
    └── cpp/               # C++ 基础练习
```

## 与仓库根目录的关系

- **根目录**只保留：`catalog/`、`reading-list/`、`problem-list/`、`solved-list/`、`tool-list/`、`legacy/`、`scripts/`
- **题解代码**在 `legacy/`（如 `legacy/Coding/`）
- **可复用工具**在 `tool-list/`（本目录）

## 维护

```bash
python3 scripts/sync_catalog_from_legacy.py
```
