# Quanta Learn — Agent Guide

Default task: run the long-horizon learning loop — ingest sources into `reading-list`, advance a study budget, archive `solved-list`, extract `tool-list`, and park short-term blockers in `problem-list`. See [DESIGN.md](DESIGN.md).

## Lists

| List | Placeholder | Use |
|------|-------------|-----|
| reading-list | `<CATALOG_READING>` | Main queue by `status`, `category`, `last_seen` |
| tool-list | `<CATALOG_TOOL>` | Match by tags, name, entry |
| solved-list | `<CATALOG_SOLVED>` | Match by topics, summary |
| problem-list | `<CATALOG_PROBLEM>` | Parking lot: `blocked` / `deferred` (also `open` / `wip` while active) |

Init: `bash scripts/init_local_catalog.sh`. Schema: [catalog/schema.md](catalog/schema.md). Core diagram: [docs/images/learning-core-flow.svg](docs/images/learning-core-flow.svg).

## Reading backlog

1. Pick `status: inbox` or `active`.
2. Search `<CATALOG_TOOL>` and `<CATALOG_SOLVED>` with tags / category / title / url.
3. If enough: set `related.*`, mark `done` (or `archived`), optional `summary`.
4. If finished with reusable pieces: write solved and propose tool-list entries.
5. If blocked soon: move / link into problem-list (`blocked` or `deferred`), not a default drill queue.

## Direct questions

`tool-list` → `solved-list` → `reading-list` → `problem-list`

## Reading fields

| Field | Use |
|-------|-----|
| `status` | inbox / active / done / archived |
| `category` | classify result |
| `tags` | align with tool / solved (Chrome: source + folder + domain) |
| `related.*` | keep after hits |
| `privacy` | Chrome ingest sets `redacted: true` |
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
- Commit author/committer: `fooSynaptic <19420328+fooSynaptic@users.noreply.github.com>` only (no personal inbox)
- Browser profile is read-only; Chrome ingest redacts and applies the local blocklist
- Skill: `skills/auto-learn-agent/SKILL.md`
