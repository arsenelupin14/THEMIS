#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

REQUIRED = [
    "THEMIS FINAL REPORT",
    "Generated workroom",
    "Conflicts",
    "Decisions",
    "Remaining risks",
    "Open questions",
    "Recommended next action",
    "THEMIS_STATE_V1",
]

FORBIDDEN_EMPTY_AGREEMENTS = [
    "\nI agree.\n",
    "\nLooks good.\n",
    "\nNo concerns.\n",
]

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: simulate_themis_output.py <output.md>")
        sys.exit(2)

    text = Path(sys.argv[1]).read_text(encoding="utf-8", errors="ignore")

    failures = []

    for item in REQUIRED:
        if item not in text:
            failures.append(f"missing required section: {item}")

    for item in FORBIDDEN_EMPTY_AGREEMENTS:
        if item in text:
            failures.append(f"empty agreement detected: {item.strip()}")

    if "CHALLENGE" not in text.upper() and "NO_BLOCKING_CONFLICT" not in text:
        failures.append("missing challenge or explicit NO_BLOCKING_CONFLICT")

    if failures:
        print("FAIL")
        for failure in failures:
            print(f"- {failure}")
        sys.exit(1)

    print("PASS: simulation output satisfies Themis rules")

if __name__ == "__main__":
    main()
