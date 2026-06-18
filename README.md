# Themis

Structured dynamic workrooms for AI agents.

Themis is a GitHub-installable AI agent skill that turns a single obedient agent into a structured dynamic workroom.

It dynamically generates task-specific roles, forces useful disagreement, maintains compact shared memory, resolves conflicts, and returns a supervisor-grade final report.

## What Themis is

- Agent skill pack
- Dynamic role-generation protocol
- Anti-sycophancy workflow
- Structured disagreement system
- Memory compression protocol
- Simulation examples

## What Themis is not

- Not a standalone CLI
- Not a web app
- Not a multi-agent framework
- Not a MiroFish clone
- Not a prediction engine
- Not a database or RAG system

## Install

### GitHub CLI

```bash
gh skill install <owner>/THEMIS themis --agent codex
gh skill install <owner>/THEMIS themis --agent claude-code
gh skill install <owner>/THEMIS themis --agent gemini
gh skill install <owner>/THEMIS themis --agent antigravity
```

`gh skill` is preview, so manual install scripts are also provided.

### Manual install

```bash
./install/install-codex.sh
./install/install-claude-code.sh
./install/install-antigravity.sh
./install/install-opencode.sh
```

## Usage

Ask your agent:

```text
Use Themis to review this product idea.
```

or

```text
Run a Themis workroom for this architecture plan.
```

## Core behavior

Themis performs:

1. Intake
2. Role synthesis
3. Independent review
4. Cross-role challenge
5. Conflict resolution
6. Supervisor report
7. State compression

## MiroFish inspiration

Themis is conceptually inspired by MiroFish’s use of seed information, agent generation, memory, simulation, and report generation.

Themis does not replicate or use MiroFish code, prompts, assets, or implementation.

## Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
python skills/themis/scripts/validate_themis_skill.py
```

## Safety

Inspect skills before installing.
Themis scripts are deterministic local helpers.
Themis does not require network access.
Themis does not execute destructive shell operations.
