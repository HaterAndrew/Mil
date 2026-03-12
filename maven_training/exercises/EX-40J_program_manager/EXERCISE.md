# EX-40J — Program Manager (Technical)
## Practical Exercise — TM-40J Proficiency

**Version 1.0 | March 2026**
**Prerequisite:** TM-40J, Program Manager (Technical) Technical Manual (and TM-10 through TM-30)
**Duration:** 2–3 hours
**Environment:** MSS with project tracking access; access to a sample project record (see ENVIRONMENT_SETUP.md)

---

## SCENARIO

You are the technical PM for a data pipeline project: an automated LOGSTAT aggregation feed that is currently 6 weeks into development. The pipeline engineer has hit a blocker — a source system API is rate-limited and the pipeline is missing its delivery milestone. You must assess the project status, update the plan, communicate the risk, and run a sprint retrospective.

**Training materials:** Pre-loaded sample project record in MSS (pipeline definition, milestone tracker, sample tickets).

---

## TASK LIST

### Task 1 — Project Status Assessment (30 min)
- [ ] Review the sample project record: identify current milestone, percent complete, and open blockers
- [ ] Produce a 1-page SITREP (BLUF, current status, blockers, recommended COA)
- [ ] Identify whether the missed milestone is a schedule slip or a scope change
- **Go:** SITREP is accurate vs. project record; slip vs. scope correctly classified
- **No-Go:** SITREP contains factual errors or misclassifies the problem type

### Task 2 — Risk and COA Analysis (30 min)
- [ ] Identify the top 3 risks to delivery given the API rate-limit blocker
- [ ] For each risk: assess likelihood (H/M/L) and impact (H/M/L)
- [ ] Propose a preferred COA with rationale (one paragraph)
- **Go:** 3 risks identified with likelihood/impact assessments; COA is actionable
- **No-Go:** Fewer than 3 risks or COA is not actionable

### Task 3 — Revised Milestone Plan (30 min)
- [ ] Produce a revised milestone table: original date, revised date, delta, reason
- [ ] Identify any downstream milestones affected by the slip
- [ ] Flag whether commander approval is needed for the scope/schedule change
- **Go:** Table is complete; downstream effects identified; approval flag is correct
- **No-Go:** Downstream effects missed or approval flag is wrong

### Task 4 — Sprint Retrospective Facilitation (30 min)
- [ ] Prepare a sprint retrospective agenda (15–20 min format): went well, blockers, improvements
- [ ] Conduct the retrospective with your evaluator playing the role of a pipeline engineer
- [ ] Produce 2–3 written action items with owners and due dates
- **Go:** Retro covers all three sections; action items have owners and dates
- **No-Go:** Action items lack owners or dates; retro is evaluative not constructive

### Task 5 — Stakeholder Communication (15 min)
- [ ] Draft a 5-sentence stakeholder update email: what happened, impact, what you're doing, ask of stakeholder, next update date
- **Go:** All five elements present; tone is appropriate for an O-5/SES audience
- **No-Go:** Missing elements or inappropriate tone

---

## EVALUATOR NOTES

**Scoring:** 5 tasks. Go on 4 of 5 = overall Go. No-Go on Task 1 = automatic No-Go (project assessment is the foundational PM competency).

**Pre-exercise checklist:**
- Confirm the synthetic project record is pre-loaded and accessible to the training account
- Review the project record yourself before the exercise so you know the correct answers for Task 1
- Prepare the evaluator scenario card for Task 4 (see ENVIRONMENT_SETUP.md) — you will play a pipeline engineer

**Common failure modes:**

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | SITREP missing BLUF | Ask participant what the first line of an Army SITREP should be; BLUF is doctrine |
| Task 1 | Slip vs. scope misclassified | Slip = same deliverable, later date; scope = requirements changed; read the project record carefully to verify the answer |
| Task 2 | Fewer than 3 risks identified | Prompt once: "Are there any risks beyond the immediate blocker?" — if still < 3, No-Go |
| Task 2 | COA is not actionable | Vague COA ("explore options") = No-Go; must include a specific recommended action with owner |
| Task 4 | Retrospective becomes blame-focused | This is the most common failure for participants without facilitation experience; evaluator should respond as a defensive engineer and observe how participant handles it |
| Task 5 | Email missing the "ask of stakeholder" element | Very common omission; mark Task 5 No-Go and coach on stakeholder communication structure |

**Timing notes:**
- Task 4 (retro facilitation) timing varies widely by background — 15 min for experienced facilitators, 40+ min for first-timers
- Task 3 (revised milestone plan) is often underestimated; budget 40 min
- Consider asking participant to narrate their SITREP to you before reviewing the written version (Task 1)

**Evaluator role-play card (Task 4):**
You are a pipeline engineer. You've been working on this project for 6 weeks. Your attitude: frustrated but professional. Key behaviors to exhibit:
- Defend your technical approach when asked
- Do not volunteer information about the rate-limit workaround you found (participant must ask the right questions)
- If the facilitator becomes evaluative ("why didn't you catch this sooner?"), become less cooperative
- If the facilitator is constructive, gradually become more engaged

---

## ENVIRONMENT SETUP

See [ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md) for full setup instructions.
