<!-- MAVEN TRAINING CORPUS — CDA REFERENCE MATERIAL
     Source: odt_workspace/docs/architecture/cda/agents/overview.md
     Supports: TM-40H (AI Engineer), TM-40M (ML Engineer), TM-40K (Knowledge Manager), TM-40L (Software Engineer)
     Type: Architecture Doctrine — Agent Reference
-->

# Agent Doctrine

These documents are the doctrinal reference layer for architecture, ontology, pipeline, and identity work in the ODT workspace.

They are not executable agent definitions. Use these docs for:
- CDA-derived operating principles and constraints
- Semantic and ontology modeling guidance
- Ingestion and entity-resolution doctrine
- Shared language across architecture, pipelines, products, and AI work

## Contents

- [CDA_AGENTS_CORE_PRINCIPLES.md](./CDA_AGENTS_CORE_PRINCIPLES.md) — cross-cutting bedrock principles (universal)
- [CDA_AGENTS_ONTOLOGY_ENGINEER.md](./CDA_AGENTS_ONTOLOGY_ENGINEER.md) — specializes the semantic layer
- [CDA_AGENTS_ENTITY_RESOLUTION.md](./CDA_AGENTS_ENTITY_RESOLUTION.md) — specializes governed identity work
- [CDA_AGENTS_INGESTION_INTEGRATION.md](./CDA_AGENTS_INGESTION_INTEGRATION.md) — specializes pipeline execution against the ontology contract

## Placement

This material is cross-layer doctrine. It is broader than the pipeline layer and applies to architecture, pipelines, products, and AI work equally.

## Hierarchy

```
CDA_AGENTS_CORE_PRINCIPLES.md          ← universal bedrock
  ├── CDA_AGENTS_ONTOLOGY_ENGINEER.md      — specializes Principles 3, 7, 8, 9, 10, 11
  ├── CDA_AGENTS_INGESTION_INTEGRATION.md  — specializes Principles 2, 4, 8, 10, 12
  └── CDA_AGENTS_ENTITY_RESOLUTION.md      — specializes Principles 8, 5, 12
```

If a specialized document ever conflicts with a core principle, **the core principle governs**.
