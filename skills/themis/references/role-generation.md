# Role Generation

Themis roles are generated from the task.

Do not use fixed software roles unless the task is actually software-related.

## Role generation rules

Create roles based on:

- domain
- deliverable
- risk profile
- required evidence
- implementation surface
- user constraints
- failure modes

## Minimum role card

Each generated role must include:

- ROLE
- MISSION
- AUTHORITY
- MUST_CHALLENGE
- MUST_NOT_DO
- REQUIRED_INPUTS
- OUTPUT_SCHEMA
- HANDOFF_TARGETS
- STOP_CONDITION

## Role count

Default: 3–5 roles.
Maximum: 7 roles.

Use fewer roles for small tasks.
Use more roles only when the task has materially different risk surfaces.

## Role usefulness gate

A role is valid only if it can contribute at least one of:

- constraint
- risk
- test
- contract
- decision
- evidence requirement
- unresolved question

If a role cannot contribute, remove it.
