# Chapter 9 · Rejection Sampling — Experiment Report

Maps to **Suggested Experiments** (§9.4) in Chapter 9 (*Rejection Sampling*) and `code/rejection_sampling/`.  
Tool placeholder: [`tool-list/rlhf-book/placeholders/rejection_sampling/`](../../../tool-list/rlhf-book/placeholders/rejection_sampling/).  
Hardware: Hopper (96GB HBM), ≤2 GPUs. Pipeline: `Qwen/Qwen3-1.7B` generate → `nvidia/AceMath-7B-RM` score → selection → SFT → GSM8K exact-match.  
Upload: disabled (`WANDB_MODE=disabled`, empty/`null` project; no API key). Metrics only in local `metrics.jsonl`.

## Book experiment ↔ this run

| Book item | Content | Status |
|-----------|---------|--------|
| 1 | Build GSM8K rollout+score cache once | ✅ done |
| 2 | Matched four-way selection (top vs random) | ✅ done |
| 3 | Sweep `n_completions` / temperature / top_k | ✅ done |
| 4 | Smaller policy (Qwen3-0.6B) matched top vs random | ✅ done |

All four Suggested Experiments completed (`exit=0`).

## Expt 2 results (main table · 1.7B default cache)

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

## Expt 3 · vary how much choice the RM gets

Same eval protocol · policy `Qwen/Qwen3-1.7B` · RM `nvidia/AceMath-7B-RM`.  
`n2` / `n16` / `temp0.2` change gen settings → **new caches**; `k2000` reuses the default cache.

| Config | Change | decidable | Exact | Accuracy | wall (approx) |
|--------|--------|-----------|-------|----------|---------------|
| `top_per_prompt_n2` | `num_completions=2` | 90/1000 = **0.090** | 162/200 | **81.0%** | ~31 min |
| `top_per_prompt` (expt2 ref) | `n=8` | 264/1000 = 0.264 | 162/200 | 81.0% | ~7 min† |
| `top_per_prompt_n16` | `num_completions=16` | 312/1000 = **0.312** | 168/200 | **84.0%** | ~74 min |
| `top_per_prompt_temp0.2` | `temperature=0.2` | 177/1000 = **0.177** | 167/200 | **83.5%** | ~45 min |
| `top_k_overall_k2000` | overall `top_k=2000` | (default cache) | 163/200 | **81.5%** | ~11 min |

† cache hit from expt2.

### Readout

1. Larger `n` raises `decidable_fraction` (2→8→16: 0.09→0.26→0.31).
2. **`n=16` best accuracy (84%)**; `n=2` ties default `n=8` at 81% with fewer decidable prompts.
3. Low temp `0.2`: decidable 0.177 · accuracy 83.5%.
4. Overall `top_k=2000` matches default overall (81.5%) — no gain on this slice.
5. Expt 3 scripts are treatment-only; random controls remain expt 2.

## Expt 4 · smaller policy (Qwen3-0.6B)

| Item | Value |
|------|-------|
| Policy | `Qwen/Qwen3-0.6B` |
| Reward model | `nvidia/AceMath-7B-RM` |
| Data | GSM8K · **500** prompts × 8 completions |
| Separate cache | yes |
| decidable (top run) | **278/500 = 0.556** |

| Strategy | Role | Exact match | Accuracy | wall (approx) |
|----------|------|-------------|----------|---------------|
| `top_per_prompt` | treatment | 131/200 | **65.5%** | ~29 min (incl. preprocess) |
| `random_per_prompt` | control | 126/200 | **63.0%** | ~5.5 min (cache hit) |

Δ: `top − random` = **+2.5 pp**. Absolute scores are lower than the 1.7B slice; reward selection slightly beats random here (single seed / 200 test).

## Expt 1 · Rollout cache (default 1.7B)

| Item | Value |
|------|-------|
| Policy | `Qwen/Qwen3-1.7B` |
| Reward model | `nvidia/AceMath-7B-RM` |
| Data | GSM8K · 1000 prompts × 8 completions = **8000** |
| Cache size | ~7.0 MB JSONL |
| decidable_fraction | **264/1000 = 0.264** |
| Reward stats | min −8.5 · max 29.0 · mean ≈8.51 |

First preprocess ~1 h including downloads. Expt 3/4 use separate cache hashes.

### Ops notes (sanitized)

1. Slow `uv sync` on shared FS → reuse an existing torch venv when possible.  
2. HF xet auth issues → disable xet + use a mirror; keep HF cache on the large data volume, not the system disk.

## What is / is not uploaded

| Content | Uploaded? |
|---------|-----------|
| loss / grad_norm / epoch / test_accuracy | only if W&B enabled (here: **no**) |
| config scalars | only if W&B enabled (here: **no**) |
| preference / GSM8K text, rollouts, selected pairs | **never** |
| checkpoints | **no** (`save_checkpoint: false`) |

## Reproduce

Full trainer is **not** in this repo (stub only under tool-list). Use upstream [natolambert/rlhf-book](https://github.com/natolambert/rlhf-book) `code/rejection_sampling/`, with an example YAML sketch in the [tool placeholder configs](../../../tool-list/rlhf-book/placeholders/rejection_sampling/configs/).

```bash
export WANDB_MODE=disabled
cd code   # from upstream rlhf-book checkout
# 1) cache
uv run python -m rejection_sampling.preprocess --config rejection_sampling/configs/top_per_prompt.yaml
# 2) matched selection
uv run python -m rejection_sampling.train --config rejection_sampling/configs/top_per_prompt.yaml
uv run python -m rejection_sampling.train --config rejection_sampling/configs/random_per_prompt.yaml
# 3–4) see configs/sweeps/
```

## Artifacts (this repo)

| path | notes |
|------|-------|
| `REPORT.md` | this file |
| (metrics) | kept in the local experiment `runs/` tree, not committed here |
| [`tool-list/.../rejection_sampling/`](../../../tool-list/rlhf-book/placeholders/rejection_sampling/) | stub + config sketch |
