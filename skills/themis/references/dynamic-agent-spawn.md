# Dynamic Agent Spawn Protocol

Themis starts with core research agents and may spawn new specialists when discussion expands.

## Initial agents

Default initial research agents:

- Master Research
- Evidence Retrieval Agent
- Citation Auditor
- Peer Reviewer
- 2–5 domain agents based on the topic

## Spawn conditions

A new agent may be spawned only if one of these conditions is met:

1. A claim requires expertise outside existing agents.
2. A conflict remains unresolved after one challenge round.
3. Citation audit exposes a new technical domain.
4. The topic expands into a field that changes the validity of the argument.
5. Master Research approves that the new agent will reduce uncertainty.

## Spawn request schema

SPAWN_REQUEST:
PROPOSED_AGENT:
REASON:
TRIGGERING_CLAIMS:
EXPECTED_CONTRIBUTION:
RISK_IF_NOT_SPAWNED:
APPROVED_BY_MASTER_RESEARCH:
STATUS:

## Anti-sprawl rule

Do not spawn agents for novelty.
Do not spawn agents that cannot add evidence, risk analysis, or methodological correction.

Default maximum total agents: 10.
