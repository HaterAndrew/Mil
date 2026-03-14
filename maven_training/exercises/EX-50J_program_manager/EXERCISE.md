# EX-50J — Advanced Program Management
## Practical Exercise — TM-50J Proficiency

| Field | Value |
|-------|-------|
| **Version** | 1.0 — March 2026 |
| **Prerequisite** | TM-40J complete (Go on file); TM-50J course completion; Workshop access confirmed |
| **Duration** | 4–5 hours (typically executed Day 3 of TM-50J) |
| **Environment** | MSS Workshop (standard PM access); no Code Workspace or pipeline access required; see ENVIRONMENT_SETUP.md |
| **Companion TM** | TM_50J_PROGRAM_MANAGER_ADVANCED.md |
| **Syllabus** | SYLLABUS_TM50J |
| **Exams** | EXAM_TM50J_POST |

## SCENARIO

You are the senior Program Manager for the USAREUR-AF MSS program. The G6 has asked you to deliver two products in preparation for a GO/SES investment review:

1. A portfolio-level investment brief covering three candidate MSS capability expansions — the G6 needs a recommendation on which to fund, defer, or cancel
2. An organizational change management plan for the highest-priority expansion, covering adoption strategy, training pipeline, and resistance mitigation

You will also conduct a brief peer review of a draft program health dashboard submitted by a junior PM.

**Training environment:** All program data, stakeholder profiles, and capability descriptions are synthetic.

## TASK LIST

### Task 1 — Portfolio Investment Brief (90 min)

You are provided three candidate capability expansion descriptions (`portfolio_candidates_synthetic.pdf`). For each candidate:

- [ ] Identify and document: primary beneficiary (WFF or specialist community), technical complexity (low/medium/high), dependency on capabilities not yet in production, estimated training burden (how many personnel require new training), and primary risk
- [ ] Assess each candidate using the USAREUR-AF MSS Investment Prioritization Framework (provided): score each on operational value, technical readiness, and organizational readiness
- [ ] Produce a 1-page portfolio recommendation table: columns for each candidate, rows for each framework criterion, and a final recommendation row (Fund / Defer / Cancel)
- [ ] Write a 3–5 sentence GO/SES investment rationale: which candidate(s) to fund and why, framed around operational value and risk — no unexplained technical terminology

| Standard | Criteria |
|----------|----------|
| **Go** | All three candidates documented on all five attributes; all three scored on all three framework criteria; recommendation table complete with final row; GO/SES rationale present, non-technical, and tied to scoring |
| **No-Go** | Any candidate missing attributes; framework scoring incomplete; recommendation table absent; GO/SES rationale contains unexplained technical terminology |

### Task 2 — Organizational Change Management Plan (90 min)

For the candidate you recommended as "Fund" (or the highest-priority if multiple):

- [ ] Stakeholder analysis: identify at least 4 stakeholder groups (by role, not name), their current adoption posture (champion/neutral/resistant), and a one-sentence engagement strategy for each
- [ ] Training pipeline design: identify what training is required (TM level and track), what the estimated training timeline is (weeks/months), and what the enrollment bottleneck is likely to be
- [ ] Resistance mitigation: identify the two most likely sources of organizational resistance; for each, propose a specific mitigation action (not generic "communicate more" — name the action and who owns it)
- [ ] Success metrics: define 3 measurable metrics that will indicate successful adoption at 30 / 90 / 180 days post-deployment

| Standard | Criteria |
|----------|----------|
| **Go** | ≥4 stakeholder groups with posture and engagement strategy; training pipeline tied to specific TM levels; 2 resistance sources with specific mitigations (action + owner); 3 success metrics with 30/90/180 timeframes |
| **No-Go** | Fewer than 4 stakeholder groups; training pipeline not tied to TM levels; resistance mitigations are generic; success metrics absent or not tied to timeframes |

### Task 3 — Peer Review of Program Health Dashboard (45 min)

*Evaluator provides a draft program health dashboard (pre-built Workshop view) at exercise start.*

- [ ] Identify at least 2 of 3 planted issues (see Evaluator Notes for planted issues)
- [ ] For each issue identified, document: (a) what the issue is, (b) why it matters for GO/SES program reporting, and (c) a specific recommended correction
- [ ] Complete the PM peer review form (sections: data currency, metric definitions, audience appropriateness, and distribution controls)

| Standard | Criteria |
|----------|----------|
| **Go** | At least 2 of 3 planted issues identified with correct impact characterization; all four PM peer review form sections completed |
| **No-Go** | Fewer than 2 issues identified; issues identified without impact description; PM review form incomplete |

### Task 4 — Brief Delivery (30 min)

Deliver a 10-minute verbal brief to the evaluator (in the role of G6):

- [ ] Cover all three portfolio candidates with recommendation
- [ ] Explain the OCM plan for the funded candidate in plain language — no acronyms without definition for a GO audience
- [ ] Answer 2 evaluator questions in character (evaluator will ask about risk tradeoffs and training burden)

| Standard | Criteria |
|----------|----------|
| **Go** | All three candidates covered; recommendation clear with rationale; OCM plan explained without undefined acronyms; both evaluator questions answered with substance |
| **No-Go** | Any candidate missing from brief; recommendation not explained; undefined acronyms used; evaluator questions deflected without substantive answer |

## EVALUATOR NOTES

**Scoring:** 4 tasks. Go on 3 of 4 = overall Go. No-Go on Task 1 = automatic No-Go (core investment analysis standard).

### Pre-Exercise Checklist

- [ ] Confirm Workshop access for participant (standard PM access — no pipeline or code permissions needed)
- [ ] Print or provide digital copy of `portfolio_candidates_synthetic.pdf` (three 1–2 page capability expansion descriptions)
- [ ] Print or provide digital copy of USAREUR-AF MSS Investment Prioritization Framework (scoring rubric — evaluator controls distribution)
- [ ] Pre-build draft program health dashboard with 3 planted issues in participant's Workshop view
- [ ] Place blank PM peer review form in participant's project folder
- [ ] Prepare 2 evaluator questions for Task 4 (suggested: "What's your biggest technical risk on the funded candidate?" and "What happens if training pipeline capacity is lower than expected?")

### Pre-Planted Dashboard Issues (Task 3)

| Issue | Location | Description |
|-------|----------|-------------|
| Issue 1 | Readiness metric tile | Data-as-of timestamp is missing — dashboard shows readiness numbers with no indication of when the underlying data was last updated |
| Issue 2 | Training completion chart | Metric label reads "Training Completion" but the underlying calculation is enrollment count, not completion count — misleading to GO/SES audience |
| Issue 3 | Distribution | Dashboard is shared with write permissions to a distribution group that includes non-program personnel — OPSEC/need-to-know violation |

### Common Failure Modes

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | GO/SES rationale contains technical terms (API, pipeline, OSDK) without explanation | Ask: "Would a general officer know what [term] means?" — require revision |
| Task 1 | Framework scoring done without documentation (mental math only) | Ask to see the scoring worksheet; undocumented scoring = No-Go on that criterion |
| Task 2 | Training pipeline tied to "MSS training" generically, not specific TM levels | Ask: "Which TM course specifically? For which audience?" |
| Task 2 | Resistance mitigations are generic ("hold town halls," "communicate the vision") | Ask: "Who owns that action? By when? What does success look like?" |
| Task 3 | Issue 3 (distribution) not identified | Probe: "Can you show me who has access to this dashboard?" — if participant does not check permissions, coach on that as a standard PM review step |
| Task 4 | Evaluator questions deflected ("I'd have to check with my team") | Partial Go accepted if one question answered substantively — both deflected = Task 4 No-Go |
