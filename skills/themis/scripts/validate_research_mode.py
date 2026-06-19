#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

REQUIRED_FILES = [
    "skills/themis/references/research-mode.md",
    "skills/themis/references/citation-hardening.md",
    "skills/themis/references/peer-review-gate.md",
    "skills/themis/references/agent-core-memory.md",
    "skills/themis/references/dynamic-agent-spawn.md",
    "skills/themis/references/internal-vs-public-output.md",
    "skills/themis/references/evidence-retrieval.md",
    "skills/themis/references/orchestration-protocol.md",
    "skills/themis/assets/research-settings.template.yml",
    "skills/themis/assets/orchestration-manifest.template.yml",
    "skills/themis/assets/claim-ledger.template.md",
    "skills/themis/assets/source-register.template.md",
    "skills/themis/assets/citation-audit.template.md",
    "skills/themis/assets/peer-review-report.template.md",
    "skills/themis/assets/agent-core-memory.template.md",
    "skills/themis/assets/agent-spawn-request.template.md",
    "skills/themis/assets/research-clean-final.template.md",
    "skills/themis/assets/search-query.template.md",
    "skills/themis/assets/candidate-source.template.md",
    "skills/themis/assets/retrieval-log.template.md",
    "skills/themis/assets/gate-card.template.md",
    "skills/themis/assets/stage-card.template.md",
    "skills/themis/assets/revision-loop.template.md",
    "skills/themis/scripts/validate_public_output.py",
    "skills/themis/scripts/validate_claim_ledger.py",
    "skills/themis/scripts/validate_retrieval_contract.py",
    "skills/themis/scripts/validate_orchestration_manifest.py",
]

def main() -> None:
    failures = []

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            failures.append(f"missing file: {rel}")

    skill_path = ROOT / "skills/themis/SKILL.md"
    if not skill_path.exists():
        failures.append("missing skills/themis/SKILL.md")
    else:
        skill = skill_path.read_text(encoding="utf-8", errors="ignore")

        required_phrases = [
            "Citation Auditor",
            "Peer Reviewer",
            "No verified citation, no evidence claim",
            "Internal labels must not appear in clean drafts or final reports",
            "spawn new specialist agents",
        ]

        for phrase in required_phrases:
            if phrase not in skill:
                failures.append(f"SKILL.md missing phrase: {phrase}")

    if failures:
        print("FAIL: research mode incomplete")
        for failure in failures:
            print(f"- {failure}")
        sys.exit(1)

    print("PASS: Themis research mode is valid")

if __name__ == "__main__":
    main()
