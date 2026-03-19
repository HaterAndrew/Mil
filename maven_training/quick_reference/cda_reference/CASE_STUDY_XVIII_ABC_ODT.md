<!-- MAVEN TRAINING CORPUS — CDA REFERENCE MATERIAL
     Source: Forney, Herrmann, and Steele, "Fighting with Live Data," Military Review (Feb 2026)
     Supports: all TM tracks, especially TM-40J (Program Manager), TM-40F (Mission Command), TM-40L (Software Engineer)
     Type: Case Study
-->
---
sidebar_position: 3
title: "Case Study: XVIII Airborne Corps Operational Data Teams"
description: How XVIII ABC built, organized, and employed ODTs to solve operational problems — prototype to program of record in nine months
layer: organization
category: case-study
---

# CS-001: XVIII Airborne Corps — Fighting with Live Data

*ODT Case Study Series — CS-001*

XVIII Airborne Corps was one of the first Army formations to experiment with the Operational Data Team (ODT) concept, beginning in 2022. Over two years, the Corps iterated through three organizational models before arriving at their current structure: multifunctional ODTs assigned to the Corps G-5. This case study documents their journey — what worked, what didn't, and the lessons they chose to publish. It is a valuable reference point from one corps' pilot, not a prescriptive template. Each command's operational context, manning, and mission set will drive different organizational choices. USAREUR-AF's ODT predates the XVIII ABC publication and operates at theater army echelon with distinct requirements.

| Field | Value |
|-------|-------|
| Series | CS-001 |
| Source | Forney, Herrmann, and Steele, "Fighting with Live Data," *Military Review* Online Exclusive, February 2026 |
| Relevance | Critical — most directly applicable pilot experience with the ODT concept |
| Doctrine Ref | Decision Optimization CONOPS, Appendix B (MCCoE); ADP 5-0; ADP 6-0 |

## Bottom Line Up Front

XVIII ABC's experience offers three key findings from their specific context: (1) combining software development and data science into multifunctional teams outperformed separating them; (2) aligning their ODTs to the G-5 (long-range planning) improved operational focus compared to standalone innovation offices or distribution across staff sections; (3) a CG-signed governance process was essential to prevent overextension. Their ODT delivered a BDA visualization prototype in three months, an MVP in six, and a full handoff to an Army program of record in nine. These are data points from a Corps-level pilot — not universal prescriptions. Different echelons, mission sets, and manning realities may drive different organizational solutions. The value is in the lessons, not in copying the org chart.

## 01 — The Organizational Journey

XVIII ABC iterated through three organizational models over two years. Each model taught a lesson that directly informs how USAREUR-AF structures its own ODT.

### Phase 1: Data Warfare Company (Jun 2022 – Dec 2023)

- Separate company with own UIC, reporting to Corps Chief Innovation Officer
- Staffed with JSOC Global Analytics Platform graduates and Galvanize-trained contractors
- **Problem:** Company admin overhead taxed a two-person HQ. Elimination of the Chief Innovation Officer billet removed advocacy at the command level. No organic data science — ORSA analysts were assigned elsewhere.
- **Lesson:** A standalone innovation company detached from the staff cannot sustain itself or align to operational priorities.

### Phase 2: Distributed Across Staff Sections (Jan 2024 – Jul 2024)

- Software developers placed in Knowledge Management Office
- Data scientists split between G-5 and G-35 (future operations)
- Cloud engineers and cybersecurity specialists moved to G-6
- ASWF and AI2C graduates arrived during this phase
- **Problem:** Interaction was limited and stove-piped within areas of assignment. Applications did not maximize combined software development and data science expertise.
- **Lesson:** Coordination across competing priorities and staff interests is not enough. Proximity without integration yields diminished returns.

### Phase 3: Unified ODTs in G-5 (Aug 2024 – Present)

- Software developers and data scientists consolidated into multifunctional ODTs under Corps G-5
- G-6 retained cloud platform engineers and cybersecurity specialists
- Development efforts aligned to CAMPLAN and formally designated operational problems
- **Result:** Applications developed coherently with lasting impact. ODTs can dynamically task-organize to requirements. "Deliberate" development meets enduring operational problems; "dynamic" development meets contingency response requirements.

> **XVIII ABC's KEY FINDING:** In their experience, combining software development and AI/ML capabilities into multifunctional teams that dynamically task-organize produced the best results. G-5 alignment worked for a Corps headquarters — other echelons and commands may find different alignment points (e.g., USAREUR-AF's C2DAO model). The underlying principle — that ODTs must be connected to operational planning, not siloed in innovation offices — is the transferable lesson.

## 02 — ODT Manning Structure

XVIII ABC's recommended ODT structure maps directly to the MSS specialist training tracks:

| ODT Role | ASI | XVIII ABC Billet | MSS Training Track |
|---|---|---|---|
| Product Manager | 5F | 1x per ODT | TM-40J (Program Manager) |
| UI/UX Designer | 5G | 1x per ODT | TM-40N (UX Designer) |
| Software Engineer | 5J | 1x per ODT | TM-40L (Software Engineer) |
| Data Engineer | D3/2V | 1x per ODT | TM-30 (Advanced Builder) / TM-40K (KM) |
| Data Scientist | 49A/D4 | 1x per ODT | TM-40G (ORSA) / TM-40M (ML Engineer) |

The Operational Data Section (ODS) runs three ODTs (Blue, White, Red) under an ODS Chief (49B/28A) and Deputy Chief, supported by Infrastructure Support Elements (G-6: Authorizing Official, Platform Engineers, RMF Team, Network Engineer) and Corps Staff ODT Enablers (Knowledge Managers, Data Analysts).

> **USAREUR-AF CONTEXT:** The MSS training curriculum produces the skill sets XVIII ABC identifies as core ODT roles. TM-40J through TM-40O cover the same disciplines. USAREUR-AF's ODT predates the XVIII ABC publication and has its own organizational structure under C2DAO — the skill overlap validates the training pipeline, not the org chart.

## 03 — Problem-Solution Development Process

XVIII ABC ODTs use a rigorous problem-solution methodology informed by ASWF best practices:

| Phase | Duration | Activity |
|---|---|---|
| Scoping | 2 weeks | Understand the operational problem, identify stakeholders, assess feasibility |
| Discovery | 4 weeks | Deep problem validation, stakeholder research |
| Framing | 4 weeks | Frame potential solutions, define MVP scope |
| Development | 8 weeks | Build MVP through iterative sprints |
| Handoff | 2 weeks | Deliberate transition to sustainment or program of record |

**Total time to MVP: at least 5 months.** Decision points at each gate: invest, divest, or pivot.

Key principles:
- Staff elements articulate a **problem**, not a desired solution
- ODT recommends prioritization; the CG approves the "cut line"
- Development cycles (~12 weeks) align within the Corps exercise cycle — each Program Increment culminates with a Corps exercise
- During exercises: MVP products receive bug fixes and minor adjustments; scoping-phase products get user research only; discovery/framing-phase products are held stable

> **USAREUR-AF CONTEXT:** This process directly maps to the DDOF Playbook v2.2 six-phase lifecycle and the Agile PM methodology taught in TM-40J. The 12-week PI cycle is analogous to the USAREUR-AF quarterly training cycle.

## 04 — Governance: Technical Innovation Objectives (TIO)

XVIII ABC's governance process prevents the ODT overextension that plagued their early efforts:

1. **G-5 and ODT host working groups** with Corps staff to develop potential TIOs aligned to CAMPLAN operational problems
2. **ODT + G-5 + Chief Technology Officer** review draft TIOs for operational value and development feasibility
3. **Proposed prioritization** submitted to Corps Deputy CG for validation
4. **CG approves** the PI plan and retains authority to retask dynamically
5. **Results from exercises/experiments** feed the next prioritization cycle

> **LESSON LEARNED:** Without a CG-signed governance policy, too many customers requested ODT resources simultaneously. No adjudication process meant overextension on unrealistic timelines. The governance policy is not optional — it is a prerequisite.

## 05 — BDA Visualization: Prototype to Program of Record

The BDA visualization capability demonstrates the operational tempo an ODT can achieve:

| Milestone | Timeline | Detail |
|---|---|---|
| Commander requirement | D+0 | Visualize attrition of enemy integrated fires complex in real-time |
| Prototype | D+90 (3 months) | Working prototype integrating targeting data with intelligence reporting |
| MVP | D+180 (6 months) | Full MVP: spatial impact visualization, analyst-tailorable charts, historical BDA record |
| POR handoff | D+270 (9 months) | Handed to Army Intelligence Data Platform (INSCOM) as enterprise capability |
| Adoption | Ongoing | Used in 4 exercises (XVIII ABC, 101st, 82nd); adoption by USAREUR-AF, III Corps |

**Operational impact:** Commanders see spatial impact of strikes on enemy formations — not just numbers destroyed. System ties intelligence reporting to targeting data, enabling longitudinal trend analysis and proactive plan adjustment.

> **USAREUR-AF CONTEXT:** The BDA visualization case study is the archetype for every TM-40 capstone exercise scenario: a commander articulates an operational problem → the ODT scopes, develops, tests, and delivers a data product → the product is validated in exercises and transitioned to sustainment.

## 06 — Echeloned ODT Employment

The Mission Command Center of Excellence (MCCoE) developed an echeloned ODT concept with XVIII ABC as lead:

- **Theater Army ODS (ASCC/CFLCC):** Highest echelon, coordinates with joint, allied, and industry data sources
- **Corps ODS (CJTF, USFOR):** Operational-level ODTs aligned to Corps CAMPLAN
- **Division ODT:** Tactical-level capability, shares tools via repository with higher echelons
- SEC ARMY directed experimentation with this concept during Transformation in Contact (TiC)

> **USAREUR-AF CONTEXT:** USAREUR-AF operates at the Theater Army ODS echelon. The MSS training curriculum is building the workforce to staff ODTs at every echelon in the USAREUR-AF formation — from theater army through subordinate Corps and Division.

## 07 — Key Lessons for USAREUR-AF

| XVIII ABC Lesson | USAREUR-AF Application |
|---|---|
| Combine software dev + data science into unified teams | MSS specialist tracks (TM-40G–O) are designed as complementary skills within a single team structure |
| Align ODTs to G-5 / long-range planning | USAREUR-AF ODT operates under C2DAO with direct alignment to theater strategy |
| CG-signed governance policy is essential | C2DAO/UDRA v1.1 provides the USAREUR-AF equivalent — governance authority for all MSS capability builds |
| Educate CG and staff on agile process | TM-10 (all personnel) and Data Literacy for Senior Leaders address this requirement directly |
| Integrate ODT efforts with exercise cycles | MSS training calendar and capstone exercises are synchronized with DEFENDER-series and theater exercises |
| Contractors supplement military personnel | USAREUR-AF augments military ODT with Galvanize/ASWF-trained contractor support |
| Document challenges for higher HQ support | USAREUR-AF experience informs the broader ODT pilot alongside XVIII ABC |

## 08 — Supplementary Context: Adkins' Decision Optimization Proposal

Adkins ("Achieving Decision Dominance," *Military Review*, January-February 2025) is a thought piece by a junior captain proposing terminology and organizational concepts for decision optimization at echelon. Several of his terms — operationalized data, AFP, DOT — have entered common usage and provide useful shorthand. The XVIII ABC article documents the most relevant pilot experience; Adkins offers supplementary context, not a theoretical foundation.

**Adkins terminology relevant to the XVIII ABC experience:**

| Adkins Concept | XVIII ABC Experience | MSS Training Application |
|---|---|---|
| **Operationalized data** — data analyzed and presented to be immediately actionable (Adkins' term) | BDA visualization: commanders see spatial impact of strikes, not raw numbers | Every TM-40 capstone produces an operationalized data product |
| **Automated Fighting Products (AFP)** — visualization tools connected to live data via automated pipelines (Adkins' term) | XVIII ABC ODTs build AFPs aligned to CAMPLAN operational problems | MSS Workshop applications are AFPs; TM-20/30 builders create them |
| **Decision Optimization Team (DOT)** — proposed formal echeloned team for data engineering, data science, decision science | XVIII ABC's ODT is a Corps-level implementation of this concept | MSS specialist tracks (TM-40G–O) produce DOT/ODT personnel |
| **Echeloned employment** — DOT from Division through HQDA | MCCoE codified: TA ODS → Corps ODS → DIV ODT | USAREUR-AF operates at Theater Army ODS echelon |
| **FA 26B + FA 49 + FA 57 workforce** | XVIII ABC combined these into unified ODTs | TM-40O (Platform Engineer), TM-40G (ORSA), TM-40K (KM) map to these FAs |
| **Gunnery table training model** | XVIII ABC demonstrated through exercise-integrated development | MSS Go/No-Go certification uses TCS framework (ADP 7-0 aligned) |
| **Cost of inaction** — asynchronous innovation, unrealistic expectations on tactical units | XVIII ABC's early DWC failure demonstrated exactly this | White Paper "Risk of Inaction" section echoes Adkins |

> **NOTE:** Adkins names the Maven Smart System as the ASCC-level COP platform — a useful data point, though the article is one officer's proposal, not doctrine.

Adkins proposes a 4-phase, 5-year implementation: (1) Reorganize/pilot with XVIII ABC, (2) Revise training and doctrine, (3) Expand DOTs at echelon, (4) Validate through exercises. The MSS training program and USAREUR-AF's ODT are executing phases 1–3 concurrently.

## References

- Forney, Andrew J., Ryan C. Herrmann, and Haley A. Steele. "Fighting with Live Data: XVIII Airborne Corps' Experience with Its Operational Data Teams." *Military Review* Online Exclusive, February 2026.
- Adkins, Alexander K. "Achieving Decision Dominance: The Arduous Pursuit of Operationalized Data." *Military Review* 105, no. 1 (January-February 2025): 88.
- U.S. Army Mission Command Center of Excellence. "Appendix B: ODT Concept and General Structure." In *Decision Optimization Concept of Operations*.
- Rainey, James E. "Continuous Transformation: Transformation in Contact." *Military Review* Online Exclusive, 9 August 2024.
- Cowden, Joshua. "New Data Warfare Company Activates as Beacon of Innovation for XVIII Airborne Corps." U.S. Army, 9 June 2022.
- MCCoE, *Decision Optimization* (Fort Leavenworth, KS, 3 April 2024).
- MCCoE, *Decision-Driven Data Concept of Operations* (white paper, Fort Leavenworth, KS, 6 July 2023).
- ASA(ALT), *Unified Data Reference Architecture* (Washington, DC, 22 March 2024).

---

*HQ USAREUR-AF · v1.0 · 2026 · DISTRIB: USG only · AUTH: C2DAO*
