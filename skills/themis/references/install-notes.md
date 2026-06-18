# Install Notes

Themis is designed as an installable agent skill.

Primary distribution:
- GitHub repository
- gh skill when supported
- manual install fallback

The product lives in:

skills/themis/SKILL.md

Do not install the development-only .agents directory as part of the end-user skill.

## Security

Inspect skills before installing.
Themis does not require network access.
Themis scripts must be deterministic local validation helpers only.
Themis must not contain hidden commands, destructive shell operations, or credential exfiltration behavior.
