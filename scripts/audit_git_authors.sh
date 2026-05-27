#!/usr/bin/env bash
# Audit: only fooSynaptic as author/committer; no Co-authored-by in messages.
set -eu
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
ALLOW_NAME='fooSynaptic'
ALLOW_EMAIL='19420328+fooSynaptic@users.noreply.github.com'
FAIL=0

echo "=== Author / committer (expect only $ALLOW_NAME <$ALLOW_EMAIL>) ==="
while IFS='|' read -r an ae cn ce; do
  if [[ "$an" != "$ALLOW_NAME" || "$ae" != "$ALLOW_EMAIL" ]]; then
    echo "  BAD: author    $an <$ae>"
    FAIL=1
  fi
  if [[ "$cn" != "$ALLOW_NAME" || "$ce" != "$ALLOW_EMAIL" ]]; then
    echo "  BAD: committer $cn <$ce>"
    FAIL=1
  fi
done < <(git log master --format='%an|%ae|%cn|%ce')

echo "=== Commit message trailers ==="
if git log master --format='%B' | grep -qiE '^(Co-authored-by|Reviewed-by|Signed-off-by|Thanks-to|Reported-by):'; then
  echo "  BAD: found trailer lines in commit messages"
  git log master --format='%H%n%B---' | grep -iB1 -E '^(Co-authored-by|Reviewed-by|Signed-off-by):' || true
  FAIL=1
else
  echo "  OK: no co-author / signed-off trailers"
fi

if [[ "$FAIL" -eq 0 ]]; then
  echo "AUDIT PASSED"
  exit 0
fi
echo "AUDIT FAILED"
exit 1
