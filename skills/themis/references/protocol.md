# Themis Protocol

Themis is a dynamic workroom protocol for AI agents.

It converts a raw user request into a structured review process:

1. Intake
2. Role synthesis
3. Independent review
4. Cross-role challenge
5. Conflict resolution
6. Supervisor final report
7. Shared memory compression

## Phase 0 — Intake

Extract:

- user goal
- domain
- constraints
- non-goals
- unknowns
- expected output
- available evidence
- missing evidence

Do not assume the user is correct.
Do not reject without reason.
Classify assumptions explicitly.

## Phase 1 — Role synthesis

Generate 3–7 task-specific functional roles.

Roles must be useful review lenses, not fictional personalities.

Bad:
- Wizard
- Genius
- Funny Guy
- Agreeable Assistant

Good:
- Security Reviewer
- Product Strategist
- QA Skeptic
- Legal/Risk Reviewer
- Infrastructure Planner
- User Researcher

Weird user-requested roles are allowed only if normalized into useful functions.

Example:
Chaos Monkey → failure-mode reviewer.
Philosopher → assumptions and ethics reviewer.
Angry Investor → commercial viability critic.
Librarian → knowledge organization reviewer.

## Phase 2 — Independent review

Each role must review independently before responding to other roles.

Every role must produce:
- position
- findings
- risks
- questions
- contracts
- challenges
- handoff
- confidence

## Phase 3 — Cross-role challenge

Roles may challenge each other only through:

- contract mismatch
- missing dependency
- feasibility risk
- safety risk
- evidence gap
- testability issue
- scope conflict

No theatrical debate.
No empty agreement.

## Phase 4 — Arbitration

The supervisor resolves conflicts.

Possible outcomes:
- decision accepted
- decision rejected
- decision revised
- blocker escalated to user
- uncertainty preserved as open question

## Phase 5 — Compression

The supervisor writes a compact shared state using THEMIS_STATE_V1.

The compressed state must be short enough to be reused in later turns.
