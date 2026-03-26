# EX_40J — Program Manager (Technical)
## Practical Exercise — SL 4J Proficiency

| Field | Value |
|-------|-------|
| **Version** | 1.0 — March 2026 |
| **Prerequisite** | SL 3 REQUIRED; SL 4J — Program Manager (Technical) Technical Manual (and SL 1 through SL 2) |
| **Duration** | 2–3 hours |
| **Environment** | MSS with project tracking access; access to a sample project record — see ENVIRONMENT_SETUP.md |

## COMPANION RESOURCES

| Resource | Reference |
|----------|-----------|
| Technical Manual | SL 4J — Program Manager (Technical) |
| Syllabus | SYLLABUS_TM40J |
| Pre-Exercise Exam | EXAM_TM40J_PRE |
| Post-Exercise Exam | EXAM_TM40J_POST |
| Continuation Track | SL 5J — Advanced Program Manager |

## WFF AWARENESS

The PM exercise centers on a data pipeline that directly serves WFF track personnel (TM-40A–F) as end-users — the LOGSTAT aggregation feed described in the scenario is a sustainment and maneuver reporting tool. Participants should recognize that delivery failures have operational impact across multiple WFF tracks, not just within the data team.

## SCENARIO

You are the technical PM for a data pipeline project: an automated LOGSTAT aggregation feed currently 6 weeks into development. The pipeline engineer has hit a blocker — a source system API is rate-limited and the pipeline is missing its delivery milestone. Assess the project status, update the plan, communicate the risk, and run a sprint retrospective.

**Training materials:** Pre-loaded synthetic project record (located in `training_data/EX_40J_project_record_package/`):
- `pipeline_definition.md` — pipeline architecture, tech stack, source systems
- `milestone_tracker.md` — 8-week project plan; week 4 milestone marked missed
- `open_tickets.md` — 4 open tickets including the rate-limit blocker (Ticket #EX40J-007)
- `project_charter.md` — original scope, stakeholders, success criteria

## TASK LIST

### Task 1 — Project Status Assessment (30 min)

- [ ] Review the sample project record: identify current milestone, percent complete, and open blockers
- [ ] Produce a 1-page SITREP (BLUF, current status, blockers, recommended COA)
- [ ] Identify whether the missed milestone is a schedule slip or a scope change

| Standard | Criteria |
|----------|----------|
| **Go** | SITREP is accurate vs. project record; slip vs. scope correctly classified |
| **No-Go** | SITREP contains factual errors or misclassifies the problem type |

### Task 2 — Risk and COA Analysis (30 min)

- [ ] Identify the top 3 risks to delivery given the API rate-limit blocker
- [ ] For each risk: assess likelihood (H/M/L) and impact (H/M/L)
- [ ] Propose a preferred COA with rationale (one paragraph)

| Standard | Criteria |
|----------|----------|
| **Go** | 3 risks identified with likelihood/impact assessments; COA is actionable |
| **No-Go** | Fewer than 3 risks or COA is not actionable |

### Task 3 — Revised Milestone Plan (30 min)

Produce a revised milestone table with four columns:

| Column | Content |
|--------|---------|
| Original Date | As planned |
| Revised Date | Updated per current status |
| Delta | Days slipped |
| Reason | Root cause |

- [ ] Identify any downstream milestones affected by the slip
- [ ] Flag whether commander approval is needed for the scope/schedule change

| Standard | Criteria |
|----------|----------|
| **Go** | Table is complete; downstream effects identified; approval flag is correct |
| **No-Go** | Downstream effects missed or approval flag is wrong |

### Task 4 — Sprint Retrospective Facilitation (30 min)

- [ ] Prepare a sprint retrospective agenda (15–20 min format): went well, blockers, improvements
- [ ] Conduct the retrospective with your evaluator playing the role of a pipeline engineer
- [ ] Produce 2–3 written action items with owners and due dates

| Standard | Criteria |
|----------|----------|
| **Go** | Retro covers all three sections; action items have owners and dates |
| **No-Go** | Action items lack owners or dates; retro is evaluative not constructive |

### Task 5 — Stakeholder Communication (15 min)

Draft a 5-sentence stakeholder update email. Required elements:

1. What happened
2. Impact
3. What you're doing
4. Ask of stakeholder
5. Next update date

| Standard | Criteria |
|----------|----------|
| **Go** | All five elements present; tone appropriate for an O-5/SES audience |
| **No-Go** | Missing elements or inappropriate tone |

## EVALUATOR NOTES

**Scoring:** 5 tasks. Go on 4 of 5 = overall Go. No-Go on Task 1 = automatic No-Go (project assessment is the foundational PM competency).

### Pre-Exercise Checklist

- [ ] Confirm the synthetic project record is pre-loaded and accessible to the training account
- [ ] Review the project record before the exercise — know the correct answers for Task 1
- [ ] Prepare the evaluator scenario card for Task 4 (see ENVIRONMENT_SETUP.md) — you will play a pipeline engineer

### Common Failure Modes

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | SITREP missing BLUF | Ask participant what the first line of an Army SITREP should be; BLUF is doctrine |
| Task 1 | Slip vs. scope misclassified | Slip = same deliverable, later date; scope = requirements changed; read the project record carefully to verify the answer |
| Task 2 | Fewer than 3 risks identified | Prompt once: "Are there any risks beyond the immediate blocker?" — if still < 3, No-Go |
| Task 2 | COA is not actionable | Vague COA ("explore options") = No-Go; must include a specific recommended action with owner |
| Task 4 | Retrospective becomes blame-focused | Most common failure for participants without facilitation experience; evaluator should respond as a defensive engineer and observe how participant handles it |
| Task 5 | Email missing the "ask of stakeholder" element | Very common omission; mark Task 5 No-Go and coach on stakeholder communication structure |

### Timing Notes

- Task 4 (retro facilitation) varies widely by background — 15 min for experienced facilitators, 40+ min for first-timers
- Task 3 (revised milestone plan) is often underestimated; budget 40 min
- Consider asking participant to narrate their SITREP before reviewing the written version (Task 1)

## NEXT STEPS

Participants who receive an overall Go on EX_40J are eligible to enroll in **SL 5J — Advanced Program Manager**. SL 5J extends into portfolio-level program management, enterprise governance, and cross-functional delivery at scale. SL 5 is G–O (advanced specialist tracks).

### Evaluator Role-Play Card (Task 4)

You are a pipeline engineer, 6 weeks into this project. Attitude: frustrated but professional.

| Behavior | Condition |
|----------|-----------|
| Defend your technical approach when asked | Always |
| Do not volunteer information about the rate-limit workaround you found | Unless participant asks the right questions |
| Become less cooperative | If the facilitator becomes evaluative ("why didn't you catch this sooner?") |
| Gradually become more engaged | If the facilitator is constructive |

## Supplemental — Build with AIP Official Tutorials

| Tutorial | Key Concepts | Relevance |
|----------|-------------|-----------|
| Platform Governance App (Platform SDK) | Metadata management, linter alerts, admin workflows | Project governance, compliance |
| Obfuscate Data with Cipher | CipherText properties, GDPR/HIPAA patterns | Data protection compliance |
| Building a Data-Rich Custom Object View | Customizable data presentation hubs | Stakeholder dashboards |

> Install via [build.palantir.com](https://build.palantir.com) — search "Examples (Build with AIP)" in the application drawer.

## ENVIRONMENT SETUP

See [ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md) for full setup instructions.
