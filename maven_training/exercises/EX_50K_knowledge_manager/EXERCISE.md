# EX_50K — Advanced Knowledge Management
## Practical Exercise — TM-50K Proficiency

| Field | Value |
|-------|-------|
| **Version** | 1.0 — March 2026 |
| **Prerequisite** | TM-40K complete (Go on file); TM-50K course completion; Workshop and AIP Logic (AI-augmented tagging) access confirmed |
| **Duration** | 4–5 hours (typically executed Day 3 of TM-50K) |
| **Environment** | MSS Workshop, Ontology read, AIP Logic (for AI-augmented tagging task); see ENVIRONMENT_SETUP.md |
| **Companion TM** | TM_50K_KNOWLEDGE_MANAGER_ADVANCED.md |
| **Syllabus** | SYLLABUS_TM50K |
| **Exams** | EXAM_TM50K_POST |

## SCENARIO

You are the senior Knowledge Manager for USAREUR-AF. A brigade is preparing for rotation and the current KM system has three known problems:

1. The document taxonomy is inconsistent — documents are tagged across 6 different schemes with no controlled vocabulary
2. The unit continuity package is incomplete — key role transitions are undocumented and three critical SOPs are not linked to the relevant Ontology objects
3. The AI-augmented tagging pipeline is producing low-confidence results for 30% of incoming documents

You have one day to audit, remediate, and document the KM system architecture before the rotation.

**Training environment:** All documents, tags, and taxonomy data are synthetic. No operational content is used.

## TASK LIST

### Task 1 — Taxonomy Audit and Remediation (75 min)

Using the `km_corpus_synthetic/` (40 documents with mixed tagging):

- [ ] Audit the existing tags: identify how many distinct tagging schemes are present; produce a deduplication map showing which tags in different schemes refer to the same concept
- [ ] Design a controlled vocabulary with no more than 4 top-level categories and 3–5 sub-tags per category, covering all 40 documents; document the rationale for each top-level category
- [ ] Re-tag all 40 documents using the new controlled vocabulary (apply tags in Workshop; do not manually type — use the taxonomy tool)
- [ ] Identify 3 documents where the correct classification is ambiguous; for each, document the ambiguity and the tag you applied with a rationale

| Standard | Criteria |
|----------|----------|
| **Go** | Deduplication map produced; controlled vocabulary documented with rationale (≤4 top-level, ≤5 sub-tags each); all 40 documents re-tagged in Workshop; 3 ambiguous documents identified with documented rationale |
| **No-Go** | No deduplication map; controlled vocabulary exceeds 4 top-level categories or has no rationale; fewer than 40 documents tagged; ambiguous documents not identified |

### Task 2 — Unit Continuity Package Completion (60 min)

Using the `unit_continuity_template.md` and the provided role roster (`rotation_roster_synthetic.csv`):

- [ ] Identify which of the 3 critical SOPs are not linked to their relevant Ontology objects; create the link for each (document the Ontology object type and property used)
- [ ] For each of the 5 key role transitions in the roster, document: current incumbent, incoming replacement (if known), critical knowledge held by incumbent (3–5 bullets), and recommended handoff action
- [ ] Produce a continuity risk register: for each role, classify transition risk as low/medium/high and provide a one-sentence mitigation; flag any role with no identified replacement as high-risk

| Standard | Criteria |
|----------|----------|
| **Go** | All 3 SOP-Ontology links created with documentation; all 5 role transitions documented with the four required elements; continuity risk register complete with risk classification and mitigation for each role |
| **No-Go** | Any SOP link missing or not documented; fewer than 5 roles documented; risk register absent or missing risk classification |

### Task 3 — AI-Augmented Tagging Audit and Correction (60 min)

The training environment includes an AI-augmented tagging pipeline in AIP Logic that has been producing low-confidence results for ~30% of incoming documents:

- [ ] Review the pipeline configuration: identify at least 2 configuration issues contributing to low confidence (see ENVIRONMENT_SETUP.md for planted issues)
- [ ] For each configuration issue, document: (a) the issue, (b) why it reduces tagging confidence, and (c) the recommended correction
- [ ] Apply at least 1 of the 2 corrections in AIP Logic configuration (the second may be documented as a recommendation requiring C2DAO support)
- [ ] Re-run the pipeline on the 12 low-confidence documents; record whether confidence improved for the documents where the applied correction was relevant

| Standard | Criteria |
|----------|----------|
| **Go** | At least 2 configuration issues identified with impact and correction described; at least 1 correction applied in AIP Logic; pipeline re-run completed with results recorded |
| **No-Go** | Fewer than 2 issues identified; no corrections applied (documented only); pipeline not re-run after correction |

### Task 4 — Knowledge System Health Assessment (45 min)

Produce the quarterly KM System Health Assessment for the brigade:

- [ ] Taxonomy coverage: what percentage of documents are tagged using the new controlled vocabulary (post-Task 1)?
- [ ] Continuity coverage: what percentage of key roles have a complete handoff package (post-Task 2)?
- [ ] Pipeline confidence: what is the average tagging confidence across the full corpus post-correction (post-Task 3)?
- [ ] Risk summary: identify the 2 highest-risk items in the KM system at this moment (any category); for each, document the risk, likelihood, impact, and recommended action
- [ ] Format as a 1-page health assessment suitable for the brigade S6 (non-technical audience)

| Standard | Criteria |
|----------|----------|
| **Go** | All three coverage metrics computed from actual task results (not estimated); 2 highest-risk items identified with likelihood/impact/action; formatted for non-technical audience |
| **No-Go** | Metrics estimated rather than computed; fewer than 2 risk items; formatted for technical audience (jargon not explained) |

## EVALUATOR NOTES

**Scoring:** 4 tasks. Go on 3 of 4 = overall Go. No-Go on Task 1 = automatic No-Go (taxonomy is the core KM competency at TM-50K level).

### Pre-Exercise Checklist

- [ ] Confirm Workshop access and Ontology read for participant
- [ ] Confirm AIP Logic access for Task 3 (configuration review and correction)
- [ ] Load `km_corpus_synthetic/` (40 documents with pre-existing mixed tags), `unit_continuity_template.md`, `rotation_roster_synthetic.csv` into training project
- [ ] Configure AIP Logic tagging pipeline with planted issues (see below) — confirm it is running but producing low-confidence results before exercise day
- [ ] Place blank KM Health Assessment template in participant's project folder
- [ ] Verify SOP-Ontology links are missing for 3 of the 5 SOPs in the training project (these are the ones participants must create in Task 2)

### Pre-Planted AIP Logic Configuration Issues (Task 3)

| Issue | Location | Description |
|-------|----------|-------------|
| Issue 1 | Taxonomy prompt | The tagging prompt provides the old (pre-remediation) taxonomy — the AI is trying to map documents to the inconsistent 6-scheme taxonomy, which produces low confidence on documents that don't fit |
| Issue 2 | Confidence threshold | Confidence threshold set to 0.90 (too high) — documents that would acceptably be tagged at 0.75 confidence are being flagged as low-confidence; threshold should be 0.70–0.75 for this document type |

Issue 1 requires updating the prompt (participant can apply directly). Issue 2 requires a configuration setting change that may require C2DAO access (acceptable to document as recommendation if the UI does not expose the threshold directly).

### Common Failure Modes

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | Controlled vocabulary designed without deduplication map first | Ask: "How do you know you've captured all existing tag concepts?" — taxonomy without deduplication risks losing concepts |
| Task 1 | More than 4 top-level categories in new vocabulary | Standard: ≤4 top-level. Ask participant to consolidate before marking Go |
| Task 2 | Role handoff documented at bullet-point level without actionable handoff actions | Ask: "What specifically does the incoming person need to do in week 1?" — bullets alone without action = partial credit only |
| Task 3 | Only 1 configuration issue identified | Both are required; evaluator may probe: "Is there anything else about the pipeline configuration that could affect confidence besides the prompt?" |
| Task 4 | Metrics estimated rather than pulled from task results | Ask: "What number did you actually get in Task 1?" — estimates are not acceptable for a health assessment |
