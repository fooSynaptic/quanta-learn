# rlhf-book · Solved Experiments

Experiment notes for the **Suggested Experiments** at the end of chapters in [*Reinforcement Learning from Human Feedback*](https://rlhfbook.com) ([natolambert/rlhf-book](https://github.com/natolambert/rlhf-book)).

Training code lives in a local workspace. This directory keeps **sanitized reports and figures only** — no training text, checkpoints, hostnames, or cluster paths.

| Chapter | Book topic | Report | Status |
|---------|------------|--------|--------|
| [6 · Policy Gradients](ch06-policy-gradients/REPORT.md) | GRPO / group-relative estimators / KL | [REPORT](ch06-policy-gradients/REPORT.md) | KL estimator full runs ✅ |
| [8 · Direct Alignment](ch08-direct-alignment/REPORT.md) | DPO / IPO / SimPO / ORPO | [REPORT](ch08-direct-alignment/REPORT.md) | Suggested 1–4 queue 8/8 ✅ |
| [9 · Rejection Sampling](ch09-rejection-sampling/REPORT.md) | RS selection → SFT | [REPORT](ch09-rejection-sampling/REPORT.md) | Expts 1+2 ✅; 3/4 not run |

## Upload policy

- Training defaults to `WANDB_MODE=disabled`; metrics stay in local `metrics.jsonl`
- No GSM8K / preference text, completions, selected pairs, or checkpoints uploaded
- Reports only keep public model/dataset names, hyperparameters, and scalar results

## How to read

1. Open the chapter `REPORT.md` “Book experiment ↔ this run” table  
2. Check result tables and `figures/`  
3. Reproduce with the commands at the end of each report (weights not shipped here)
