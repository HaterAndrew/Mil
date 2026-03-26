# EX_40N — UI/UX Designer
## Practical Exercise — SL 4N Proficiency

| Field | Value |
|-------|-------|
| **Version** | 1.0 — March 2026 |
| **Prerequisite** | SL 3 REQUIRED; SL 4N — UI/UX Designer Technical Manual (and SL 1 through SL 2) |
| **Duration** | 3–4 hours |
| **Environment** | MSS with Workshop access, design tool (Figma or equivalent) — see ENVIRONMENT_SETUP.md |

## COMPANION RESOURCES

| Resource | Reference |
|----------|-----------|
| Technical Manual | SL 4N — UI/UX Designer |
| Syllabus | SYLLABUS_TM40N |
| Pre-Exercise Exam | EXAM_TM40N_PRE |
| Post-Exercise Exam | EXAM_TM40N_POST |
| Continuation Track | SL 5N — Advanced UI/UX Designer |

## WFF AWARENESS

The application designed in this exercise will serve WFF track personnel (TM-40A–F) in an operational context. Evaluators should verify that the design supports the target WFF's decision-making process, maintains classification marking compliance, meets WCAG 2.1 AA accessibility standards, and includes all required states (loading, empty, error, success).

## SCENARIO

The OPDATA team has received a request from a staff section to build a new MSS Workshop application. The application will display operational data and support a specific decision-making workflow. The requesting unit has provided a brief requirements document, but has not specified how the application should look or behave.

The trainee will conduct the full SCD design cycle: research → define → develop → validate — producing a design specification package ready for handoff to a SL 4L Software Engineer.

**Training context:** Trainees will use paired role-playing for user research (partner acts as the staff section user). Design tool and Workshop access provided.

## TASK LIST

### Task 1 — User Research (45 min)

- [ ] Write a research plan: objectives, methodology (contextual inquiry or semi-structured interview), participant criteria
- [ ] Conduct a 20-minute semi-structured interview with a paired trainee role-playing as the target user
- [ ] Document findings using structured notes: quotes, observations, pain points, tasks, environment constraints
- [ ] Synthesize findings into a problem statement (1–2 sentences)

| Standard | Criteria |
|----------|----------|
| **Go** | Research plan written before interview; interview conducted using SCD methodology; problem statement derived from evidence, not assumptions |
| **No-Go** | No research plan; interview not conducted; problem statement is an assumption rather than research finding |

### Task 2 — Persona and Information Architecture (30 min)

- [ ] Create a user persona: role, rank range, operational context, 3+ key tasks, 3+ pain points
- [ ] Design an information architecture: identify data elements, priority hierarchy, spatial organization
- [ ] Apply the "glance, scan, commit" framework — annotate the IA with 2s/10s/30s reading levels

| Standard | Criteria |
|----------|----------|
| **Go** | Persona grounded in research data (not invented); IA follows decision-first hierarchy; glance/scan/commit levels annotated |
| **No-Go** | Persona disconnected from research; IA organized by data model instead of user decision; no consideration of information priority |

### Task 3 — Visual Design and Workshop Layout (45 min)

- [ ] Produce a wireframe/mockup of the primary screen using MSS visual design standards
- [ ] Include classification banners (correct color and placement)
- [ ] Apply status color conventions with redundant encoding (color + icon + text)
- [ ] Verify minimum contrast ratios (4.5:1 body text, 3:1 large text)
- [ ] Specify Workshop layout: grid positions, widget types, data bindings

| Standard | Criteria |
|----------|----------|
| **Go** | Classification banners present and correct; status indicators use redundant encoding; contrast ratios verified; Workshop widget specification complete |
| **No-Go** | Missing classification banners; color-only status indicators; contrast ratios not verified |

### Task 4 — Interaction Specification (30 min)

- [ ] Document all interactions: click, filter, sort, submit, navigate
- [ ] Design all states: default, loading, empty, error, success
- [ ] Specify edge cases: 0 results, maximum results, null values, long text overflow
- [ ] Include error messages that are specific and actionable

| Standard | Criteria |
|----------|----------|
| **Go** | All five states designed; edge cases addressed; error messages are specific (not generic "an error occurred") |
| **No-Go** | Only happy-path designed; loading/empty/error states missing; edge cases not considered |

### Task 5 — Accessibility Audit (20 min)

- [ ] Complete the MSS accessibility checklist (SL 4N §6-2) against your design
- [ ] Verify keyboard navigability of all interactive elements
- [ ] Verify text alternatives for all non-text content
- [ ] Verify touch target sizes (minimum 44x44px)
- [ ] Document any accessibility gaps and planned remediation

| Standard | Criteria |
|----------|----------|
| **Go** | Checklist completed; all critical items pass or have documented remediation plan |
| **No-Go** | Checklist not completed; critical accessibility gaps with no remediation plan |

### Task 6 — Usability Test and Handoff (45 min)

- [ ] Conduct a 15-minute usability test with a paired trainee using think-aloud protocol
- [ ] Document task completion, errors, confusion points, and severity ratings
- [ ] Iterate design based on usability findings (at least 1 design change based on testing)
- [ ] Produce final handoff package: persona, IA, wireframes, interaction spec, accessibility checklist, Workshop layout specification

| Standard | Criteria |
|----------|----------|
| **Go** | Usability test conducted with a non-designer; at least 1 design change based on test findings; handoff package complete and a SL 4L SWE could implement without follow-up |
| **No-Go** | No usability test conducted; handoff package incomplete or requires follow-up clarification for implementation |

---

## EVALUATOR NOTES

- Evaluate the design process, not aesthetic preference. The design does not need to be "pretty" — it needs to be researched, structured, accessible, and implementable.
- Verify that research findings actually influenced the design (trace from interview notes → problem statement → persona → IA → design decisions).
- Check for the common failure mode: designing first, then backfilling research to justify the design.
- Classification banners are a hard Go/No-Go item. Missing banners = No-Go regardless of design quality.
