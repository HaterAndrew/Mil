# ENVIRONMENT SETUP — EX-50K Advanced Knowledge Manager (TM-50K)

**Companion resources:** TM_50K_KNOWLEDGE_MANAGER_ADVANCED.md | SYLLABUS_TM50K | EXAM_TM50K_POST

## Environment Type

MSS Workshop, Ontology (read), and AIP Logic (configuration review and limited edit). No Code Workspace or pipeline write access required. AIP Logic access is needed for Task 3 — confirm this separately from Workshop access.

## Required Access

| Account | Role |
|---------|------|
| Participant | Workshop (create/edit views, apply tags), Ontology read (Task 2 link creation), AIP Logic (view and edit pipeline configuration — limited), training project read/write |
| Evaluator | Training project read (to verify submitted products), AIP Logic editor (to configure planted issues before exercise) |

**Lead time:** AIP Logic access for Task 3 must be confirmed no fewer than **7 duty days** before exercise. Workshop and Ontology access are standard and typically available within 2–3 days. Do not assume AIP Logic access is bundled with Workshop access.

## Pre-Load Instructions

### 1. Synthetic KM Corpus

Load `EX-50K_KM_Training_Data/km_corpus_synthetic/` (40 documents):

| Attribute | Specification |
|-----------|---------------|
| Document count | 40 synthetic documents |
| Document types | SOPs (12), after-action reviews (10), training schedules (8), logistics memoranda (10) |
| Pre-existing tags | Mixed across 6 different schemes (see below) |
| Ambiguous documents | At least 3 documents deliberately span two categories — identify these in advance for evaluator reference |

**Pre-existing tag schemes (intentionally inconsistent):**

| Scheme | Tags | Notes |
|--------|------|-------|
| Scheme 1 | OPS, LOG, INTEL, TRAIN | Abbreviation-based |
| Scheme 2 | Operations, Logistics, Intelligence, Training | Full-word version of Scheme 1 |
| Scheme 3 | G3, G4, G2, G1 | Staff section-based |
| Scheme 4 | SOP, AAR, SCHED, MEMO | Document type-based |
| Scheme 5 | Priority-1, Priority-2, Priority-3 | Priority-based (no content category) |
| Scheme 6 | (untagged — 8 documents have no tags) | — |

The deduplication map the participant must produce should show at minimum: Scheme 1 ↔ Scheme 2 (synonyms), Scheme 3 ↔ Scheme 1 (partial overlap), Scheme 4 (orthogonal — document type vs. content type).

### 2. Unit Continuity Materials

Load `EX-50K_KM_Training_Data/unit_continuity_template.md` — standard USAREUR-AF unit continuity package template with sections pre-populated for this rotation scenario.

Load `EX-50K_KM_Training_Data/rotation_roster_synthetic.csv`:

| Field | Description |
|-------|-------------|
| `role_id` | Role identifier (R01–R05) |
| `role_title` | Position title |
| `incumbent` | Current holder (synthetic name) |
| `replacement` | Incoming replacement (some blank — indicating no replacement identified) |
| `transition_date` | Planned rotation date |

**SOP-Ontology link status (pre-exercise configuration):**

| SOP | Ontology Object | Link Status |
|-----|----------------|-------------|
| SOP-001 (Equipment Readiness Reporting) | Equipment Object Type | Linked |
| SOP-002 (Maintenance Request Procedure) | Maintenance Request Object Type | **Missing — participant must create** |
| SOP-003 (LOGSTAT Submission) | LOGSTAT Object Type | Linked |
| SOP-004 (Personnel Accountability) | Personnel Object Type | **Missing — participant must create** |
| SOP-005 (Incident Reporting) | Incident Object Type | **Missing — participant must create** |

Verify these link statuses before exercise day by checking the Ontology in the training project.

### 3. AIP Logic Tagging Pipeline

Configure the AI-augmented tagging pipeline in AIP Logic with planted issues before exercise day:

**Pipeline design:**
- Input: documents from `km_corpus_synthetic/`
- Processing: LLM-based taxonomy tagger (synthetic model endpoint)
- Output: suggested tags with confidence scores, written to document metadata

**Planted Issue 1 — Stale taxonomy in prompt:**
Update the tagger prompt to reference the old 6-scheme taxonomy (not the new controlled vocabulary). The prompt should contain a tag list matching Schemes 1–4 above. This causes the model to attempt to apply inconsistent tags, producing low-confidence results on documents that span categories.

**Planted Issue 2 — Threshold too high:**
Set the pipeline's confidence threshold to 0.90. Documents with model confidence between 0.70 and 0.89 will be flagged as low-confidence and held for human review. The correct threshold for this document type is 0.70–0.75.

Verify before exercise day that ~30% of documents are being held as low-confidence (flagged for human review). If the percentage is significantly different, adjust the threshold parameter.

### 4. Blank Templates

Place the following in participant's project folder before exercise:

- `km_health_assessment_blank.md` — sections: Taxonomy Coverage, Continuity Coverage, Pipeline Confidence, Risk Summary, Signature block
- Standard USAREUR-AF unit continuity package (populated header section for this rotation scenario)

## Environment URL

```
[Insert training MSS tenant URL here]
```

## Scoring Sheet Reference

Evaluators record task Go/No-Go on standard EX-50K Evaluation Form (available from training NCO). For Task 1, attach or photograph the controlled vocabulary design and deduplication map. For Task 3, record which configuration issues were identified and which correction was applied. Overall Go/No-Go, participant name, evaluator name, and date required for training record submission.

## Notes

- The taxonomy ambiguous documents should not be identified for the participant before the exercise — part of the task is identifying which documents are ambiguous
- AIP Logic editing for Task 3: updating the prompt (Issue 1) should be accessible via standard AIP Logic config interface; adjusting the confidence threshold (Issue 2) may require C2DAO backend access — if the threshold is not UI-editable, accept documented recommendation as Go for that element
- All corpus documents are synthetic; they are formatted to resemble operational SOPs, AARs, and memoranda but contain no real unit data or operational content
- The 6-scheme tagging disorder is intentionally severe — a real KM corpus at this level would typically have 2–3 competing schemes, not 6; the exercise uses 6 to ensure the deduplication task requires substantive analysis
