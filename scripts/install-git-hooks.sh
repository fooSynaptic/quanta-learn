#!/usr/bin/env bash
set -eu
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOOK="$ROOT/.git/hooks/commit-msg"
SRC="$ROOT/scripts/commit-msg-reject-coauthor"
cp "$SRC" "$HOOK"
chmod +x "$HOOK"
echo "Installed: $HOOK"
