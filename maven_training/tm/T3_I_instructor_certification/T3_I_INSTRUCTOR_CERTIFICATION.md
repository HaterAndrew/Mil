# T3-I — INSTRUCTOR CERTIFICATION · MAVEN SMART SYSTEM (MSS)

> **Forward:** T3-I certifies MSS instructors. It formalizes the instructor development pipeline into a structured course covering adult learning principles, platform deep-dive for instruction, lab facilitation, assessment design, Go/No-Go standardization, and common trainee error management. Graduates enter the supervised practicum (Phase 2) and, upon completion, are authorized to teach independently.
> **Prereqs:** TM-30, Advanced Builder (Go on file); C2DAO Training OIC selection; CONCEPTS_GUIDE_T3I_INSTRUCTOR_CERTIFICATION (read before this manual).
> *HQ USAREUR-AF · v1.0 · 2026 · DISTRIB: USG only · AUTH: C2DAO/UDRA v1.1*

> **WARNING:** Instructor quality directly affects operational data quality across USAREUR-AF. An MSS data product built by a trainee is only as good as the instruction they received.

---

## CHAPTER 1 — INTRODUCTION: THE MSS INSTRUCTOR

### 1-1. Instructor Certification Manual

**BLUF:** T3-I transforms a qualified MSS operator into a qualified MSS instructor. It replaces the previous ad-hoc 4-phase apprenticeship with a structured, documented certification pathway.

This manual provides the reference material for the T3-I course. It covers everything an instructor candidate needs to understand the MSS training program, develop instructional competency, and prepare for the supervised practicum.

**T3-I covers** adult learning principles applied to technical training (andragogy, experiential learning cycle, scaffolding); MSS platform deep-dive from the instructor perspective — every TM-10 through TM-30 lab exercise, common break points, access issues; lab facilitation techniques including managing heterogeneous skill levels, pacing, and dead time elimination; assessment and evaluation design (T&EO structure, Go/No-Go standardization, evaluator calibration); common trainee error taxonomy (the top 10 errors by course level, root causes, intervention techniques); instructor performance standards (the 7 observation criteria from FDP §6-1); pre-course administration (environment setup, access provisioning, material preparation); and lesson improvement process (identifying gaps, proposing revisions, version control).

**T3-I does NOT cover** domain-specific content for TM-40/TM-50 courses (domain qualification is a separate prerequisite per FDP §2-1); C2DAO SME designation — see C2DAO SME Designation Rubric; Unit Data Trainer certification — see T3-F (MSC Force Multiplier); or curriculum design from scratch (T3-I teaches instructors to deliver and improve existing curriculum, not to author new courses).

> **NOTE:** T3-I is a two-phase program. Phase 1 (5 days classroom) is delivered as a formal course. Phase 2 (supervised practicum) is scheduled separately around actual course iterations. This manual covers Phase 1 content. Phase 2 procedures are documented in Chapter 7.

> **GOVERNANCE:** The Faculty Development Plan (FDP) establishes the overarching 4-phase instructor certification lifecycle (Audit → Assistant → Lead Observed → Certification). T3-I implements FDP Phases 2-4 through its 2-phase delivery structure. See FDP §3-3 for the phase reconciliation mapping. The FDP remains the authoritative governance document for instructor qualification standards, sustainment requirements, and performance standards.

---

### 1-2. The Instructor in the MSS Ecosystem

The MSS Training Program is a tiered, progressive curriculum spanning TM-10 (Maven User) through TM-50 (Advanced Specialist). Instructors are the primary mechanism for quality assurance across this entire chain. Every Go/No-Go decision an instructor makes determines whether a person enters the operational data ecosystem with the skills to contribute — or the gaps to cause harm.

The training program operates in a geographically distributed theater (USAREUR-AF across Europe). Instructors travel with the MTT, deliver courses at MSC locations, certify Unit Data Trainers, and maintain training standards across a theater where no two sites have identical infrastructure, connectivity, or personnel tempo.

**Instructor tier structure:**

| Tier | Role | Path |
|---|---|---|
| Instructor | Deliver assigned courses; conduct Go/No-Go evaluations | T3-I Go + domain qualification |
| Senior Instructor | Certify new instructors; approve lesson plan revisions | Instructor + 12 months + 4 iterations + OIC recommendation |
| Master Instructor | Certify Senior Instructors; approve curriculum changes; delegate certification authority | Senior + 24 months + 2 cross-certs + 2 mentored candidates + OIC designation |

See Instructor Tier Definitions for full criteria.

---

### 1-3. Prerequisites and Entry Standards

| Prerequisite | Requirement |
|---|---|
| TM-30 Go | On file with C2DAO. TM-30 is the minimum operational qualification — it ensures the candidate can build on MSS, not just use it. |
| C2DAO Selection | The C2DAO Training OIC selects instructor candidates based on operational need, platform proficiency, and demonstrated aptitude for instruction. Self-nomination is permitted but selection is not guaranteed. |
| Domain Qualification | Not required for T3-I entry, but required before independent teaching assignment. See FDP §2-1 for domain requirements by course level. |
| Pre-Course Reading | CONCEPTS_GUIDE_T3I_INSTRUCTOR_CERTIFICATION (complete before Day 1) |

---

## CHAPTER 2 — ADULT LEARNING PRINCIPLES

### 2-1. Why This Matters

MSS trainees are adults — military and Civilian professionals with operational experience, existing mental models, and immediate performance requirements. They are not cadets in a schoolhouse. The instructional approach must account for how adults actually learn technical skills.

### 2-2. Andragogy vs. Pedagogy

Malcolm Knowles identified six principles of adult learning that directly apply to MSS instruction:

| Principle | Application to MSS Training |
|---|---|
| **Need to Know** | Adults need to know why they are learning something before they engage. Every block of instruction must begin with operational context: "Here is the mission problem this skill solves." |
| **Self-Concept** | Adults resist being treated as dependent learners. Lab-heavy instruction works because it puts the trainee in control. Lectures where the trainee passively watches the instructor build are the weakest delivery method. |
| **Experience** | Adults bring operational experience. Use it. Ask the Intel analyst how they currently track CCIRs before showing them the MSS way. Build on what they know. |
| **Readiness** | Adults learn what they need to learn for their current role. TM-40 WFF tracks succeed because the content maps directly to the trainee's job. |
| **Orientation** | Adults are problem-oriented, not subject-oriented. Frame every exercise as a problem to solve, not a feature to learn. |
| **Motivation** | Adults are motivated by internal factors (competence, job performance) more than external ones (grades, rankings). Go/No-Go evaluations work because they certify operational competence, not academic achievement. |

### 2-3. The Experiential Learning Cycle (Kolb)

MSS instruction follows the Kolb cycle for every major skill:

```
Concrete Experience     →  The trainee does the task (lab exercise)
         ↓
Reflective Observation  →  The trainee reviews what happened (check-on-learning)
         ↓
Abstract Conceptualization → The instructor connects the experience to the concept
         ↓
Active Experimentation  →  The trainee applies the concept to a new scenario (practical exercise)
```

**Implication for instructors:** Do not start with the concept and then do the lab. Start with the lab (or a demonstration), let the trainee experience the skill, then explain the underlying principle. The concept sticks because the trainee already has a concrete reference point.

### 2-4. Scaffolding

Scaffolding means providing support structures that are gradually removed as the trainee develops competence.

**MSS scaffolding example (pipeline building):**
1. Day 1: Instructor builds a pipeline step-by-step; trainee follows along (maximum scaffolding)
2. Day 2: Instructor provides the pipeline design; trainee builds it independently (reduced scaffolding)
3. Day 3: Trainee receives a data problem; designs and builds the pipeline from scratch (no scaffolding)
4. Practical Exercise: Trainee receives an operational scenario; designs, builds, tests, and governs a complete pipeline (assessment)

**The instructor's job is to know when to remove the scaffold.** Remove it too early and the trainee fails and disengages. Remove it too late and the trainee never develops independence.

---

## CHAPTER 3 — ARMY INSTRUCTIONAL METHODOLOGY

### 3-1. Regulatory Framework

MSS instruction operates under:
- **AR 350-1** (Army Training and Leader Development): master regulation for all Army training
- **TR 350-70** (Army Learning Policy and Systems): TRADOC master regulation for institutional training
- **TP 350-70-3** (Faculty and Staff Development): governs instructor certification and development
- **TP 350-70-7** (Army Educational Processes): governs assessment and evaluation design

T3-I does not require memorization of these publications. It requires understanding the principles they establish and how those principles apply to MSS-specific instruction.

### 3-2. Task-Condition-Standard (TCS)

Every learning objective in the MSS curriculum is written in TCS format:

| Element | Definition | Example (TM-20, Pipeline Building) |
|---|---|---|
| **Task** | What the trainee will do (action verb) | Build a Pipeline Builder pipeline |
| **Condition** | The circumstances under which the task is performed | Given a MSS training environment with Editor access, a source dataset, and the TM-20 task reference |
| **Standard** | The measurable performance criteria | Pipeline ingests source data, applies at least 2 transforms, outputs to a dataset; pipeline builds successfully on first execution; pipeline is governed with description and tags per C2DAO naming standards |

**Instructors must understand TCS because:**
- Every T&EO is built from TCS objectives — the Go/No-Go criteria are the standards
- When a trainee asks "what do I need to do to pass?" the answer is the standard
- When an evaluator is uncertain whether to give Go or No-Go, the standard is the arbiter — not the evaluator's personal judgment

### 3-3. Terminal and Enabling Learning Objectives

| Type | Definition | Example |
|---|---|---|
| **Terminal Learning Objective (TLO)** | The overall skill the trainee will demonstrate at the end of a lesson or course | Build and govern a multi-source pipeline on MSS |
| **Enabling Learning Objective (ELO)** | A sub-skill that must be mastered to achieve the TLO | Configure a file ingestion source; apply a join transform; apply a group-by aggregation; add governance metadata |

**The instructor's role:** Teach ELOs in sequence, building toward the TLO. Do not skip ELOs — even if some trainees already know them. Check on learning at each ELO before moving to the next.

### 3-4. Methods of Instruction

| Method | Code | When to Use | MSS Application |
|---|---|---|---|
| Lecture | LEC | Concepts that cannot be demonstrated; regulatory context | Chapter introductions, governance procedures |
| Discussion | DIS | Building on trainee experience; exploring edge cases | After-action reviews, error analysis, design critiques |
| Seminar | SEM | Small-group exploration of complex topics | Training philosophy, assessment design |
| Lab | LAB | Hands-on practice of a specific skill | All platform skills (pipeline building, Workshop, Ontology) |
| Workshop | WKS | Trainee-led design or problem-solving with instructor facilitation | Ontology design exercise, project planning |
| Brief | BRF | Orientation, administrative information, evaluations | Course overview, evaluation procedures |
| Evaluation | EVAL | Summative assessment of trainee performance | Practical exercises, microteaching, Go/No-Go evaluations |

**For MSS courses:** LAB dominates. The typical MSS course is 60-70% lab time. Lectures should be short (15-20 minutes maximum) and immediately followed by a lab exercise that applies the concept.

---

## CHAPTER 4 — PLATFORM DEEP-DIVE FOR INSTRUCTION

### 4-1. The Instructor Seat

Teaching on MSS is different from building on MSS. The instructor must:
- Know every lab step and its expected outcome before the trainee encounters it
- Know every common failure mode for each lab step (wrong click, stale data, access denied, type mismatch)
- Be able to diagnose and resolve failures in real time without disrupting the class
- Maintain a second environment (instructor account) to demonstrate while trainees work in their own accounts

### 4-2. TM-10 Through TM-30 Exercise Walkthroughs

T3-I Day 2 covers a full walkthrough of every lab exercise in TM-10, TM-20, and TM-30 from the instructor perspective. The walkthrough covers:

| Course | Key Failure Points | Instructor Action |
|---|---|---|
| TM-10 | CAC authentication failure; Viewer vs. Builder confusion; export/classification marking errors | Pre-verify all student accounts before Day 1; demo the correct classification marking before students attempt it |
| TM-20 | Pipeline build failures (source schema change, type mismatch); Workshop layout issues; governance metadata omission | Keep a pre-built reference pipeline for comparison; teach "check the build log first" as the universal troubleshooting step |
| TM-30 | Ontology design errors (circular links, missing PKs, wrong cardinality); AIP Logic config errors; Quiver linked view failures | Use the design critique rubric to catch errors early; pre-stage a known-bad Ontology for the critique exercise |

### 4-3. Environment Troubleshooting

Instructors must be able to resolve the following without escalation:

| Issue | Root Cause | Resolution |
|---|---|---|
| CAC auth failure | Expired certificate, wrong CAC in reader, browser cache | Clear browser cache; re-insert CAC; verify certificate expiry |
| Account expired | Account not refreshed within MSS renewal window | Contact MSS Admin for reactivation; use backup student account in the interim |
| Wrong environment | Student navigated to production instead of training | Redirect to training environment URL; verify bookmarks |
| Missing project access | Student account not provisioned to the training project | Instructor grants temporary access (if authorized) or contacts MSS Admin |
| Stale training data | Synthetic data not refreshed since last course iteration | Re-run synthetic data loader script; notify C2DAO if script fails |
| Pipeline build error | Schema change in source dataset since last iteration | Identify changed columns; update pipeline transform; document for lesson improvement |

---

## CHAPTER 5 — LAB FACILITATION

### 5-1. Circulation

During lab exercises, the instructor circulates continuously. The circulation pattern:
1. Walk the entire room once to identify students who are stuck (body language: leaning back, not typing, staring at an error message)
2. Assist the most stuck student first — a student stuck for 5 minutes is likely to disengage for the rest of the block
3. After assisting, do not linger — move on. The goal is to unblock, not to co-pilot
4. On the second pass, check students who appeared to be working — verify they are on the right step, not 3 steps behind and building something wrong

### 5-2. The Help Gradient

| Student Signal | Instructor Response |
|---|---|
| "I got an error" | "Read me the error message." Guide them to interpret it. Do not take the keyboard. |
| "I don't know what to do next" | "What step are you on? What does the task reference say to do next?" Redirect to the materials. |
| "Can you just show me?" (during lab) | "Let me walk you through the thinking. What are you trying to accomplish?" Teach the reasoning, not the clicks. |
| "Can you just show me?" (during evaluation) | "I can't assist during the evaluation. Take a moment, re-read the task, and try your best approach." |
| Student is ahead of pace | Assign a stretch task or ask them to help a neighbor (peer instruction reinforces learning for both). |

### 5-3. Time Management

- Announce time checks: "You should be on Step 4 by now. If you're not, raise your hand."
- Keep a clock visible. Students lose time sense during labs.
- If 50%+ of the class is behind, stop individual assistance and do a group catch-up (demo the step everyone is stuck on)
- If 1-2 students are significantly behind and the rest are ready to move on, pair them with an ahead-of-pace student and continue

### 5-4. Dead Time Elimination

Dead time is when students are waiting and not working. Common causes:
- Instructor is helping one student for too long (cap individual assistance at 3 minutes; if unresolved, park the issue and return)
- Lab environment is loading or building (have a discussion question ready: "While your pipeline builds, let's talk about what would happen if the source schema changed")
- Students finished early (have stretch tasks pre-planned for every lab block)

---

## CHAPTER 6 — ASSESSMENT AND EVALUATION

### 6-1. T&EO Structure

Every MSS course evaluation is governed by a Training and Evaluation Outline (T&EO). T&EOs contain:

| Component | Description |
|---|---|
| Task Number | Unique identifier (e.g., TM10-01, TM20-03) |
| Task Title | What the trainee must do |
| Condition | Circumstances (environment, tools, references available) |
| Standard | Measurable performance criteria — the Go line |
| Performance Measures | Specific observable actions the evaluator checks |
| Critical Items | Performance measures marked as critical — failure on any critical item is automatic No-Go regardless of other performance |

### 6-2. Go/No-Go Standardization

The most important skill an evaluator develops is consistency. Two evaluators watching the same performance must reach the same Go/No-Go decision.

**Calibration process (taught in T3-I Day 2):**
1. All evaluators review the same T&EO
2. All evaluators watch the same recorded performance (or observe the same live performance)
3. Each evaluator scores independently
4. Evaluators compare scores and discuss discrepancies
5. The group establishes a common standard

**Common calibration failures:**
- Evaluator gives Go because the trainee "tried hard" — effort is not a performance measure
- Evaluator gives No-Go because the trainee used an unexpected method — if the result meets the standard, the method is acceptable unless the T&EO specifies a required method
- Evaluator assists during evaluation and then gives Go — any evaluator assistance during an evaluation period invalidates the Go

### 6-3. No-Go Counseling

Delivering a No-Go result is an instructor responsibility. The counseling must be:
- **Immediate:** Within the same day as the evaluation
- **Specific:** Identify exactly which performance measures were not met and why
- **Documented:** Record the No-Go result, the specific deficiencies, and the remediation plan
- **Constructive:** The goal is remediation, not punishment. Tell the trainee what they need to do differently, not what they did wrong

### 6-4. Pre-Test and Post-Test Administration

| Parameter | Standard |
|---|---|
| Pre-test timing | Day 1, first 20 minutes after course overview |
| Pre-test purpose | Diagnostic only — does not count toward Go/No-Go; identifies trainee baseline |
| Post-test timing | Final day, after all instruction blocks; before practical exercise |
| Post-test passing score | Varies by course (see POI); typically 70-80% |
| Answer key handling | Answer keys are instructor-only documents. Do not distribute the full exam file to students. Print student versions without answer keys. |

---

## CHAPTER 7 — PHASE 2: SUPERVISED PRACTICUM

### 7-1. Purpose

Phase 2 replaces the previous unstructured apprenticeship. It provides a documented, evaluated progression from classroom learning to independent course delivery.

### 7-2. Practicum Steps

| Step | Activity | Duration | Evaluator | Deliverable |
|---|---|---|---|---|
| P2-1 | **Co-teach:** Deliver 40%+ of blocks for one full course iteration under supervision | 1 course iteration (1-5 days) | Senior or Master Instructor | Co-teach observation notes from supervising instructor |
| P2-2 | **Lead observed:** Deliver the full course independently with observer present for at least 2 blocks per day | 1 course iteration | Training OIC or designated Senior Instructor | Formal Instructor Observation Report (FDP Appendix B) |
| P2-3 | **Evaluator observation** (if seeking evaluator certification): Conduct at least 1 complete Go/No-Go evaluation under observation | During P2-2 | Training OIC | Evaluator observation notes |
| P2-4 | **Certification:** Training OIC reviews all Phase 2 documentation and issues certification | Upon satisfactory P2-2 | Training OIC | Certification memorandum; entry in Instructor Roster |

### 7-3. Phase 2 Scheduling

Phase 2 is not contiguous with Phase 1. It is scheduled around actual course iterations:
- The T3-I graduate coordinates with the C2DAO Training OIC to identify upcoming course iterations
- P2-1 (co-teach) should occur within 90 days of Phase 1 completion to maintain momentum
- P2-2 (lead observed) should occur within 60 days of P2-1 completion
- If scheduling delays exceed these timelines, the candidate completes a re-familiarization lab before proceeding

### 7-4. Phase 2 Failure and Remediation

| Outcome | Action |
|---|---|
| P2-1 unsatisfactory (supervising instructor notes significant deficiencies) | Candidate repeats P2-1 with the same or different supervising instructor |
| P2-2 unsatisfactory on 1 criterion | Candidate receives written improvement plan; repeats P2-2 for the deficient area |
| P2-2 unsatisfactory on 2+ criteria | Candidate returns to Phase 1 (attends next T3-I iteration) before re-attempting Phase 2 |

---

## CHAPTER 8 — INSTRUCTOR PERFORMANCE STANDARDS

### 8-1. The Seven Observation Criteria

All instructors are evaluated on these criteria during Phase 2 observations and annual sustainment observations (per FDP §6-1):

| # | Criterion | Satisfactory Standard |
|---|---|---|
| 1 | **Technical Accuracy** | Instruction is technically correct. Errors are corrected immediately upon identification. No uncorrected errors in the observation period. |
| 2 | **Instructional Clarity** | Explanations are clear, appropriately paced, and reinforced with operationally relevant examples. |
| 3 | **Student Engagement** | Students are actively engaged during labs. Instructor identifies and assists students who are stuck. Dead time is minimized. |
| 4 | **Check on Learning** | Instructor uses effective check-on-learning questions throughout each block. Questions require more than yes/no answers. |
| 5 | **Lab Management** | Labs proceed on schedule. Instructor manages common errors efficiently without solving every student's problem for them. |
| 6 | **Evaluation Fidelity** | Evaluations follow T&EO procedures exactly. Evaluator does not assist during evaluation periods. Go/No-Go decisions are documented. |
| 7 | **Course Materials Currency** | Lesson plan is current. Slides reference the correct platform version. Materials have been reviewed before delivery. |

### 8-2. Hard No-Go Criteria for Instructor Evaluation

During T3-I Phase 1 microteaching and Phase 2 observations, the following are automatic No-Go:
- Unsatisfactory on **Technical Accuracy** — an instructor who teaches incorrect information causes operational harm
- Unsatisfactory on **Evaluation Fidelity** — an instructor who evaluates incorrectly certifies unqualified personnel

---

## CHAPTER 9 — LESSON IMPROVEMENT AND CURRICULUM MAINTENANCE

### 9-1. Lesson Improvement Log

Instructors are responsible for continuously improving course content. The process:
1. **During delivery:** Note any lesson weakness in the Lesson Improvement Log (FDP Appendix D)
2. **After each course iteration:** Review notes and draft revisions
3. **Submit:** Proposed revisions to Senior Instructor or Training OIC
4. **Approved revisions:** Incorporated into lesson plans; version history updated

### 9-2. Curriculum Maintenance SOP

The Curriculum Maintenance SOP governs the review cadence, approval authority, and version control for all MSS course materials. Instructors should be familiar with:
- Quarterly review cadence (Platform Monitor role)
- Change request process
- Version numbering conventions
- Review authority by change scope (minor wording → Instructor; structural → Senior Instructor; new content → Master Instructor or Training OIC)

---

*USAREUR-AF Operational Data Team*
*T3-I Instructor Certification | Version 1.0 | March 2026*
