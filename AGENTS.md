# AGENTS.md

This repository builds Themis.

Themis is an installable AI agent skill pack.
Do not turn it into a standalone CLI, web app, or multi-agent framework.

## Product boundary

The product lives in:

skills/themis/SKILL.md

Supporting files:

skills/themis/references/
skills/themis/assets/
skills/themis/scripts/

The `.agents/` directory is development-only and exists to help maintainers build Themis in parallel.

## Product boundary clarification

The `.agents/` directory is development-only.

Do not treat `.agents/agents` or `.agents/commands` as part of the installable Themis skill.

The only installable skill package is:

skills/themis/

## v0.2 research hardening rules

Themis is now research-specialist by default.

Do not allow public drafts or final reports to contain internal workroom labels such as:
- FACT-...
- CONFLICT-...
- CONTRACT-...
- DECISION-...
- TASK-...
- RISK-...
- QUESTION-...
- NEXT-...
- THEMIS_STATE_V1
- ROLE:
- POSITION:
- HANDOFF:
- CLAIM_ID
- SOURCE_ID
- SOURCE_STATUS
- [EVIDENCE]
- [ASSUMPTION]
- [UNKNOWN]
- [NEEDS-CITATION]

These labels are allowed only in internal workroom files, agent memory, claim ledgers, and citation audit files.

Every research workroom must include:
- Master Research
- Evidence Retrieval Agent
- Citation Auditor
- Peer Reviewer

Every source-required claim must pass citation audit before entering public output.

## Rules

- Do not copy code, prompts, or assets from MiroFish.
- Do not claim prediction capability.
- Do not expose or invent private chain of thought.
- Do not add network dependencies.
- Do not add paid API requirements.
- Do not add destructive scripts.
- Do not allow empty agreement in Themis examples.

## Required checks

Before finalizing changes, run:

```bash
pytest
python skills/themis/scripts/validate_themis_skill.py
python skills/themis/scripts/validate_research_mode.py
python skills/themis/scripts/validate_retrieval_contract.py
```
