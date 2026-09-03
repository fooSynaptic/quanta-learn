# rlhf-book · Solved Experiments

Experiment notes for the **Suggested Experiments** at the end of chapters in [*Reinforcement Learning from Human Feedback*](https://rlhfbook.com) ([natolambert/rlhf-book](https://github.com/natolambert/rlhf-book)).

Training code is **not** vendored here. Use [tool-list/rlhf-book](../../tool-list/rlhf-book/) stubs + upstream [natolambert/rlhf-book](https://github.com/natolambert/rlhf-book). This directory keeps **sanitized reports and figures only** — no training text, checkpoints, hostnames, or cluster paths.

| Chapter | Book topic | Report | Status |
|---------|------------|--------|--------|
| [6 · Policy Gradients](ch06-policy-gradients/REPORT.md) | GRPO / group-relative estimators / KL | [REPORT](ch06-policy-gradients/REPORT.md) · [NOTES](ch06-policy-gradients/NOTES_kl_estimators_is_vs_kl.md) | Pre-fix KL tables archived; see notes |
| [8 · Direct Alignment](ch08-direct-alignment/REPORT.md) | DPO / IPO / SimPO / ORPO | [REPORT](ch08-direct-alignment/REPORT.md) | Suggested 1–4 queue 8/8 ✅ |
| [9 · Rejection Sampling](ch09-rejection-sampling/REPORT.md) | RS selection → SFT | [REPORT](ch09-rejection-sampling/REPORT.md) | Suggested 1–4 ✅ |
| [12 · Synthetic Data / Distillation](ch12-synthetic-data/REPORT.md) | SDPO / on-policy knobs | [REPORT](ch12-synthetic-data/REPORT.md) | Smoke + 4-knob sweep ✅ |

## Upload policy

- Training defaults to `WANDB_MODE=disabled`; metrics stay in local `metrics.jsonl`
- No GSM8K / preference / task text, completions, selected pairs, or checkpoints uploaded
- Reports only keep public model/dataset names, hyperparameters, and scalar results

## How to read

1. Open the chapter `REPORT.md` “Book experiment ↔ this run” table  
2. Check result tables and `figures/` / `summary.json`  
3. Open the linked **tool-list** placeholder, then reproduce from upstream with the report’s commands (weights not shipped here)
