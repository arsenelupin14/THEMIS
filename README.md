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

## Why Themis

While general-purpose AI agents can produce research-style outputs quickly, their internal reasoning and source dependencies are often difficult to review. Themis introduces a structured research workflow that separates retrieval from verification, monitors claims and citations, and enforces an explicit review process before generating final reports.

## How it works

Themis runs the research workroom through a sequential multi-stage pipeline:

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

## Research roles

Every research workroom requires four core management roles alongside 2–5 task-specific domain agents:

* **Master Research**: Coordinates the workroom, manages the revision loop, approves dynamic spawning, and synthesizes the final report.
* **Evidence Retrieval Agent**: Formulates queries and gathers candidate sources for claims requiring external evidence.
* **Citation Auditor**: Performs metadata checks on candidate sources and audits whether they support the associated claims.
* **Peer Reviewer**: Audits methodology, checks for overclaiming, and verifies final-report readiness.

## Evidence and citation flow

To ensure auditability, Themis decouples search from validation:

1. **Retrieval**: The Evidence Retrieval Agent finds candidate space or literature sources when tools are available.
2. **Auditing**: The Citation Auditor verifies source metadata and audits whether the claims match the source.
3. **Review**: The Peer Reviewer checks the methodology, formatting, and potential overclaiming.
4. **Approval**: The Master Research agent compiles the verified findings into the clean draft.

## Repository layout

The installable Themis skill lives in:

```text
skills/themis/
```

The `.agents/` directory contains maintainer-only Antigravity build automation and is not part of the end-user skill package.

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

## Safety

Inspect skills before installing.

Themis validation scripts are local, deterministic helpers. They do not require network access. Retrieval tasks are performed by the host agent when search or database tools are provided.

## License

MIT License.
