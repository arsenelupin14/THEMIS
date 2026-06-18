# Simulation: OSS Security Tool

PROMPT:
Design an open-source repo scanner for risky AI GitHub workflows.

GENERATED WORKROOM:
- Security Reviewer
- GitHub Actions Specialist
- OSS Maintainer
- QA Skeptic
- Safety/Abuse Reviewer

CHALLENGE:
Safety/Abuse Reviewer challenges Security Reviewer:
[RISK] The scanner must not generate exploit payloads or trigger workflows.

DECISION:
The MVP performs local-only static analysis of workflow YAML files.

THEMIS_STATE_V1

G: OSS scanner for risky AI GitHub workflows
D: security/devtools
C: defensive-only, local-only
R: Security, GitHub Actions, OSS, QA, Safety
F: workflows can contain risky triggers and permissions
A: static analysis is acceptable for MVP
Q: SARIF export now or later
K: useful security output vs misuse risk
V: no exploit generation, no GitHub API in MVP
T: define rules for pull_request_target, issue_comment, write permissions
X: false positives can reduce trust
N: write rule taxonomy
