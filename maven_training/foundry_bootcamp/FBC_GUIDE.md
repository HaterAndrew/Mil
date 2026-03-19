# FOUNDRY BOOTCAMP (FBC)
## Participant Guide — Maven Smart System
### USAREUR-AF Operational Data Team

> **BLUF:** The Foundry Bootcamp is a quarterly 5-day supervised build event. You bring a validated operational problem. You build a solution. SMEs are in the room for consultation. Minimal instruction — this is not a course. You leave with a functional product and a handoff package.
> **Prereq:** TM-20 (Builder) Go on file + command-approved project.
> *HQ USAREUR-AF · v1.0 · 2026 · DISTRIB: USG only · AUTH: C2DAO/UDRA v1.1*

---

## 1. WHAT THE FOUNDRY BOOTCAMP IS

The Foundry Bootcamp is not part of the TM-10 through TM-50 training sequence. It does not grant TM-30 credit or unlock TM-40 enrollment. It is a separate, standalone event for personnel who:

- Hold TM-20 qualification
- Have a real operational problem that needs a Foundry solution
- Have command approval to spend a week building it

The bootcamp exists because the best learning often happens when someone has a problem they actually need to solve. The training environment, synthetic exercises, and structured curriculum of TM-20/30 are essential — but some people learn faster when their problem is on the line.

FBC is that opportunity. Build something real, with support, under a governance-aware environment.

**The bootcamp does not replace TM-30.** If you need structured instruction on advanced platform skills, enroll in TM-30. FBC assumes you can already operate the platform at TM-20 level and supplements that by putting you in a room to apply those skills to a real problem.

---

## 2. WHO ATTENDS

| Requirement | Detail |
|---|---|
| TM-20 Go on file | Hard requirement — no exceptions |
| Command-approved project | Validated Project Brief approved by C2DAO coordinator ≥14 days before bootcamp Day 1 |
| Command sponsorship | Supervisor signature on enrollment request |

TM-30 qualification is not required and not necessary. Personnel who hold TM-30 may attend FBC if they have an operational project and want supervised build time — the bootcamp is open to any TM-20+ qualified builder with an approved project.

---

## 3. THE PROJECT REQUIREMENT

The project is the core of the bootcamp. Without a validated project, there is no bootcamp seat.

### 3-1. What Makes a Good FBC Project

A valid FBC project has:

**A specific output.** Not "improve data quality" — but "a Workshop dashboard for the G4 NCOIC that shows current equipment readiness by unit, filterable by date and equipment type."

**A named consumer.** Someone specific will use this. Name them by role or by name. "The formation" is not a consumer.

**Accessible data.** Before Day 1, you have confirmed access to every dataset the project needs. Bootcamp time is not spent waiting on permissions.

**TM-20/30 scope.** The work does not require writing Python, TypeScript, or OSDK integrations. If it does, you need TM-40 specialist training, not FBC.

**5-day feasibility.** A functional prototype can be built in five days. Not a complete production system — a functional prototype that demonstrates the solution and can be refined post-bootcamp.

### 3-2. Project Brief

Submit the Project Brief (Appendix A) to C2DAO through your Unit Training NCO/Officer at least 14 calendar days before bootcamp Day 1. The brief captures:

- Problem statement (2–5 sentences)
- Output type (Workshop app / pipeline / Ontology type / Contour view / Quiver product)
- Named end user
- Data sources (confirm access)
- Scope statement (what will be done in 5 days; what is out of scope)
- Supervisor signature

C2DAO reviews and returns approval or feedback within 5 duty days.

### 3-3. Scope Examples

| Project | Status | Reason |
|---|---|---|
| Workshop readiness dashboard for G4 NCOIC from existing equipment Object Type | VALID | Clear output, named user, in-scope tools |
| Python model to forecast maintenance demand | OUT OF SCOPE | Requires code — enroll in TM-40G or TM-40H |
| "Improve the data pipeline" | NOT VALID | No specific output, no named user |
| Contour geospatial view of logistics nodes for S4, filtered by unit and date | VALID | Clear output, named user, TM-20/30 scope |
| Full ontology redesign for the brigade | OUT OF SCOPE | Too large; requires C2DAO Change Review before work begins |
| Quiver personnel tracker replacing a manual SharePoint tracker | VALID | Clear output, named user, in-scope tools |

---

## 4. SPRINT WEEK STRUCTURE

### 4-1. Schedule

| Day | Activity |
|---|---|
| **Day 1** | In-brief (0800–0900): scope review, environment check, kickoff. Build (0900–1700). |
| **Days 2–4** | Daily standup (0800, 15 min). Build (0815–1700). SME available throughout. |
| **Day 5** | Product demo / peer review (0800–1000). Evaluator Go/No-Go (1000–1200). Out-brief and documentation handoff (1300–1500). |

### 4-2. Daily Standup

15 minutes, each build day. Three questions per participant:
1. What did I build yesterday?
2. What am I building today?
3. Do I have a blocker?

Keep answers to 60 seconds. Blockers surface immediately so SME support is targeted.

### 4-3. SME Support

One SME per ≤8 participants. The SME consults — they do not teach and do not build any part of your product.

**SME assists with:**
- Specific platform questions when you're stuck
- Governance decisions (naming, branching, data steward coordination)
- Scope management when an approach is too complex

**SME will not:**
- Teach platform skills from scratch (that's TM-30)
- Build any part of your product
- Override your validated scope

If your project turns out to require code-level work, the SME will document this and recommend the appropriate TM-40 track.

---

## 5. GO STANDARD

You receive a Go when:

| Standard | Criterion |
|---|---|
| Functional product | The product does what your Project Brief says it will do — your named consumer can use it |
| Documentation | Naming conventions followed; product description explains its purpose and data sources |
| Handoff package | Complete by end of Day 5 — see Appendix B |
| Governance | Product is in a branch; promotion plan documented or production promotion initiated |

An 80% complete but functional and documented product passes. A polished but non-functional product does not.

---

## 6. HANDOFF PACKAGE

The handoff package is required. It is how the bootcamp product becomes a lasting asset.

Required contents:
1. **Product description** — What it is, what problem it solves, who uses it
2. **Data sources** — What datasets or Object Types feed the product; where they live
3. **Known limitations** — What the product does not do; what would break it
4. **Maintenance guidance** — What changes over time and how to handle it
5. **Promotion status** — Training environment, dev, or production? What is required to promote?
6. **Point of contact** — Who owns this going forward?

Format: Markdown document committed to the Foundry project description or your unit's documentation space. The template is in Appendix B.

---

## 7. GOVERNANCE STANDARDS

Bootcamp products are subject to the same governance standards as any other Foundry product.

| Standard | Reference |
|---|---|
| Dataset and project naming | NAMING_AND_GOVERNANCE_STANDARDS.md |
| Branching and promotion workflow | TM-30, Chapter 6 |
| C2DAO coordination for production | CDA_CONSTRAINTS_AND_DIRECTIVES.md |
| Classification handling | TM-10, Chapter 7 |

If you have not read TM-30's governance chapter, read it before Day 1. The SME will walk through governance basics at the Day 1 in-brief, but you are expected to arrive knowing the conventions.

---

## 8. PRE-SPRINT CHECKLIST

Complete **at least 5 duty days before Day 1:**

- [ ] Project Brief submitted and C2DAO approval received
- [ ] TM-20 Go record submitted with enrollment request
- [ ] Bootcamp workspace access provisioned and confirmed (log in and verify environment loads)
- [ ] Data access confirmed: every dataset the project needs is accessible in your environment
- [ ] Handoff package template downloaded (Appendix B) and participant sections pre-filled
- [ ] Naming and governance conventions reviewed (NAMING_AND_GOVERNANCE_STANDARDS.md)

If any item is not complete 5 days before Day 1, contact C2DAO. Late access issues burn bootcamp time and affect other participants.

---

## APPENDIX A — PROJECT BRIEF TEMPLATE

```
FOUNDRY BOOTCAMP — PROJECT BRIEF
Submitted by: [Name, Rank, Unit, MOS, DSN, Email]
Bootcamp iteration: [Quarter/Year, e.g., Q2 FY26]
Supervisor: [Name, Rank, Signature block]

PROBLEM STATEMENT (2–5 sentences):
[What is the problem? Who has it? What would solving it look like?]

OUTPUT (select one and describe):
[ ] Workshop application — describe:
[ ] Pipeline / dataset transformation — describe:
[ ] Ontology type(s) — describe:
[ ] Contour view — describe:
[ ] Quiver product — describe:

NAMED CONSUMER:
[Name or role of the person who will use this product]

DATA SOURCES:
[List each dataset or Object Type; confirm access status: CONFIRMED / PENDING]

SCOPE STATEMENT:
In scope (what will be done in 5 days):

Out of scope (explicitly excluded):

SUPERVISOR SIGNATURE:
[Signature / Date]
```

---

## APPENDIX B — HANDOFF PACKAGE TEMPLATE

```
FOUNDRY BOOTCAMP — HANDOFF PACKAGE
Builder: [Name, Rank, Unit]
Bootcamp: [Quarter/Year]
Product name: [Foundry project/resource name, following naming standards]

1. PRODUCT DESCRIPTION
[What it is; what problem it solves; who uses it]

2. DATA SOURCES
[Dataset/Object Type name | Location in Foundry | Refresh cadence]

3. KNOWN LIMITATIONS
[What the product does not do; what would break it]

4. MAINTENANCE GUIDANCE
[What changes over time; who handles it; how]

5. PROMOTION STATUS
[ ] Training environment only
[ ] Dev branch (pending review)
[ ] Production (promotion complete — date: ___)
[ ] Production promotion planned — next steps: ___

6. POINT OF CONTACT
[Name, Role, Unit, Contact info — who owns this product going forward]
```

---

*USAREUR-AF Operational Data Team*
*Foundry Bootcamp (FBC) Participant Guide | Version 1.0 | March 2026*
