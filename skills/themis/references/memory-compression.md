# Memory Compression

Themis uses compact public memory.

It must not expose private chain of thought.
It must not store full transcripts unless explicitly needed.
It stores the public work state.

## THEMIS_STATE_V1

G: goal
D: domain
C: constraints
O: expected output
R: roles
F: facts
A: assumptions
Q: open questions
K: conflicts
V: decisions
T: tasks
X: risks
N: next actions

## Compression rules

- Prefer short clauses.
- Remove repeated phrasing.
- Preserve decisions and unresolved blockers.
- Preserve evidence labels.
- Preserve risk labels.
- Do not compress away uncertainty.
- Do not invent facts.

## Maximum default size

Target: under 800 words.
Hard limit: under 1,500 words unless the user asks for a full record.
