# COURSE SYLLABUS
## TM-40K — KNOWLEDGE MANAGER
### Maven Smart System (MSS) — USAREUR-AF

| | |
|---|---|
| **Level** | TM-40K (Knowledge Manager Specialist Track) |
| **Duration** | 4 days (32 hours) |
| **Prerequisites** | TM-10, TM-20, and TM-30 (all Go evaluations on file, required). |
| **Audience** | KMOs, 37F Psychological Operations, S2/S3/S6 knowledge officers, unit knowledge managers |
| **Format** | Instructor-led lab + design workshop + practical exercise |
| **Location** | MSS Training Environment (AIP Logic configuration access required) |

---

## What This Course Does for You

Institutional knowledge walks out the door at every PCS cycle. After this course you can build the systems that stop that — structured AAR capture, lessons-learned pipelines, SOP version control, personnel expertise mapping, and PCS knowledge transfer packages, all running on MSS. AIP Logic adds a force multiplier: automatic summarization, theme extraction, and knowledge Q&A against your unit's repository.

Four days provides time to build each KM system component in depth: Day 1 establishes the knowledge architecture and AIP Logic foundation; Day 2 builds the search and retrieval applications; Day 3 covers expertise mapping, continuity systems, and gives trainees a full afternoon to draft their PCS transfer package before instructor review; Day 4 opens with the instructor PCS review, then moves to the practical exercise with adequate time to demonstrate all six evaluated tasks.

---

## Learning Objectives

By the end of training, you will be able to:

1. Design a knowledge architecture for a unit KM scenario: Document, Lesson, AAR, SOP, ExpertiseProfile Object Types with Link Types and documented schema
2. Configure a Workshop AAR submission form that writes to the AAR Object Type with required-field validation and submission confirmation
3. Configure a lessons-learned intake pipeline with tagging and distribution routing logic
4. Configure an AIP Logic summarization workflow for document intake with a mandatory human review gate — no AIP output auto-publishes
5. Iterate on AIP prompt engineering to improve extraction quality: test against provided samples, revise prompt, retest
6. Build a knowledge browser application with search, filter by tag/unit/date, and drill-down to lesson detail
7. Build a PCS knowledge transfer package for a specific role using TM-40K Chapter 9 procedures — specific to the Foundry project, Object Types, pipelines, and contacts

---

## Before You Attend: Pre-Course Checklist

Complete **5+ duty days before Day 1:**
- [ ] Request **Builder access** in the MSS Training Environment from your unit MSS Administrator
- [ ] Request AIP Logic **configuration** access — this may require C2DAO coordination. Configuration access lets you set up triggers and connect inputs/outputs. If you have only the TM-30 level AIP Logic view, confirm with your MSS Administrator whether it is sufficient for this course's AIP lab. Confirm access is active before Day 1.
- [ ] Read TM-40K, Chapter 1 (Introduction, Safety Summary) — 25 min
- [ ] Read TM-40K, Chapter 2 (Knowledge Architecture Design) — domain analysis and Object Type design sections

---

## Daily Schedule

**Day 1 — Knowledge Architecture, AAR Systems, and Lessons Learned**

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 1  | Brief    | KM role on MSS; knowledge architecture methodology; why KM systems fail and what makes them survive personnel turbulence |
| 0900–1100 | 2  | Lab      | Ontology: Knowledge Object Types — Document, Lesson, AAR, SOP, ExpertiseProfile; Link Types; design on paper before building |
| 1100–1115 | —  | Break    | |
| 1115–1200 | 3  | Lab      | Workshop: AAR submission form — required-field validation, submission confirmation, routing to AAR Object Type |
| 1200–1300 | —  | Lunch    | |
| 1300–1500 | 4  | Lab      | Lessons learned pipeline: intake, deduplication logic, tagging taxonomy design, distribution routing by unit/classification/echelon |
| 1500–1515 | —  | Break    | |
| 1515–1700 | 5  | Lab      | AIP Logic: document summarization workflow; automatic theme extraction; human review queue — all AIP-generated objects begin as `status = Draft`, not Published |

**Evening reading:** TM-40K, Chapter 3 (AAR Capture) — review the form validation logic; TM-40K, Chapter 5 (AIP-Assisted Knowledge Work) — read the WARNING on AIP output review requirements.

---

**Day 2 — Search, Retrieval Applications, and AIP Prompt Engineering**

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | —  | Review   | Day 1 questions; AIP review gate requirements — the non-negotiable standard |
| 0830–1030 | 6  | Lab      | Workshop: knowledge browser — search by keyword, filter by tag/unit/date, drill-down from result to lesson detail view |
| 1030–1045 | —  | Break    | |
| 1045–1200 | 7  | Lab      | SOP/doctrine version control: lifecycle management, version tagging, SOP review notification workflow (TM-40K Section 7-6 procedures) |
| 1200–1300 | —  | Lunch    | |
| 1300–1315 | —  | Brief    | AIP prompt engineering methodology: why prompt quality determines system quality; the scoring rubric used in Block 8 |
| 1315–1530 | 8  | Lab      | **AIP prompt iteration lab (extended):** each trainee iterates on their summarization prompt — test against 5 provided documents, score extraction quality using the rubric, revise, retest minimum 3 cycles; instructor coaches; final prompt version documented with rationale for each change |
| 1530–1545 | —  | Break    | |
| 1545–1700 | 9  | Exercise | Prompt comparison debrief: trainees share one prompt revision (before/after) with the group; class identifies the structural change that improved extraction quality; instructor closes with the common prompt failure patterns from this cohort |

**Evening reading:** TM-40K, Chapter 9 (Knowledge Transfer and Continuity) — read in full; TM-40K, Section 8-1 (Privacy Act authorities for ExpertiseProfile data); TM-40K, Section 5-3 (AIP prompt template) — document modifications from Day 2 lab.

---

**Day 3 — Expertise Mapping, PCS Continuity, and Package Draft**

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | —  | Review   | Day 2 questions; privacy act and classification of knowledge objects |
| 0830–1030 | 10 | Lab      | Personnel expertise mapping: ExpertiseProfile Object Type, skills taxonomy design, SME directory application; Privacy Act authorities (TM-40K Section 8-1) — emphasis on what data can and cannot be captured |
| 1030–1045 | —  | Break    | |
| 1045–1145 | 11 | Lab      | PCS knowledge transfer methodology: key person dependency analysis; transfer package design; Foundry project handoff checklist structure per TM-40K Chapter 9 |
| 1145–1200 | —  | Brief    | PCS package requirements brief: evaluator explains Chapter 9 completeness criteria; trainees understand what a passing package contains before drafting |
| 1200–1300 | —  | Lunch    | |
| 1300–1700 | 12 | Lab      | **PCS package draft lab (full afternoon):** each trainee produces a complete draft PCS transfer package — specific Foundry project, Object Types and current data quality, pipelines and schedules, required contacts, access requirements. Instructor available for questions on completeness criteria; no content guidance. Package must be submitted to instructor by 1700 for morning review |

**Evening task:** Finalize PCS package draft. Instructor reviews all packages overnight and prepares targeted feedback for each trainee.

---

**Day 4 — Governance, Instructor Review, and Practical Exercise**

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | —  | Review   | Day 3 questions; access management, C2DAO governance for knowledge objects |
| 0830–1045 | 13 | Lab      | **PCS package instructor review:** each trainee receives written feedback from overnight review; individually confers with instructor; revises package against Chapter 9 completeness criteria. Trainees with complete packages use remaining time to refine AIP workflow documentation |
| 1045–1100 | —  | Break    | |
| 1100–1145 | 14 | Brief    | Practical exercise scenario brief; review Go criteria for AIP review gate and PCS package completeness |
| 1145–1200 | —  | Buffer   | Questions / final environment check |
| 1200–1300 | —  | Lunch    | |
| 1300–1700 | 15 | **Eval** | **Practical exercise (evaluated)** |

---

## Required Reading Summary

| When | Reading |
|---|---|
| Before Day 1 | TM-40K, Ch 1 (Introduction/Safety) |
| Before Day 1 | TM-40K, Ch 2 (Knowledge Architecture Design) |
| Day 1 evening | TM-40K, Ch 3 (AAR Capture — validation logic) |
| Day 1 evening | TM-40K, Ch 5 (AIP — WARNING on review requirements) |
| Day 2 evening | TM-40K, Section 8-1 (Privacy Act authorities for ExpertiseProfile) |
| Day 2 evening | TM-40K, Section 5-3 (AIP prompt template) — document modifications from Day 2 lab |
| Day 2 evening | TM-40K, Ch 9 (Knowledge Transfer/Continuity) — required before PCS draft lab Day 3 |
| Day 3 evening | Finalize PCS package draft — submit to instructor by 1700 (evaluated overnight) |

---

## Practical Exercise

**Scenario:** Your brigade S3 needs a KM system for exercise AARs and lessons learned. The KMO is PCSing in 90 days; the new KMO needs a complete transfer package.

**Tasks:**
1. Design a knowledge ontology for 5 Object Types (AAR, Lesson, SOP, ExpertiseProfile, Unit) — document the schema before building
2. Configure a Workshop AAR submission form with required-field validation and confirmation on submit
3. Configure a lessons-learned intake pipeline: ingest provided AAR data, apply unit/event-type/echelon tags, route lessons by distribution rules
4. Configure an AIP Logic summarization workflow for document intake; implement a human review queue — all AIP-generated draft lessons must begin with `status = Draft` and require KM review before `status = Published`
5. Build a knowledge browser application: search by keyword, filter by unit and date, drill-down to lesson text
6. Produce a complete PCS knowledge transfer package for the outgoing KMO role — specific to the Foundry project, Object Types, pipelines, data quality status, and required contacts

**Go standard:** Pass 5 of 6 tasks. AIP workflow has a documented, tested human review gate — no AIP output auto-publishes (hard No-Go if violated). PCS package reviewed by instructor against TM-40K Chapter 9 completeness criteria.

---

## What "Go" Looks Like

The AIP review gate is non-negotiable. Any workflow that routes AIP-generated lessons directly to `status = Published` without a human review queue fails that task regardless of workflow functionality. The evaluator will specifically test whether a Draft lesson can bypass review and publish directly. Design your workflow so that is impossible.

The PCS transfer package is a real product, not a template. It must name the specific Foundry project, specific Object Types and their current data quality status, specific pipelines and their schedules, and the contacts the incoming KMO needs. Generic boilerplate will not pass the Chapter 9 completeness review.

---

## Tips From Previous Graduates

- The AIP summarization prompt matters more than the workflow configuration. A poorly-written prompt produces garbage summaries that flood the review queue as noise — technically compliant, operationally useless. Spend time on the prompt during Day 2's prompt iteration lab. TM-40K Section 5-3 has the recommended template — start there and modify.
- The biggest design mistake is building a KM system only you can use. Design for the person who replaces you in 12 months. Use naming conventions and descriptions that are self-explanatory. The evaluator will ask: "If you PCS'd today, could a new KMO operate this system using only the documentation?"
- Privacy Act applies to ExpertiseProfile data. The evaluator will ask what Privacy Act authorities cover your skills database. The answer is in TM-40K Section 8-1. Read it before Day 2.
- The lessons-learned tagging taxonomy takes longer to design than it looks. "Unit" and "Event Type" are obvious. Think about what a future analyst will filter on: TTP category, classification level, applicable echelon, related doctrine reference. Design the taxonomy before building the pipeline.
- The Day 3 instructor review of your PCS package is a graded preparation event, not optional. Trainees who arrive to Day 3 with an incomplete draft consistently fail the PCS package task on the evaluation.

---

## Continuation

Graduates designing enterprise knowledge architectures or leading cross-organizational KM initiatives may pursue **TM-50K (Advanced Knowledge Management)**. TM-50K covers multi-domain taxonomy design, AI-augmented knowledge synthesis at scale, knowledge retrieval infrastructure, quality governance frameworks, and continuity systems that survive personnel turnover. Prerequisites: TM-40K Go evaluation on file; 12+ months active KM practice in a military or large organizational context.

---

## Associated Exercises and Assessments

| Item | Reference |
|---|---|
| Pre-course exam | EXAM_TM40K_PRE |
| Post-course exam | EXAM_TM40K_POST |
| Practical exercise | EX_40K (EXERCISE.md + ENVIRONMENT_SETUP.md) |

---

## Relationship to WFF Tracks

WFF track analysts (TM-40A through TM-40F) are the operational consumers of lessons-learned systems, AAR pipelines, and knowledge repositories built in this course. Knowledge managers should understand the capture and retrieval needs of each WFF community: mission command analysts (TM-40F) consume commander decision logs and SOP repositories; intelligence analysts (TM-40A) use lessons-learned databases for pattern recognition; protection analysts (TM-40E) maintain TTPs and incident histories in KM-managed repositories.

---

*USAREUR-AF Operational Data Team*
*Syllabus TM-40K | Version 2.0 | March 2026*
