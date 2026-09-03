# Chapter 12 · Distillation / SDPO — Experiment Report

Maps to **Suggested Experiments** (§12.3.4) in Chapter 12 (*Synthetic Data & Distillation*) and `code/distillation/`.  
Tool placeholder: [`tool-list/rlhf-book/placeholders/distillation/`](../../../tool-list/rlhf-book/placeholders/distillation/).  
Hardware: Hopper (96GB HBM) · ≤2 GPUs. Model: `Qwen/Qwen3-1.7B`. Task: Reasoning Gym `spell_backward`.  
Upload: disabled (`WANDB_MODE=disabled`, `wandb_project: null`). Metrics in local `metrics.jsonl` only.

## Book experiment ↔ this run

| Book item | Content | Status |
|-----------|---------|--------|
| **1** | Run SDPO string-reversal; watch `reward` / `loss` / `skipped` | ✅ smoke (`num_steps=40`) |
| **2** | Sweep `num_rollouts`, `kl_top_k`, `prompts_per_step` | ✅ four knobs (`num_steps=40` each) |

Book default `sdpo.yaml` uses `num_steps=200`, `data.size=10000`. This queue used **smoke-length** configs (`num_steps=40`, `data.size=2000`) so the dual-GPU queue finishes in hours. Full-length YAML remains in-tree for a longer follow-up.

Queue wall (UTC): **07:19 → 16:19** · `ALL tracks done exit=0`.

## Setup (shared)

| Item | Value |
|------|-------|
| algo | SDPO (per-token top-K reverse KL) |
| model | `Qwen/Qwen3-1.7B` (student = self-teacher) |
| task | `spell_backward`, `data.size=2000` |
| lr | `1e-6` · `max_norm=1.0` · seed `42` |
| sampling | temp `0.6` · top_p `0.95` · top_k `20` |
| baseline knobs | `num_rollouts=8`, `kl_top_k=20`, `prompts_per_step=16` |
| train length | `num_steps=40` |

## Experiment 1 · SDPO smoke

| run | wall | reward first→last (mean) | skipped last (mean) | loss mean |
|-----|------|--------------------------|---------------------|-----------|
| `sdpo_smoke` | 2.65 h | 0.638 → **0.702** (0.700) | 1 (6.6) | 0.518 |

`reward` climbed; `skipped` fell toward the end (last step 1). Matches the book narrative that fewer prompts are skipped as the student improves.

## Experiment 2 · on-policy knobs

| config | changed knob | wall | reward first→last (mean) | skipped mean | loss mean |
|--------|--------------|------|--------------------------|--------------|-----------|
| `num_rollouts_2` | `num_rollouts=2` | 3.07 h | 0.807 → 0.818 (**0.834**) | **16.6** | 0.581 |
| `sdpo_smoke` (ref) | `num_rollouts=8` | 2.65 h | 0.638 → 0.702 (0.700) | 6.6 | 0.518 |
| `num_rollouts_16` | `num_rollouts=16` | 2.62 h | 0.498 → **0.702** (0.665) | **4.0** | 0.504 |
| `kl_top_k_5` | `kl_top_k=5` | 2.66 h | 0.638 → **0.830** (0.699) | 6.6 | 0.515 |
| `prompts_per_step_4` | `prompts_per_step=4` | **0.64 h** | 0.623 → 0.656 (0.681) | **1.6** | 0.524 |

### Readout

1. **`num_rollouts`**: fewer rollouts → much higher `skipped` (harder to find a correct sibling demo). `n=16` keeps skipped low (~4) and still reaches ~0.70 final reward. Absolute mean reward is not monotonic in `n` on this short smoke (single seed).
2. **`kl_top_k=5`**: narrower top-K KL still trains; final reward **0.83** on this seed — promising, needs multi-seed confirmation vs baseline `k=20`.
3. **`prompts_per_step=4`**: cheapest wall clock (~0.6 h); reward gains are milder over 40 steps (smaller optimizer batch signal).
4. Limits: single seed · 40 steps · not the book’s 200-step default. Treat rankings as directional.

## Checklist

| Check | Outcome |
|-------|---------|
| `reward` rises | yes on smoke / n16 / kl5 / pps4; n=2 stays high but flat |
| `skipped` falls or stays manageable | yes for n≥8; n=2 stays high (~17) |
| `loss` / `grad_norm` usable | no catastrophic spikes logged in these smokes |
| Upload of text / checkpoints | none |

## Reproduce

Full trainer is **not** in this repo (stub only under tool-list). Use upstream [natolambert/rlhf-book](https://github.com/natolambert/rlhf-book) `code/distillation/`, with an example YAML sketch in the [tool placeholder configs](../../../tool-list/rlhf-book/placeholders/distillation/configs/).

```bash
export WANDB_MODE=disabled
export HF_HUB_OFFLINE=1   # if model already cached
cd code   # from upstream rlhf-book checkout
uv run python -m distillation.train --config distillation/configs/sdpo_smoke.yaml
uv run python -m distillation.train --config distillation/configs/sweeps/sdpo_num_rollouts_2.yaml
# likewise num_rollouts_16 / kl_top_k_5 / prompts_per_step_4
# full book default:
uv run python -m distillation.train --config distillation/configs/sdpo.yaml
```

## Artifacts

| path | notes |
|------|-------|
| `summary.json` | aggregate stats for this queue |
| (metrics) | per-run curves stay in the local experiment tree, not committed here |
| [`tool-list/.../distillation/`](../../../tool-list/rlhf-book/placeholders/distillation/) | stub + config sketch |
