# catalog（本地私密）

**本目录下的 `*.yaml` 索引文件不进入公开仓库**，仅保留在本机。

## 首次使用

```bash
cd /path/to/auto-learn   # 或 auto_learn

cp catalog/reading-list.yaml.example catalog/reading-list.yaml
cp catalog/problem-list.yaml.example catalog/problem-list.yaml
cp catalog/solved-list.yaml.example catalog/solved-list.yaml
cp catalog/tool-list.yaml.example catalog/tool-list.yaml

python3 scripts/sync_catalog_from_legacy.py
python3 scripts/import_chrome_sources.py
python3 scripts/classify_reading_items.py
python3 scripts/reading_to_problem.py
```

## 公开仓库包含

- `schema.md` — 字段定义
- `*.yaml.example` — 空模板

## 本地生成（已 gitignore）

| 文件 | 内容 |
|------|------|
| `reading-list.yaml` | Chrome 书签/历史 |
| `problem-list.yaml` | 待解决问题 |
| `solved-list.yaml` | 题解索引 |
| `tool-list.yaml` | 工具注册 |
