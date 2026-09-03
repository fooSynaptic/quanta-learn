# rlhf-book · Tools

Sanitized **placeholders** for the book’s Suggested Experiment packages.  
This repo does **not** ship full trainers, weights, rollouts, or cluster launchers.

| Tool id | Package | Solved report | Upstream path |
|---------|---------|---------------|---------------|
| `tool-rlhf-policy-gradients` | [`placeholders/policy_gradients/`](placeholders/policy_gradients/) | [ch06](../../solved-list/rlhf-book/ch06-policy-gradients/REPORT.md) | `code/policy_gradients/` |
| `tool-rlhf-direct-alignment` | [`placeholders/direct_alignment/`](placeholders/direct_alignment/) | [ch08](../../solved-list/rlhf-book/ch08-direct-alignment/REPORT.md) | `code/direct_alignment/` |
| `tool-rlhf-rejection-sampling` | [`placeholders/rejection_sampling/`](placeholders/rejection_sampling/) | [ch09](../../solved-list/rlhf-book/ch09-rejection-sampling/REPORT.md) | `code/rejection_sampling/` |
| `tool-rlhf-distillation` | [`placeholders/distillation/`](placeholders/distillation/) | [ch12](../../solved-list/rlhf-book/ch12-synthetic-data/REPORT.md) | `code/distillation/` |

Upstream book: [rlhfbook.com](https://rlhfbook.com) · code: [natolambert/rlhf-book](https://github.com/natolambert/rlhf-book)  
Attribution / licenses: [SOURCE.md](SOURCE.md)

## What is in-repo

| Keep | Drop |
|------|------|
| Module stub (`train.py` exits with pointer) | Full training loops / CUDA kernels |
| Example YAML matching reported runs | Checkpoints, HF caches, rollouts, GSM8K text |
| Conventions below | Hostnames, cluster paths, product GPU SKU codes |

## Conventions

| Concern | Convention |
|---------|------------|
| Metrics | Per-run `metrics.jsonl` (+ optional `meta.json`); group runs with `compare_group` |
| W&B | Off by default (`WANDB_MODE=disabled`, `wandb_project: null`) |
| Hardware wording | `Hopper (96GB HBM)` only — never the product SKU code |
| Launchers | Local only; not published here |
| Report template | `solved-list/rlhf-book/chXX-*/REPORT.md` |

## How to actually run

1. Clone [natolambert/rlhf-book](https://github.com/natolambert/rlhf-book) and use `code/<package>/`.  
2. Copy the example YAML from `placeholders/<package>/configs/` as a starting point (public model/dataset names only).  
3. Match hyperparameters to the linked solved report.  
4. Expect stub `python -m …` here to **exit non-zero** — that is intentional.
