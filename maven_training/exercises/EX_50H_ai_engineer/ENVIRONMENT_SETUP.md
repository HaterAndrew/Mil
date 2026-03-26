# ENVIRONMENT SETUP — EX_50H Advanced AI Engineer (SL 5H)

**Companion resources:** TM_50H_AI_ENGINEER_ADVANCED.md | SYLLABUS_TM50H | EXAM_TM50H_POST

## Environment Type

MSS Code Workspace (Python) and AIP Logic (multi-agent orchestration). Standard viewer or Workshop-only access is insufficient for this exercise. Both Code Workspace and AIP Logic must be confirmed operational before exercise day.

## Required Access

| Account | Role |
|---------|------|
| Participant | Code Workspace (Python), AIP Logic (create and execute multi-agent workflows), Ontology read, training project read/write, Workshop publish |
| Evaluator | Training project read (to receive Task 4–5 Workshop submissions), AIP Logic read (to review agent configurations) |

**Lead time:** AIP Logic access must be requested from C2DAO no fewer than **7 duty days** before exercise. Confirm access with a test workflow creation before the exercise day — do not assume access is active based on prior provisioning.

## Pre-Load Instructions

### 1. Synthetic RAG Corpus

Load `EX_50H_AI_Training_Data/rag_corpus_synthetic/` into training project (50 documents):

| Attribute | Specification |
|-----------|---------------|
| Document count | 50 synthetic staff memoranda and doctrine excerpts |
| Average length | 400–800 words per document |
| Topics | Unit readiness, logistics synchronization, operations planning, force protection (all synthetic, non-operational) |
| Format | Plain text (.txt) or PDF — evaluator selects based on participant environment capabilities |
| Metadata | `doc_id`, `title`, `date`, `source_type` (memo/doctrine/report) |

Place in: `[Training Project]/EX_50H/source/rag_corpus/`

### 2. Evaluation Question Set

Load `EX_50H_AI_Training_Data/eval_questions.json` (10 questions):

```json
[
  {
    "query_id": "Q01",
    "question": "What is the readiness threshold for a BCT to be considered mission capable?",
    "ground_truth_answer": "...",
    "relevant_doc_ids": ["doc_012", "doc_031"]
  },
  ...
]
```

The ground truth answers are calibrated against the synthetic corpus — the RAG system should achieve ≥70% faithfulness on a well-configured system. Questions Q07 and Q09 are intentionally difficult (ambiguous retrieval) to surface failure modes.

Place in: `[Training Project]/EX_50H/eval/`

### 3. Python Environment Verification

Verify before exercise day:

```python
import sentence_transformers
import faiss            # or chromadb, qdrant-client — any vector store accepted
import evaluate
import bert_score
import nltk
import openai           # or anthropic — for LLM-as-judge faithfulness check
print("All imports OK")
```

### 4. AIP Logic Multi-Agent Template

Pre-create a blank two-agent AIP Logic workflow in the training project with:
- Agent 1 slot: "Research Agent" (label only, no configuration)
- Agent 2 slot: "Synthesis Agent" (label only, no configuration)
- Connection between agents: blank (participant must configure)

This gives participants a starting scaffold. Do not pre-configure tools or prompts.

### 5. Blank Governance Checklist

Place `usareur_ai_governance_checklist_blank.md` in participant's project folder before exercise start:

Sections:
1. Data Provenance (source, curation, update cadence)
2. Model Card (embedding model name, version, limitations, applicable use cases)
3. Failure Mode Register (table: failure mode, likelihood, impact, mitigation)
4. Human Oversight Plan (supported decisions, human-in-the-loop decisions, escalation path)
5. Signature block (analyst name, date, evaluator name)

## Environment URL

```
[Insert training MSS tenant URL here]
```

## Scoring Sheet Reference

Evaluators record task Go/No-Go on standard EX_50H Evaluation Form (available from training NCO). For Task 3, record the evaluation harness metrics table in the notes — this is the primary evidence of Go for Task 3. Overall Go/No-Go, participant name, evaluator name, and date required for training record submission.

## Notes

- The LLM-as-judge faithfulness check (Task 3) requires an API call to an LLM (Claude or equivalent); confirm the training environment has an available API key or on-prem model endpoint before exercise day
- If AIP Logic is unavailable on exercise day (environment issue, not participant access), substitute Task 2 with a Python-based multi-agent implementation using LangGraph or equivalent; note the deviation on the evaluation form
- All corpus documents are synthetic; field names and formatting mirror operational document types for training realism but contain no actual staff memoranda or operational content
- Participant should not be informed which evaluation questions are "difficult" (Q07, Q09) before the exercise
