# Themis Orchestration Protocol

Themis defines a structured multi-stage contract (`THEMIS_ORCHESTRATION_V1`) to manage the progression of a research task.

## Orchestration Stages

1. **intake**: Analyze the user's research request, extract boundaries, and define scope.
2. **workroom_init**: Create the `.themis/workrooms/<topic-slug>/` directory structure.
3. **core_agent_spawn**: Spawn the core management roles: Master Research, Evidence Retrieval Agent, Citation Auditor, and Peer Reviewer.
4. **domain_agent_spawn**: Initialize 2–5 domain-specific specialist agents based on the research topic.
5. **independent_research**: Domain agents conduct independent analysis and draft core arguments.
6. **claim_ledger_build**: Consolidate key claims from all agents into the unified claim ledger.
7. **evidence_retrieval**: Evidence Retrieval Agent gathers search queries and candidates for claims requiring sources.
8. **retrieval_gate**: Evaluate if candidates cover all required claims. If retrieval fails or tools are missing, flag claims as unverified.
9. **citation_audit_gate**: Citation Auditor evaluates candidate sources, verifies metadata, and sets verification status.
10. **dynamic_spawn_check**: Master Research evaluates if additional domain expertise is needed to resolve conflicts or gaps.
11. **revision_loop**: Agents refine claims based on citation audits and peer comments.
12. **peer_review_gate**: Peer Reviewer audits methodology, check for overclaiming, and issues a pass/fail verdict.
13. **public_output_gate**: Final check to ensure all internal formatting/labels are removed from the draft.
14. **final_report**: Generate the clean user-facing research report.
