#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${HOME}/.agents/skills/themis"

mkdir -p "$(dirname "$TARGET")"
rm -rf "$TARGET"
cp -R "$ROOT/skills/themis" "$TARGET"

echo "Installed Themis for Codex at: $TARGET"
