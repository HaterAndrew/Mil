# T3-F — MSC FORCE MULTIPLIER · MAVEN SMART SYSTEM (MSS)

> **BLUF:** T3-F certifies MSC-level personnel as Unit Data Trainers (UDTs) to deliver TM-10 independently at their units between MTT visits. Half-day course. Graduates receive the lesson plan, prove they can deliver it, and start training.
> **Prereqs:** TM-20, Builder (Go on file); unit commander nomination.
> *HQ USAREUR-AF · v2.0 · 2026 · DISTRIB: USG only · AUTH: C2DAO/UDRA v1.1*

---

## CHAPTER 1 — THE UNIT DATA TRAINER

### 1-1. Purpose and Scope

**BLUF:** C2DAO cannot be everywhere. USAREUR-AF is distributed across Europe. Between MTT visits, new arrivals need TM-10 (Maven User) qualification. UDTs fill that gap by delivering TM-10 using published lesson plans.

**T3-F covers:**

- How to use the TM-10 training materials (lesson plans, exercises, exams, T&EOs)
- How to deliver TM-10 using the published lesson plans
- How to administer and score TM-10 evaluations (pre-tests, post-tests, Go/No-Go practicals)
- How to report training completion to C2DAO

**T3-F does NOT cover:**

- Delivering TM-20, TM-30, or any TM-40/TM-50 course — requires C2DAO-certified instructor
- Modifying curriculum, lesson plans, or evaluation criteria — curriculum authority resides with C2DAO
- Advanced instructional methodology — see T3-I (Instructor Certification)

---

### 1-2. The Unit Data Trainer in the Training Ecosystem

```
C2DAO Training Division
  ├── MTT (quarterly rotation to MSCs)
  │     ├── Delivers TM-20, TM-30, TM-40 as scheduled
  │     ├── Delivers T3-F to nominated UDT candidates
  │     └── Observes existing UDTs, provides feedback
  │
  └── Certified Instructors (T3-I graduates)
        └── Deliver all TM courses per assignment

MSC / Unit Level
  └── Unit Data Trainer (T3-F graduate)
        ├── Delivers TM-10 to new arrivals between MTT visits
        ├── Proctors TM-10 exams for self-study/remote personnel
        └── Reports training status to C2DAO
```

---

### 1-3. Prerequisites

| Prerequisite | Requirement |
|---|---|
| TM-20 Go | On file with C2DAO. Ensures Builder-level platform skills. |
| Commander Nomination | Unit commander signs nomination memorandum identifying the candidate and certifying the duty position requirement. |
| Platform Access | Active MSS account with Builder-level access. |

---

### 1-4. Authorities and Limitations

| Can Do | Cannot Do |
|---|---|
| Deliver TM-10 (all 9 blocks) | Deliver TM-20 or above |
| Administer TM-10 Go/No-Go evaluations | Modify curriculum or evaluation criteria |
| Proctor TM-10 pre/post exams (standalone) | Grant enrollment exceptions |
| Report training status to C2DAO | Certify other instructors or UDTs |
| | Provision MSS accounts |

---

## CHAPTER 2 — THE TM-10 TRAINING MATERIALS

### 2-1. Document Set

The UDT delivers published materials. You do not design instruction.

| Document | Location | Purpose |
|---|---|---|
| TM-10 Course Content | `tm/TM_10_maven_user/TM_10_MAVEN_USER.md` | Primary reference; student reading material |
| TM-10 Lesson Plans | `training_management/lesson_plans/TM10/TM10_LESSON_PLANS.md` | Block-by-block delivery guide with instructor notes, activities, check-on-learning questions |
| TM-10 Syllabus | `syllabi/SYLLABUS_TM10.md` | Schedule, learning objectives, assessment criteria |
| TM-10 Exercise | `exercises/EX-10_operator_basics/EXERCISE.md` | Practical exercise task list with Go/No-Go criteria |
| TM-10 Pre-Test | `exercises/exams/EXAM_TM10_PRE.md` | Diagnostic exam (Day 1 morning) |
| TM-10 Post-Test | `exercises/exams/EXAM_TM10_SUPPLEMENTAL.md` | Knowledge check (end of course) |
| TM-10 T&EOs | `training_management/TEO_MSS.md` (Part I) | Go/No-Go performance measures and standards |

### 2-2. How to Use the Lesson Plans

Each TM-10 lesson plan block contains:

| Section | What It Tells You |
|---|---|
| **Purpose** | Why this block exists — read this aloud or paraphrase at the start |
| **TLO / ELOs** | What the trainee must be able to do after the block |
| **Instructor Notes** | What to demonstrate, emphasize, or skip if time is short |
| **Student Activity** | What the trainee does hands-on |
| **Check-on-Learning** | Questions to verify comprehension — use these, do not skip them |
| **Common Errors** | Errors trainees frequently make and how to address them |

**Delivery rule:** Follow the lesson plan as written. If you believe a lesson plan has an error, deliver it as published and submit a note to C2DAO after the iteration.

### 2-3. Materials Preparation

Before each TM-10 iteration:
- Print the student handout (abbreviated task reference)
- Print pre-test and post-test packets (student versions only — **do not print the answer key for distribution**)
- Print T&EO scoring sheets (1 per student)
- Secure the answer key in your instructor binder
- Verify all enrolled students have active MSS accounts
- Test-login from classroom workstations
- Notify C2DAO of planned iteration (date, student count, location)

---

## CHAPTER 3 — DELIVERING TM-10

### 3-1. Course Flow

TM-10 is a 1-day course with 9 blocks:

| Block | Topic | Method | Duration |
|---|---|---|---|
| — | Course overview, admin, pre-test | BRF | 30 min |
| 1 | What is MSS and why it matters | LEC | 30 min |
| 2 | Navigating the MSS environment | LAB | 60 min |
| 3 | Finding and viewing data | LAB | 60 min |
| — | Lunch | — | 60 min |
| 4 | Understanding dashboards and reports | LAB | 45 min |
| 5 | Basic data interpretation | LAB | 45 min |
| 6 | Classification and export rules | LEC/LAB | 30 min |
| 7 | Requesting help and reporting issues | DIS | 15 min |
| 8 | Practical exercise | EVAL | 60 min |
| 9 | Post-test, AAR, closeout | BRF | 30 min |

### 3-2. Key Delivery Points

**Block 1 — Operational context:** Do not read slides. Tell the class why MSS matters to their unit. Use local examples.

**Block 2 — Navigation:** This is where students get lost. Circulate continuously. Verify every student has logged in within the first 5 minutes. If anyone cannot log in, troubleshoot immediately — do not proceed while a student is locked out. If you cannot resolve a login issue quickly, contact C2DAO.

**Block 6 — Classification:** Most consequential block. An incorrect classification marking on an export is a security violation. Ensure every student can correctly identify classification of data before attempting the export exercise. Hard No-Go item on the T&EO.

**Block 8 — Practical exercise:** Switch to evaluator mode. Announce clearly: "From this point I cannot provide assistance. You may use your task reference and notes." Do not help. Do not hint. Score each performance measure on the T&EO scoring sheet.

### 3-3. Evaluation

**T&EO scoring:** Each performance measure is Go or No-Go based on observed performance.

| Score | Meaning |
|---|---|
| **Go** | Trainee performed the task to standard without assistance |
| **No-Go** | Trainee did not perform to standard, required assistance, or did not attempt |

**Critical items** are marked in the T&EO. Failure on any critical item is automatic No-Go for the entire task. TM-10 critical items include correct classification marking on export (TM10-06) and not navigating to the production environment.

**No-Go procedures:** If a student receives No-Go, inform them same-day, identify which performance measures were not met, document the result on the T&EO scoring sheet, coordinate remediation with the unit training NCO, and report to C2DAO within 24 hours.

---

## CHAPTER 4 — REPORTING AND SUSTAINMENT

### 4-1. Unit Training Status Report

After each TM-10 iteration, submit the Unit Training Status Report to C2DAO within 5 duty days. Key fields:
- UDT name and unit
- Iteration dates
- Students enrolled / completed / Go / No-Go
- Pre-test and post-test mean scores
- Issues encountered

### 4-2. Standalone Exam Proctoring

UDTs may proctor TM-10 exams for personnel who completed TM-10 via self-study or remote instruction. Verify the student completed all required reading, administer the post-test under standard conditions, and coordinate with C2DAO for practical exercise scheduling.

### 4-3. Sustainment

- Deliver TM-10 at least quarterly to maintain UDT designation
- Attend semi-annual C2DAO PD sessions (virtual OK)
- Annual re-certification observation by C2DAO (2 blocks of instruction + 1 Go/No-Go evaluation)
- Review lesson plan updates before each iteration

### 4-4. When You PCS or Change Duty

If you PCS, ETS, or change to a duty position without training responsibilities:
- Notify C2DAO and your unit training NCO
- Recommend a replacement candidate to your commander
- Transfer local knowledge to your replacement
- Your UDT designation lapses; your replacement must complete T3-F independently

### 4-5. Escalation

If a training request exceeds your authority (TM-20+, enrollment exceptions, curriculum changes), say so and connect the requestor with C2DAO. If you encounter an environment issue you cannot resolve quickly, escalate to C2DAO. Attempting training beyond your scope causes more harm than delaying until C2DAO is available.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*T3-F MSC Force Multiplier | Version 2.0 | March 2026*
