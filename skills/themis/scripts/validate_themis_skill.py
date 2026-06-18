#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / "skills" / "themis" / "SKILL.md"

REQUIRED_FILES = [
    "skills/themis/SKILL.md",
    "skills/themis/references/protocol.md",
    "skills/themis/references/role-generation.md",
    "skills/themis/references/challenge-loop.md",
    "skills/themis/references/memory-compression.md",
    "skills/themis/references/anti-sycophancy.md",
    "skills/themis/references/simulation.md",
    "skills/themis/references/install-notes.md",
    "skills/themis/assets/role-card.template.md",
    "skills/themis/assets/role-report.template.md",
    "skills/themis/assets/conflict-card.template.md",
    "skills/themis/assets/shared-state.template.md",
    "skills/themis/assets/final-report.template.md",
    "skills/themis/assets/simulation-case.template.md",
]

FORBIDDEN_CLAIMS = [
    "predict everything",
    "guaranteed",
    "100% accurate",
    "private chain-of-thought",
    "copy mirofish",
]

def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)

def main() -> None:
    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if not path.exists():
            fail(f"missing required file: {rel}")

    text = SKILL.read_text(encoding="utf-8")

    if not text.startswith("---"):
        fail("SKILL.md missing YAML frontmatter")

    if "name: themis" not in text:
        fail("SKILL.md missing name: themis")

    if "description:" not in text:
        fail("SKILL.md missing description")

    required_phrases = [
        "Do not simply agree",
        "No empty agreement",
        "Generate 3–7 task-specific functional roles",
        "Compressed state",
    ]

    for phrase in required_phrases:
        if phrase not in text:
            fail(f"SKILL.md missing required phrase: {phrase}")

    all_text = "\n".join(
        path.read_text(encoding="utf-8", errors="ignore")
        for path in ROOT.rglob("*.md")
    ).lower()

    for claim in FORBIDDEN_CLAIMS:
        if claim in all_text:
            fail(f"forbidden claim found: {claim}")

    print("PASS: Themis skill structure is valid")

if __name__ == "__main__":
    main()
