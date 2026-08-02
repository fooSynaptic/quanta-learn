# rlhf-book · Tools

Reusable experiment conventions (implementations stay in the local experiment pack; large artifacts are not in-repo):

| Concern | Convention |
|---------|------------|
| Metrics | Per-run `metrics.jsonl` + `meta.json`; portal overlays by `compare_group` |
| W&B | Off by default; network only if `RLHF_ENABLE_WANDB=1` and a non-empty project is set |
| Launchers | Chapter `scripts/0x_*.sh` map to Suggested Experiments numbering |
| Report template | `solved-list/rlhf-book/chXX-*/REPORT.md`: book item ↔ config ↔ results ↔ figures |

See the Reproduce section at the end of each solved report.
