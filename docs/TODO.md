# Quanta Learn — 待办（开发）

## 数据源

- [ ] **飞书任务清单抓取**（`import_feishu_tasks.py`）
  - 开放平台自建应用 + 用户 OAuth（`user_access_token`）
  - 权限：`task:task:read`（「我负责的」）；可选 `task:tasklist:read`（按清单拉取）
  - 合并进 `<CATALOG_PROBLEM>`，`source: feishu-task`，`source_ref` 为 `task_guid` / 分享链接
  - 环境变量：`FEISHU_APP_ID`、`FEISHU_APP_SECRET`、`FEISHU_USER_ACCESS_TOKEN`（或 refresh 流程）
  - 文档：DESIGN 补充「飞书数据源」一节；流水线与 Chrome 并列

## 展示层（Dashboard）

设计见 [UI-DESIGN.md](UI-DESIGN.md)（**v0.2 已确认**）。

- [ ] P0：`scripts/build_dashboard_stats.py`（指标 + `dashboard/stats.json`）
- [ ] P1/v1：`dashboard/server.py` + 前端
  - 默认 **阅读看板**；`archived` **默认折叠**
  - Tab：阅读 / 问题 / **题解**；顶栏 **`solved_count`**
  - **拖拽**改 reading/problem `status` 并写回 YAML
- [ ] P2：搜索、筛选持久化、导出 CSV
- [ ] （后置）飞书 `feishu-task` 筛选 — 随飞书导入一起做

## 消化与匹配

- [ ] Phase 2：reading 匹配评分（tags / topics 相似度）
- [ ] Phase 2：批量消化命令（按 `status: inbox` 队列处理）

## Agent / 集成

- [ ] Phase 3：MCP —「取下一篇 inbox」「写 related」等
- [ ] Phase 3：飞书导入纳入 `init` / 维护脚本一键顺序

## 已完成

- [x] Chrome 书签 / 历史 / 会话只读导入
- [x] reading 指标（classify）与 reading → problem 转化
- [x] 四清单框架与开源文档（SVG 流程图）
