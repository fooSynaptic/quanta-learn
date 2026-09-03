# Quanta Learn — Design

> Design v2.0 · long-horizon learning agent  
> Canonical core diagram: [docs/images/learning-core-flow.svg](docs/images/learning-core-flow.svg) (routing decisions: split/plan → match tool/solved → finish-this-loop → reusable/extract). This is list-transition policy, not an LLM/agent API sequence. Older SVGs under `docs/images/` may still show the Chrome-only pipeline.

## Goal

Build an agent that **accelerates learning** over long loops:

1. Ingest **Lark tasks** and **Chrome reading indexes** into `reading-list`
2. Split materials into knowledge points and a study plan
3. Archive completed work in `solved-list`
4. Extract reusable pieces into `tool-list`
5. Park items that cannot be solved soon in `problem-list`
6. Run multi-scale loops: daily → weekly → monthly → semiannual seminar

## Lists

| List | Role |
|------|------|
| reading-list | Intake queue (Lark-derived materials + Chrome URLs) |
| solved-list | Finished study / experiment notes tied to a plan |
| tool-list | Reusable scripts, templates, helpers extracted from solved work |
| problem-list | **Short-term unblockable / deferred** items (parking lot) |

| Flow | Order |
|------|-------|
| Learn | ingest → tag/classify → plan → solve → tool (or problem) |
| Answer a question | tool → solved → reading → problem |

## Sources

| Source | Status | Notes |
|--------|--------|-------|
| Chrome bookmarks / history / session | **Implemented** | Read-only; tags + redaction + blocklist |
| Lark Task OpenAPI | Planned | Tasks become learning goals, then reading items |
| Manual | Supported | `source: manual` |

Chrome privacy (must hold):

- Drop any item matching the local blocklist (URL + title + folder path)
- Blocklist lives outside version control: `config/blocklist.local.txt` or `QUANTA_BLOCKLIST`
- Redact emails, JWTs, home paths, sensitive query keys, URL userinfo, fragments
- Manifest profile path is home-redacted; snapshots stay gitignored

## Time loops

| Loop | Cadence | Output |
|------|---------|--------|
| daily | ~1 day | Ingest, tag, advance a small active budget, write related links |
| weekly | ~1 week | Review active/problem, re-prioritize, flag stalled items |
| monthly | ~1 month | Coverage check, review needs, tool-candidate quality |
| seminar | ~6 months | Cross-domain summary, open problems, next-horizon plan |

Implementation target: `python -m quanta_learn run daily|weekly|monthly|semiannual` (not fully landed yet).

## Reading metrics

| Field | Use |
|-------|-----|
| `status` | inbox → active → done → archived |
| `category` | from `classify_reading_items.py` (rules; LLM later) |
| `tags` | Chrome: source + folder + domain; used to match tool / solved |
| `source` | chrome-* / lark-task / manual |
| `privacy` | Chrome ingest marks `redacted: true` |
| `last_seen` | revisit priority |
| `related.*` | cross-links after hits |

Full schema: [catalog/schema.md](catalog/schema.md).

## Pipeline (current vs target)

**Current (Chrome path):**

| Step | Script | Output |
|------|--------|--------|
| 1 | `import_chrome_sources.py` | reading catalog + gitignored snapshots |
| 2 | `classify_reading_items.py` | category / tags |
| 3 | `reading_to_problem.py` | problem catalog (legacy “actionable” path; semantics migrating to parking-lot) |
| 4 | `sync_catalog_from_legacy.py` | tool / solved path index |

**Target:**

```text
[Lark + Chrome adapters] → reading-list
        → daily agent (plan / solve budget)
        → solved-list → tool-list
        → problem-list (blocked / deferred)
        → weekly / monthly / seminar reviews
```

```bash
export CHROME_USER_DATA_DIR="${HOME}/Library/Application Support/Google/Chrome"
python3 scripts/import_chrome_sources.py
python3 scripts/classify_reading_items.py
```

## Layers

| Layer | Public | Local only |
|-------|--------|------------|
| Framework | schema, templates, scripts, skills | — |
| Index | field docs | `catalog/*.yaml` |
| Content | tool / solution skeletons, domain notes | reading snapshots, auto problem bodies |
| Domains | e.g. `rlhf` under reading/solved/tool | personal catalogs |

`bash scripts/init_local_catalog.sh` builds local catalogs from `*.yaml.example`.

## Domains

Domains are **content partitions**, not the product story. Example: `rlhf` holds RLHF-book reading entrypoints and experiment reports under `*/rlhf-book/`.

## Problem semantics

| Status / kind | Intent |
|---------------|--------|
| `blocked` / `deferred` | Primary use: cannot finish soon |
| `open` / `wip` | Actively being worked |
| `solved` | Ready to promote into solved-list |

Older docs treated problem-list as a hands-on backlog spawned from Chrome categories. New agents should prefer **parking-lot** semantics; spawn scripts will be tightened later.

## Code archives

| Area | Content |
|------|---------|
| `tool-list/` | reusable implementations + placeholders |
| `legacy/` | historical solutions indexed by sync script |
| `solved-list/<domain>/` | finished study artifacts |
