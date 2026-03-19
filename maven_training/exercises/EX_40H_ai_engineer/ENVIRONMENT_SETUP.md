# ENVIRONMENT SETUP — EX_40H AI Engineer

**Track:** EX_40H — AI Engineer (TM-40H) | **Prerequisite:** TM-30 REQUIRED | **Continuation:** TM-50H — Advanced AI Engineer
**Companion exams:** EXAM_TM40H_PRE (administer before exercise), EXAM_TM40H_POST (administer after exercise)

## Environment Type
MSS with AIP Logic, Agent Studio, and Python Transforms enabled. Embedding model must be available.

## Required Access

| Account | Role |
|---------|------|
| Training accounts | AIP Logic author, Agent Studio create, Python Transform create/edit |
| Evaluator account | Viewer on participant AIP Logic workflows and agent definitions |

## Pre-Load Instructions

### 1. Corpus
Load `EX_40H_intsum_corpus/` directory (200 .txt files) from training data package:
- Each file: 300–800 words, one synthetic intelligence summary
- Naming convention: `INTSUM_YYYYMMDD_NNN.txt`
- Load as a dataset of text records with fields: `doc_id`, `date`, `content`
- Place in: `[Training Project]/EX_40H/corpus/`

### 2. Ground Truth Labels (Task 3)
Pre-label 10 documents with event type for the accuracy check:

| File | Contents |
|------|----------|
| `EX_40H_GroundTruth_10docs.csv` | `doc_id`, `event_type` |

Event type taxonomy (define before the exercise):

| Category | Label |
|----------|-------|
| Patrol contact | `PATROL_CONTACT` |
| IED event | `IED_EVENT` |
| Cache discovery | `CACHE_DISCOVERY` |
| Observation report | `OBSERVATION_REPORT` |
| Admin | `ADMIN` |

Hand the ground truth file to the participant at the start of Task 3 only.

### 3. AIP Logic
- Confirm at least one LLM (e.g., GPT-4o or equivalent) is available to training accounts
- Confirm prompt templates can be authored without admin privileges

### 4. Agent Studio
- Confirm Agent Studio is enabled for training accounts
- Confirm vector index type is supported for agent tool use
- Optionally pre-create a test vector index to verify the workflow end-to-end

### 5. Accuracy Threshold Note
Task 3 Go threshold: ≥70% accuracy on 10 labeled documents (7/10 correct).
If the available LLM performs poorly on the taxonomy (< 60% in testing), adjust the taxonomy or use a simpler classification scheme — re-test before each exercise run.

## Environment URL
```
[Insert training MSS tenant URL here]
```

## Notes
- Do not pre-load embeddings — participants must build the pipeline themselves
- If Agent Studio is unavailable, Task 4 cannot be completed — escalate to training management before the exercise
