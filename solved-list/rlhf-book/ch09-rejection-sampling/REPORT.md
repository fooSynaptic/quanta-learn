# Chapter 9 · Rejection Sampling — Experiment Report

Maps to **Suggested Experiments** (§9.4) in Chapter 9 (*Rejection Sampling*) and `code/rejection_sampling/`.  
Hardware: NVIDIA H20, ≤2 GPUs. Pipeline: `Qwen/Qwen3-1.7B` generate → `nvidia/AceMath-7B-RM` score → selection → SFT → GSM8K exact-match.  
Upload: disabled (`WANDB_MODE=disabled`, empty/`null` project; no API key). Metrics only in local `metrics.jsonl`.

## Book experiment ↔ this run

| Book item | Content | Status |
|-----------|---------|--------|
| 1 | Build GSM8K rollout+score cache once | ✅ done |
| 2 | Matched four-way selection (top vs random) | ✅ done |
| 3 | Sweep `n_completions` / temperature / top_k | ⏸ not run |
| 4 | Smaller policy (e.g. Qwen3-0.6B) | ⏸ not run |

Main book path (1+2) is complete. Items 3/4 are extensions.

## Expt 2 results (main table)

Protocol: GSM8K **test exact-match** · `max_test_samples=200` · shared rollout cache · SFT 2 epochs.

| Strategy | Role | Exact match | Accuracy | wall (approx) |
|----------|------|-------------|----------|---------------|
| `top_per_prompt` | treatment | 162/200 | **81.0%** | ~7.3 min |
| `random_per_prompt` | control | 166/200 | **83.0%** | ~7.6 min |
| `top_k_overall` | treatment | 163/200 | **81.5%** | ~7.5 min |
| `random_k_overall` | control | 160/200 | **80.0%** | ~7.2 min |

Paired Δ (treatment − control):

| Pair | Δ Accuracy |
|------|------------|
| `top_per_prompt` − `random_per_prompt` | **−2.0 pp** (reward pick did not beat random) |
| `top_k_overall` − `random_k_overall` | **+1.5 pp** (reward slightly ahead) |

With `decidable_fraction≈26%`, within-prompt contrast is limited. Gaps look like small-sample noise — **not** evidence that RM selection reliably beats random on this slice.

Four strategies serially: ~30 min after cache hit.

## Expt 1 · Rollout cache

| Item | Value |
|------|-------|
| Policy | `Qwen/Qwen3-1.7B` |
| Reward model | `nvidia/AceMath-7B-RM` |
| Data | GSM8K · 1000 prompts × 8 completions = **8000** |
| Cache size | ~7.0 MB JSONL |
| decidable_fraction | **264/1000 = 0.264** |
| Reward stats | min −8.5 · max 29.0 · mean ≈8.51 |

### Wall clock (approx)

| Stage | Time |
|-------|------|
| Load Qwen3-1.7B | ~3 min |
| Stage 1 generate | ~32 min |
| Load AceMath-7B-RM | ~10 min |
| Stage 2 score | ~13 min |
| **Total** | **~1 h** (incl. first download) |

### Ops notes (sanitized)

1. Slow `uv sync` on shared FS → reuse an existing torch venv when possible.  
2. HF xet auth issues → disable xet + use a mirror; keep HF cache on the large data volume, not the system disk.

## What is / is not uploaded

| Content | Uploaded? |
|---------|-----------|
| loss / grad_norm / epoch / test_accuracy | only if W&B enabled (here: **no**) |
| config scalars (model name, dataset name, hparams) | only if W&B enabled (here: **no**) |
| preference / GSM8K text, rollouts, selected pairs | **never** (no `wandb.Table` / Artifact in this slice) |
| checkpoints | **no** (`save_checkpoint: false`) |

Default YAML uses a personal project name only if W&B is turned on; it does **not** auto-publish to the public `rlhf-book` org. This run used `WANDB_MODE=disabled`.

## Expt 3 / 4 (not run)

See chapter README and `configs/sweeps/` in the experiment pack when needed.

## Reproduce

```bash
export WANDB_MODE=disabled
cd code
# 1) cache
uv run python -m rejection_sampling.preprocess --config rejection_sampling/configs/top_per_prompt.yaml
# 2) matched selection pair
uv run python -m rejection_sampling.train --config rejection_sampling/configs/top_per_prompt.yaml
uv run python -m rejection_sampling.train --config rejection_sampling/configs/random_per_prompt.yaml
# likewise top_k_overall / random_k_overall
```

## Artifacts (this repo)

| path | notes |
|------|-------|
| `REPORT.md` | this file |
| (metrics) | kept in the local experiment `runs/` tree, not committed here |
