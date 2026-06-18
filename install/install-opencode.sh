#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET=".opencode/commands"

mkdir -p "$TARGET"
cp "$ROOT/opencode/commands/themis.md" "$TARGET/themis.md"

echo "Installed Themis OpenCode command at: $TARGET/themis.md"
