# Quanta Learn

A personal learning index: ingest material into `reading-list`, archive solutions in `solved-list`, and keep reusable pieces in `tool-list`.

**Repository**: [github.com/fooSynaptic/quanta-learn](https://github.com/fooSynaptic/quanta-learn)

This repo may include solutions and experiment notes for [*Reinforcement Learning from Human Feedback*](https://github.com/natolambert/rlhf-book) (rlhf-book).

## Features
- Four lists: `reading-list` → `solved-list` → `tool-list` (plus `problem-list` for open work)
- Read-only Chrome bookmark / history / session import into the reading index
- Local dashboard: `python3 dashboard/server.py` → http://127.0.0.1:8765/

## Quick Start
```bash
git clone https://github.com/fooSynaptic/quanta-learn.git
cd quanta-learn
pip install -r requirements.txt
bash scripts/init_local_catalog.sh
```

## Domains
| Domain | reading | solved | tool |
|--------|---------|--------|------|
| [rlhf-book](reading-list/rlhf-book/) | [reading-list/rlhf-book](reading-list/rlhf-book/) | [solved-list/rlhf-book](solved-list/rlhf-book/) | [tool-list/rlhf-book](tool-list/rlhf-book/) |

## Documentation
| Document | Content |
|----------|---------|
| [DESIGN.md](DESIGN.md) | Digestion loop, data flow, roadmap |
| [AGENTS.md](AGENTS.md) | Agent protocol |
| [docs/UI-DESIGN.md](docs/UI-DESIGN.md) | Dashboard UI |
| [docs/TODO.md](docs/TODO.md) | Backlog |
| [catalog/README.md](catalog/README.md) | Local catalog setup |

## Maintenance
```bash
export CHROME_USER_DATA_DIR="<your-browser-profile-dir>"
python3 scripts/import_chrome_sources.py
python3 scripts/classify_reading_items.py
python3 scripts/reading_to_problem.py
python3 scripts/sync_catalog_from_legacy.py
python3 scripts/build_dashboard_stats.py
```

## Dependencies
Python 3.10+:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

```bash
ruff check scripts dashboard tests tool-list
python3 -m pytest tests/ -q
```
