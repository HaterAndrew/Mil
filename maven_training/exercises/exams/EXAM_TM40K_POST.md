# POST-TEST — TM-40K: KNOWLEDGE MANAGER
## Maven Smart System (MSS) — USAREUR-AF

| | |
|---|---|
| **Course** | TM-40K: Knowledge Manager |
| **Form** | Post-Test |
| **Level** | TM-40K (Specialist) |
| **Audience** | KMOs / 37F / knowledge officers; prerequisite: TM-10 + TM-20 |
| **Time Allowed** | 45 minutes |
| **Passing Score** | 70% (42/60) |

---

## INSTRUCTIONS

This assessment evaluates mastery of course learning objectives. A passing score of 70% is required to receive credit. Complete independently without reference to training materials.

---

## SECTION 1 — MULTIPLE CHOICE

*Circle the letter of the best answer. (2 points each)*

**1. The five Object Types required in a TM-40K knowledge architecture are:**

A. Report, Summary, Record, Document, Brief
B. Document, Lesson, AAR, SOP, ExpertiseProfile
C. Knowledge, Source, Topic, User, Archive
D. File, Tag, Category, Review, Publish

**2. In a Workshop AAR submission form, "required-field validation" means:**

A. The form requires a digital signature before submission
B. The system prevents submission if mandatory fields (unit, date, category, observer) are empty, and displays a clear error message identifying the missing fields
C. Required fields are highlighted in a different color as a reminder
D. The form is routed to the KM officer for completion if any fields are blank

**3. A lessons-learned intake pipeline must route incoming lessons based on unit, classification level, and echelon. This is called:**

A. Tagging
B. Archiving
C. Distribution routing logic
D. Knowledge validation

**4. Per TM-40K, an AIP Logic summarization workflow that processes AAR text MUST include:**

A. A minimum of three AI inference steps to validate consistency
B. A mandatory human review gate — the output remains in Draft status until a KM officer reviews and approves it
C. Automatic publishing after a 24-hour review window if no feedback is received
D. A classification downgrade step before the AIP workflow processes the text

**5. The human review gate for AIP-generated knowledge summaries is:**

A. Required only for SECRET-level documents
B. Configurable based on operational tempo — commanders can waive it for routine lessons
C. NON-NEGOTIABLE — all AIP-generated content remains Draft until an authorized KM officer approves it
D. Required only for documents that will be distributed outside the brigade

**6. An AIP prompt that is producing inconsistent entity extractions (unit names formatted differently across outputs) should be improved by:**

A. Switching to a different LLM model
B. Adding explicit output format instructions and few-shot examples to the prompt, then testing against a sample set and iterating
C. Post-processing the outputs with a normalization script
D. Increasing the LLM temperature setting to produce more varied outputs

**7. A knowledge browser application must support which of the following capabilities per TM-40K?**

A. Full-text keyword search, filter by tag/unit/date, and drill-down to lesson detail page
B. Browsing by document type only, with a single export-all function
C. Real-time search against the live ADRP database
D. Automatic translation of lessons from partner nation languages

**8. A PCS knowledge transfer package that consists only of a generic "key things to know" document without project-specific details is considered:**

A. Acceptable as a starting point for the incoming Soldier
B. Non-compliant with TM-40K Chapter 9 — it fails the specificity requirement
C. Acceptable if accompanied by a handoff brief
D. Compliant if reviewed and approved by the KM officer

**9. Privacy Act requirements for ExpertiseProfile objects in MSS apply because:**

A. ExpertiseProfiles are classified at SECRET by default
B. ExpertiseProfiles may contain PII (name, role, unit, contact information, specific expertise) about individual Soldiers, requiring access controls and handling per the Privacy Act
C. Army Regulation 25-400-2 requires Privacy Act statements for all digital records systems
D. ExpertiseProfile data is derived from personnel records and is automatically FOUO

**10. The correct status workflow for a lessons-learned item in MSS is:**

A. Submitted → Published → Archived
B. Draft → KM Review → Published (with optional Archived terminal state)
C. Open → In Progress → Closed
D. Identified → Validated → Distributed → Closed

**11. A new AAR submission comes in with the category field tagged as "LOGISTICS" but the content clearly relates to communications. Per TM-40K, the KM officer should:**

A. Reject the AAR and require the submitter to resubmit with the correct category
B. Correct the category during the review step before approving and publishing
C. Publish the AAR as submitted — content review is not within the KM officer's scope
D. Archive the AAR until the submitter confirms the correct category

**12. A lessons-learned intake pipeline that automatically assigns tags based on keyword matching would be classified as:**

A. A fully automated publish workflow requiring no human review
B. An AI-assisted pre-tagging step — tags are suggested automatically but must be reviewed and confirmed by the KM officer before the lesson is published
C. A validated tagging approach that eliminates the need for human categorization review
D. A prohibited use of AI for knowledge management per TM-40K

**13. Your brigade's knowledge browser displays lessons from 2019 prominently because they have the most views. Current personnel cannot easily find recent lessons. The MOST appropriate fix is:**

A. Delete all lessons older than 3 years
B. Add a date filter and configure the default sort order to show most recent lessons first
C. Archive all lessons older than 2 years
D. Create separate knowledge browser pages for each year

**14. Per TM-40K Section 8-1, which of the following is required before aggregating individual Soldiers' ExpertiseProfiles into a searchable directory?**

A. Commander approval in a signed memorandum
B. A Privacy Act review to ensure the data collection, storage, and distribution comply with Privacy Act requirements and authorized system of records notices
C. G6 verification that the MSS platform is an approved Privacy Act system of records
D. Individual Soldier written consent for each ExpertiseProfile record

**15. The distribution routing logic in a lessons-learned pipeline must, at minimum, route lessons based on:**

A. Document file size and creation timestamp
B. Unit designation, classification level, and echelon — ensuring SECRET lessons do not route to unclassified systems and that lessons reach the relevant audience
C. The KM officer's manually selected routing destination
D. The submitter's echelon only — lessons are shared within the same echelon by default

---

## SECTION 2 — SHORT ANSWER

*Answer in 2–5 sentences. (6 points each)*

**SA-1. Describe the complete knowledge architecture you would design for a brigade KM system in MSS. Identify the five required Object Types, the key Link Types connecting them, and explain how this architecture supports a Soldier searching for lessons related to a specific topic and unit.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-2. Walk through the complete AIP Logic summarization workflow for incoming AAR documents, from ingestion through published lesson. Identify each step, the status of the knowledge item at each step, and the NON-NEGOTIABLE review gate.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-3. You are building a PCS knowledge transfer package for a departing brigade S2 NCO who managed two active MSS projects and one AIP Logic workflow. Describe what must be included in the package per TM-40K Chapter 9 procedures. Explain why a generic "key things" document is insufficient.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-4. An AIP prompt for extracting action items from AAR text is returning outputs that sometimes include action items and sometimes include full paragraph summaries. Describe your prompt iteration process to fix this inconsistency, including how you would test and score the output before considering the prompt production-ready.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-5. Describe the Privacy Act considerations for an MSS ExpertiseProfile system that will be used by the brigade to identify Soldiers with specific technical skills for assignment to task forces. Include what data fields raise Privacy Act concerns, what access controls are required, and what must be done before the system is activated.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

---

## SCORING SUMMARY

| Section | Questions | Points Each | Total Points |
|---|---|---|---|
| Multiple Choice | 15 | 2 | 30 |
| Short Answer | 5 | 6 | 30 |
| **Total** | — | — | **60** |

Passing: 42/60 (70%) — Post-test only. Pre-test is diagnostic.

---

## ANSWER KEY — INSTRUCTOR USE ONLY

*Do not distribute to students.*

**Multiple Choice:**
1. B — Document, Lesson, AAR, SOP, ExpertiseProfile are the five TM-40K required Object Types.
2. B — Required-field validation prevents submission with empty mandatory fields and displays an error.
3. C — Distribution routing logic routes lessons by unit, classification, and echelon.
4. B — AIP output stays Draft until KM officer reviews and approves — mandatory gate.
5. C — NON-NEGOTIABLE — all AIP-generated content requires human approval before publishing.
6. B — Prompt revision with explicit format instructions and few-shot examples, then test-score-iterate.
7. A — Knowledge browser requires keyword search, tag/unit/date filter, and drill-down to lesson detail.
8. B — Generic documents without project-specific details fail TM-40K Chapter 9 specificity requirement.
9. B — ExpertiseProfiles contain PII about individual Soldiers requiring Privacy Act handling.
10. B — Draft → KM Review → Published (with optional Archived) is the correct status workflow.
11. B — KM officer corrects category during review before approving and publishing.
12. B — AI-suggested tags are a pre-tagging aid — KM officer must confirm before publishing.
13. B — Date filter and recency-first default sort is the correct knowledge browser fix.
14. B — Privacy Act review before aggregating individual Soldier profiles is required per TM-40K Section 8-1.
15. B — Routing must address unit designation, classification level, and echelon at minimum.

**Short Answer Guidance:**

SA-1. Full credit: Object Types — Document, Lesson, AAR, SOP, ExpertiseProfile; Link Types — AAR-to-Lesson (AAR generates lessons), Lesson-to-SOP (lesson drives SOP update), Document-to-Lesson (document references lesson), ExpertiseProfile-to-Lesson (SME has expertise relevant to lesson); search path — Soldier uses keyword search in knowledge browser → results filtered by unit and date → selects a Lesson → drills down to linked AARs and SOPs → views ExpertiseProfile of the SME who authored it. Must include all 5 Object Types and at least 2 Link Types with explanation of search path.

SA-2. Full credit: (1) AAR submitted via Workshop form — status: submitted; (2) intake pipeline validates required fields, assigns preliminary tags via keyword matching — status: Draft; (3) AIP Logic workflow processes AAR text, generates structured lesson summary — status: Draft (AIP output); (4) KM officer review queue — KM officer reviews summary for accuracy, corrects tags, edits as needed — this is the NON-NEGOTIABLE review gate; (5) KM officer approves — status: Published; (6) distribution pipeline routes to appropriate unit/echelon channels. Must explicitly identify the NON-NEGOTIABLE review gate at step 4.

SA-3. Full credit: per TM-40K Chapter 9 — package must include: (1) named MSS projects with project ID, link, and description of status; (2) list of Object Types and pipelines owned by the departing NCO; (3) specific key contacts with name, unit, role, and contact information (not "see contact list"); (4) recurring task schedule with specific dates and procedures; (5) active AIP Logic workflow description and configuration; (6) access credentials transfer instructions (who to contact for access reassignment). Generic document is insufficient because it leaves the incoming Soldier without operational specifics — they cannot identify which systems need attention, who to call for help, or what deadlines are approaching.

SA-4. Full credit: revision process — (1) add explicit output format instructions: "Return ONLY a JSON array of action items with fields: action, owner, due_date. Do not include summary paragraphs."; (2) add 2-3 few-shot examples showing correct action-item-only output; (3) test against a sample set of 10–15 AARs; (4) score outputs: count items correctly formatted as action-item arrays vs. full paragraphs; target 90%+ correct format; (5) iterate prompt wording if below target; (6) re-test and confirm stable before marking production-ready. Must include explicit format instruction, few-shot examples, and quantitative scoring criteria.

SA-5. Full credit: Privacy Act concerns — name, rank, MOS, unit, contact info, skill specialties are PII; Soldiers may not expect their skills to be searchable by all brigade staff; access controls required: role-based access limiting who can view specific profile fields; need-to-know principle for skill-based searches; before activation: conduct Privacy Act review (consult Staff Judge Advocate or Privacy Officer); confirm the MSS project qualifies as an authorized system of records for this data; notify Soldiers that their data will be collected (Privacy Act Statement); limit data fields to mission-essential information only. Full credit requires identifying specific PII fields, access controls, and pre-activation Privacy Act review requirement.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*TM-40K Post-Test | Version 1.0 | March 2026*
