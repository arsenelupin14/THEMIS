#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

REQUIRED_STAGES = [
    "intake",
    "workroom_init",
    "core_agent_spawn",
    "domain_agent_spawn",
    "independent_research",
    "claim_ledger_build",
    "evidence_retrieval",
    "retrieval_gate",
    "citation_audit_gate",
    "dynamic_spawn_check",
    "revision_loop",
    "peer_review_gate",
    "public_output_gate",
    "final_report",
]

REQUIRED_GATES = [
    "retrieval_gate",
    "citation_gate",
    "peer_review_gate",
    "public_output_gate",
    "spawn_gate",
]

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: validate_orchestration_manifest.py <manifest.yml>")
        sys.exit(2)

    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8", errors="ignore")

    failures = []

    if "THEMIS_ORCHESTRATION_V1" not in text:
        failures.append("Missing THEMIS_ORCHESTRATION_V1 key")

    # Verify stages
    for stage in REQUIRED_STAGES:
        # Check if the stage is present in the document
        if stage not in text:
            failures.append(f"Missing stage in manifest: {stage}")

    # Verify gates
    for gate in REQUIRED_GATES:
        if gate not in text:
            failures.append(f"Missing gate in manifest: {gate}")

    if failures:
        print("FAIL: orchestration manifest invalid")
        for failure in failures:
            print(f"- {failure}")
        sys.exit(1)

    print("PASS: orchestration manifest is valid")

if __name__ == "__main__":
    main()
