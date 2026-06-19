# Internal vs Public Output

Themis uses internal labels to coordinate research agents.

These labels are useful internally but must not appear in user-facing drafts or final reports.

## Internal-only labels

- FACT-...
- CONFLICT-...
- CONTRACT-...
- DECISION-...
- TASK-...
- RISK-...
- QUESTION-...
- NEXT-...
- CLAIM_ID
- SOURCE_ID
- THEMIS_STATE_V1
- ROLE:
- POSITION:
- HANDOFF:
- CONFIDENCE:
- [EVIDENCE]
- [ASSUMPTION]
- [UNKNOWN]
- [NEEDS-CITATION]

## Allowed locations

Internal labels may appear in:

- agents/*/core_memory.md
- internal/*
- claims/*
- sources/*
- peer_review/*

## Forbidden locations

Internal labels must not appear in:

- drafts/clean_draft.md
- final/final_report.md
- any polished paper draft
- any user-facing executive summary

## Public output style

Public reports must use normal prose, clean headings, and normal citations.

Bad:
[FACT-ML-1] Standard statistical bounds assume i.i.d. data.

Good:
Standard statistical learning bounds often rely on assumptions that are poorly matched to chaotic solar dynamics.
