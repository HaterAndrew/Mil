# EX-40B — AI Engineer
## Practical Exercise — TM-40B Proficiency

**Version 1.0 | March 2026**
**Prerequisite:** TM-40B, AI Engineer Technical Manual (and TM-10 through TM-30)
**Duration:** 3–4 hours
**Environment:** MSS with AIP Logic, Agent Studio access; Python Transforms enabled (see ENVIRONMENT_SETUP.md)

---

## SCENARIO

The S2 section has a large corpus of synthetic intelligence summaries (free text). You are the AI Engineer tasked to: build a retrieval pipeline over the corpus, create an AIP Logic workflow that classifies summaries by event type, and stand up a basic Agent Studio agent that answers natural-language queries about the corpus.

**Training dataset:** ~200 synthetic INTSUM documents (plain text, unclassified).

---

## TASK LIST

### Task 1 — Ingest and Chunk Documents (30 min)
- [ ] Ingest the synthetic INTSUM corpus into Foundry as a dataset
- [ ] Build a chunking transform: split each document into ~500-token chunks with metadata (doc_id, date, event_type_label)
- [ ] Verify chunk count and schema
- **Go:** Chunks dataset created; metadata columns present; no empty chunks
- **No-Go:** Chunking fails or metadata is missing

### Task 2 — Build a Retrieval Pipeline (45 min)
- [ ] Generate embeddings for the chunk dataset using an available embedding model in AIP
- [ ] Store embeddings in a vector index
- [ ] Run a test query and confirm top-3 relevant chunks are returned
- **Go:** Vector index builds; test query returns plausible top-3 results
- **No-Go:** Index fails to build or query returns nonsensical results

### Task 3 — AIP Logic Classification Workflow (45 min)
- [ ] Build an AIP Logic workflow that: takes a document as input, calls an LLM to classify it into one of 5 event types (define your taxonomy), outputs the classification label and confidence
- [ ] Test on 10 documents; report accuracy vs. the pre-labeled ground truth
- **Go:** Workflow runs; classification accuracy ≥ 70% on test set
- **No-Go:** Workflow errors or accuracy < 50%

### Task 4 — Agent Studio Basic Agent (60 min)
- [ ] Create an Agent Studio agent with access to the vector index and document metadata
- [ ] Define at least 2 tools: (1) search corpus, (2) retrieve document by ID
- [ ] Test: ask the agent a question answerable from the corpus; verify it cites source documents
- **Go:** Agent answers the test question; citations reference real document IDs
- **No-Go:** Agent hallucinates citations or cannot use tools

### Task 5 — Governance Documentation (20 min)
- [ ] Document: model/embedding used, retrieval parameters, known failure modes
- [ ] Add a data lineage note: source → chunks → embeddings → index
- **Go:** Documentation is present and accurate
- **No-Go:** Documentation absent or contains factual errors

---

## EVALUATOR NOTES

> **TODO:** Complete after dry run. Task 4 is environment-sensitive — confirm Agent Studio is enabled and vector index is accessible. Pre-label 10 ground truth documents for Task 3 accuracy check.

Scoring: 5 tasks. Go on 4 of 5 = overall Go. No-Go on Task 2 or Task 4 = automatic No-Go.

---

## ENVIRONMENT SETUP

> **TODO:** Load synthetic INTSUM corpus. Enable AIP Logic and Agent Studio for training accounts. Pre-label 10 documents with ground truth event types. Document in `ENVIRONMENT_SETUP.md`.
