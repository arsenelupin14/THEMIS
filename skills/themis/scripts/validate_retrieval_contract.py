#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

def main() -> None:
    failures = []

    retrieval_ref_path = ROOT / "skills/themis/references/evidence-retrieval.md"
    skill_path = ROOT / "skills/themis/SKILL.md"

    if not retrieval_ref_path.exists():
        print(f"FAIL: missing evidence-retrieval reference at {retrieval_ref_path}")
        sys.exit(1)

    retrieval_text = retrieval_ref_path.read_text(encoding="utf-8", errors="ignore")
    skill_text = skill_path.read_text(encoding="utf-8", errors="ignore") if skill_path.exists() else ""

    # 1. Evidence Retrieval Agent exists in the references or skill file
    if "Evidence Retrieval Agent" not in retrieval_text and "Evidence Retrieval Agent" not in skill_text:
        failures.append("Evidence Retrieval Agent role is not defined.")

    # 2. Check candidate sources are defined
    if "candidate sources" not in retrieval_text.lower():
        failures.append("Candidate sources definition is missing in retrieval contract.")

    # 3. Evidence Retrieval Agent must not mark claims as VERIFIED
    if "must not verify" not in retrieval_text.lower() and "must not mark" not in retrieval_text.lower():
        failures.append("Contract does not explicitly restrict Evidence Retrieval Agent from verifying claims.")

    # 4. Citation Auditor is the only role allowed to mark a claim as VERIFIED
    if "only the citation auditor" not in retrieval_text.lower() and "citation auditor is the only role" not in skill_text.lower():
        failures.append("Verification authority constraint not found.")

    # 5. NEEDS_SOURCE behaviour exists
    if "needs_source" not in retrieval_text.lower() and "needs-citation" not in skill_text.lower():
        failures.append("needs_source/needs-citation fallback state is not defined.")

    if failures:
        print("FAIL: retrieval contract validation failed")
        for failure in failures:
            print(f"- {failure}")
        sys.exit(1)

    print("PASS: retrieval contract is valid")

if __name__ == "__main__":
    main()
