#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

FORBIDDEN_PATTERNS = [
    r"\bFACT-[A-Z0-9-]+",
    r"\bCONFLICT-[A-Z0-9-]+",
    r"\bCONTRACT-[A-Z0-9-]+",
    r"\bDECISION-[A-Z0-9-]+",
    r"\bTASK-[A-Z0-9-]+",
    r"\bRISK-[A-Z0-9-]+",
    r"\bQUESTION-[A-Z0-9-]+",
    r"\bNEXT-[A-Z0-9-]+",
    r"\bTHEMIS_STATE_V1\b",
    r"^ROLE:",
    r"^POSITION:",
    r"^HANDOFF:",
    r"\bCLAIM_ID\b",
    r"\bSOURCE_ID\b",
    r"\bSOURCE_STATUS\b",
    r"\[EVIDENCE\]",
    r"\[ASSUMPTION\]",
    r"\[UNKNOWN\]",
    r"\[NEEDS-CITATION\]",
]

def validate(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    failures = []

    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, text, flags=re.MULTILINE):
            failures.append(f"{path}: forbidden internal marker matched: {pattern}")

    return failures

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: validate_public_output.py <file-or-directory> [...]")
        sys.exit(2)

    failures = []

    for arg in sys.argv[1:]:
        path = Path(arg)
        if path.is_dir():
            for file in path.rglob("*.md"):
                failures.extend(validate(file))
        else:
            failures.extend(validate(path))

    if failures:
        print("FAIL: public output contains internal Themis markers")
        for failure in failures:
            print(f"- {failure}")
        sys.exit(1)

    print("PASS: public output is clean")

if __name__ == "__main__":
    main()
