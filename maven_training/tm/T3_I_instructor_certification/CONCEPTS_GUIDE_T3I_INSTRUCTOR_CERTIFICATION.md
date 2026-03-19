# CONCEPTS GUIDE — T3-I COMPANION — INSTRUCTOR CERTIFICATION · MAVEN SMART SYSTEM (MSS)

> **Forward:** This guide develops the mental models required to teach MSS effectively. It does not teach platform mechanics — it teaches how to teach platform mechanics to adults under operational time pressure.
> **Purpose:** Read before beginning T3-I classroom instruction. Return to individual sections as reference during Phase 2 practicum.
> *HQ USAREUR-AF · v1.0 · 2026 · DISTRIB: USG only*

---

## PREFACE

**BLUF:** Most instructional failures on MSS are not caused by instructors who lack platform knowledge. They are caused by instructors who cannot transfer that knowledge efficiently to adults with heterogeneous skill levels, limited time, and immediate operational need.

The best MSS operator is not automatically the best MSS instructor. Building a pipeline and teaching someone to build a pipeline are fundamentally different skills. This guide addresses the second skill.

Read this guide linearly before beginning T3-I. The sections build on each other.

---

## SECTION 1 — THE INSTRUCTIONAL PROBLEM

### 1-1. What Makes MSS Instruction Different

MSS instruction is not vendor product training. It is not a conference demo. It is operational training that certifies people to build data products that directly support commander decision-making in a theater of operations.

**Key differences from commercial training:**

| Commercial Training | MSS Training |
|---|---|
| Trainees choose to attend | Trainees are directed to attend |
| No formal evaluation | Go/No-Go evaluation with operational consequences |
| General use cases | Specific operational problems (CCIR, readiness, targeting) |
| One skill level per class | Mixed skill levels in every class |
| Unlimited retake | Limited iterations; remediation timeline enforced |
| Instructor is a presenter | Instructor is a certifier |

### 1-2. The Mixed Classroom

Every MSS course — especially TM-10 and TM-20 — contains trainees with wildly different backgrounds:
- The 25-series Soldier who has been building in Foundry for 6 months and is here for the formal certification
- The O-5 who was directed to attend and has never opened a web application more complex than email
- The contractor with 10 years of data engineering experience who has never used Foundry specifically
- The junior enlisted Soldier who is eager but has no data background

**The instructor must serve all of them simultaneously.** The temptation is to teach to the middle. The reality is that the lowest-skilled trainee sets the floor (they must pass Go/No-Go) and the highest-skilled trainee sets the engagement ceiling (they will disengage if not challenged).

**Strategies:**
- Stretch tasks for advanced trainees (pre-planned, available for every lab block)
- Peer pairing: advanced trainees assist struggling trainees (reinforces their own learning)
- Differentiated check-on-learning: easier questions to verify baseline comprehension; harder questions to challenge advanced trainees
- Never publicly identify the skill spread. Treat every trainee as a professional who is there to earn a qualification.

### 1-3. The Time Constraint

MSS courses are compressed. TM-10 is 1 day. TM-20 is 5 days. There is no slack in the schedule for extended discussions, repeated demonstrations, or off-topic exploration.

**Implication for instructors:** Every minute of instruction must be purposeful. The lesson plan is the contract. If a block is scheduled for 90 minutes, it runs 90 minutes. If the class is behind, the instructor adjusts within the block — not by cutting the next block.

---

## SECTION 2 — HOW ADULTS LEARN TECHNICAL SKILLS

### 2-1. The Demonstration-Practice-Feedback Loop

Adults learn technical skills through a cycle of watching, doing, and receiving feedback. The instructor's job is to manage this cycle efficiently.

```
Demonstrate (5 min) → Practice (15 min) → Feedback (5 min) → Repeat
```

**The 75% rule:** In any lab block, trainees should be working (hands on keyboard) for at least 75% of the time. If the instructor is talking for more than 25% of a lab block, the balance is wrong.

### 2-2. Cognitive Load Theory

Working memory is limited. Adults can hold approximately 4-7 new items in working memory at once. MSS platform operations involve many simultaneous elements (navigation, data selection, configuration, naming, governance).

**Managing cognitive load:**
- Introduce one new concept per lab step. Do not combine "learn to build a pipeline" with "learn the governance naming convention" in the same step.
- Use pre-built reference artifacts. When teaching Workshop layout, start with a pre-built dashboard and modify it rather than building from a blank page.
- Externalize memory. Teach trainees to use the task reference as a checklist, not to memorize procedures.

### 2-3. Error as Learning

Errors are not failures during training — they are learning events. The instructor's goal is not to prevent all errors. It is to ensure that errors are productive.

**Productive error:** The trainee builds a pipeline that fails because they chose the wrong join type. The error message tells them what happened. The instructor asks: "What does the error say? What join type did you use? What would happen if you used a left join instead?" The trainee corrects the error and understands the concept.

**Unproductive error:** The trainee cannot log in because their account was not provisioned. There is nothing to learn. This is an infrastructure failure that the instructor should have prevented during pre-course setup.

**The instructor's job:** Eliminate unproductive errors through preparation. Allow productive errors during labs. Intervene only when the trainee cannot recover independently after a reasonable attempt (3-5 minutes).

---

## SECTION 3 — THE INSTRUCTOR-EVALUATOR DUAL ROLE

### 3-1. The Tension

During lab blocks, the instructor helps trainees succeed. During evaluation periods, the evaluator observes without assistance. These are fundamentally different roles performed by the same person, sometimes on the same day.

**The line:** During instruction, the instructor is a coach. During evaluation, the instructor is a referee. The trainee must know which mode is active. Announce transitions clearly: "We are now entering the practical exercise. From this point, I cannot provide assistance. You may use your task reference and any notes you took during the course."

### 3-2. The Assistance Trap

The most common evaluator error: helping a struggling trainee during the evaluation because the evaluator wants them to succeed. This invalidates the evaluation and ultimately harms the trainee (and every operational user who depends on data products built by that trainee).

**Rule:** If you assist during an evaluation, the evaluation is void. The trainee must be re-evaluated on a new scenario or at a later time. There is no exception.

### 3-3. Evaluation Documentation

Every Go/No-Go decision must be documented using the T&EO scoring sheet:
- Each performance measure is scored Go or No-Go individually
- The overall Go/No-Go is determined by the T&EO rules (typically: Go on all critical items + Go on X of Y total items)
- The evaluator signs the scoring sheet
- The scoring sheet is filed in the course records and the trainee's training file

---

## SECTION 4 — THE COMMON TRAINEE ERROR TAXONOMY

### 4-1. Why Catalog Errors

Experienced instructors see the same errors across multiple course iterations. Cataloging these errors and their root causes allows:
- Faster diagnosis during labs (the instructor recognizes the symptom instantly)
- Better prevention (the instructor warns about the error before the step where it occurs)
- Curriculum improvement (if 80% of trainees make the same error, the instruction or exercise design needs revision)

### 4-2. The Top 10 (by course level)

| # | Course | Error | Root Cause | Intervention |
|---|---|---|---|---|
| 1 | TM-10 | Incorrect classification marking on export | Trainee does not understand classification applies to the data content, not the file format | Pre-brief classification rules before first export exercise; check every trainee's first export |
| 2 | TM-10 | Navigating to production instead of training environment | Bookmarked wrong URL or followed a link from an email | Verify bookmarks during pre-course; announce the correct URL at start of every day |
| 3 | TM-20 | Pipeline build failure — type mismatch | Trainee joined columns with different data types without casting | Teach "check column types before joining" as a mandatory pre-join step |
| 4 | TM-20 | Workshop filter does not work | Trainee applied filter to wrong data source or used wrong column name | Teach the filter configuration pattern: source → column → operator → value |
| 5 | TM-20 | Governance metadata omitted | Trainee did not add description and tags before promoting | Add governance check to the exercise checklist; use it as a check-on-learning question |
| 6 | TM-30 | Ontology design — circular link types | Trainee created a bidirectional link instead of two unidirectional links | Use the design critique rubric; teach the "draw it on paper first" technique |
| 7 | TM-30 | Ontology design — wrong primary key | Trainee used a non-unique column as PK, causing silent data loss on sync | Teach the PK uniqueness check before sync; show what happens when PK is not unique |
| 8 | TM-30 | AIP Logic config error — wrong trigger condition | Trainee connected a continuous trigger instead of on-demand | Walk through trigger types before the config exercise; use a pre-built workflow with labeled triggers |
| 9 | TM-30 | Quiver linked view — cross-object filter not propagating | Link type not configured for the filter direction | Teach the link direction concept before the Quiver exercise; use a diagram |
| 10 | All | Student falls behind and stops asking for help | Trainee disengages out of frustration or embarrassment | Instructor circulates and proactively checks quiet students; normalize asking for help in the course overview |

### 4-3. Using the Taxonomy

- Review the relevant errors before each course iteration
- Brief the most common errors at the start of the block where they occur (prevention)
- When a trainee makes a cataloged error, use the documented intervention rather than ad-hoc troubleshooting
- Log new errors not in the taxonomy in the Lesson Improvement Log

---

## SECTION 5 — THE PRE-COURSE CHECKLIST

### 5-1. Why It Matters

The pre-course checklist is the single most important administrative task an instructor performs. A failed pre-course setup wastes the first hours of Day 1 — hours that cannot be recovered in a compressed course schedule.

### 5-2. Universal Pre-Course Checklist

The following applies to every MSS course:

- [ ] Verify all enrolled students have active MSS accounts at the correct access level
- [ ] Confirm training environment is accessible from classroom workstations
- [ ] Load or refresh synthetic training data (course-specific dataset)
- [ ] Print student materials: task reference handout, exercise packet
- [ ] Print evaluation materials: pre-test, post-test (answer keys secured separately), T&EO scoring sheets
- [ ] Verify projector/display and instructor workstation connectivity
- [ ] Review lesson plans for currency (check for platform updates since last iteration)
- [ ] Confirm evaluator availability and credentials for Go/No-Go blocks
- [ ] Brief evaluators on T&EOs (even if they evaluated the same course last iteration — standards may have been updated)

### 5-3. Course-Specific Additions

Each course has additional pre-course requirements (e.g., TM-40M requires GPU Code Workspace provisioned 10+ days in advance; TM-40L requires OSDK developer access). See the course-specific syllabus for the complete pre-course checklist.

---

## SECTION 6 — THE AFTER-ACTION REVIEW

### 6-1. Purpose

Every course iteration ends with an After-Action Review (AAR). The AAR is not a satisfaction survey. It is a structured review of what happened, why, and what to change.

### 6-2. AAR Format

| Phase | Question | Duration |
|---|---|---|
| 1. What was planned? | Review the learning objectives and daily schedule | 5 min |
| 2. What happened? | What went well? What didn't? Open discussion with trainees and co-instructors | 10 min |
| 3. Why? | Root cause for significant deviations (schedule overrun, high No-Go rate, environment failures) | 10 min |
| 4. What do we change? | Specific, actionable changes for the next iteration. Assign owners and deadlines. | 5 min |

### 6-3. AAR Outputs

- Lesson Improvement Log entries for any curriculum issues identified
- Environment issue reports for any infrastructure failures
- Updated instructor notes for the next iteration
- Trainee feedback (captured but not attributed — candid feedback requires anonymity)

---

*USAREUR-AF Operational Data Team*
*Concepts Guide — T3-I Instructor Certification | Version 1.0 | March 2026*
