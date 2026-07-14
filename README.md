# Quanta Learn

## Four-List Index Framework
Automatically aggregate learning materials (e.g., Chrome bookmarks, task trackers). Manage your backlog via reading metrics, and reuse `tool-list` / `solved-list` to speed up knowledge absorption.

**Repository**: [github.com/fooSynaptic/quanta-learn](https://github.com/fooSynaptic/quanta-learn)

## Features
- **Four core lists workflow**: `tool-list` → `solved-list` → `reading-list` → `problem-list`
- **Browser data importer**: Read-only import bookmarks, browsing history & sessions into the `reading-list` index
- **Local dashboard**: Run `python3 dashboard/server.py` to access the panel at http://127.0.0.1:8765/

## Quick Start
```bash
git clone https://github.com/fooSynaptic/quanta-learn.git
cd quanta-learn

pip install -r requirements.txt
bash scripts/init_local_catalog.sh
```

## Documentation
| Document | Content |
|------|------|
| [DESIGN.md](DESIGN.md) | Knowledge digestion loop, data flow & roadmap |
| [AGENTS.md](AGENTS.md) | Agent protocol specs |
| [docs/UI-DESIGN.md](docs/UI-DESIGN.md) | Dashboard UI design |
| [docs/TODO.md](docs/TODO.md) | Development backlog |
| [catalog/README.md](catalog/README.md) | Local catalog initialization guide |

## Maintenance Scripts
```bash
export CHROME_USER_DATA_DIR="<your-browser-profile-dir>"
python3 scripts/import_chrome_sources.py
python3 scripts/classify_reading_items.py
python3 scripts/reading_to_problem.py
python3 scripts/sync_catalog_from_legacy.py
python3 scripts/build_dashboard_stats.py
```

## Dependencies
Python 3.10 or newer:
```bash
pip install -r requirements.txt          # Runtime dependencies for scripts & SMO
pip install -r requirements-dev.txt      # Dev tools: pytest, ruff linter
```

Local pre-check (matches CI pipeline rules):
```bash
ruff check scripts dashboard tests tool-list
python3 -m pytest tests/ -q
```
