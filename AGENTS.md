# AGENTS.md

This repository builds Themis.

Themis is an installable AI agent skill pack.
Do not turn it into a standalone CLI, web app, or multi-agent framework.

## Product boundary

The product lives in:

skills/themis/SKILL.md

Supporting files:

skills/themis/references/
skills/themis/assets/
skills/themis/scripts/

The `.agents/` directory is development-only and exists to help maintainers build Themis in parallel.

## Rules

- Do not copy code, prompts, or assets from MiroFish.
- Do not claim prediction capability.
- Do not expose or invent private chain of thought.
- Do not add network dependencies.
- Do not add paid API requirements.
- Do not add destructive scripts.
- Do not allow empty agreement in Themis examples.

## Required checks

Before finalizing changes, run:

```bash
pytest
python skills/themis/scripts/validate_themis_skill.py
```
