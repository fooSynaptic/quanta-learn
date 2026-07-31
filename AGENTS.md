# Quanta Learn — Agent Guide

Default task: work the `reading-list` backlog in `<CATALOG_READING>`; match `tool-list` and `solved-list` first; open `problem-list` items when needed. See [DESIGN.md](DESIGN.md).

## Lists

| List | Placeholder | Use |
|------|-------------|-----|
| reading-list | `<CATALOG_READING>` | Main queue by `status`, `category`, `last_seen` |
| tool-list | `<CATALOG_TOOL>` | Match by tags, name, entry |
| solved-list | `<CATALOG_SOLVED>` | Match by topics, summary |
| problem-list | `<CATALOG_PROBLEM>` | Open / `wip` work |

Init: `bash scripts/init_local_catalog.sh`. Schema: [catalog/schema.md](catalog/schema.md).

## Reading backlog

1. Pick `status: inbox` or `active`.
2. Search `<CATALOG_TOOL>` and `<CATALOG_SOLVED>` with tags / category / title / url.
3. If enough: set `related.*`, mark `done` (or `archived`), optional `summary`.
4. If hands-on and category is algorithm / debug / system-design: ensure a problem exists, then solve and link back.
5. After solve: write solved; register tools when reusable.

## Direct questions

`tool-list` → `solved-list` → `reading-list` → `problem-list` (`open`)

## Reading fields

| Field | Use |
|-------|-----|
| `status` | inbox / active / done / archived |
| `category` | classify result; may spawn a problem |
| `tags` | align with tool / solved |
| `related.*` | keep after hits |
| `last_seen` | prefer recently revisited URLs |

## Pipeline

```bash
export CHROME_USER_DATA_DIR="<your-browser-profile-dir>"
python3 scripts/import_chrome_sources.py
python3 scripts/classify_reading_items.py
python3 scripts/reading_to_problem.py
python3 scripts/sync_catalog_from_legacy.py
```

## Constraints

- Read local `catalog/*.yaml`; public repo keeps `*.yaml.example` only
- Do not commit catalog secrets, reading snapshots, or auto-generated problem bodies
- No AI/bot co-authors in commits (see `.cursor/rules/`)
- Browser profile is read-only; keep `source` and URL
- Skill: `skills/auto-learn-agent/SKILL.md`
