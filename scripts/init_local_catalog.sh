#!/usr/bin/env bash
# Create local-only catalog YAML files from examples (not committed to git).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

for name in reading-list problem-list solved-list tool-list; do
  src="catalog/${name}.yaml.example"
  dst="catalog/${name}.yaml"
  if [[ -f "$dst" ]]; then
    echo "skip (exists): $dst"
  else
    cp "$src" "$dst"
    echo "created: $dst"
  fi
done

echo "Done. Run sync/import scripts to populate local catalogs."
