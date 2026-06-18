#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

STATE_KEYS = ["G:", "D:", "C:", "O:", "R:", "F:", "A:", "Q:", "K:", "V:", "T:", "X:", "N:"]

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: compact_themis_state.py <state.md>")
        sys.exit(2)

    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8", errors="ignore").splitlines()

    kept = []
    for line in text:
        stripped = line.strip()
        if any(stripped.startswith(key) for key in STATE_KEYS) or stripped.startswith("-"):
            kept.append(line.rstrip())

    print("THEMIS_STATE_V1\n")
    print("\n".join(kept[:200]))

if __name__ == "__main__":
    main()
