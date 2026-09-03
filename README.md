# Quanta Learn

Rep motivation: ingest material into `reading-list`, archive solutions in `solved-list`, and keep reusable pieces in `tool-list`.

This repo may include solutions and experiment notes for [*Reinforcement Learning from Human Feedback*](https://github.com/natolambert/rlhf-book) (rlhf-book). Full trainers are **not** vendored — see [`tool-list/rlhf-book`](tool-list/rlhf-book/) placeholders that point at upstream `code/`.

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

## Experiment summary (rlhf-book) · expected vs observed

I ran the book’s **Suggested Experiments** (plus one KL extension) on Hopper (96GB HBM) and logged only scalars. Below is whether each setup’s **design expectation** showed up in the **measured outcome**. Full tables live under [`solved-list/rlhf-book/`](solved-list/rlhf-book/).

**Overall:** mechanistic / training-dynamics checks mostly matched; a few “popular story” or headline-gain claims did **not**.

| Chapter | Setup intent (what I expected to see) | What I observed | Match? |
|---------|----------------------------------------|-----------------|--------|
| [6 · Policy Gradients](solved-list/rlhf-book/ch06-policy-gradients/REPORT.md) | Matched GRPO with only `kl_estimator` changed; common write-ups suggest `kl3` is stabler / better | Clear ranking **kl1 ≥ kl2 ≫ kl3** on correctness; `kl3` early loss/grad spikes | **Partial** — comparison worked; **against** the “kl3 is safer” story |
| [8 · Direct Alignment](solved-list/rlhf-book/ch08-direct-alignment/REPORT.md) | YAML DPO-family learns preference (acc↑, margins↑); ref-free harder; “vary data before loss” | YAML DPO/IPO/DPO-Norm learn strongly; SimPO weak; ORPO margins barely move; CLI data sweep stuck under weak LR | **Mostly yes** for loss comparison / ref-free pickiness; **no** for a clean data-vs-loss verdict (LR confound) |
| [9 · Rejection Sampling](solved-list/rlhf-book/ch09-rejection-sampling/REPORT.md) | Cache once; RM **top** beats **random**; larger `n` → more decidable / better pick | Cache OK; 1.7B top vs random mixed (−2.0 / +1.5 pp); `n`↑ raises decidable; `n=16` best (84%); 0.6B top−random **+2.5 pp** | **Partial** — pipeline & `n`/decidable as expected; **no** reliable “RM beats random” on the 1.7B slice |
| [12 · Distillation / SDPO](solved-list/rlhf-book/ch12-synthetic-data/REPORT.md) | SDPO smoke: `reward`↑, `skipped`↓; fewer rollouts → harder to find a correct sibling (`skipped`↑) | Smoke reward 0.64→0.70, skipped ends low; `n=2` skipped ~17 vs `n=16` ~4 | **Yes** (directional on smoke-length runs; not full 200-step default) |

### Short readouts

1. **Ch6** — The experiment *did* isolate the KL estimator and produce a stable ranking; I did **not** confirm the folklore that training with `kl3` is the safe default here (`beta=0.04`, spell_backward, single seed).
2. **Ch8** — With the full YAML recipe, preference losses behave as taught; reference-free methods need more care. Growing data under CLI `lr=5e-7` / 1 epoch did not unlock learning — optimizer settings dominated.
3. **Ch9** — Rejection-sampling plumbing works. On this GSM8K + AceMath slice, reward selection is **not** a free lunch vs random when `decidable_fraction` is low (~26% at 1.7B); giving the RM more candidates (`n=16`) helped more than the default matched top/random gap.
4. **Ch12** — SDPO smoke tracks the book narrative (reward up, skipped manageable when rollouts are plentiful). Knob rankings stay directional until a longer multi-seed run.

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
