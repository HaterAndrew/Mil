# CONCEPTS GUIDE — T3-F COMPANION — MSC FORCE MULTIPLIER · MAVEN SMART SYSTEM (MSS)

> **BLUF:** This guide prepares MSC-level personnel to sustain MSS training at their unit. It does not teach platform skills — you already have those from TM-20. It develops the judgment to deliver training, evaluate trainees, and maintain training standards when C2DAO is not in the room.
> **Purpose:** Read before beginning T3-F. Return to individual sections as reference when delivering TM-10 at your unit.
> *HQ USAREUR-AF · v1.0 · 2026 · DISTRIB: USG only*

---

## PREFACE

**BLUF:** You are not becoming an instructor. You are becoming a trainer — a force multiplier who ensures your unit's personnel can use MSS without waiting for the next MTT visit.

The difference matters. An instructor (T3-I graduate) designs and delivers the full MSS curriculum. A Unit Data Trainer (T3-F graduate) delivers TM-10 using published materials and maintains a local training capability within defined limits. You do not need to be an instructional design expert. You need to be reliable, consistent, and honest about what you can and cannot do.

---

## SECTION 1 — WHY UNIT-LEVEL TRAINING MATTERS

### 1-1. The Geography Problem

USAREUR-AF spans a theater. Units are stationed across multiple countries, often hours apart. C2DAO's MTT rotates through MSCs on a quarterly cycle. Between visits, new arrivals, newly assigned personnel, and cross-leveled soldiers arrive at units without TM-10 qualification.

Without a UDT, these personnel:
- Cannot access MSS data products they need for their jobs
- Learn MSS informally from a coworker (unstandard, unevaluated, potentially wrong)
- Wait months for the next MTT visit
- Accumulate as a backlog that overwhelms the MTT when it arrives

### 1-2. What You Solve

A UDT at each MSC ensures:
- New arrivals get TM-10 within their first 30 days (per Commander's Guide)
- Training quality is consistent because it follows the same lesson plans, the same T&EOs, and the same Go/No-Go standards as C2DAO-delivered TM-10
- Training records are reported to C2DAO, maintaining theater-wide visibility
- The MTT can focus on TM-20, TM-30, and TM-40 courses during visits instead of running TM-10 catch-up iterations

---

## SECTION 2 — ABBREVIATED ADULT LEARNING PRINCIPLES

### 2-1. What You Need to Know

You do not need the full adult learning theory covered in T3-I. You need three principles:

**Principle 1: Adults learn by doing.**
TM-10 is lab-heavy. Let the trainees work. Do not lecture for 20 minutes when the lesson plan says to lecture for 5 and then move to a lab. The hands-on time is where learning happens.

**Principle 2: Adults need to know why.**
Before every block, tell the trainees why this skill matters to their job. Do not say "we're going to learn about dashboards." Say "your unit's readiness data is on a dashboard in MSS — after this block you'll know how to read it."

**Principle 3: Adults learn from mistakes — but only productive ones.**
When a trainee makes an error during a lab, do not immediately fix it for them. Ask: "What happened? What does the error message say?" Guide them to the fix. If the error is an infrastructure problem (account not working, environment down), fix it yourself immediately — that's not a learning opportunity, it's a blocker.

### 2-2. Managing the Mixed Classroom

Your TM-10 class will contain people with wildly different backgrounds. Some will pick up MSS navigation in 5 minutes. Others will need 30 minutes for the same task.

**Strategies:**
- Walk the room continuously during labs. Check on quiet students first — they are most likely stuck.
- If someone finishes early, ask them to help a neighbor. Peer teaching helps both people.
- If someone is significantly behind, pair them with a faster student and adjust your pace for the next block.
- Never single out a struggling student publicly. Everyone is there to earn a qualification.

---

## SECTION 3 — THE EVALUATOR MINDSET

### 3-1. The Switch

During instruction, you help. During evaluation, you observe. These are different roles and the trainees must know when the switch happens.

**Announce it clearly:** "We are now starting the practical exercise. From this point, I cannot provide assistance. You may use your task reference and any notes from today. Begin."

### 3-2. The Hardest Part

The hardest part of being a UDT is giving a No-Go to someone you work with every day. You will evaluate people from your own unit — people you eat lunch with, people your commander needs qualified.

**The rule is simple:** If the trainee does not meet the standard, the answer is No-Go. A No-Go is not a punishment. It is a statement that the trainee needs more practice before operating independently in MSS. Giving a false Go harms the trainee (they will struggle and fail operationally) and harms the data quality of every product they touch.

### 3-3. Borderline Cases

When you are unsure whether a performance is Go or No-Go:
- Re-read the T&EO standard. The standard is the arbiter, not your personal judgment.
- If the trainee met the standard using an unexpected method, it is Go (unless the T&EO specifies a required method).
- If you assisted the trainee during the evaluation — even a small hint — the evaluation is void. Re-evaluate on another scenario or at a later time.
- When genuinely uncertain, score No-Go and document why. It is always safer to require remediation than to certify someone who is not ready.

---

## SECTION 4 — KNOWING YOUR LIMITS

### 4-1. The Escalation Decision

The most important skill a UDT has is knowing when to say "this is beyond my scope." Escalation is not failure. Attempting to deliver training you are not qualified to deliver is failure.

**The escalation matrix:**

| Situation | UDT Action |
|---|---|
| Someone asks for TM-20 training | "I can facilitate a refresher on the basics (Blocks 1-10), but initial TM-20 certification requires a C2DAO instructor. Let me check the next MTT schedule." |
| Someone asks for TM-30+ training | "That's beyond my scope. I'll connect you with C2DAO to schedule the right course." |
| A commander asks you to waive a prerequisite | "I don't have authority to waive prerequisites. Let me connect you with C2DAO Training Division." |
| You think a lesson plan has an error | Deliver as written. Note the issue. Report to C2DAO after the iteration. Do not freelance a fix during delivery. |
| An environment issue you can't resolve | Stop troubleshooting after the time limit. Escalate to C2DAO. Work around the issue if possible (pair the affected student, use a demo). |

### 4-2. TM-20 Refresher Scope

You are authorized to facilitate TM-20 refresher labs for Blocks 1-10 only. These cover:
- Project creation and navigation
- File ingestion
- Basic pipeline building (single source, simple transforms)

You are NOT authorized to deliver:
- Blocks 11+ (multi-source joins, computed columns, advanced transforms)
- Workshop application building
- Ontology design
- AIP Logic configuration
- Governance workflow execution

If a TM-20-qualified person needs refresher training on topics beyond Blocks 1-10, they need a C2DAO instructor or the next MTT visit.

---

## SECTION 5 — BUILDING YOUR LOCAL TRAINING PROGRAM

### 5-1. Scheduling

Work with your unit training NCO to establish a regular TM-10 cadence:
- Monthly if your unit receives 5+ new personnel per month
- Bi-monthly for lower turnover
- Minimum quarterly to maintain your UDT designation

### 5-2. Classroom Setup

You need:
- A room with a projector and workstations (1 per student + 1 for you)
- Network access to the MSS training environment from each workstation
- Printed materials (student handouts, exams, T&EO scoring sheets)

If your unit does not have a dedicated classroom, coordinate with S3 or S6 for a conference room with laptop connectivity. MSS is web-based — any computer with a browser and CAC reader works.

### 5-3. Building Unit Buy-In

Your commander nominated you, but the rest of the unit may not understand why TM-10 matters. Frame it in terms of their mission:
- "You can't access the readiness data your boss needs without TM-10."
- "TM-10 takes one day. After that, you can pull your own reports instead of asking someone else."
- "This is a Go/No-Go qualification — it goes in your training record."

### 5-4. Working with the MTT

When the MTT visits your MSC:
- Coordinate in advance: provide your training status report, identify gaps, request specific courses
- Sit in on MTT-delivered courses when possible (observer seat) — it refreshes your skills
- Expect the MTT to observe your TM-10 delivery for annual re-certification
- Introduce the MTT to your unit training NCO and key leaders

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*Concepts Guide — T3-F MSC Force Multiplier | Version 1.0 | March 2026*
