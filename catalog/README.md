# catalog (local)

`*.yaml` index files stay on the machine; they are not published.

## First run

```bash
cp catalog/reading-list.yaml.example catalog/reading-list.yaml
cp catalog/problem-list.yaml.example catalog/problem-list.yaml
cp catalog/solved-list.yaml.example catalog/solved-list.yaml
cp catalog/tool-list.yaml.example catalog/tool-list.yaml

python3 scripts/sync_catalog_from_legacy.py
python3 scripts/import_chrome_sources.py
python3 scripts/classify_reading_items.py
python3 scripts/reading_to_problem.py
```

## Public

- `schema.md`
- `*.yaml.example`

## Local (gitignored)

| File | Content |
|------|---------|
| `reading-list.yaml` | Chrome bookmarks / history |
| `problem-list.yaml` | Open problems |
| `solved-list.yaml` | Solution index |
| `tool-list.yaml` | Tool registry |
