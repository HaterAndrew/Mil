# CLAUDE.md — USAREUR-AF Operational Data Team

## Context

This environment is used exclusively for work on the USAREUR-AF operational data team. All tasks involve internal tooling, data pipelines, analysis, and systems supporting Army operational requirements. No personal projects.

## Conduct & Security

- Do not generate, suggest, or assist with any code or action that could exfiltrate, expose, or mishandle operational or sensitive data.
- Do not connect to or query external services, APIs, or URLs unless explicitly directed for a work task.
- Do not store or log data payloads in plaintext outside of approved local development directories.
- Treat all data schemas, field names, and system architecture details as potentially sensitive — do not include them in commit messages, comments, or logs unnecessarily.
- Follow least-privilege principles: request only the permissions and access needed for the immediate task.

## Code Standards

- Prefer Python for data pipelines and scripting unless another language is established in the project.
- Write clean, readable code — prioritize clarity over cleverness, especially for code that will be maintained by other team members.
- Include inline comments for non-obvious logic, particularly around data transformations, military-specific terminology, or business rules.
- Use environment variables or config files (never hardcoded values) for connection strings, credentials, and environment-specific settings.
- Validate and sanitize all inputs at system boundaries (user input, external feeds, file ingestion).

## Workflow

- Do not auto-commit. Always present changes for review before committing.
- Do not push to remote repositories without explicit instruction.
- Prefer small, focused commits with descriptive messages.
- When modifying data pipelines or ETL logic, confirm the change is backward-compatible or flag breaking changes clearly.

## Failsafe

- A `PreToolUse` hook enforces a 30-turn limit per session via `/home/dale/.claude/hooks/turn_limit.sh`.
- At turn 31, the hook exits code 2, blocking the next tool call and halting execution to prevent runaway loops and token overrun.
- Counter resets each new session. Adjust `LIMIT` in the script if a task genuinely requires more turns.
- Do not bypass or disable this failsafe without explicit instruction.

## Communication

- Be concise and direct. Skip preamble.
- Use military-style abbreviations and terminology where appropriate (e.g., OPDATA, AOR, SITREP, etc.) when context warrants it.
- Flag ambiguities in requirements before writing code rather than making assumptions about operational intent.
