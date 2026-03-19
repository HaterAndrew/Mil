# EX_50H — Advanced AI Engineering
## Practical Exercise — TM-50H Proficiency

| Field | Value |
|-------|-------|
| **Version** | 1.0 — March 2026 |
| **Prerequisite** | TM-40H complete (Go on file); TM-50H course completion; AIP Logic and Code Workspace access confirmed |
| **Duration** | 6–8 hours (typically executed Day 5 of TM-50H) |
| **Environment** | MSS Code Workspace (Python), AIP Logic (multi-agent orchestration), Ontology access; see ENVIRONMENT_SETUP.md |
| **Companion TM** | TM_50H_AI_ENGINEER_ADVANCED.md |
| **Syllabus** | SYLLABUS_TM50H |
| **Exams** | EXAM_TM50H_POST |

## SCENARIO

You are the senior AI Engineer for an USAREUR-AF theater data team. Your team has been tasked with building a production-ready enterprise Retrieval-Augmented Generation (RAG) system to serve a multi-functional staff. The system must be deployed, evaluated against a defined quality standard, and documented for handoff.

Additionally, you are responsible for configuring a two-agent orchestration pattern (a research agent and a synthesis agent) and completing a governance review before the system can be presented to leadership for approval.

**Training environment:** All documents, queries, and evaluation datasets are synthetic. No operational or classified content is used.

## TASK LIST

### Task 1 — Enterprise RAG System Build (120 min)

Using the provided synthetic document corpus (`rag_corpus_synthetic/`):

- [ ] Implement document ingestion pipeline: chunking strategy documented (chunk size, overlap, rationale), embedding model selected and documented
- [ ] Build a retrieval layer: configure top-k retrieval with a reranking step; document the retrieval parameters selected
- [ ] Implement a generation step: prompt template designed for the operational use case (staff briefing support); system prompt includes explicit instructions for citing source documents
- [ ] Run the provided 10-question evaluation set against the RAG system; compute and record precision@5 and answer faithfulness for each query

| Standard | Criteria |
|----------|----------|
| **Go** | Ingestion pipeline documented (chunking + embedding rationale); retrieval with reranking configured; system prompt requires source citation; evaluation metrics computed for all 10 queries |
| **No-Go** | No chunking rationale documented; no reranking step; system prompt does not require citations; evaluation not completed or fewer than 10 queries run |

### Task 2 — Multi-Agent Orchestration (90 min)

Configure the two-agent system in AIP Logic:

**Agent 1 — Research Agent:** Given a staff query, retrieves relevant passages from the RAG corpus and returns a list of retrieved excerpts with source attributions.

**Agent 2 — Synthesis Agent:** Given the Research Agent's retrieved excerpts, produces a synthesized staff-ready response with inline citations.

- [ ] Configure Agent 1 with the RAG retrieval tool as its only tool; set max_iterations and tool_call budget
- [ ] Configure Agent 2 to accept Agent 1's output as context; design the synthesis prompt for a general staff audience (no unexplained jargon)
- [ ] Run 3 test queries through the full pipeline; record the retrieved excerpts and the synthesized response for each
- [ ] Identify and document at least one failure mode observed during testing (hallucination, citation error, retrieval miss, etc.)

| Standard | Criteria |
|----------|----------|
| **Go** | Both agents configured with documented parameters; 3 test queries run with results recorded; at least one failure mode identified and documented |
| **No-Go** | Agent configuration not documented; fewer than 3 test queries; no failure mode identified or documented |

### Task 3 — Evaluation Harness (60 min)

- [ ] Build a reusable evaluation harness that accepts: a query, a ground-truth answer, and the RAG system's generated answer; computes and records: BLEU (or equivalent lexical metric), faithfulness check (LLM-as-judge or BERTScore), and citation presence flag
- [ ] Run the 10-question evaluation set through the harness; produce an evaluation report table (query ID, metric values, pass/fail per metric)
- [ ] Identify 2 queries where the system underperformed; propose one specific prompt engineering or retrieval configuration change for each

| Standard | Criteria |
|----------|----------|
| **Go** | Harness accepts all three inputs and computes all three metrics; evaluation report table complete for all 10 queries; 2 underperforming queries identified with specific improvement proposals |
| **No-Go** | Only one metric computed; evaluation table incomplete; no specific improvement proposals |

### Task 4 — AI Governance Review (45 min)

Complete the USAREUR-AF AI Governance Checklist for the RAG system:

- [ ] Data provenance: document the source, curation method, and update cadence for the training corpus
- [ ] Model card: document the embedding model (name, version, known limitations, applicable use cases)
- [ ] Failure mode register: document at least 3 failure modes (from testing and known LLM failure patterns); for each, document likelihood, impact, and mitigation
- [ ] Human oversight plan: describe what decisions the system supports, what decisions require a human in the loop, and what the escalation path is when the system produces an uncertain or conflicting output
- [ ] Checklist signed and submitted to evaluator via Workshop

| Standard | Criteria |
|----------|----------|
| **Go** | All four checklist sections completed; failure mode register has ≥3 entries with likelihood/impact/mitigation; human oversight plan explicitly names human-in-the-loop decision points |
| **No-Go** | Any section absent; failure mode register has fewer than 3 entries; human oversight plan does not identify specific decision points |

### Task 5 — Leadership Brief Preparation (30 min)

Prepare a 5-slide leadership brief (Workshop or PowerPoint) covering:

1. System overview: what it does and who it serves
2. Evaluation results: key metrics, strengths, and limitations
3. Failure modes and mitigations (top 3)
4. Human oversight and escalation path
5. Recommendation: deploy as-is, deploy with restrictions, or defer with rationale

- [ ] All five slides present with the required content
- [ ] Brief is written for a GO/SES audience — no unexplained technical terms
- [ ] Recommendation includes a rationale grounded in the evaluation results

| Standard | Criteria |
|----------|----------|
| **Go** | All five slides present; GO/SES language used throughout; recommendation tied explicitly to evaluation results |
| **No-Go** | Missing slide(s); technical jargon without explanation; recommendation not grounded in evaluation results |

## EVALUATOR NOTES

**Scoring:** 5 tasks. Go on 4 of 5 = overall Go. No-Go on Task 1 or Task 4 = automatic No-Go (core engineering and governance standards).

### Pre-Exercise Checklist

- [ ] Confirm AIP Logic access provisioned for participant — minimum 7 duty days prior; test that multi-agent workflows can be created and executed
- [ ] Confirm Code Workspace (Python) access with required packages: sentence-transformers, faiss-cpu (or equivalent), evaluate, bert-score, nltk
- [ ] Load `rag_corpus_synthetic/` (50 documents) and 10-question evaluation set into training project — verify all documents load and retrieval returns results
- [ ] Place blank USAREUR-AF AI Governance Checklist in participant's project folder
- [ ] Confirm evaluator account can receive Workshop link submission (Task 4 and Task 5)

### Common Failure Modes

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | No chunking rationale documented | Ask: "Why did you choose this chunk size?" — undocumented = No-Go on that criterion even if technically correct |
| Task 1 | System prompt does not require citations | Probe: ask the participant to show the system prompt; if citation instruction is absent, Task 1 No-Go on that criterion |
| Task 2 | Agent 2 prompt designed for technical audience | Ask participant to read the synthesized response aloud and identify any term a staff officer would not know — if present, must revise |
| Task 2 | No failure mode identified during testing | Most common issue when evaluation queries are easy; evaluator may hint: "Did the system ever retrieve a passage that wasn't relevant?" |
| Task 3 | Only BLEU computed | BERTScore or LLM-as-judge faithfulness is required; BLEU alone is insufficient for faithfulness assessment |
| Task 4 | Human oversight plan is generic | Ask: "Show me a specific decision a staff officer should never delegate to this system." If participant cannot name one, plan is insufficiently specific |
| Task 5 | Recommendation not tied to evaluation results | Ask: "Which specific evaluation result drove this recommendation?" If no connection, revise required before Go |
