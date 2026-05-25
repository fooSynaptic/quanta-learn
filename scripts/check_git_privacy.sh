#!/usr/bin/env bash
# Fail if private paths are tracked by git (run before push).
set -eu

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

violations=0

check_pattern() {
  local pat="$1"
  local f
  while IFS= read -r f; do
    [[ -n "$f" ]] || continue
    echo "PRIVATE TRACKED: $f"
    violations=$((violations + 1))
  done < <(git ls-files "$pat" 2>/dev/null || true)
}

for f in catalog/*.yaml; do
  [[ -f "$f" ]] || continue
  if git ls-files --error-unmatch "$f" &>/dev/null; then
    echo "PRIVATE TRACKED: $f"
    violations=$((violations + 1))
  fi
done

check_pattern 'reading-list/sources'
check_pattern 'problem-list/algorithm'
check_pattern 'problem-list/debug'
check_pattern 'problem-list/system-design'
check_pattern 'problem-list/generated-from-reading'
check_pattern 'dashboard/data.json'

if [[ "$violations" -gt 0 ]]; then
  echo "Abort: $violations private file(s) would be public. Check .gitignore."
  exit 1
fi

echo "OK: no private paths tracked."
