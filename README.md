# Themis

![GitHub stars](https://img.shields.io/github/stars/arsenelupin14/THEMIS?style=flat-square)
![GitHub forks](https://img.shields.io/github/forks/arsenelupin14/THEMIS?style=flat-square)
![GitHub watchers](https://img.shields.io/github/watchers/arsenelupin14/THEMIS?style=flat-square)
![GitHub release](https://img.shields.io/github/v/release/arsenelupin14/THEMIS?style=flat-square)
![License](https://img.shields.io/github/license/arsenelupin14/THEMIS?style=flat-square)
![CI](https://img.shields.io/github/actions/workflow/status/arsenelupin14/THEMIS/validate.yml?branch=main&style=flat-square)

Research workrooms for AI agents.

Themis is a GitHub-installable agent skill for evidence-aware research synthesis, citation auditing, adversarial review, and clean final reports.

Themis turns a single general-purpose AI agent into a structured research workroom. It creates task-specific specialist roles, separates evidence retrieval from citation verification, records claims and sources, forces useful disagreement, reviews overclaiming, maintains compact workroom memory, and produces a clean supervisor-grade final report.

## Why Themis exists

General-purpose AI agents can produce plausible research-style outputs quickly, but their reasoning is often hard to audit. Claims may be unsupported, citations may be weak, internal assumptions may leak into final prose, and disagreement may collapse into agreement too early.

Themis makes the research process explicit.

It requires agents to separate claims from sources, retrieval from verification, disagreement from final synthesis, and internal workroom state from public output.

## Core model

Themis uses a structured workroom model:

```text
Intake
  ↓
Workroom initialization
  ↓
Specialist role synthesis
  ↓
Independent review
  ↓
Claim ledger
  ↓
Evidence retrieval
  ↓
Retrieval gate
  ↓
Citation audit
  ↓
Adversarial challenge
  ↓
Peer review
  ↓
Public output gate
  ↓
Clean final report
```

## Required research roles

In research mode, Themis requires:

* Master Research
* Evidence Retrieval Agent
* Citation Auditor
* Peer Reviewer
* 2–5 task-specific domain agents

The roles are intentionally separated.

Evidence Retrieval Agent finds candidate sources.

Citation Auditor verifies source metadata and whether the source actually supports the claim.

Peer Reviewer checks methodology, overclaiming, and final-report readiness.

Master Research coordinates the workroom, resolves conflicts, approves specialist spawning, and owns the final report.

## What Themis is

Themis is:

* an AI agent skill pack
* a research workroom protocol
* an evidence-aware synthesis workflow
* a citation-audit scaffold
* an adversarial review system
* a compact workroom-memory protocol
* a public-output cleanup boundary
* a portable orchestration contract

## What Themis is not

Themis is not:

* a standalone CLI
* a web app
* a full multi-agent runtime framework
* an autonomous scientist
* an experiment runner
* a database or RAG system
* a prediction engine
* a truth machine

Themis does not execute experiments. It does not guarantee that a host agent will follow the protocol. It does not prove that a claim is true. It makes the workroom process explicit and auditable.

## Repository layout

The installable Themis skill lives in:

```text
skills/themis/
```

The `.agents/` directory is maintainer-only automation for repository development. It is not required by end users and is not part of the installable Themis skill package.

```text
THEMIS/
  skills/
    themis/
      SKILL.md
      references/
      assets/
      scripts/

  examples/
    research-solar-physics-v02/

  tests/
    fixtures/

  install/

  .agents/
    agents/
    commands/
```

## Install

Using GitHub skill install:

```bash
gh skill install arsenelupin14/THEMIS themis --agent codex
gh skill install arsenelupin14/THEMIS themis --agent claude-code
gh skill install arsenelupin14/THEMIS themis --agent gemini
gh skill install arsenelupin14/THEMIS themis --agent antigravity
```

Manual install scripts are also provided:

```bash
./install/install-codex.sh
./install/install-claude-code.sh
./install/install-antigravity.sh
./install/install-opencode.sh
```

## Usage

Ask your agent:

```text
Use Themis to run a research workroom for this topic.
```

or:

```text
Use Themis to audit this technical report for unsupported claims, citation issues, and overclaiming.
```

or:

```text
Run a Themis workroom for this architecture plan and return a supervisor-grade final report.
```

## Research mode

Research mode creates a structured workroom with mandatory gates:

```text
claim ledger
evidence retrieval
retrieval gate
citation audit
peer review
public output gate
final report
```

A claim cannot enter the final report as an evidence-backed statement unless it passes citation audit.

If no retrieval tools are available, source-required claims must remain `NEEDS_SOURCE`, `UNVERIFIED`, or `QUARANTINED`.

## Evidence retrieval boundary

Themis separates retrieval from verification.

The Evidence Retrieval Agent may search for candidate sources when the host environment provides web, browser, file-search, scholarly search, or dataset tools.

The Evidence Retrieval Agent must not mark claims as `VERIFIED`.

Only the Citation Auditor may mark a claim as `VERIFIED`.

## Public output boundary

Themis allows internal labels inside workroom files, but not in public reports.

Internal markers such as `FACT-*`, `CONFLICT-*`, `CLAIM_ID`, `SOURCE_ID`, `THEMIS_STATE_V1`, `[EVIDENCE]`, and role handoff notes are allowed only in internal workroom state, claim ledgers, source registers, citation audits, and orchestration logs.

They must not appear in clean drafts or final reports.

## Validation

Development setup:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Run validation:

```bash
pytest
python skills/themis/scripts/validate_themis_skill.py
python skills/themis/scripts/validate_research_mode.py
python skills/themis/scripts/validate_retrieval_contract.py
python skills/themis/scripts/validate_public_output.py examples/research-solar-physics-v02/clean-final-sample.md
python skills/themis/scripts/validate_claim_ledger.py examples/research-solar-physics-v02/claim-ledger-sample.md
python skills/themis/scripts/validate_orchestration_manifest.py tests/fixtures/valid-orchestration-manifest.yml
```

## Known limitations

Themis is currently a skill-level protocol, not an independent runtime.

Current limitations:

* no independent execution runtime
* no benchmark dataset yet
* no benchmark-proven hallucination reduction yet
* no experiment execution
* no guarantee that every host agent will follow the protocol
* retrieval quality depends on available host tools
* citation verification depends on source access and host-agent discipline

These are explicit design limitations, not hidden claims.

## Roadmap

```text
v0.2.0
Research orchestration, evidence retrieval, citation firewall, peer review gates, public output validation.

v0.2.1
Overclaiming rubric and source-support rubric.

v0.2.2
Small Themis-Bench evaluation set.

v0.3.0
Optional runtime adapter for enforcing THEMIS_ORCHESTRATION_V1 as a state machine.

v0.4.0
Measured evaluation of citation hallucination and overclaiming reduction.
```

## Safety

Inspect skills before installing.

Themis validation scripts are deterministic local helpers. They do not require network access and do not execute destructive shell operations.

Retrieval is a host-agent behavior. Validation scripts must remain local and deterministic.

## License

MIT License.
