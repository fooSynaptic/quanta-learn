# reading-list

个人学习与知识提取的**入口层**：新书、文章、课程材料先落在这里消化，再向 solved / tool 沉淀。

索引元数据在本地 [`../catalog/reading-list.yaml`](../catalog/reading-list.yaml)（不进公开仓）。

## 递进关系

```text
reading-list/<domain>/   →  材料与阅读进度
        ↓ 动手跑通 / 排障
solved-list/<domain>/    →  实验与题解归档
        ↓ 可复用抽象
tool-list/<domain>/      →  可复用工具与入口
```

同一主题用**相同子域名**对齐（例如 `rlhf-book`），不要把「我在读某本书」写进 solved/tool 的根 README。

## 目录约定

| 路径 | 作用 |
|------|------|
| `inbox/` / `active/` / `archive/` | 消化工作流状态桶（松散条目） |
| `<domain>/` | 按主题归档的阅读域（书、系列、专题） |
| `rlhf-book/` | 示例域：*Reinforcement Learning from Human Feedback* |

## 维护

字段见 [`catalog/schema.md`](../catalog/schema.md)。整体设计见 [DESIGN.md](../DESIGN.md)。
