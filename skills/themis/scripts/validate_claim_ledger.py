#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

REQUIRED_HEADERS = [
    "CLAIM_ID",
    "Claim",
    "Origin Agent",
    "Requires Source",
    "Source Status",
    "Verification Status",
    "Source IDs",
    "Risk",
    "Action",
]

VALID_STATUSES = [
    "VERIFIED",
    "UNVERIFIED",
    "NEEDS_CITATION",
    "CITATION_FAILED",
    "DISPUTED",
    "QUARANTINED",
    "RETRACTED",
]

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: validate_claim_ledger.py <claim-ledger.md>")
        sys.exit(2)

    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8", errors="ignore")

    failures = []

    for header in REQUIRED_HEADERS:
        if header not in text:
            failures.append(f"missing required column/header: {header}")

    if "[EVIDENCE]" in text:
        failures.append("legacy [EVIDENCE] label found; use verification statuses instead")

    for line in text.splitlines():
        if "|" not in line or line.strip().startswith("|---"):
            continue
        if "VERIFIED" in line and "SOURCE-" not in line:
            failures.append("verified claim without SOURCE-* reference")

    if failures:
        print("FAIL: claim ledger invalid")
        for failure in failures:
            print(f"- {failure}")
        sys.exit(1)

    print("PASS: claim ledger structure is valid")

if __name__ == "__main__":
    main()
