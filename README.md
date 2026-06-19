<p align="center">
  <img src="assets/THEMIS.png" alt="Themis Logo" width="600">
</p>

<h1 align="center">Themis</h1>

<p align="center">
  <img src="https://img.shields.io/github/stars/arsenelupin14/THEMIS?style=flat-square" alt="GitHub stars">
  <img src="https://img.shields.io/github/forks/arsenelupin14/THEMIS?style=flat-square" alt="GitHub forks">
  <img src="https://img.shields.io/github/watchers/arsenelupin14/THEMIS?style=flat-square" alt="GitHub watchers">
  <img src="https://img.shields.io/github/v/release/arsenelupin14/THEMIS?style=flat-square" alt="GitHub release">
  <img src="https://img.shields.io/github/license/arsenelupin14/THEMIS?style=flat-square" alt="License">
  <img src="https://img.shields.io/github/actions/workflow/status/arsenelupin14/THEMIS/validate.yml?branch=main&style=flat-square" alt="CI">
</p>

<p align="center">
  <strong>Research workrooms for AI agents.</strong>
</p>

<p align="center">
  A GitHub-installable agent skill for evidence-aware research synthesis, citation auditing, adversarial review, and clean final reports.
</p>

Themis is an AI agent skill that converts a single general-purpose assistant into a structured, multi-agent research workflow. By establishing clear boundaries, it turns messy reasoning into an auditable process covering evidence retrieval, citation verification, adversarial review, and clean final reports.

## Why Themis

While a standard LLM agent workflow can produce research-style outputs quickly, the underlying reasoning is often difficult to audit. Claims may lack backing, citation verification can be weak, and agents might agreeic-ally collapse too early.

Themis implements an agentic research workflow that makes structured research synthesis explicit. It forces the system to separate evidence retrieval from citation verification, maintain a claim ledger and a source register, and run peer review gates before compiling a clean final report.

## How it works

Themis coordinates the research workroom using a structured orchestration manifest that drives the following stages:

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

To manage this multi-agent research workflow, Themis defines four core management roles alongside 2–5 task-specific domain agents:

* **Master Research**: Oversees the workspace, manages the revision loop, approves dynamic specialist spawning, and compiles the final supervisor-grade final report.
* **Evidence Retrieval Agent**: Responsible for formulating search queries and gathering candidate sources for claims that require citations.
* **Citation Auditor**: Conducts metadata checks and citation audits to ensure the source supports the claims.
* **Peer Reviewer**: Audits methodology, conducts overclaiming reviews, and checks readiness for the public output gate.

## Evidence and citation flow

Themis establishes a strict division between information gathering and validation:

1. **Retrieval**: The Evidence Retrieval Agent queries host-provided search or database tools to compile candidates.
2. **Citation Verification**: The Citation Auditor verifies candidate metadata and updates the claim ledger with verified or quarantined statuses.
3. **Peer Review**: The Peer Reviewer conducts a source-grounded review to verify formatting, citation alignment, and check for overclaiming.
4. **Final Compilation**: Once all gates pass, the Master Research agent writes the clean final report.

## Repository layout

The installable skill package lives in:

```text
skills/themis/
```

The `.agents/` directory is maintainer-only automation and is not required by end users.

## Install

Themis can be installed as a Codex skill, Claude Code skill, Gemini CLI skill, or Antigravity skill.

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
python skills/themis/scripts/validate_public_output.py tests/fixtures/valid-clean-final.md
python skills/themis/scripts/validate_claim_ledger.py tests/fixtures/valid-claim-ledger.md
python skills/themis/scripts/validate_orchestration_manifest.py tests/fixtures/valid-orchestration-manifest.yml
```

## Safety

Inspect skills before installing.

Themis validation scripts are local, deterministic helpers that do not require network access. Retrieval tasks are performed by the host agent when search or database tools are provided.

## License

MIT License.
