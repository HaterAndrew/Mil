<!-- MAVEN TRAINING CORPUS — CDA REFERENCE MATERIAL
     Source: odt_workspace/docs/architecture/gdap/adr-0001-llamaindex-boundaries.md
     Supports: TM-40H (AI Engineer), TM-40I (ML Engineer), TM-40L (Software Engineer), TM-50H/I/L (Advanced)
     Type: Architecture Decision Record — GDAP ADR-0001
-->

# ADR-0001: LlamaIndex vs DuckDB Responsibility Boundaries

Date: 2026-03-07
Status: Accepted

## Context

GDAP already uses DuckDB (`GraphStore`) as a durable, queryable system of record for doctrine atoms, alignment outputs, temporal history, and DVEE entities.

The LlamaIndex roadmap introduces a retrieval and orchestration layer (ingestion pipeline, indexes, query engines, tools, and evaluation).

Without explicit boundaries, we risk duplicate truth stores, data drift, and unclear recovery procedures.

## Decision

**DuckDB remains the source of truth.**
**LlamaIndex indexes are derived, rebuildable serving artifacts.**

### DuckDB Owns

- Canonical doctrine records: `documents`, `sections`, `elements`
- Temporal lineage and auditability: `version_diffs`, `concept_drift`, `superseded_at`
- Coalition/domain analytics: `alignment_pairs`, `authority_*`, `exploitability_scores`, `coalition_seams`
- Read-only SQL query surface and deterministic filtering

### LlamaIndex Owns

- Document-to-node transformations for retrieval
- Embedding generation and vector/sparse/graph index serving
- Query orchestration: routing, post-processing, synthesis, tool composition
- Evaluation and observability hooks for retrieval/response quality

## Consequences

**Positive:**
- Clear failure domain separation
- Deterministic rebuild path from DuckDB to indexes
- Simplified compliance/audit story

**Tradeoffs:**
- Requires robust index lifecycle management
- Requires explicit sync/rebuild triggers for version changes

## Implementation Notes

- All LlamaIndex nodes must carry GDAP primary identity metadata (`unique_id`, nation/doc/version/temporal fields).
- Index writes are idempotent and derived from DuckDB snapshots/diffs.
- No workflow may mutate DuckDB through LlamaIndex agent tools.

## See Also

- [GDAP_PERSISTENCE_STRATEGY.md](./GDAP_PERSISTENCE_STRATEGY.md) — concrete persistence layers and rebuild policy
- [GDAP_ACCEPTANCE_TESTS.md](./GDAP_ACCEPTANCE_TESTS.md) — Section H: Operations and Lifecycle gates
