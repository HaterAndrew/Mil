# MSS TRAINING PROGRAM — INSTRUCTOR OVERVIEW
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Program** | Maven Smart System (MSS) Training Program |
| **Owner** | USAREUR-AF Operational Data Team |
| **Version** | 1.0 — March 2026 |
| **Audience** | Instructors, lead instructors, training OICs, and newly onboarded training NCOs |

---

## BLUF

This document gives a qualified instructor everything needed to understand the MSS training program and begin teaching. All documents referenced below exist in this repository. Nothing needs to be built from scratch — load the environment, print the materials, and execute the plan.

---

## Authoritative References

| Publication | Title | Relevance |
|---|---|---|
| AR 350-1 | Army Training and Leader Development | Master regulation for Army training policy; governs instructor qualification requirements |
| TR 350-70 | Army Learning Policy and Systems | TRADOC master regulation governing instructor certification, course delivery standards, and learning products |
| TP 350-70-3 | Faculty and Staff Development Program | TRADOC pamphlet governing instructor development, certification, and sustainment training |
| TP 350-70-7 | Army Educational Processes | TRADOC pamphlet governing instructional methodology, assessment design, and evaluation |
| FM 7-0 | Training | Unit training management procedures; provides context for how institutional training integrates with unit training plans |

> **NOTE:** TR 350-70, TP 350-70-3, and TP 350-70-7 are published by TRADOC at adminpubs.tradoc.army.mil, not DA APD.

---

## 1. PROGRAM OVERVIEW

The MSS Training Program is a tiered, progressive curriculum that trains USAREUR-AF personnel to operate, build on, and lead with the Maven Smart System.

### Training Track Architecture

```
TM-10 → TM-20 → TM-30 → TM-40 (all tracks) → TM-50 (specialist advanced only)

T3-I (Instructor Certification)     ← prereq: TM-30 + C2DAO selection
T3-F (MSC Force Multiplier)         ← prereq: TM-20 + CDR nomination
```

| Level | Course | Duration | Audience | Prereq |
|-------|--------|----------|----------|--------|
| TM-10 | Maven User | 1 day | All MSS users | None |
| TM-20 | Builder | 5 days | Analysts, data builders | TM-10 |
| TM-30 | Advanced Builder | 5 days | Senior analysts, pipeline builders | TM-20 |
| TM-40A | Intelligence WFF | 3 days | G2/S2 staff | TM-30 |
| TM-40B | Fires WFF | 3 days | FSE, targeting teams | TM-30 |
| TM-40C | Movement & Maneuver WFF | 3 days | G3/S3 maneuver staff | TM-30 |
| TM-40D | Sustainment WFF | 3 days | G4/S4, FSB/BSB staff | TM-30 |
| TM-40E | Protection WFF | 3 days | Force protection officers, CBRN | TM-30 |
| TM-40F | Mission Command WFF | 3 days | G3/S3, battle captains, XOs | TM-30 |
| TM-40G | ORSA | 5 days | FA49, data scientists | TM-30 |
| TM-40H | AI Engineer | 5 days | AI engineers, AIP practitioners | TM-30 |
| TM-40M | ML Engineer | 5 days | ML engineers | TM-30 |
| TM-40J | Program Manager | 4 days | MSS program managers | TM-30 |
| TM-40K | Knowledge Manager | 4 days | KMs, S6 data teams | TM-30 |
| TM-40L | Software Engineer | 5 days | SWEs, Foundry developers | TM-30 |
| TM-50G | Advanced ORSA | 5 days | Senior FA49, theater ORSA | TM-40G |
| TM-50H | Advanced AI Engineer | 5 days | Senior AI engineers | TM-40H |
| TM-50M | Advanced ML Engineer | 5 days | Senior ML engineers | TM-40M |
| TM-50J | Advanced Program Manager | 3 days | Senior PMs | TM-40J |
| TM-50K | Advanced Knowledge Manager | 3 days | Senior KMs | TM-40K |
| TM-50L | Advanced Software Engineer | 5 days | Senior SWEs, platform leads | TM-40L |

**Critical note:** There is no TM-50A through TM-50F. TM-50 is specialist advanced only (G–O). All TM-40 WFF tracks (A–F) are terminal — graduates proceed to their operational role, not to a TM-50.

---

## 2. WHERE EVERYTHING LIVES

All documents are under `maven_training/`. The directory structure is:

```
maven_training/
├── INSTRUCTOR_OVERVIEW.md          ← this document
├── README.md                       ← program summary, track table, prereq tree
├── QUICK_START.md                  ← 1-page orientation for new students
│
├── tm/                             ← Course content (read by students and instructors)
│   ├── TM_10_maven_user/
│   │   └── TM_10_MAVEN_USER.md
│   ├── TM_20_builder/
│   │   └── TM_20_BUILDER.md
│   ├── TM_30_advanced_builder/
│   │   └── TM_30_ADVANCED_BUILDER.md
│   ├── TM_40A_intelligence/        ← (and TM_40B through TM_40L)
│   │   ├── TM_40A_INTELLIGENCE.md
│   │   └── CONCEPTS_GUIDE_TM40A_INTELLIGENCE.md
│   ├── TM_50G_orsa_advanced/       ← (and TM_50H through TM_50L)
│   │   ├── TM_50G_ORSA_ADVANCED.md
│   │   └── CONCEPTS_GUIDE_TM50G_ORSA_ADVANCED.md
│   ├── T3_I_instructor_certification/
│   │   ├── T3_I_INSTRUCTOR_CERTIFICATION.md
│   │   └── CONCEPTS_GUIDE_T3I_INSTRUCTOR_CERTIFICATION.md
│   └── T3_F_msc_force_multiplier/
│       ├── T3_F_MSC_FORCE_MULTIPLIER.md
│       └── CONCEPTS_GUIDE_T3F_MSC_FORCE_MULTIPLIER.md
│
├── syllabi/                        ← One syllabus per course (schedule, learning objectives)
│   ├── SYLLABUS_TM10.md
│   ├── SYLLABUS_TM20.md
│   ├── SYLLABUS_TM30.md
│   ├── SYLLABUS_TM40A.md           ← (through TM40L)
│   └── SYLLABUS_TM50G.md           ← (through TM50L)
│
├── exercises/
│   ├── README.md                   ← exercise index
│   ├── exams/                      ← all PRE and POST exams (with embedded answer keys)
│   │   ├── EXAM_TM40A_PRE.md
│   │   ├── EXAM_TM40A_POST.md
│   │   └── ...                     ← complete for all TM-10 through TM-50 series
│   ├── EX_10_operator_basics/
│   │   ├── EXERCISE.md
│   │   └── ENVIRONMENT_SETUP.md
│   ├── EX_20_no_code_builder/
│   ├── EX_30_advanced_builder/
│   ├── EX_40A_intelligence/        ← (through EX_40L)
│   └── EX_50G_orsa/               ← (through EX_50L)
│
├── training_management/            ← Program administration documents
│   ├── INSTRUCTOR_OVERVIEW.md      ← this document
│   ├── MTP_MSS.md                  ← Mission Training Plan
│   ├── POI_MSS.md                  ← Program of Instruction
│   ├── CAD_MSS.md                  ← Course Administrative Data
│   ├── TEO_MSS.md                  ← Training and Evaluation Outline
│   ├── ENROLLMENT_SOP.md           ← Enrollment procedures
│   ├── ANNUAL_TRAINING_SCHEDULE.md ← Schedule and throughput targets
│   ├── FACULTY_DEVELOPMENT_PLAN.md ← Instructor qualification standards
│   └── lesson_plans/
│       ├── TM10/TM10_LESSON_PLANS.md
│       ├── TM20_LESSON_PLAN_OUTLINES.md
│       ├── TM30_LESSON_PLAN_OUTLINES.md
│       ├── TM40_WFF_LESSON_PLAN_OUTLINES.md     ← TM-40A through TM-40F
│       ├── TM40_SPECIALIST_LESSON_PLAN_OUTLINES.md  ← TM-40G through TM-40O
│       └── TM50_ADVANCED_LESSON_PLAN_OUTLINES.md   ← TM-50G through TM-50O
│
├── doctrine/                       ← Reference doctrine (not course-specific)
│   ├── DATA_LITERACY_technical_reference.md
│   ├── DATA_LITERACY_senior_leaders.md
│   └── GLOSSARY_data_foundry.md
│
├── standards/
│   └── NAMING_AND_GOVERNANCE_STANDARDS.md
│
└── pdf/                            ← Generated PDFs of all above documents
```

---

## 3. WHAT TO READ BEFORE YOU TEACH

### Before your first course (any level):

1. **This document** — you're reading it now
2. `training_management/POI_MSS.md` — official program of instruction; defines what you are authorized to teach and how
3. `training_management/TEO_MSS.md` — training and evaluation outline; defines the Go/No-Go standards for every evaluation
4. `training_management/FACULTY_DEVELOPMENT_PLAN.md` — your own instructor qualification requirements; verify your Go is on file before teaching

### Before teaching a specific course:

1. **The TM** — read the full TM for the course you are teaching (`tm/TM_XX_name/TM_XX_NAME.md`); if a Concepts Guide exists for the course, read it too
2. **The syllabus** — `syllabi/SYLLABUS_TMxx.md`; this is your day-by-day schedule and learning objectives
3. **The lesson plan** — `training_management/lesson_plans/[relevant outline]`; each block has a TLO, delivery method, student activity, and common errors table
4. **The exercise** — `exercises/EX_XX_name/EXERCISE.md` and `ENVIRONMENT_SETUP.md`; do the setup personally before Day 1, not on the morning of the exercise
5. **Both exams** — `exercises/exams/EXAM_TMxx_PRE.md` and `EXAM_TMxx_POST.md`; the answer key is embedded at the bottom of each file under "INSTRUCTOR USE ONLY" — do not distribute the full file to students

---

## 4. PRE-COURSE CHECKLIST (ALL LEVELS)

Complete these steps **no later than 5 duty days before Day 1** unless otherwise noted:

### Admin
- [ ] Verify enrollment is finalized — ENROLLMENT_SOP.md defines the process; verify students have documented prereqs on file
- [ ] Confirm room and equipment (projector, whiteboard, student workstations)
- [ ] Print PRE exam (student version — the sections above the answer key divider line)
- [ ] Confirm your instructor Go evaluation is current and on file with the training NCO

### Training Environment (MSS Access)
- [ ] Verify student training accounts are provisioned and accessible — have at least one student attempt login 2 days before Day 1
- [ ] Load synthetic training data for the practical exercise — see `ENVIRONMENT_SETUP.md` for the specific course; do this yourself to verify before exercise day
- [ ] For TM-50G/H/I/L: confirm Code Workspace with GPU allocation — **10 duty days minimum**; this is the most commonly missed lead time
- [ ] For TM-50L: confirm CI/CD pipeline access — **10 duty days minimum**; separate from Code Workspace access

### Evaluator
- [ ] If you are not the evaluator for the Day 3/5 practical exercise, confirm your evaluator is briefed and has read the EXERCISE.md
- [ ] Evaluator must have a separate evaluator account with the permissions described in ENVIRONMENT_SETUP.md
- [ ] Print and review the TEO section for the course you are teaching — the TEO defines the Go/No-Go criteria that override the instructor's individual judgment

---

## 5. EXAM ADMINISTRATION

### PRE-TEST (Day 1, Morning)
- Administer before any instruction begins
- 20 minutes, paper or digital
- Diagnostic only — score does not affect enrollment or course outcome
- Collect, review during lunch on Day 1, and use results to calibrate depth of instruction for identified gaps
- Answer key is embedded in the exam file — do not distribute the file; score manually

### POST-TEST (Day 3 or Day 5, after practical exercise)
- 30 minutes, paper or digital
- Passing score varies by course (see the exam file header for the passing score)
- A failing score does not automatically disqualify a student from a Go on the practical exercise — the two assessments are independent
- Both the practical exercise evaluation form and the POST test score go into the training record

---

## 6. PRACTICAL EXERCISE EVALUATION

The practical exercise is the primary evaluation for every TM-40 and TM-50 course. Key rules:

1. **Go/No-Go is task-based.** Each task has explicit Go and No-Go criteria in EXERCISE.md. The evaluator scores each task independently; the overall course Go/No-Go is derived from the task scores per the scoring rule at the bottom of the exercise (e.g., "Go on 5 of 6 tasks = overall Go").

2. **Automatic No-Go tasks exist.** Each exercise designates 1–2 tasks as automatic No-Go tasks — a No-Go on these tasks results in an overall course No-Go regardless of other task scores. These tasks reflect the core competency the course is designed to establish.

3. **Data staleness/inject events are scripted.** Exercises with inject events (e.g., EX_40A's SIGINT feed staleness inject at T+90 min) must be executed at the prescribed time. Do not hint at the inject before it occurs.

4. **Coaching vs. evaluation.** During the exercise, do not coach. Answer direct questions about the training environment (environment issues are not evaluation events), but do not provide procedural hints. The line: "Can you show me what you're seeing on your screen?" is observation, not coaching.

5. **Evaluation forms go to the training NCO** within 24 hours of exercise completion. Overall Go/No-Go, participant name, evaluator name, and date are required fields.

---

## 7. T:I RATIOS AND CLASS CAPS

| Level | Max Students | Min Instructors | Notes |
|-------|-------------|-----------------|-------|
| TM-10 | 24 | 1 | Lab sessions: 2 instructors recommended |
| TM-20 | 18 | 1 | Day 4–5 labs: 2 instructors required |
| TM-30 | 12 | 1 | Day 5 PE: dedicated evaluator required |
| TM-40 (WFF A–F) | 12 | 1 | Day 3 PE: dedicated evaluator required; T:I ≤ 6:1 for PE |
| TM-40 (Specialist G–O) | 10 | 1 | Day 3 PE: dedicated evaluator; technical depth requires T:I ≤ 5:1 |
| TM-50 (all) | 8 | 1 | Day 5 PE: dedicated evaluator; peer review component requires instructor presence throughout |

If enrollment exceeds these caps, split sections. Do not exceed class maximums — the exercise environments are not designed for larger groups and evaluator attention cannot be maintained.

---

## 8. COMMON MISTAKES TO AVOID

These are the most frequently recurring errors observed in MSS course delivery. They are documented here because they are non-obvious and not covered in the TM itself.

| Mistake | What It Looks Like | Correct Approach |
|---------|-------------------|------------------|
| Running the practical exercise on the morning of Day 3/5 | Environment issues discovered at 0750 on exercise day with no time to resolve | Complete ENVIRONMENT_SETUP.md setup the day before; personally verify all data loads and test data fires the alerts |
| Distributing the full exam file | Student receives the file with the answer key at the bottom | Print the student version only (everything above the "ANSWER KEY — INSTRUCTOR USE ONLY" divider); never share the file itself |
| Coaching during the practical exercise | Telling a student what button to click when they're stuck | Observe and document; redirect environment questions; do not provide procedural hints |
| Marking a student No-Go without evaluator form | Verbal Go/No-Go communicated; no written record | All Go/No-Go decisions require the evaluation form submitted to the training NCO; verbal is insufficient |
| Teaching TM-40 WFF content to students without TM-30 prereq | Student enrolled "by exception" | The prereq is a hard requirement, not a recommendation; a student without TM-30 documented cannot be evaluated to the TM-40 standard; escalate to the training NCO before Day 1 |
| Conflating reported status and assessed status when demonstrating the COP | Instructor describes a data layer as "showing current status" without noting it is reported data from the last submission | Model the language explicitly: "This shows reported status as of [timestamp]. The commander's assessment may differ." This is a core distinction across all WFF tracks |
| Skipping the PRE test | "We ran long on logistics; we'll just start the instruction" | The PRE is how you know what to emphasize on Day 1; administer it first, even if you don't have time to score it until break |

---

## 9. INSTRUCTOR CERTIFICATION PROCESS

This section establishes the certification pathway for MSS instructors per TP 350-70-3, *Faculty and Staff Development Program*. For detailed instructor qualification standards, prerequisites, and evaluator criteria, see `training_management/FACULTY_DEVELOPMENT_PLAN.md`.

### 9-1. Certification Pathway

All MSS instructors must complete the following progression before independently delivering instruction:

| Phase | Activity | Duration | Evaluator |
|---|---|---|---|
| 1. Attend | Complete the target course as a student; achieve Go on all evaluations | Per course schedule | Course lead instructor |
| 2. Shadow | Observe a certified instructor deliver the full course; take notes on pacing, transitions, and student management | 1 course iteration | Supervising instructor |
| 3. Co-Teach | Deliver 2–3 blocks of instruction under observation; receive structured feedback | 1 course iteration | Supervising instructor |
| 4. Lead (Observed) | Deliver the full course as lead instructor with an observer present | 1 course iteration | Training OIC/NCOIC |
| 5. Certify | Training OIC/NCOIC signs certification memorandum; instructor added to certified roster | Upon completion of Phase 4 | Training OIC/NCOIC |

> **NOTE:** Phase 2 (Shadow) and Phase 3 (Co-Teach) may occur in the same course iteration if the supervising instructor determines the candidate is ready to deliver blocks during that iteration. Phases may not be skipped.

### 9-2. Recertification

- Instructors must deliver at least one iteration of their certified course every 12 months to maintain certification.
- If 12 months elapse without delivery, the instructor must complete Phase 3 (Co-Teach) before resuming independent delivery.
- Curriculum updates that change >25% of course content require all certified instructors to complete a delta briefing before next delivery.

### 9-3. Certification Authority

The USAREUR-AF C2DAO Training OIC is the certification authority for all MSS instructor certifications. Certification memoranda are maintained by the training NCOIC.

### 9-4. Cross-Certification

Instructors certified for one TM-40 specialist track (G–O) may cross-certify for additional tracks by completing Phases 1 and 3 for the new track. WFF tracks (A–F) require full certification pathway due to domain-specific content.

> **Reference:** TP 350-70-3, *Faculty and Staff Development Program* (TRADOC). See also `training_management/FACULTY_DEVELOPMENT_PLAN.md` for instructor qualification matrices and evaluator prerequisites.

---

## 10. CONTACTS AND ESCALATION

| Issue | Contact |
|-------|---------|
| Training environment access, provisioning failures | C2DAO (submit access request; lead times vary by capability — see course ENVIRONMENT_SETUP.md) |
| Enrollment, training records, evaluation forms | Training NCO |
| Curriculum questions, content errors, TM updates | USAREUR-AF Operational Data Team |
| Student enrollment exceptions (missing prereqs) | Training OIC; do not make exceptions independently |
| Classification or OPSEC concerns about course material | Training OIC + unit S2/S6 |

---

## 11. QUICK REFERENCE — COURSE DOCUMENT MAP

For any given course, the complete instructor document set is:

| Document | Location | Purpose |
|----------|----------|---------|
| TM | `tm/TM_XX_name/TM_XX_NAME.md` | Student and instructor primary reference |
| Concepts Guide (TM-40+) | `tm/TM_XX_name/CONCEPTS_GUIDE_TMxx_NAME.md` | Supplemental background reading |
| Syllabus | `syllabi/SYLLABUS_TMxx.md` | Schedule and learning objectives |
| Lesson Plan | `training_management/lesson_plans/[outline file]` | Block-by-block delivery guide |
| PRE Exam | `exercises/exams/EXAM_TMxx_PRE.md` | Day 1 diagnostic (answer key embedded) |
| POST Exam | `exercises/exams/EXAM_TMxx_POST.md` | Final knowledge check (answer key embedded) |
| Exercise | `exercises/EX_XX_name/EXERCISE.md` | Practical exercise task list and evaluation criteria |
| Environment Setup | `exercises/EX_XX_name/ENVIRONMENT_SETUP.md` | Pre-exercise environment configuration |
| PDF versions | `pdf/` | Print-ready versions of all above |

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*INSTRUCTOR_OVERVIEW | Version 1.0 | March 2026*
