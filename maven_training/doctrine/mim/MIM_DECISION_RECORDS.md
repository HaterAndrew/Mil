<!-- MAVEN TRAINING CORPUS — CDA REFERENCE MATERIAL
     Source: odt_workspace/docs/architecture/mim/decision-records.md
     Supports: TM-40H (AI Engineer), TM-40L (Software Engineer), TM-50H/L (Advanced)
     Type: Architecture Decision Record — MIM ADR Structure
-->

# ADR: Decision Records for MIM Repository and Packages

## Context

The MIM repository is a monorepo with multiple installable packages. Past architectural decisions are spread across issues and docs, which makes it hard to discover why key structural choices were made.

## Decision

- Store repository-level ADRs under `docs/` at the repo root.
- Require each installable package to include at least one ADR under `docs/` describing its scope and boundaries.
- Keep ADRs short, focused, and updated as decisions evolve.

## Consequences

- Cross-cutting decisions are discoverable from the root.
- Package-specific decisions stay close to their code.
- Contributors have a consistent place to record architectural changes.

## Status

Accepted
