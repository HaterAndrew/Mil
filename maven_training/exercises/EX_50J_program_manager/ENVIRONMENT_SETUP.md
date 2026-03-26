# ENVIRONMENT SETUP — EX_50J Advanced Program Manager (SL 5J)

**Companion resources:** TM_50J_PROGRAM_MANAGER_ADVANCED.md | SYLLABUS_TM50J | EXAM_TM50J_POST

## Environment Type

MSS Workshop (standard PM access). This is the least technically complex of the SL 5 exercises — no Code Workspace, no Pipeline Builder, no GPU allocation required. The exercise is a product and decision-making exercise, not a technical build exercise. Confirm Workshop access only.

## Required Access

| Account | Role |
|---------|------|
| Participant | Workshop (create and publish views), training project read/write |
| Evaluator | Workshop editor (to pre-build the draft program health dashboard with planted issues); training project read (to receive submitted products) |

**Lead time:** Standard Workshop access — 2–3 duty days. Confirm access at least 5 duty days before the exercise to allow time to resolve any provisioning issues.

## Pre-Load Instructions

### 1. Portfolio Candidates Package

Prepare `EX_50J_PM_Training_Data/portfolio_candidates_synthetic.pdf` (or .md):

Three synthetic capability expansion descriptions, each 1–2 pages:

| Candidate | Name | Summary |
|-----------|------|---------|
| Candidate A | Automated CCIR Threshold Recommendations | AI-powered system suggesting CCIR thresholds based on historical trigger patterns; medium technical complexity; depends on production LOGSTAT and SIGACT pipelines (both in production) |
| Candidate B | Cross-Echelon Readiness Federated View | Federated readiness dashboard aggregating data across division, brigade, and battalion MSS instances; high technical complexity; requires Ontology federation capability not yet in production |
| Candidate C | Training Environment Automation | Automated synthetic dataset generation for the TM training program; low technical complexity; no new infrastructure dependencies |

**Designed outcome:** Candidate A is the "Fund" recommendation under standard prioritization (high operational value, medium complexity, no blocking dependencies). Candidate B has high value but is not fundable until federated Ontology is delivered. Candidate C is fundable but low operational priority. Evaluator should not reveal the expected outcome — participants may reasonably recommend differently with documented rationale.

### 2. Investment Prioritization Framework

Prepare the USAREUR-AF MSS Investment Prioritization Framework scoring rubric (1 page):

| Criterion | 1 (Low) | 2 (Medium) | 3 (High) |
|-----------|---------|-----------|---------|
| Operational Value | Addresses niche use case for <10% of users | Addresses common use case for a WFF or specialist community | Addresses cross-cutting use case for multiple WFFs or enterprise-wide |
| Technical Readiness | Requires capabilities not yet in production | Requires non-trivial integration with existing production capabilities | Ready to build on current production stack with no new dependencies |
| Organizational Readiness | Requires extensive new training and change management | Requires moderate training for a defined user population | Minimal additional training; target users largely trained |

Distribute to participant at exercise start.

### 3. Pre-Built Dashboard (Task 3 Peer Review)

Build the draft program health dashboard in participant's Workshop view before exercise day. The dashboard should appear professionally formatted but contain the 3 planted issues:

**Dashboard structure:**
- Tile 1: Readiness metric (current value, missing data-as-of timestamp) → Issue 1
- Tile 2: Training completion bar chart (enrollment count mislabeled as completion) → Issue 2
- Distribution settings: shared with write access to non-program distribution group → Issue 3

The dashboard should look plausible — issues should require examination to find, not be immediately obvious.

### 4. Blank PM Peer Review Form

Place `pm_peer_review_form_blank.md` in participant's project folder:

Sections:
1. Data Currency (are timestamps present and current?)
2. Metric Definitions (do labels accurately describe the underlying calculation?)
3. Audience Appropriateness (is the product appropriate for the stated audience without unexplained terminology?)
4. Distribution Controls (are permissions and classification markings correct?)
5. Signature block

## Environment URL

```
[Insert training MSS tenant URL here]
```

## Scoring Sheet Reference

Evaluators record task Go/No-Go on standard EX_50J Evaluation Form (available from training NCO). For Task 1, attach or photograph the portfolio recommendation table as evidence. For Task 3, record which planted issues were identified. For Task 4, record evaluator question and participant response summary in notes. Overall Go/No-Go, participant name, evaluator name, and date required for training record submission.

## Notes

- This is the only SL 5 exercise that does not require Code Workspace or GPU allocation — it is a product-and-decision exercise
- If the evaluator is not available for Task 4 (10-minute verbal brief), an asynchronous written response may substitute, but the live Q&A component is strongly preferred
- The portfolio candidates are calibrated for approximately 90 minutes of analysis work at the SL 5J level; if a participant completes Task 1 in under 60 minutes, probe depth of the framework scoring before awarding Go
- The "planted issues" in the dashboard are designed to test the skills explicitly taught in SL 5J (program health dashboard standards, distribution controls) — they should not be trivially obvious on first view
