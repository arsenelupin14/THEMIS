# Research Mode

Themis research mode turns a user topic into a controlled research workroom.

Research mode is not a paper generator by default.
It first creates a research dossier, then a clean final report only after citation and peer review gates.

## Required agents

Every research workroom must include:

- Master Research
- Evidence Retrieval Agent
- Citation Auditor
- Peer Reviewer
- Domain Agents

## Master Research

Mission:
Coordinate the workroom, approve agent spawning, resolve conflicts, and decide what enters the clean final report.

Authority:
May reject role outputs, quarantine claims, request citation repair, and spawn new specialist agents.

## Evidence Retrieval Agent

Mission:
Search for and gather candidate sources relevant to claims that require external backing.

Authority:
May only populate candidate source logs and search queries; must not mark claims as verified.

## Citation Auditor

Mission:
Verify that every evidence-bearing claim has a real, relevant, and correctly represented source.

Authority:
May downgrade [EVIDENCE] to [UNVERIFIED], [NEEDS-CITATION], [DISPUTED], or [QUARANTINED].

## Peer Reviewer

Mission:
Check methodological soundness, overclaiming, unsupported reasoning, citation mismatch, and final-report readiness.

Authority:
May block the final report until claims are repaired.

## Domain Agents

Mission:
Analyze the topic from a specific domain perspective.

Domain agents must maintain their own core memory and submit claims into the claim ledger.

## Output modes

Internal output may contain IDs and labels.
Public output must be clean and human-facing.
