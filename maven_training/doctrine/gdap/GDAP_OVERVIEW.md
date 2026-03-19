<!-- MAVEN TRAINING CORPUS — CDA REFERENCE MATERIAL
     Source: odt_workspace/docs/architecture/gdap/overview.md
     Supports: TM-40H (AI Engineer), TM-40M (ML Engineer), TM-40K (Knowledge Manager), TM-40L (Software Engineer), TM-50H/I/K/L (Advanced)
     Type: Architecture Reference — GDAP Overview
-->

# GDAP — Global Doctrine Alignment Platform

Bi-temporal coalition knowledge graph for doctrine analysis.

---

## LlamaIndex Retrieval Stack

Phase 3 retrieval primitives live under `gdap.llamaindex`:

- Dense semantic retrieval (`VectorStoreIndex`)
- Sparse lexical retrieval (`BM25SparseRetriever`)
- Reciprocal-rank fusion (`QueryFusionRetriever`)
- Property-graph construction (`PropertyGraphIndex`)

Example usage:

```python
from llama_index.core import Document
from gdap.llamaindex import HashEmbedding, build_retrieval_stack, route_query

docs = [
    Document(
        id_="US:ADP-TEST:ch1:001:1.0",
        text="The commander retains risk acceptance authority.",
        metadata={"unique_id": "US:ADP-TEST:ch1:001:1.0", "source_nation": "US"},
    )
]

stack = build_retrieval_stack(
    documents=docs,
    embedding_model=HashEmbedding(embed_dim=96),
    include_property_graph=True,
)

results = stack.fusion_retriever.retrieve("risk acceptance authority")
route = route_query("Show authority chain dependencies")
```

---

## API Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| `/health` | GET | Health check |
| `/stats` | GET | Knowledge graph table counts |
| `/elements` | GET | Query doctrine elements (filters: nation, content_type, wff, search) |
| `/elements/{id}` | GET | Single element by unique ID |
| `/divergences` | GET | Cross-national divergences |
| `/align` | POST | Run alignment analysis between two nations |
| `/diffs` | GET | Version diffs |
| `/drift` | GET | Concept drift records |
| `/data-map` | GET | Doctrine-to-data mapping coverage |
| `/authority/{doc_id}` | GET | Authority graph for a document |
| `/exploitability` | GET | DVEE exploitability scores |
| `/seams` | GET | Coalition seams |
| `/query` | POST | Raw read-only SQL |

---

## Related Documents

- [GDAP_VISION.md](./GDAP_VISION.md) — Full platform vision, 10 use-case domains, DVEE
- [GDAP_PERSISTENCE_STRATEGY.md](./GDAP_PERSISTENCE_STRATEGY.md) — DuckDB canonical truth, LlamaIndex derived artifacts
- [GDAP_ACCEPTANCE_TESTS.md](./GDAP_ACCEPTANCE_TESTS.md) — P0/P1/P2 release gates
- [GDAP_ADR_0001_LLAMAINDEX.md](./GDAP_ADR_0001_LLAMAINDEX.md) — DuckDB vs LlamaIndex boundary decision
