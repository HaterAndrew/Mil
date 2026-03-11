# TM-40D — MAVEN SMART SYSTEM (MSS)
## PROGRAM MANAGER TECHNICAL MANUAL

**HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA**
Wiesbaden, Germany

2026

**PREREQUISITE PUBLICATIONS:** TM-10, Maven User; TM-20, Builder; TM-30, Advanced Builder; ADRP 1, Data Literacy (required)

**DISTRIBUTION RESTRICTION:** Approved for public release; distribution is unlimited.

---

## SAFETY SUMMARY

Program managers operating at TM-40D level build and maintain tracking infrastructure that senior leaders depend on for operational decisions. Errors in PM systems — incorrect milestone dates, wrong funding figures, missed risk escalations — affect resource allocation, commander assessments, and operational outcomes.

Before performing any task at TM-40D level:

- Validate all data inputs at ingestion boundaries. PM systems often aggregate data from multiple source systems (GCSS-Army, GFEBS, IPPS-A, manual submissions). Each boundary is a potential corruption point.
- Never publish a dashboard to production without a documented data lineage path from source to display. Senior leaders must be able to trace any displayed figure to an authoritative source.
- Coordinate with the USAREUR-AF C2DAO before creating new Object Types that intersect with shared enterprise ontology domains (Personnel, Equipment, Finance).
- Automated reporting pipelines that generate SITREP, LOGREP, or PERSTAT data products require C2DAO review before scheduling in production. These pipelines feed command reporting chains.
- Access control on PM systems must be explicitly configured. Budget figures, risk registers, and personnel data are sensitive — default-open permissions are not acceptable.
- Changes to production reporting pipelines require a 24-hour notification to downstream consumers before implementation.

> **WARNING: PM systems at TM-40D level directly support command reporting chains. An error in an automated SITREP pipeline or a corrupted funding dashboard can result in a commander briefing incorrect data to USAREUR-AF or USEUCOM leadership. Apply the same rigor to data system changes that a unit applies to a FRAGO — confirm, coordinate, and communicate before executing.**

---

## TABLE OF CONTENTS

- Chapter 1 — Introduction: The PM Track
- Chapter 2 — PM System Architecture
- Chapter 3 — Status and Milestone Tracking
- Chapter 4 — Resource and Budget Tracking
- Chapter 5 — Risk Register Design
- Chapter 6 — Reporting Pipelines
- Chapter 7 — Senior Leader Dashboards
- Chapter 8 — Portfolio Analysis
- Chapter 9 — PM System Governance
- Appendix A — PM System Design Checklist
- Appendix B — Army Reporting Requirements Cross-Reference
- Appendix C — Dashboard Design Standards for Senior Leaders
- Glossary

---

## CHAPTER 1 — INTRODUCTION: THE PM TRACK

### 1-1. Purpose and Scope

**BLUF:** TM-40D qualifies program managers, project managers, resource managers, and S-shop staff managers to design, build, and sustain program management tracking systems on the Maven Smart System (MSS). This track is the MSS authority for PM-domain system design.

This manual provides task-level instruction for building PM tracking infrastructure on MSS. It covers the full lifecycle of a PM system: design, build, operation, reporting, and governance. TM-40D graduates design and operate the tracking systems their programs depend on — from milestone boards to risk registers to automated SITREP pipelines to senior leader dashboards.

**TM-40D covers:**
- Designing PM tracking Object Type models for programs, milestones, tasks, risks, resources, and personnel
- Building milestone and schedule tracking systems with date-based logic and schedule risk indicators
- Designing risk registers with likelihood/impact scoring and automated escalation
- Building resource and budget tracking systems (funding, obligation, equipment, personnel)
- Building automated reporting pipelines that generate SITREP, LOGREP, and PERSTAT data products on schedule
- Designing senior leader dashboards for commander consumption in briefings
- Conducting portfolio analysis across multiple programs using Contour
- Governing PM systems: access control, audit trails, data stewardship, and sustainment planning

**TM-40D does NOT cover:**
- Raw coding of custom transforms, API integrations, or Functions on Objects — see TM-40B (Software Engineer) for those requirements
- Machine learning model development — see TM-40C (ML Engineer)
- AI workflow automation and Agent Studio — see TM-40A (AI Engineer)
- Advanced statistical analysis and modeling — see TM-40D (ORSA)

> **NOTE:** TM-40D is a no-code/low-code track. PM-series personnel may write light Python or SQL in reporting pipelines (Chapter 6), but the primary toolset is Foundry Workshop, Pipeline Builder, Contour, and Ontology design. Personnel without any Python background can complete this manual. Personnel who do write Python should consult TM-40B for code standards.

---

### 1-2. The PM Role in the MSS Ecosystem

Program managers in USAREUR-AF operate at the intersection of mission execution and resource management. A PM supporting a theater modernization program tracks dozens of milestones, hundreds of line items, cross-functional dependencies, risk factors, contract actions, and personnel assignments — simultaneously, across multiple phases of execution. The volume and velocity of tracking data exceeds what SharePoint spreadsheets, email threads, or manual tracking boards can handle at USAREUR-AF scale.

MSS provides the PM with a purpose-built tracking environment: structured Object Types that enforce data consistency, Action-based update workflows that route updates through defined chains, automated pipelines that generate required reports on schedule, and dashboards that give commanders real-time program status without requiring a briefer to manually compile slides.

**The PM's role in the MSS data chain:**

```
PROGRAM EXECUTION
        |
        v
   DATA INGESTION             <- Source system feeds + manual Action inputs
   (GCSS-Army, GFEBS,
    IPPS-A, manual)
        |
        v
   PM TRACKING SYSTEM         <- TM-40D operates here
   (Object Types, Actions,
    Pipelines, Governance)
        |
        v
   REPORTING PRODUCTS         <- Automated SITREP, LOGREP, PERSTAT
   (Scheduled transforms,
    Workshop dashboards)
        |
        v
   SENIOR LEADER CONSUMPTION  <- Commander dashboards, briefing products
   (-10 users at command level)
```

The PM is both a system designer and a data steward. You design the tracking infrastructure, ensure data quality through the full pipeline, govern access and audit trails, and sustain the system as the program evolves. This is a higher governance obligation than the TM-30 advanced builder role — PM systems are operational infrastructure, not analytical experiments.

---

### 1-3. PM Responsibilities in System Design

TM-40D graduates accept system design responsibilities that extend beyond tool operation. Before building any PM tracking system on MSS, you are responsible for:

1. **Defining the data model.** What are the entities in your program? What are the relationships? What properties does each entity carry? Chapter 2 provides the methodology.
2. **Establishing data ownership.** For every data element in your system, identify who is authoritative. A milestone date entered by a contractor's PM and the same date entered by the G4 cannot coexist without a defined authority hierarchy.
3. **Designing update workflows.** How do data inputs flow into the system? Manual Action forms, scheduled ingestion from source systems, or both? Every update path must be documented and enforced.
4. **Governing access.** Who can view what? Who can edit what? PM systems often contain sensitive budget data, personnel information, and risk assessments that require role-based access control.
5. **Sustaining the system.** Programs change. Milestones get added. Risks materialize. Funding lines shift. The PM system must be designed for change — with a documented process for adding, modifying, and retiring Object Types and properties.

> **NOTE:** Consult `learn-data.armydev.com` for the Object Type Cookbook v2 and DDOF Playbook before beginning any new PM system design. These reference materials provide canonical patterns for program management Object Types used across the Army data ecosystem.

---

### 1-4. Governing References

| Document | Relevance |
|---|---|
| Army CIO Data Stewardship Policy (April 2, 2024) | Data stewardship hierarchy, governance chain, PM data product standards |
| UDRA v1.1 (February 2025) | Unified Data Reference Architecture — domain ownership, federated governance |
| DoD Data Strategy (2020) | VAUTI framework — Visible, Accessible, Understandable, Trustable, Interoperable |
| USAREUR-AF C2DAO Guidance | Theater-level architecture standards for MSS data products |
| AR 11-2 | Managers' Internal Control Program — relevant for audit trail requirements |
| AR 70-1 | Army Acquisition Policy — milestone authority definitions for ACAT programs |
| DA PAM 30-22 | Operations Management of the Army Food Program (LOGSTAT context) |
| ADP 4-0 | Sustainment — LOGREP and LOGSTAT doctrinal context |
| FM 6-0 | Commander and Staff Organization — SITREP doctrinal context, MDMP integration |
| EUCOM EXORD | Theater-specific reporting requirements applicable to USAREUR-AF programs |

> **NOTE:** All PM data products published on MSS must trace to an authoritative Army or DoD policy source. "We have always tracked it this way" is not sufficient justification for a new Object Type or data field in a shared production system.

---

### 1-5. Prerequisites and Access Requirements

Before performing TM-40D level work on MSS, confirm the following:

**Knowledge prerequisites:**
- [ ] TM-10 (Maven User) completed
- [ ] TM-20 (Builder) completed
- [ ] TM-30 (Advanced Builder) completed — fluency confirmed by team lead or chain of command
- [ ] ADRP 1, Data Literacy completed (required at TM-40 level)
- [ ] Familiarity with your program's reporting requirements (SITREP, LOGREP, PERSTAT, USR as applicable)

**Access requirements:**
- [ ] PM Builder role requested and approved through chain of command
- [ ] Editor or Owner role on your program's designated MSS project folder
- [ ] Read access to relevant source system datasets (GCSS-Army feed, GFEBS feed, IPPS-A feed, as applicable) coordinated with data stewards
- [ ] C2DAO coordination completed if new shared Object Types are required

**System design prerequisites:**
- [ ] Program charter or equivalent defining program scope, milestones, and reporting requirements
- [ ] Identification of all data consumers (who will use the dashboards and reports)
- [ ] Identification of all data producers (who will enter and update data)
- [ ] Governing reporting schedule (daily, weekly, monthly, event-driven)

---

## CHAPTER 2 — PM SYSTEM ARCHITECTURE

### 2-1. Overview

**BLUF:** PM system architecture on MSS is an Ontology design problem. Get the Object Type model right before building anything else. A well-designed data model makes every downstream task — dashboards, reports, risk registers, portfolio analysis — faster and more reliable. A poorly designed model creates technical debt that compounds as the program evolves.

This chapter provides a methodology for designing the complete Object Type model for a PM tracking system. Apply this methodology before touching Foundry tools. The output of this chapter is a documented design specification you can implement in Chapter 3 through 8 and hand to a -40 developer for any technical implementation beyond your capability.

---

### 2-2. Core PM Object Type Model

Every USAREUR-AF PM system on MSS begins with a standard set of Object Types. This canonical model is validated against Army doctrine, EUCOM program management requirements, and UDRA v1.1. Do not deviate from this model without C2DAO coordination.

**Standard PM Object Type Set:**

| Object Type | Primary Key | Purpose |
|---|---|---|
| Program | Program ID | Top-level program entity — the anchor for all other objects |
| Milestone | Milestone ID | Key events with date, authority, and completion status |
| Task | Task ID | Work packages nested under milestones |
| Risk | Risk ID | Documented risks with scoring, status, and mitigation |
| Issue | Issue ID | Materialized risks and blockers requiring active management |
| Action Item | Action ID | Assigned actions with owner, due date, and status |
| Resource Line | Resource ID | Funding lines, equipment allocations, personnel billets |
| Contract | Contract ID | Contract actions linked to program funding |
| Personnel | Personnel ID | Key personnel assignments linked to tasks and roles |
| Organization | Org ID | Units and organizations involved in the program |

**Mandatory Link Types:**

| Link Type | From Object | To Object | Cardinality |
|---|---|---|---|
| hasParentProgram | Milestone | Program | Many-to-One |
| hasParentMilestone | Task | Milestone | Many-to-One |
| hasDependency | Milestone | Milestone | Many-to-Many |
| isLinkedToRisk | Milestone | Risk | Many-to-Many |
| isLinkedToRisk | Task | Risk | Many-to-Many |
| hasResourceLine | Program | Resource Line | One-to-Many |
| hasContract | Resource Line | Contract | One-to-Many |
| isAssignedTo | Task | Personnel | Many-to-One |
| isOwnedBy | Risk | Personnel | Many-to-One |
| belongsTo | Personnel | Organization | Many-to-One |

> **NOTE:** This model is the minimum. Your program may require additional Object Types (e.g., Deliverable, Dependency, Change Request). Add Object Types at the margin — extending a well-designed core model is significantly less costly than refactoring a poorly designed one.

---

### 2-3. Object Type Property Design

Each Object Type requires a defined property set. Properties fall into three categories: identifier properties (unique keys), status properties (current state), and reference properties (links to doctrine, contracts, or external systems).

**Program Object Type — Required Properties:**

| Property | Type | Description | Required |
|---|---|---|---|
| Program ID | String | Unique identifier (follow Army program numbering convention) | Yes |
| Program Name | String | Official program name (match EUCOM/HQDA documentation) | Yes |
| Program Phase | String (enum) | Concept / Development / Production / Sustainment / Closeout | Yes |
| Program Manager | String | Name or EDIPI of designated PM | Yes |
| Sponsor Organization | String | Funding sponsor unit/command | Yes |
| Start Date | Date | Approved program start | Yes |
| End Date | Date | Approved program end / completion | Yes |
| Program Status | String (enum) | On Track / At Risk / Off Track / Paused / Complete | Yes |
| Overall Health Score | Integer | Composite score (0–100) from milestone + risk + resource health | Computed |
| Last Updated | Timestamp | Auto-populated on any edit | Yes |
| ACAT Level | String | ACAT I / ACAT II / ACAT III / Below ACAT (acquisition programs) | Conditional |
| Classification | String (enum) | UNCLASSIFIED / CUI / FOUO | Yes |

**Milestone Object Type — Required Properties:**

| Property | Type | Description | Required |
|---|---|---|---|
| Milestone ID | String | Unique identifier | Yes |
| Milestone Name | String | Official milestone title | Yes |
| Milestone Type | String (enum) | Planning / Decision / Delivery / Review / Reporting | Yes |
| Scheduled Date | Date | Approved baseline date | Yes |
| Forecast Date | Date | Current projected completion date | Yes |
| Actual Date | Date | Actual completion date (null if incomplete) | Conditional |
| Status | String (enum) | Not Started / In Progress / Complete / Delayed / Cancelled | Yes |
| Schedule Variance | Integer | Forecast Date minus Scheduled Date (days, computed) | Computed |
| Responsible Owner | String | Name or EDIPI of milestone owner | Yes |
| Authority | String | Who approves milestone completion | Yes |
| Completion Criteria | String | Documnted criteria for declaring completion | Yes |
| Notes | String | Free text for status comments | No |

> **CAUTION: Never define Scheduled Date as editable after program baseline is approved. Schedule Variance is only meaningful if Scheduled Date is locked. Use a separate Rebaseline Date property and a corresponding Action with approval workflow if the baseline must change. Allowing direct edits to Scheduled Date destroys schedule integrity.**

**Task Object Type — Required Properties:**

| Property | Type | Description | Required |
|---|---|---|---|
| Task ID | String | Unique identifier | Yes |
| Task Name | String | Descriptive task title | Yes |
| Task Type | String (enum) | Action / Analysis / Coordination / Procurement / Training | Yes |
| Assigned To | String | Personnel or organization responsible | Yes |
| Start Date | Date | Planned start | Yes |
| Due Date | Date | Planned completion | Yes |
| Completion Date | Date | Actual completion (null if incomplete) | Conditional |
| Percent Complete | Integer | 0–100, updated by action workflow | Yes |
| Status | String (enum) | Not Started / In Progress / Complete / Blocked / Cancelled | Yes |
| Blocking Factor | String | Description of block if Status = Blocked | Conditional |
| Priority | String (enum) | High / Medium / Low | Yes |

---

### 2-4. Designing for Army Reporting Requirements

PM tracking systems must be designed from the start to support required Army reporting outputs. Each reporting requirement maps to specific Object Type properties and pipeline logic. Design the data model to support reporting outputs — do not retrofit reporting onto a completed Object Type model.

**Reporting Requirements to Object Type Property Mapping:**

| Report | Primary Object Type | Required Properties | Output Format |
|---|---|---|---|
| SITREP (Weekly) | Program, Milestone, Risk | Status, Schedule Variance, Risk Score | Tabular summary per program |
| LOGREP / LOGSTAT | Resource Line, Contract | Obligation Rate, Delivery Status | Equipment/supply status |
| PERSTAT | Personnel | Assignment Status, Duty Position, Present/Absent | Personnel count by category |
| USR (Unit Status Report) | Program, Resource Line | Readiness Rating, Equipment Availability | S-category readiness format |
| Risk Register | Risk | Likelihood, Impact, Score, Mitigation Status | Risk matrix table |
| Commander's Update Brief | Program, Milestone, Risk | All status properties | Dashboard / briefing product |

> **NOTE:** Define all properties required for reporting outputs before you begin building Object Types. A property you discover is needed after Object Types are published requires an ontology change request — a coordination step that adds time. Front-load the design work.

---

### 2-5. Phased Build Approach

Build PM systems in phases. Attempting to build the complete system in a single sprint produces an unvalidated system with high error rates.

**Recommended Build Sequence:**

| Phase | Tasks | Duration |
|---|---|---|
| Phase 1: Foundation | Program, Milestone, Task Object Types; basic status dashboard | Week 1–2 |
| Phase 2: Risk and Issues | Risk and Issue Object Types; risk dashboard; escalation actions | Week 2–3 |
| Phase 3: Resources | Resource Line, Contract Object Types; budget dashboard | Week 3–4 |
| Phase 4: Reporting | SITREP pipeline; LOGREP integration; scheduled transforms | Week 4–5 |
| Phase 5: Senior Leader | Commander dashboard; brief-ready products; portfolio view | Week 5–6 |
| Phase 6: Governance | Access control review; audit trail verification; sustainment plan | Week 6 |

Do not proceed to the next phase until the current phase has been validated with at least one actual data consumer. A milestone dashboard that the S3 cannot use is not a working system.

---

### 2-6. Task: Design a PM System Object Type Model

**CONDITIONS:** You have a program charter or equivalent scope document. You have identified the primary data consumers. You have access to the Ontology Manager in MSS at Advanced Builder level or higher.

**STANDARDS:** Complete Object Type model documented, covering all entities in the program scope. All Object Types have defined required and optional properties. All Link Types defined with stated cardinality. Reporting requirements mapped to properties. Design reviewed by program manager and C2DAO coordinator before implementation begins.

**EQUIPMENT:** MSS access (Ontology Manager), `learn-data.armydev.com` (Object Type Cookbook v2), program charter, reporting requirements list.

**PROCEDURE:**

1. Read the program charter and identify all trackable entities. Create a list.
2. Map each entity to a Core PM Object Type (para 2-2). Note any entities that do not map to a standard type — these are candidates for custom Object Types.
3. For each Object Type, list all properties required for reporting (use para 2-4 mapping table). Add properties required for operational tracking.
4. Assign each property a data type (String, Integer, Date, Boolean, Enum). Flag all computed properties.
5. Define all Link Types. For each Link Type, specify cardinality (One-to-One, One-to-Many, Many-to-Many).
6. For each computed property, write the formula in plain English. Flag for -40B developer implementation if the logic requires TypeScript Functions on Objects.
7. Map all Object Types to the 5-Layer Data Stack (para 1-4 of TM-30). Confirm Layers 2 and 3 are appropriately separated (pipeline → ontology, not pipeline directly to Workshop).
8. Present design to program manager for validation. Confirm all required reporting fields are captured.
9. Coordinate with C2DAO if any new Object Types will be published to shared enterprise ontology domains.
10. Document the approved design. This document is your build specification for Chapters 3 through 8.

> **NOTE:** A well-documented design specification is the most important output of Chapter 2. Every hour spent on design saves three hours of rework in implementation.

---

## CHAPTER 3 — STATUS AND MILESTONE TRACKING

### 3-1. Overview

**BLUF:** Milestone tracking is the core PM function on MSS. Build a system where milestone status is always current, schedule variance is immediately visible, and delayed milestones automatically surface for commander attention. The system works when a PM can open the dashboard at 0600 and brief the commander by 0700 without any manual data compilation.

---

### 3-2. Date-Based Property Logic

Foundry Ontology supports date and timestamp properties natively. PM systems rely heavily on date arithmetic for schedule variance, days-until-due, and overdue calculations.

**Core date properties every Milestone Object Type must carry:**

| Property | Logic | Usage |
|---|---|---|
| Scheduled Date | Locked at baseline approval | Schedule baseline anchor |
| Forecast Date | Updated via Action workflow | Current projected completion |
| Actual Date | Set by completion Action | Records actual performance |
| Schedule Variance (SV) | Forecast Date − Scheduled Date (days) | Positive = delayed; negative = ahead |
| Days Until Due | Scheduled Date − Today (days) | Time remaining to baseline date |
| Overdue Flag | Boolean: Today > Scheduled Date AND Status ≠ Complete | Triggers alert styling in Workshop |
| At-Risk Flag | Boolean: SV > threshold (default: 14 days) | Triggers amber status |

> **CAUTION: Date arithmetic in Foundry Pipeline Builder uses UTC. If your reporting consumers expect local time (CET/CEST for USAREUR-AF), configure timezone conversion in the transform before computing Schedule Variance. A milestone showing as overdue due to a UTC/CET mismatch will generate unnecessary command attention and erode trust in the system.**

---

### 3-3. Schedule Risk Indicators

Schedule risk indicators provide automated, visual cues on the status of milestones without requiring a PM to manually flag each one. Define thresholds at system design time and enforce them through computed properties and Workshop conditional formatting.

**Standard Schedule Risk Indicator Thresholds:**

| Color Code | Condition | Action Required |
|---|---|---|
| GREEN | SV ≤ 7 days AND no blocking factors | No action |
| AMBER | SV 8–30 days OR blocking factor present | PM action: update forecast, document mitigation |
| RED | SV > 30 days OR Overdue Flag = True | Commander attention: brief in next update cycle |
| BLUE | Status = Complete | Closed |
| GREY | Status = Cancelled OR Status = Not Started (future) | Informational |

Implement color codes as computed string properties on the Milestone Object Type (e.g., `ScheduleRiskColor`). Workshop conditional formatting reads this property to apply cell or card background colors automatically.

> **NOTE:** Define threshold values as configurable properties on a Program Settings object, not as hardcoded values in pipelines or Workshop functions. Different programs have different reporting tolerances. A program with a 90-day reporting cycle will have different amber/red thresholds than one with a 7-day cycle.

---

### 3-4. Action Item Management

Action items are the currency of PM execution. Every review meeting generates action items. A PM system that does not track action items rigorously will revert to email tracking within weeks.

**Action Item Object Type — Extended Properties:**

| Property | Type | Description |
|---|---|---|
| Action ID | String | Unique identifier (auto-generated) |
| Title | String | Short descriptive title |
| Description | String | Full description of required action |
| Source Event | String | Meeting, review, or EXORD that generated the action |
| Assigned To | String (Personnel link) | Person responsible for completion |
| Assigned By | String | Person who assigned the action |
| Priority | Enum: High / Medium / Low | — |
| Due Date | Date | Completion deadline |
| Status | Enum: Open / In Progress / Complete / Overdue | — |
| Completion Date | Date | Actual completion (null if open) |
| Days Overdue | Integer | Computed: Today − Due Date if Status ≠ Complete |
| Escalation Flag | Boolean | Auto-set if Days Overdue > 7 |
| Comments | String | Latest status comment |
| Last Updated | Timestamp | Auto-populated |

**Action Item Update Workflow Design:**

Design a three-step Action workflow for action item updates:
1. **Assignee Update**: Assignee updates Percent Complete, Status, and Comments. System auto-populates Last Updated timestamp.
2. **Completion Confirmation**: When Status is set to Complete, system prompts for Completion Date and brief summary. Notification sent to assigning officer.
3. **Escalation**: When Days Overdue exceeds threshold, system sets Escalation Flag = True. AIP Logic can be configured to generate an escalation notification to the PM.

---

### 3-5. Task: Build the Milestone Tracking Dashboard

**CONDITIONS:** Program Object Type model from Chapter 2 is implemented and populated with at least one program's baseline data. You have Workshop Editor access. At least three milestones are entered with Scheduled Date, Forecast Date, and Status properties populated.

**STANDARDS:** Dashboard displays all milestones for the selected program with color-coded schedule risk indicators. Schedule variance is visible for each milestone. Overdue milestones surface in a dedicated alert section. Dashboard refreshes on page load without manual intervention.

**EQUIPMENT:** MSS Workshop, Program and Milestone Object Types with linked data, Schedule Risk Color computed property configured on Milestone.

**PROCEDURE:**

1. Open Workshop. Create a new application: "Program Status — [Program Name]."
2. Page 1: Program Summary.
   - Add a Program selector widget (Object Set Filter on Program Object Type).
   - Add four KPI tiles: Total Milestones, On Track (GREEN), At Risk (AMBER), Overdue (RED). Use Object Set aggregation with ScheduleRiskColor filter for each count.
   - Add a Timeline widget configured against Scheduled Date and Forecast Date properties. This shows baseline vs. current schedule at a glance.
3. Page 2: Milestone Detail.
   - Add a Table widget showing all Milestone objects linked to the selected Program.
   - Configure columns: Milestone Name, Type, Scheduled Date, Forecast Date, Schedule Variance, Responsible Owner, Status.
   - Apply conditional row formatting: background color = ScheduleRiskColor property.
   - Sort default: Schedule Variance descending (most delayed at top).
4. Page 3: Overdue and At-Risk Alerts.
   - Add filtered Object Set showing only milestones where Overdue Flag = True.
   - Add separate filtered Object Set showing milestones where ScheduleRiskColor = AMBER.
   - Display as cards with: Milestone Name, Days Until Due, Responsible Owner, Last Notes.
5. Page 4: Action Items.
   - Add Table widget on Action Item Object Type, filtered to current program.
   - Columns: Title, Assigned To, Due Date, Days Overdue, Status, Last Updated.
   - Conditional formatting: red row if Days Overdue > 0.
   - Add Quick Update Action button inline: opens Action form for Assignee Update workflow.
6. Configure page-level security: restrict Pages 3 and 4 (alerts and action items) to PM and above. Allow all program stakeholders read access to Pages 1 and 2.
7. Test with real data. Verify color coding fires correctly. Verify Schedule Variance calculations are correct against manual spot check.
8. Publish to program stakeholder group. Brief users on the update workflow (how to enter Actual Dates, how to update Action Items).

> **WARNING: Do not publish the dashboard to production until you have verified that Overdue Flag and ScheduleRiskColor computed properties are producing correct values. An erroneous RED status on a milestone that is actually on track will damage PM system credibility and prompt stakeholders to revert to manual tracking.**

---

### 3-6. Update Workflow Design Principles

The milestone tracking system is only as good as the data feeding it. Design update workflows that minimize friction for data providers while enforcing data quality.

**Workflow Design Principles:**

1. **Single entry point.** Each data element has exactly one authorized update path. If both the contractor PM and the G4 can update the same Forecast Date independently, you will have conflicting data within one update cycle.
2. **Role-based edit access.** Configure Action permissions so only the designated Responsible Owner can update a specific milestone's Forecast Date. The PM can update any milestone. No one edits Scheduled Date without an approval workflow.
3. **Mandatory fields at update.** When Forecast Date is changed, require a Comments entry explaining the change. Undocumented date changes create an audit trail gap.
4. **Timestamp everything.** Every update Action must auto-populate a Last Updated timestamp. Build dashboards to display "Data as of [timestamp]" so consumers know when data was last refreshed.
5. **Notification on status change.** Configure AIP Logic or email notification when a milestone status changes to DELAYED or when Overdue Flag is set. The PM should not be the last to know a milestone is at risk.

---

## CHAPTER 4 — RESOURCE AND BUDGET TRACKING

### 4-1. Overview

**BLUF:** Resource tracking in PM systems covers three categories: funding (GFEBS), equipment (GCSS-Army), and personnel (IPPS-A). Each has a distinct data model, a different authoritative source system, and a different update cadence. Build separate Object Types for each category. Do not attempt to force all resource data into a single generic "Resource" Object Type — the properties are too different and the reporting requirements diverge.

---

### 4-2. Funding Object Type Design

Funding tracking is the most sensitive data category in a PM system. Budget figures, obligation rates, and expenditure data are directly linked to command accountability.

**Funding Line Object Type — Required Properties:**

| Property | Type | Description | Authority |
|---|---|---|---|
| Funding Line ID | String | Unique identifier (align with GFEBS line item) | System |
| Line Item Description | String | Official program element description | GFEBS |
| Appropriation | Enum | O&M / MILCON / RDTE / PROC / MILPERS / Other | GFEBS |
| Fiscal Year | Integer | FY of appropriation | GFEBS |
| Total Authorized | Decimal | Total authorized amount (USD) | GFEBS |
| Obligated | Decimal | Amount obligated to date (USD) | GFEBS |
| Expended | Decimal | Amount expended to date (USD) | GFEBS |
| Uncommitted | Decimal | Computed: Authorized − Obligated | Computed |
| Obligation Rate | Decimal | Computed: (Obligated / Authorized) × 100 | Computed |
| Expenditure Rate | Decimal | Computed: (Expended / Authorized) × 100 | Computed |
| Obligation Target | Decimal | Planned obligation rate for current date (based on execution plan) | PM input |
| Obligation Variance | Decimal | Computed: Obligation Rate − Obligation Target | Computed |
| Data As Of | Date | Date of most recent GFEBS extract | GFEBS feed |
| Status | Enum | On Plan / Under Execution / At Risk / Overrun / Closed | Computed |

> **CAUTION: Funding data ingested from GFEBS is authoritative. Never allow manual overwrite of Obligated or Expended values. Manual edits to authoritative financial data can create discrepancies between MSS and GFEBS that result in anti-deficiency violations or audit findings. All financial figures must trace to a GFEBS extract with a documented data-as-of date.**

**Obligation Status Computation Logic:**

| Condition | Status |
|---|---|
| Obligation Variance within ±5% of target | On Plan |
| Obligation Rate below target by 5–15% | Under Execution |
| Obligation Rate below target by >15% | At Risk |
| Obligated > Authorized | Overrun (flag immediately) |
| Funding Line ID closed in GFEBS | Closed |

---

### 4-3. Contract Object Type Design

Contracts are a distinct tracking entity from funding lines. A single funding line may support multiple contracts. A single contract may draw from multiple funding lines. Track them separately with an explicit link.

**Contract Object Type — Required Properties:**

| Property | Type | Description |
|---|---|---|
| Contract Number | String | Official contract number (matches FPDS-NG) |
| Vendor Name | String | Contractor name |
| Contract Type | Enum | FFP / T&M / CPFF / IDIQ / BPA / Other |
| Period of Performance Start | Date | Contract start |
| Period of Performance End | Date | Contract end (base period) |
| Option End Date | Date | End of all options exercised |
| Total Contract Value | Decimal | Total awarded value |
| Obligated to Date | Decimal | Amount obligated against this contract |
| COTR | String | Contracting Officer Technical Representative (name or EDIPI) |
| Status | Enum | Pre-Award / Active / Option Period / Closeout / Complete |
| Days Until Expiration | Integer | Computed: Period of Performance End − Today |
| Option Exercise Required By | Date | Date by which option must be exercised |
| Days Until Option Decision | Integer | Computed: Option Exercise Required By − Today |

> **NOTE:** Configure an alert threshold for Days Until Expiration ≤ 90 days and Days Until Option Decision ≤ 60 days. These are standard lead times for contract actions. A dashboard that surfaces expiring contracts 90 days out gives the PM and contracting officer sufficient time to act. Discovery at 30 days is a crisis; discovery at 90 days is a workflow.

---

### 4-4. Equipment and Personnel Resource Tracking

**Equipment Resource Object Type (GCSS-Army aligned):**

| Property | Type | Description |
|---|---|---|
| Equipment ID | String | GCSS-Army bumper number or LIN |
| Equipment Type | String | Nomenclature |
| Assigned Unit | String (Org link) | Unit of assignment |
| Readiness Status | Enum | FMC / PMC / NMC |
| Location | String | Current location or AOR |
| Maintenance Due Date | Date | Next scheduled service |
| Days Until Maintenance | Integer | Computed |
| Program Link | String | Program ID (links to Program Object Type) |

**Personnel Billet Object Type (IPPS-A aligned):**

| Property | Type | Description |
|---|---|---|
| Billet ID | String | Authorized position ID |
| Position Title | String | Duty position title |
| Required Grade | String | Required grade/rank |
| MOS / AOC | String | Required MOS or AOC |
| Fill Status | Enum | Filled / Vacant / Excess / TDA Change |
| Incumbent | String | Current occupant (name or EDIPI) — leave null if vacant |
| Projected Fill Date | Date | If vacant: projected fill date |
| Program Link | String | Program ID |
| Organization | String (Org link) | Unit of assignment |

---

### 4-5. Resource Dashboard Design

**Resource Dashboard — Required Sections:**

1. **Funding Summary KPIs.** Four tiles: Total Authorized, Total Obligated, Obligation Rate, Variance vs. Plan. Color-code: GREEN if Variance ±5%, AMBER if −5% to −15%, RED if <−15% or overrun.
2. **Funding Line Table.** All funding lines for selected program, sorted by Obligation Variance (worst first). Include Appropriation, FY, Authorized, Obligated, Rate, Variance, Status.
3. **Contract Expiration Alert.** Filtered view: contracts with Days Until Expiration ≤ 90 or Days Until Option Decision ≤ 60. Display COTR, expiration date, contract value.
4. **Obligation Execution Trend.** Contour chart showing cumulative obligation rate over time vs. planned execution curve. This is the single most important funding visualization for a commander brief.
5. **Personnel Fill Status.** Summary table: Total Authorized Billets, Filled, Vacant, Vacancy Rate. Filtered list of vacant billets with Projected Fill Date.
6. **Equipment Readiness Summary.** FMC/PMC/NMC count with percentages. Table of NMC equipment with Maintenance Due Date.

---

### 4-6. Task: Build the Resource Tracking Dashboard

**CONDITIONS:** Funding Line, Contract, Personnel Billet, and Equipment Object Types implemented and populated with program data. GFEBS feed ingested (or sample data loaded for initial build). Workshop Editor access confirmed.

**STANDARDS:** Dashboard displays current obligation rates, contract expiration alerts, personnel fill status, and equipment readiness in a single unified view. All financial figures display with a "Data as of [date]" label. Obligation Variance color coding matches thresholds from para 4-2. Contract expiration alerts surface contracts within 90-day threshold.

**EQUIPMENT:** MSS Workshop, Resource Object Types, GFEBS extract dataset.

**PROCEDURE:**

1. Create a new Workshop page: "Resource Status — [Program Name]."
2. Add a Global Object Set Filter on Program ID. All widgets on this page inherit the program filter.
3. Add Funding Summary KPI tiles (para 4-5, item 1). Use Object Set aggregation: SUM(Total Authorized), SUM(Obligated), computed Obligation Rate.
4. Add a "Data as of" display: pull the maximum Data As Of date from the Funding Line Object Set. This label must appear adjacent to all financial figures.
5. Add Funding Line Table (para 4-5, item 2). Configure conditional row formatting using Obligation Status property.
6. Add Contract Expiration Alert section with filtered table (Days Until Expiration ≤ 90). Sort ascending by expiration date. Add badge/count of contracts in threshold window.
7. Add an Obligation Execution chart. Use Contour embedded in Workshop if the trend data requires time-series aggregation from a separate pipeline output dataset.
8. Add Personnel Fill and Equipment Readiness sections (para 4-5, items 5 and 6).
9. Lock all financial display widgets to read-only. No edit actions on the Resource Dashboard page — updates happen through the designated update workflow, not inline editing.
10. Test with actual GFEBS extract data. Verify computed rates match manual calculation.
11. Present to program's resource manager for validation before publishing.

---

## CHAPTER 5 — RISK REGISTER DESIGN

### 5-1. Overview

**BLUF:** A risk register that nobody updates is worse than no risk register — it creates false confidence. Design the risk register for minimal update friction, maximum visibility, and automatic escalation. The PM's job is to ensure risks are identified early and mitigated before they become issues. The system's job is to make that easy.

---

### 5-2. Risk Object Type Design

**Risk Object Type — Required Properties:**

| Property | Type | Description |
|---|---|---|
| Risk ID | String | Unique identifier (auto-generated, e.g., RISK-001) |
| Risk Title | String | Short descriptive title (max 80 characters) |
| Risk Description | String | Full description of the risk condition |
| Risk Category | Enum | Schedule / Cost / Technical / Resource / External / Dependency |
| Likelihood | Integer | 1–5 score (1 = Rare, 5 = Almost Certain) |
| Impact | Integer | 1–5 score (1 = Minimal, 5 = Critical) |
| Risk Score | Integer | Computed: Likelihood × Impact (1–25) |
| Risk Level | Enum | Low / Medium / High / Critical | Computed from Score |
| Risk Owner | String (Personnel link) | Person responsible for monitoring and mitigation |
| Status | Enum | Open / Monitoring / Mitigating / Accepted / Closed / Realized |
| Mitigation Strategy | String | Documented approach to reducing likelihood or impact |
| Contingency Plan | String | Response plan if risk is realized |
| Target Mitigation Date | Date | Date by which mitigation should be complete |
| Residual Likelihood | Integer | 1–5, after mitigation |
| Residual Impact | Integer | 1–5, after mitigation |
| Residual Score | Integer | Computed: Residual Likelihood × Residual Impact |
| Linked Milestones | Object links | Milestones affected by this risk |
| Linked Funding Lines | Object links | Funding lines affected by this risk |
| Date Identified | Date | When risk was first recorded |
| Last Review Date | Date | Date of last formal risk review |
| Days Since Review | Integer | Computed: Today − Last Review Date |
| Stale Flag | Boolean | True if Days Since Review > 30 |
| Escalation Flag | Boolean | True if Risk Level = Critical OR Days Since Review > 45 |

**Risk Level Thresholds:**

| Score | Risk Level | Color | Required Action |
|---|---|---|---|
| 1–4 | Low | GREEN | Document and monitor |
| 5–9 | Medium | AMBER | Mitigation plan required |
| 10–19 | High | RED | PM brief at next update cycle |
| 20–25 | Critical | RED (flashing/priority) | Immediate commander notification |

---

### 5-3. Issue Object Type Design

Issues are risks that have been realized — they require active management, not just monitoring. Track issues separately from risks. A risk that becomes an issue should be linked between both Object Types for traceability.

**Issue Object Type — Required Properties:**

| Property | Type | Description |
|---|---|---|
| Issue ID | String | Unique identifier (e.g., ISSUE-001) |
| Issue Title | String | Short descriptive title |
| Description | String | Full description of the issue and current impact |
| Source Risk | Risk link | Risk that generated this issue (if applicable) |
| Category | Enum | Schedule / Cost / Technical / Resource / External |
| Impact Statement | String | Documented impact on program (scope, schedule, cost) |
| Schedule Impact | Integer | Days of schedule impact (positive = delay) |
| Cost Impact | Decimal | Estimated cost impact (USD) |
| Issue Owner | String (Personnel link) | Person responsible for resolution |
| Priority | Enum | Critical / High / Medium / Low |
| Status | Enum | Open / In Resolution / Resolved / Escalated / Closed |
| Resolution Plan | String | Documented plan to resolve |
| Target Resolution Date | Date | Planned resolution date |
| Actual Resolution Date | Date | Actual resolution (null if open) |
| Days Open | Integer | Computed: Today − Date Identified |
| Escalated To | String | Commander or authority issue was escalated to |

---

### 5-4. Risk Dashboard Design

**Risk Dashboard — Required Sections:**

1. **Risk Summary Matrix.** A 5×5 heat map visualization showing risk distribution by Likelihood × Impact. Risks plotted as points. Color zones: green (low), amber (medium), red (high/critical). This is the primary risk visualization for commander briefs.
2. **Risk Register Table.** Full risk register with columns: Risk ID, Title, Category, Score, Risk Level, Owner, Status, Target Mitigation Date, Days Since Review. Sort default: Score descending.
3. **Critical and High Risk Alert Panel.** Filtered view showing only Risk Level = Critical or High. Display as high-visibility cards with escalation flag indicator.
4. **Stale Risk Alert.** Filtered view: risks where Stale Flag = True (Days Since Review > 30). Surfaces risks that have not been reviewed recently. A stale risk register is an unmanaged risk register.
5. **Issue Tracker.** Open issues with schedule and cost impact columns visible. Sort by Days Open descending.
6. **Risk Trend Chart.** Count of Open/Mitigating/Closed risks over time. Shows whether the risk profile is improving (closing risks) or degrading (new risks opening faster than old ones close).

---

### 5-5. Automated Risk Escalation Design

Design AIP Logic workflows to automate risk escalation notifications. Escalation should not depend on a PM remembering to escalate — the system escalates automatically based on defined triggers.

**Escalation Trigger Configuration:**

| Trigger | Action |
|---|---|
| Risk Score increases to ≥ 20 (Critical) | Auto-set Escalation Flag = True; notify PM via AIP Logic message |
| Days Since Review > 30 | Auto-set Stale Flag = True; surface on Stale Risk dashboard section |
| Days Since Review > 45 | Auto-set Escalation Flag = True; notify PM and Risk Owner |
| Issue Days Open > 14 with Status = Open | Auto-escalate Issue Priority to Critical; notify PM |
| Target Mitigation Date passes with Status ≠ Closed | Flag as overdue; notify Risk Owner and PM |

> **NOTE:** Configure escalation notification recipients at the Program level (Program Object Type property: PM EDIPI, Deputy PM EDIPI, Senior Advisor EDIPI). This allows escalation to route correctly for each program without hardcoding personnel in workflow logic.

---

### 5-6. Task: Build the Risk Register and Dashboard

**CONDITIONS:** Risk and Issue Object Types implemented with properties from para 5-2 and 5-3. At least five Risk objects entered with full property sets. Workshop Editor access confirmed. AIP Logic available for escalation workflow configuration.

**STANDARDS:** Risk dashboard displays heat map, risk register table, critical/high alert panel, stale risk alert, and issue tracker. All filter and sort controls functional. Risk Score and Risk Level computed correctly. Escalation flags auto-populate based on threshold logic.

**EQUIPMENT:** MSS Workshop, Risk and Issue Object Types, AIP Logic (for escalation notification).

**PROCEDURE:**

1. Verify all computed properties on Risk Object Type (Risk Score, Risk Level, Days Since Review, Stale Flag, Escalation Flag) are producing correct values before building the dashboard.
2. Create a new Workshop page: "Risk Register — [Program Name]."
3. Build the Risk Summary Matrix. If a native 5×5 heat map widget is available in Workshop, use it. If not, build a scatter plot using Likelihood (X-axis) and Impact (Y-axis) with Risk Level as the color property.
4. Add Risk Register Table. Configure all required columns. Apply conditional row formatting: Risk Level drives row color.
5. Add Critical and High Risk Alert Panel as a filtered card layout above the full table.
6. Add Stale Risk Alert section. Include count badge ("X risks not reviewed in 30+ days"). Sort by Days Since Review descending.
7. Add Issue Tracker table on Risk page or as a separate tab. Include Schedule Impact and Cost Impact columns.
8. Add Risk Trend Chart. This requires a pipeline output dataset that records risk counts by status and date. If this dataset does not yet exist, document the requirement and build the pipeline (Chapter 6 covers pipeline development).
9. Configure AIP Logic escalation workflow per para 5-5 trigger table.
10. Test escalation triggers with a test risk object. Verify flags set and notifications route correctly.
11. Present to program manager for validation. Brief risk review process: who reviews, on what schedule, using what Action workflow.
12. Publish. Brief all risk owners on the update workflow — especially the requirement to update Last Review Date after each review.

---

## CHAPTER 6 — REPORTING PIPELINES

### 6-1. Overview

**BLUF:** Automated reporting pipelines eliminate the manual compilation burden from routine Army reporting requirements. A pipeline built once runs on schedule, generates consistent outputs, and frees PM staff from spending hours each week aggregating data for reports that a well-designed system can produce automatically. This chapter covers pipeline design for SITREP, LOGREP, and PERSTAT reporting — the three most common PM-level reporting requirements in USAREUR-AF.

---

### 6-2. Pipeline Architecture for PM Reporting

PM reporting pipelines follow a standard three-stage architecture:

```
STAGE 1: EXTRACT
Source Ontology Objects
(Program, Milestone, Risk,
 Resource, Personnel)
        |
        v
STAGE 2: TRANSFORM
Aggregation and Formatting
(Python/SQL transforms
 in Pipeline Builder)
        |
        v
STAGE 3: LOAD
Output Dataset
(Formatted report table,
 readable by Workshop and
 downstream consumers)
```

All PM reporting pipelines must be:
- **Scheduled:** Run on the reporting cadence, not manually triggered.
- **Idempotent:** Running the pipeline twice should produce the same output as running it once. Use INSERT OR REPLACE logic or watermark-based incremental patterns.
- **Documented:** Every pipeline has a README dataset describing inputs, transformation logic, outputs, and the reporting requirement it satisfies.
- **Validated:** Pipeline output is spot-checked against authoritative source data on first run and after any structural change.

---

### 6-3. SITREP Automation Pipeline

The SITREP (Situation Report) is the standard weekly reporting product for Army programs. USAREUR-AF programs typically submit SITREPs to the appropriate brigade/division/corps headquarters on a defined schedule. An automated SITREP pipeline reads current Object data and generates a structured SITREP output dataset that the PM reviews, validates, and submits.

**SITREP Output Dataset Schema:**

| Column | Source | Description |
|---|---|---|
| report_date | Pipeline runtime | Date of SITREP generation |
| program_id | Program OT | Unique program identifier |
| program_name | Program OT | Official program name |
| program_status | Program OT | Overall program status (enum) |
| health_score | Program OT | Composite health score (0–100) |
| milestones_total | Milestone OT (count) | Total milestones in program |
| milestones_complete | Milestone OT (count) | Milestones with Status = Complete |
| milestones_delayed | Milestone OT (count) | Milestones where SV > 0 |
| milestones_overdue | Milestone OT (count) | Milestones where Overdue Flag = True |
| next_milestone_name | Milestone OT | Name of next scheduled milestone |
| next_milestone_date | Milestone OT | Scheduled Date of next milestone |
| risk_high_critical_count | Risk OT (count) | Count of High + Critical risks |
| top_risk_title | Risk OT | Title of highest-scored open risk |
| obligation_rate | Funding Line OT | Current overall obligation rate (%) |
| personnel_fill_rate | Personnel Billet OT | Current fill rate (%) |
| commander_summary | PM input | Free-text commander's summary (PM enters weekly) |
| primary_concern | PM input | Primary concern statement (PM enters weekly) |
| significant_activities | PM input | Key activities this reporting period |

**SITREP Pipeline Python Transform (Foundry Code Repository):**

> **NOTE:** The following transform is a reference implementation. Implement in a Foundry Code Repository or Pipeline Builder Python step. Coordinate with a TM-40B developer if Code Repository access is not available to your role.

```python
# sitrep_generator.py
# Generates weekly SITREP output dataset from PM tracking Object Types
# Runs on scheduled cadence (every Sunday 2000L CET)
# Consult TM-40B for Code Repository deployment procedures

from transforms.api import transform_df, Input, Output
import pyspark.sql.functions as F
from datetime import datetime, timezone

@transform_df(
    Output("/programs/{program_id}/reporting/sitrep_weekly"),
    milestones=Input("/programs/{program_id}/ontology/milestones_dataset"),
    risks=Input("/programs/{program_id}/ontology/risks_dataset"),
    funding=Input("/programs/{program_id}/ontology/funding_lines_dataset"),
    personnel=Input("/programs/{program_id}/ontology/personnel_billets_dataset"),
    program=Input("/programs/{program_id}/ontology/program_dataset"),
)
def compute(milestones, risks, funding, personnel, program):
    """
    Aggregates current-state PM tracking data into SITREP output format.
    Output is one row per program per reporting period.
    Commander summary fields (free text) are populated via separate
    Action workflow and merged in final step.
    """
    report_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Milestone aggregations
    milestone_summary = milestones.agg(
        F.count("milestone_id").alias("milestones_total"),
        F.sum(F.when(F.col("status") == "Complete", 1).otherwise(0))
         .alias("milestones_complete"),
        F.sum(F.when(F.col("schedule_variance") > 0, 1).otherwise(0))
         .alias("milestones_delayed"),
        F.sum(F.when(F.col("overdue_flag") == True, 1).otherwise(0))
         .alias("milestones_overdue"),
    )

    # Next upcoming milestone (nearest Scheduled Date, not yet complete)
    next_milestone = (
        milestones
        .filter(F.col("status") != "Complete")
        .orderBy("scheduled_date")
        .limit(1)
        .select(
            F.col("milestone_name").alias("next_milestone_name"),
            F.col("scheduled_date").alias("next_milestone_date"),
        )
    )

    # Risk aggregations
    risk_summary = risks.filter(
        F.col("status").isin(["Open", "Monitoring", "Mitigating"])
    ).agg(
        F.sum(
            F.when(F.col("risk_level").isin(["High", "Critical"]), 1).otherwise(0)
        ).alias("risk_high_critical_count")
    )

    # Top risk (highest score, open)
    top_risk = (
        risks
        .filter(F.col("status").isin(["Open", "Monitoring", "Mitigating"]))
        .orderBy(F.col("risk_score").desc())
        .limit(1)
        .select(F.col("risk_title").alias("top_risk_title"))
    )

    # Obligation rate (overall, across all funding lines)
    funding_summary = funding.agg(
        (F.sum("obligated") / F.sum("total_authorized") * 100)
        .alias("obligation_rate")
    )

    # Personnel fill rate
    fill_summary = personnel.agg(
        (
            F.sum(F.when(F.col("fill_status") == "Filled", 1).otherwise(0))
            / F.count("billet_id") * 100
        ).alias("personnel_fill_rate")
    )

    # Program base row
    program_base = program.select(
        "program_id",
        "program_name",
        "program_status",
        "overall_health_score",
    )

    # Assemble final output — cross join single-row summaries
    result = (
        program_base
        .crossJoin(milestone_summary)
        .crossJoin(next_milestone)
        .crossJoin(risk_summary)
        .crossJoin(top_risk)
        .crossJoin(funding_summary)
        .crossJoin(fill_summary)
        .withColumn("report_date", F.lit(report_date))
    )

    return result
```

> **CAUTION: The transform above uses crossJoin on single-row aggregation DataFrames. This is correct only when each aggregation step produces exactly one row (one program, one report period). If your pipeline runs across multiple programs, add a program_id join key to all aggregations and replace crossJoin with a keyed join. A crossJoin on multi-row DataFrames will produce a cartesian product and corrupt your output.**

---

### 6-4. LOGREP / LOGSTAT Integration

LOGREP (Logistics Report) and LOGSTAT (Logistics Status) track equipment and supply status. For PM systems supporting sustainment programs, LOGREP integration with GCSS-Army feeds is critical.

**LOGREP Output Dataset Schema (standard fields):**

| Column | Source | Description |
|---|---|---|
| report_date | Pipeline | Date of report |
| program_id | Program OT | Program identifier |
| equipment_line | Equipment OT | Equipment nomenclature |
| total_on_hand | Equipment OT (count) | Total equipment in inventory |
| fmc_count | Equipment OT (count) | Fully Mission Capable |
| pmc_count | Equipment OT (count) | Partially Mission Capable |
| nmc_count | Equipment OT (count) | Non-Mission Capable |
| fmc_rate | Computed | FMC / Total × 100 |
| maintenance_due_30days | Equipment OT (count) | Equipment with maintenance due in ≤30 days |
| supply_fill_rate | Supply Line OT | Supply fill rate (%) if tracked |
| critical_shortfalls | Equipment OT | List of NMC items with critical mission impact |

> **NOTE:** GCSS-Army feeds into MSS through a connector managed by the USAREUR-AF C2DAO. Do not attempt to build a direct GCSS-Army connector — use the enterprise feed. Coordinate with the C2DAO data steward for the Equipment domain to confirm feed availability and schema before designing your LOGREP pipeline.

---

### 6-5. PERSTAT Pipeline Design

PERSTAT (Personnel Status) is reported daily or on commander's requirement. For PM systems with personnel tracking, PERSTAT automation reduces a daily manual compilation task to a pipeline review.

**PERSTAT Output Dataset Schema:**

| Column | Source | Description |
|---|---|---|
| report_date | Pipeline | Date and time of report (DTG format) |
| program_id | Program OT | — |
| org_name | Organization OT | Reporting unit |
| authorized_strength | Personnel Billet OT | Total authorized billets |
| assigned_strength | Personnel OT (count) | Total personnel assigned |
| present_for_duty | Personnel OT (count) | Personnel present (not TDY, leave, etc.) |
| tdy_count | Personnel OT (count) | Personnel on TDY |
| leave_count | Personnel OT (count) | Personnel on leave |
| other_absent | Personnel OT (count) | Other absences |
| percent_present | Computed | Present / Assigned × 100 |
| vacant_billets | Personnel Billet OT (count) | Unfilled positions |

> **CAUTION: PERSTAT data contains personnel assignment and duty status information. This dataset must be classified appropriately (minimum FOUO) and access restricted to authorized personnel in the reporting chain. Do not publish PERSTAT pipeline outputs to open-access folders. Configure folder-level access control before the first pipeline run.**

---

### 6-6. Scheduling Pipeline Transforms

All PM reporting pipelines run on defined schedules. Configure schedules in Pipeline Builder using the scheduling interface.

**Standard Reporting Cadences for USAREUR-AF:**

| Report | Cadence | Suggested Run Time | Notes |
|---|---|---|---|
| SITREP | Weekly | Sunday 2000L CET | Allows PM review before Monday morning brief |
| LOGREP | Weekly | Friday 1800L CET | Aligns to end-of-week equipment status |
| PERSTAT | Daily | 0600L CET | Morning accountability cycle |
| USR | Monthly | Last day of month, 1800L CET | End-of-month readiness snapshot |
| Risk Register Summary | Weekly | Sunday 2000L CET | Companion to SITREP |
| Obligation Execution | Weekly | Monday 0600L CET | Beginning-of-week financial status |

> **NOTE:** Schedule all pipelines to run at least 2 hours before the first consumer review of that data. A SITREP pipeline that runs at 0700 Monday when the PM needs to review by 0800 creates unnecessary risk. Front-load the processing window.

**Pipeline Failure Notification:**

Configure Pipeline Builder failure alerts for all scheduled PM reporting transforms. Designate at least two notification recipients (PM and a backup). A failed SITREP pipeline that nobody notices until the report is due is a PM system failure, not a technical curiosity.

---

### 6-7. Task: Build and Schedule the SITREP Pipeline

**CONDITIONS:** Program, Milestone, Risk, Funding Line, and Personnel Billet Object Type datasets are available as Foundry datasets (backed by pipeline from Ontology). Pipeline Builder access confirmed. Code Repository access confirmed for Python transform deployment (or TM-40B developer identified for implementation).

**STANDARDS:** SITREP pipeline produces correct output dataset with all columns from para 6-3 schema. Pipeline runs on Sunday 2000L CET schedule. Pipeline failure notification routes to PM and backup. Output dataset is read-accessible to SITREP review Workshop page.

**EQUIPMENT:** MSS Pipeline Builder, Code Repository, Program Object Type datasets.

**PROCEDURE:**

1. Confirm all input datasets exist and have fresh data. Check lineage for each input dataset to verify it is being populated by current Object Type write-back.
2. In Code Repository, create a new Python transform file: `sitrep_generator.py`. Implement the transform from para 6-3. Adjust column names to match your Object Type property names exactly.
3. Configure Input and Output paths. Output path: `/programs/[program_id]/reporting/sitrep_weekly`.
4. Test locally using Foundry's preview functionality. Verify row count (should equal number of programs in scope), verify computed aggregations against manual counts from the Milestone dashboard.
5. In Pipeline Builder, add the Code Repository transform as a node. Connect input dataset nodes for each source dataset.
6. Configure schedule: Weekly, Sunday, 2000 CET. Enable.
7. Configure failure notification: add PM EDIPI and backup EDIPI as notification recipients for pipeline failure events.
8. Create a SITREP Review Workshop page. Display the SITREP output dataset in a structured table. Add a "Review and Certify" Action that allows the PM to add Commander Summary, Primary Concern, and Significant Activities free text before the report is submitted.
9. Run the pipeline manually for the first execution. Verify output.
10. Brief the PM on the review workflow: pipeline runs automatically, PM reviews and certifies in Workshop, certified output is the submittable SITREP.

---

## CHAPTER 7 — SENIOR LEADER DASHBOARDS

### 7-1. Overview

**BLUF:** Senior leader dashboards are the primary interface between the PM system and the command. They must be visually unambiguous, instantly readable, and require zero training to interpret. A commander at a battle update brief should be able to look at the dashboard and answer "what is the program status?" in under 10 seconds without asking a follow-up question.

---

### 7-2. Senior Leader Dashboard Design Principles

**Principle 1: One question, one screen.** Each dashboard page answers exactly one question. "What is the overall program status?" is one question. "Which milestones are delayed?" is a different question. Do not combine both on one page.

**Principle 2: Color communicates status, not aesthetics.** Use RED/AMBER/GREEN for status indicators only. Do not use color for visual variety. A commander who sees red assumes something is wrong. If you use red for a header bar, you have diluted your status signaling.

**Principle 3: Numbers need context.** "Obligation Rate: 67%" means nothing without context. "Obligation Rate: 67% (Target: 72%, Variance: -5%)" is actionable. Every KPI must display its target and variance.

**Principle 4: Minimize cognitive load.** Eliminate all decorative elements. No logos, no gradients, no animation. Every pixel on a senior leader dashboard should carry information.

**Principle 5: Brief-ready by default.** The dashboard should look the same at 0700 when the PM is reviewing it and at 0800 when it is on the screen during the battle update brief. No pre-brief manipulation required.

**Principle 6: Action-oriented.** Every flagged item (overdue milestone, critical risk, expiring contract) must have a clear path to action. If the commander asks "what are we doing about this?" the answer should be accessible from the dashboard.

---

### 7-3. Commander's Program Summary Page Layout

The Commander's Program Summary is the opening page of the senior leader dashboard. It provides a single-screen, complete status snapshot of the program.

**Required Layout — Commander's Program Summary:**

```
+--------------------------------------------------+
| PROGRAM: [Name]          DATA AS OF: [DTG]       |
| PM: [Name]               PHASE: [Phase]          |
+--------------------------------------------------+
|  STATUS     |  MILESTONE  |   RISK    |  BUDGET  |
|  [GREEN]    |  [AMBER]    |  [RED]    |  [GREEN] |
|  On Track   |  2 Delayed  |  1 Crit.  |  On Plan |
+--------------------------------------------------+
|  SCHEDULE         |  RISK SUMMARY                |
|  Timeline view    |  5x5 matrix (compact)        |
|  baseline vs.     |  or Risk count by level      |
|  current forecast |                              |
+--------------------------------------------------+
|  UPCOMING MILESTONES         |  TOP ISSUES        |
|  Next 3 milestones with      |  Top 3 open issues |
|  dates and owners            |  with impact       |
+--------------------------------------------------+
|  COMMANDER'S SUMMARY                             |
|  [Free text field - PM certified this period]    |
+--------------------------------------------------+
```

> **NOTE:** The four status tiles at top (Status / Milestone / Risk / Budget) are the most important visual elements on the page. They must be large enough to read across a room during a brief. Configure minimum tile height to 120px and font size ≥ 24pt for the status label.

---

### 7-4. Drill-Down Page Design

Senior leader dashboards must support drill-down from summary to detail without requiring navigation to a different application. Design two drill-down pages: Milestone Detail and Risk Detail.

**Milestone Detail Page:**
- Timeline visualization (all milestones, baseline vs. current)
- Full milestone table with all status properties
- Schedule variance chart (bar chart, one bar per milestone)
- Delayed/overdue milestone detail cards
- Comparison: planned vs. actual percent complete

**Risk Detail Page:**
- 5×5 risk heat map (full size)
- Risk register table with full property set
- Issue tracker table
- Risk trend chart (open/closed over time)
- Mitigation status tracker

**Resource Detail Page:**
- Obligation execution trend chart
- Funding line table
- Contract expiration alerts
- Personnel and equipment status

Configure navigation tiles on the Commander's Summary page that open each detail page. Use consistent naming: "Milestone Detail," "Risk Detail," "Resource Detail."

---

### 7-5. Brief-Ready Configuration Standards

Dashboards used directly in command briefs require specific configuration to function reliably in presentation conditions.

**Brief-Ready Configuration Checklist:**

| Requirement | Configuration |
|---|---|
| Background color | White or very light grey — projectors wash out dark backgrounds |
| Text size | Minimum 14pt for table cells, 24pt for KPI tiles |
| Color contrast | All text meets WCAG AA contrast ratio (4.5:1) |
| Auto-refresh | Configure Workshop page to auto-refresh every 5 minutes |
| No loading spinners visible | Pre-load all Object Sets before brief. Spinners during a brief indicate poor design. |
| Date/time display | Always show "Data as of [DTG]" on every page |
| Responsive layout | Test on the display resolution of the conference room projector/screen |
| Print/export | Configure Workshop PDF export for post-brief distribution |
| No draft or development indicators | Verify no "dev" or "test" labels appear on production dashboard |
| Bookmark URL | Configure a stable Workshop URL that can be bookmarked by the commander's staff |

---

### 7-6. Task: Build the Commander's Program Summary Dashboard

**CONDITIONS:** All PM Object Types implemented and populated. SITREP pipeline operational. Risk dashboard (Chapter 5) and Resource dashboard (Chapter 4) complete and validated. Workshop Editor access confirmed.

**STANDARDS:** Commander's Program Summary page displays all required sections per para 7-3 layout. Four status tiles are color-coded and data-current. Drill-down navigation functional to Milestone, Risk, and Resource detail pages. Dashboard passes all brief-ready configuration checks from para 7-5.

**EQUIPMENT:** MSS Workshop, all PM Object Types, SITREP pipeline output dataset.

**PROCEDURE:**

1. Create a new Workshop application: "[Program Name] — Commander's Dashboard."
2. Configure page 1: "Program Summary." Build per para 7-3 layout.
   - Pull STATUS tile from Program Object Type `program_status` property.
   - Pull MILESTONE tile from SITREP pipeline output: count of milestones_delayed.
   - Pull RISK tile from Risk Object Type: count where Risk Level = Critical or High.
   - Pull BUDGET tile from Funding Line Object Type: Obligation Variance vs. target.
   - Add Timeline widget for scheduled/forecast milestone dates.
   - Add compact risk summary (count by level or embedded small heat map).
   - Add Upcoming Milestones card list: filter to next 3 by Scheduled Date.
   - Add Top Issues card list: filter to Issues where Status = Open, sort by Priority.
   - Add Commander's Summary text block: pull from SITREP output dataset `commander_summary` column.
3. Configure pages 2, 3, 4: Milestone Detail, Risk Detail, Resource Detail per para 7-4.
4. Add navigation tiles on page 1 linking to pages 2, 3, 4.
5. Apply brief-ready configuration per para 7-5 checklist. Test each item explicitly.
6. Add "Data as of [DTG]" display to every page. Pull from the maximum `report_date` in the SITREP output dataset.
7. Configure Workshop application permissions: read access to all stakeholders, no edit access on dashboard pages.
8. Test on target display hardware if possible (projector or large-format display).
9. Present to PM for final review. Present to commander or XO for acceptance. Document any change requests.
10. Publish to production. Provide commander's staff with bookmarked URL.

> **WARNING: Do not brief an untested dashboard to the commander for the first time. The first brief using a new dashboard should be a rehearsal with the PM present, not the live BUB. Discover layout issues in rehearsal, not in front of the command.**

---

## CHAPTER 8 — PORTFOLIO ANALYSIS

### 8-1. Overview

**BLUF:** Portfolio analysis answers the questions that single-program dashboards cannot: Which programs are collectively at risk? Where are resource conflicts across the portfolio? What does overall portfolio health look like to USAREUR-AF leadership? Contour is the primary tool for portfolio-level analysis — it provides the aggregation, comparison, and trend analysis that Workshop dashboards do not.

---

### 8-2. Portfolio Object Type Design

Portfolio analysis requires a Portfolio Object Type that aggregates across multiple Programs.

**Portfolio Object Type — Required Properties:**

| Property | Type | Description |
|---|---|---|
| Portfolio ID | String | Unique identifier |
| Portfolio Name | String | Official portfolio name (e.g., "USAREUR-AF FY26 Modernization Portfolio") |
| Portfolio Manager | String | Senior PM or G-staff officer responsible |
| Sponsor | String | Command or HQDA sponsor |
| Programs | Object links | All Program Objects in this portfolio |
| Total Authorized Budget | Decimal | Sum of all authorized funding (computed) |
| Total Obligated | Decimal | Sum of all obligated funding (computed) |
| Portfolio Obligation Rate | Decimal | Computed |
| Programs On Track | Integer | Count of programs with status = On Track (computed) |
| Programs At Risk | Integer | Count of programs with status = At Risk (computed) |
| Programs Off Track | Integer | Count of programs with status = Off Track (computed) |
| High Critical Risk Count | Integer | Sum of high/critical risks across all programs (computed) |
| Portfolio Health Score | Integer | Weighted composite of all program health scores (computed) |

---

### 8-3. Contour Analysis Patterns for Portfolio PMs

Contour provides the analytical workspace for portfolio-level analysis. These are the standard analysis patterns for USAREUR-AF portfolio PMs.

**Pattern 1: Cross-Program Schedule Performance Analysis**

Purpose: Compare schedule variance across all programs in the portfolio to identify systemic schedule issues vs. program-specific issues.

Steps:
1. In Contour, open the Milestone Object Type dataset scoped to all programs in the portfolio.
2. Pivot by Program Name (rows) and Milestone Type (columns).
3. Value: average Schedule Variance (days) for each cell.
4. Highlight cells where average variance > 14 days.
5. Interpretation: If one program shows high variance across all milestone types, the issue is program-specific. If high variance concentrates in one milestone type across multiple programs (e.g., all programs are late on "Decision" milestones), the issue is systemic.

**Pattern 2: Portfolio Budget Execution Variance**

Purpose: Identify which programs are at risk of year-end under-execution or over-run.

Steps:
1. Open Funding Line Object Type dataset scoped to portfolio.
2. Pivot by Program Name (rows) and Fiscal Quarter (columns).
3. Value: Obligation Variance (actual rate minus planned rate) for each program/quarter cell.
4. Sort rows by current-quarter Obligation Variance ascending (most at-risk programs at top).
5. Programs with persistent negative Obligation Variance (under-executing) are at risk of fiscal year-end lapse. Escalate to resource manager.

**Pattern 3: Risk Profile Comparison**

Purpose: Compare risk posture across programs. Identify which programs carry disproportionate portfolio risk.

Steps:
1. Open Risk Object Type dataset scoped to portfolio.
2. Group by Program Name. Aggregate: count of High+Critical risks, average Risk Score, count of Stale risks.
3. Sort by count of High+Critical risks descending.
4. Cross-reference with Program Health Score. A program with few risks but low health score has unmeasured or underreported risk — investigate.

**Pattern 4: Milestone Completion Trend Analysis**

Purpose: Project portfolio completion trajectory based on historical milestone completion rates.

Steps:
1. Open historical SITREP output dataset (requires SITREP pipeline to have been running for ≥ 4 reporting periods).
2. Plot milestones_complete over time for each program.
3. Fit trend line. Project to program end date.
4. Programs where trajectory does not intersect with required completion count by end date require schedule intervention.

---

### 8-4. Portfolio Reporting to USAREUR-AF Leadership

Portfolio-level reporting supports USAREUR-AF headquarters reporting requirements. The standard portfolio report structure for USAREUR-AF programs:

**USAREUR-AF Portfolio Brief Structure:**

1. **Portfolio Summary.** Total programs, overall health distribution (count by status), total portfolio authorized budget, overall obligation rate, high/critical risk count.
2. **Program-by-Program Status Matrix.** Table with one row per program: Program Name, Phase, Status (color-coded), Milestone Health, Risk Level, Budget Status, PM.
3. **Top Issues Across Portfolio.** Issues from all programs where Priority = Critical or High, sorted by Schedule Impact.
4. **Schedule Performance Summary.** Programs with Schedule Variance > 30 days on any milestone, with explanation.
5. **Budget Execution Summary.** Programs with Obligation Variance < −10%, with explanation and proposed mitigation.
6. **Recommendations.** PM's recommended actions for command decision. Specific, actionable, with proposed decision dates.

Configure a Portfolio Dashboard in Workshop with a dedicated "Portfolio View" page that generates this brief structure from live data. This page is read-only for all users except the Portfolio Manager.

---

### 8-5. Task: Build the Portfolio Analysis View in Contour

**CONDITIONS:** Portfolio Object Type implemented and linked to ≥ 2 Program objects. Historical SITREP pipeline output dataset available (≥ 4 reporting periods). Contour analysis access confirmed.

**STANDARDS:** Portfolio analysis view in Contour displays cross-program schedule performance, budget execution variance, and risk profile comparison. Pivot tables produce correct aggregations validated against source data. Analysis is saved as a named Contour view, accessible to Portfolio Manager.

**EQUIPMENT:** MSS Contour, Portfolio and Program Object Type datasets, historical SITREP output dataset.

**PROCEDURE:**

1. Open Contour. Load the Milestone Object Type dataset.
2. Build Pattern 1 (Cross-Program Schedule Performance) per para 8-3. Save as named view: "Portfolio — Schedule Performance."
3. Load the Funding Line Object Type dataset. Build Pattern 2 (Budget Execution Variance) per para 8-3. Save as "Portfolio — Budget Execution."
4. Load the Risk Object Type dataset. Build Pattern 3 (Risk Profile Comparison) per para 8-3. Save as "Portfolio — Risk Profile."
5. Load the SITREP output dataset. Build Pattern 4 (Milestone Completion Trend) per para 8-3. Save as "Portfolio — Completion Trend."
6. In Workshop, create a Portfolio page in the Commander's Dashboard application. Embed key portfolio views (or replicate with Workshop aggregations if Contour embedding is not configured).
7. Add Program-by-Program Status Matrix table per para 8-4.
8. Validate all aggregations. Cross-check total portfolio obligation rate against sum of individual program rates.
9. Brief Portfolio Manager on the four Contour analysis patterns. Ensure they can reproduce and update the analysis independently.

---

## CHAPTER 9 — PM SYSTEM GOVERNANCE

### 9-1. Overview

**BLUF:** PM systems are operational infrastructure. They require ongoing governance — access control, audit trails, data stewardship, change management, and sustainment planning — from the day they are published. Governance is not an afterthought. A PM system with no governance degrades within one reporting cycle.

---

### 9-2. Access Control Design

PM systems contain sensitive data: budget figures, risk registers, personnel assignments, and program strategies. Access control must be explicitly designed and enforced from the outset.

**Access Control Matrix — Standard PM System:**

| Role | Program Summary Page | Resource Dashboard | Risk Register | SITREP Pipeline Output | Action Edit Rights |
|---|---|---|---|---|---|
| Commander / XO | Read | Read (aggregated only) | Read | Read | None |
| Program Manager | Read/Write | Read/Write | Read/Write | Read/Write | All Actions |
| Deputy PM | Read/Write | Read | Read/Write | Read | Assigned Actions |
| Resource Manager | Read | Read/Write | Read | Read | Resource Actions |
| Risk Officer | Read | Read | Read/Write | Read | Risk Actions |
| Staff (general) | Read (Pages 1-2 only) | None | None | None | None |
| Contractor Support | Read (limited scope) | None | Read (own risks only) | None | Assigned Task Actions |

> **NOTE:** This matrix is a minimum baseline. Adjust based on program classification level and command-specific access policies. If any data in the system is classified CUI or higher, access control must be reviewed by the security officer before publication. Do not rely on Foundry role configuration alone — confirm with your security officer that the Foundry access configuration meets classification handling requirements for CUI data.

**Access Control Implementation Steps:**

1. In the Foundry project folder, configure role-based access groups aligned to the matrix above.
2. Create Workshop-level page permissions for each page (e.g., Resource Dashboard page restricted to Resource Manager role and PM).
3. Configure Action permissions on each Action to match the matrix (who can execute which Actions).
4. Document the access matrix in the PM system README dataset. Review at each quarterly governance cycle.

---

### 9-3. Audit Trail Requirements

PM systems that support Army reporting chains (SITREP, LOGREP, PERSTAT submission) require audit trails. An audit trail answers: who changed what, when, and why.

**Audit Trail Requirements by Data Category:**

| Data Category | Minimum Audit Requirement | Retention |
|---|---|---|
| Milestone Scheduled Date changes | Action log: who changed, old value, new value, reason | Program lifetime |
| Risk Score changes | Action log with old/new Likelihood and Impact | Program lifetime |
| Funding figures (Authorized, Obligated) | System log + GFEBS extract reconciliation log | 7 years (financial records) |
| SITREP certification | PM digital signature equivalent (Action with EDIPI capture) | 2 years |
| Access control changes | Admin action log | 2 years |
| Personnel Billet changes | Action log with old/new values | Program lifetime |

**Foundry Audit Implementation:**

Foundry's Object Type history feature tracks all property changes with timestamp and user information. This is the primary audit trail for Object Type data. Verify that Foundry Object history is enabled on all sensitive Object Types. For financial data, configure an additional audit log pipeline that writes all Funding Line changes to a separate, restricted audit dataset.

---

### 9-4. Data Stewardship Responsibilities

The PM is the data steward for the PM tracking system. Data stewardship responsibilities are defined by the Army CIO Data Stewardship Policy (April 2, 2024) and UDRA v1.1.

**PM Data Steward Responsibilities:**

| Responsibility | Cadence | Action |
|---|---|---|
| Data quality review | Weekly (before SITREP) | Review Object Type data for completeness, accuracy, and timeliness. Flag stale records. |
| Access control review | Quarterly | Review and certify user access list. Remove departed personnel. Add new team members. |
| Object Type schema review | Quarterly | Review whether current Object Types still match program needs. Document any required changes. |
| Pipeline health check | Weekly | Verify all scheduled pipelines ran successfully. Investigate and resolve any failures. |
| Downstream consumer survey | Quarterly | Contact dashboard consumers. Collect feedback on accuracy and usability. |
| Governance documentation update | At each structural change | Update README dataset, data dictionary, and lineage documentation when any structural change is made. |
| C2DAO coordination | Before any shared OT change | Coordinate with C2DAO before any change to Object Types that are shared with other programs or enterprise ontology. |

---

### 9-5. Change Management for PM Systems

PM systems change as programs evolve. A well-designed change management process prevents uncoordinated changes from corrupting production data.

**Change Categories and Approval Authority:**

| Change Type | Examples | Approval Required | Process |
|---|---|---|---|
| Minor property addition | Adding an optional text field to an existing OT | PM approval | Implement in dev branch, test, publish |
| Required property change | Changing enum values, renaming existing property | PM + C2DAO coordination | Design review, impact assessment, change notification to users, 48-hr notice before implementation |
| New Object Type | Adding a new entity to the tracking system | PM + C2DAO | Full design review per Chapter 2 methodology |
| Pipeline logic change | Modifying SITREP aggregation logic | PM + pipeline owner | Test in non-production environment, spot-check output, 24-hr notice to downstream consumers |
| Access control change | Adding or removing roles | PM + security officer review | Document change, update access matrix |
| Decommission Object Type | Retiring an unused Object Type | PM + C2DAO | Archive data, update lineage, notify all consumers, 30-day notice |

> **CAUTION: Never modify a production Object Type schema or pipeline logic without testing in a development branch first. Foundry branching is available for this purpose. A schema change deployed directly to production without testing can corrupt all downstream applications and reports in the program's data stack simultaneously.**

---

### 9-6. Sustainment Planning

PM systems require a sustainment plan from the day they are published. People rotate. Programs evolve. Technology changes. A system with no sustainment plan becomes unmaintainable within one PCS cycle.

**PM System Sustainment Plan — Required Elements:**

1. **System Owner.** Named individual responsible for the system. Updated whenever the PM rotates. Succession plan: who assumes ownership on PCS/separation?
2. **Technical Point of Contact (TPOC).** TM-40D qualified individual responsible for technical maintenance. Must not be the same person as system owner — single point of failure risk.
3. **User Documentation.** Workshop user guide (how to use the dashboard), data entry guide (how to update milestones, risks, resources), and pipeline documentation (what runs when, what to do if it fails).
4. **Quarterly Review.** Scheduled quarterly governance review: data quality, access control, schema currency, consumer feedback, pipeline health.
5. **Training Plan.** How are new users trained on the system? Minimum: one structured onboarding session per new user. Recommended: document onboarding checklist in the system README.
6. **Data Archive Plan.** What happens to system data when the program closes? Define data retention, archival procedures, and who is responsible for closeout actions.
7. **Dependency Documentation.** What enterprise feeds does the system depend on? (GCSS-Army, GFEBS, IPPS-A feeds.) Who is the C2DAO contact for each? What is the process if a feed goes down?

---

### 9-7. Task: Conduct PM System Governance Review

**CONDITIONS:** PM system is in production with at least one full reporting cycle complete. Access control matrix is documented. All pipeline schedules are configured and running.

**STANDARDS:** Governance review produces a written summary covering: data quality findings, access control currency, pipeline health status, consumer feedback, and outstanding change requests. Review completed within 30 days of system going to production, then quarterly thereafter.

**EQUIPMENT:** MSS admin access, access control documentation, pipeline health dashboard, consumer feedback (collected via survey or direct contact).

**PROCEDURE:**

1. Pull the full user access list from the Foundry project folder. Cross-reference against current assigned personnel roster. Identify any accounts for personnel who have PCS'd, separated, or changed roles.
2. Remove or modify access for all personnel identified in step 1. Document changes in access control log.
3. Review pipeline run history for all scheduled pipelines. Identify any failures or partial runs. Investigate root cause for any failures.
4. Open all Object Types. Review record completeness. Flag records where required properties are null. Contact responsible data owners for updates.
5. Check Stale Risk flags. Contact Risk Owners for all risks where Days Since Review > 30.
6. Check Action Item Days Overdue. Escalate any action items overdue > 14 days to PM for direct follow-up.
7. Review the access control matrix against current program requirements. Are current roles still appropriate? Are any roles needed that do not yet exist?
8. Contact at least two dashboard consumers and collect feedback. Document feedback.
9. Review outstanding change requests. Prioritize. Schedule implementation for approved changes.
10. Produce written governance review summary. Distribute to PM and chain of command as appropriate.
11. Schedule next quarterly review.

---

## APPENDIX A — PM SYSTEM DESIGN CHECKLIST

Use this checklist before beginning any PM system build on MSS. The checklist is also the acceptance criteria for system sign-off before production publication.

### A-1. Pre-Build Design Checklist

**Program Scope:**
- [ ] Program charter reviewed and understood
- [ ] All trackable entities identified and mapped to Object Types
- [ ] All reporting requirements identified (SITREP, LOGREP, PERSTAT, USR, other)
- [ ] Reporting frequencies and consumers documented

**Object Type Design:**
- [ ] All required Object Types defined per Chapter 2 standard model
- [ ] All required properties defined for each Object Type
- [ ] Computed properties identified and formulas documented
- [ ] All Link Types defined with cardinality
- [ ] Data authority defined for each property (authoritative source system or manual entry)
- [ ] Reporting property mapping completed (para 2-4)

**Governance Pre-Build:**
- [ ] Domain ownership identified (who is the data domain owner for each OT?)
- [ ] C2DAO coordination completed for any shared enterprise OT domains
- [ ] Access control matrix drafted
- [ ] Data classification reviewed (any CUI/sensitive data? Security officer consulted?)
- [ ] System Owner and TPOC designated

### A-2. Build Completion Checklist

**Object Types:**
- [ ] All Object Types published in correct project folder
- [ ] All required properties present on each OT
- [ ] All computed properties producing correct values (spot-checked against manual calculation)
- [ ] All Link Types functional (traverse links from at least 3 objects to verify)

**Workshop Dashboards:**
- [ ] Milestone tracking dashboard (Chapter 3) built and validated
- [ ] Resource dashboard (Chapter 4) built and validated
- [ ] Risk Register dashboard (Chapter 5) built and validated
- [ ] Senior Leader dashboard (Chapter 7) built and validated
- [ ] Brief-ready configuration checklist (para 7-5) completed

**Pipelines:**
- [ ] SITREP pipeline built, scheduled, and tested (Chapter 6)
- [ ] LOGREP pipeline built, scheduled, and tested (if applicable)
- [ ] PERSTAT pipeline built, scheduled, and tested (if applicable)
- [ ] All pipelines have failure notification configured

**Governance:**
- [ ] Access control implemented per matrix
- [ ] Audit trail enabled on sensitive Object Types
- [ ] Data stewardship responsibilities documented and assigned
- [ ] Sustainment plan completed
- [ ] User documentation written
- [ ] System README dataset created with: description, data dictionary, lineage notes, contact information

### A-3. Pre-Production Sign-Off

Before publishing to production, the following must be complete:
- [ ] PM validation: data accuracy confirmed against source records
- [ ] Consumer validation: at least one designated dashboard consumer has reviewed and accepted the dashboard
- [ ] Security review: classification and access control confirmed
- [ ] C2DAO notification: C2DAO notified of new production system
- [ ] UDRA compliance: VAUTI criteria checklist completed (Visible, Accessible, Understandable, Trustable, Interoperable)

---

## APPENDIX B — ARMY REPORTING REQUIREMENTS CROSS-REFERENCE

### B-1. SITREP (Situation Report)

| Element | Doctrinal Reference | MSS Source | Update Cadence |
|---|---|---|---|
| Unit / Program Status | FM 6-0 | Program Object Type: `program_status` | Weekly |
| Current Operations Summary | FM 6-0 | PM manual input via Workshop Action | Weekly |
| Significant Activities | FM 6-0 | PM manual input | Weekly |
| Personnel Status (brief) | FM 6-0 | PERSTAT pipeline output | Weekly |
| Equipment Status (brief) | FM 6-0 | LOGREP pipeline output | Weekly |
| Logistics Status | ADP 4-0 | Resource Line Object Type | Weekly |
| Risk Summary | FM 6-0 | Risk Object Type aggregation | Weekly |
| Next Period Actions | FM 6-0 | Action Item Object Type (upcoming) | Weekly |

### B-2. LOGREP / LOGSTAT

| Element | Doctrinal Reference | MSS Source | Update Cadence |
|---|---|---|---|
| Equipment on hand | ADP 4-0, GCSS-Army | Equipment Object Type | Daily / on demand |
| FMC/PMC/NMC rates | DA Pam 750-8 | Equipment Object Type: `readiness_status` | Daily |
| Supply fill rates | ADP 4-0 | Supply Line Object Type (if tracked) | Weekly |
| Class IX demand | GCSS-Army | GCSS-Army enterprise feed | On demand |
| Maintenance due | DA Pam 750-8 | Equipment Object Type: `maintenance_due_date` | Weekly |

### B-3. PERSTAT (Personnel Status)

| Element | Doctrinal Reference | MSS Source | Update Cadence |
|---|---|---|---|
| Authorized strength | AR 600-8-105 | Personnel Billet Object Type: count | Daily |
| Assigned strength | AR 600-8-105 | Personnel Object Type: count assigned | Daily |
| Present for duty | AR 600-8-105 | Personnel Object Type: duty status filter | Daily |
| Absent (TDY/Leave/Other) | AR 600-8-105 | Personnel Object Type: absence category | Daily |
| Vacancy breakdown | AR 600-8-105 | Personnel Billet: Fill Status = Vacant | Daily |

### B-4. USR (Unit Status Report)

| Element | Doctrinal Reference | MSS Source | Update Cadence |
|---|---|---|---|
| S1 (Personnel) | AR 220-1 | PERSTAT pipeline output | Monthly |
| S2 (Equipment/Fill Rate) | AR 220-1 | Equipment Object Type aggregation | Monthly |
| S3 (Training) | AR 220-1 | Training Milestone Object Type (if tracked) | Monthly |
| S4 (Supply/Maintenance) | AR 220-1 | LOGREP pipeline output | Monthly |
| Overall Rating | AR 220-1 | Computed from S1–S4 inputs | Monthly |

> **NOTE:** USR computation rules (S-category rating thresholds, overall rating algorithm) are defined in AR 220-1. Do not implement custom rating logic — implement the AR 220-1 algorithm exactly. Any deviation constitutes a materially false report. If in doubt, coordinate with the unit S1/G1 before implementing USR logic.

### B-5. Risk Register (No Standard Army Form — Best Practice)

Risk registers are not prescribed by a specific Army form, but are required by Army audit policy and command risk management doctrine (AR 11-2 Managers' Internal Control Program). The MSS risk register constitutes the program's risk management record. Ensure:

- All risks are documented before submission of any external program status report.
- Risk register is reviewed at each formal program review.
- Critical risks are escalated to command per para 5-5 escalation policy.
- Risk register is retained for the life of the program and for the prescribed records retention period after closeout.

---

## APPENDIX C — DASHBOARD DESIGN STANDARDS FOR SENIOR LEADERS

### C-1. Visual Design Standards

**Color Standards:**

| Use | Color | Hex Code |
|---|---|---|
| Status GREEN | Army Green | #4CAF50 |
| Status AMBER | Army Amber | #FF9800 |
| Status RED | Army Red | #F44336 |
| Status BLUE (Complete) | Neutral Blue | #2196F3 |
| Status GREY (N/A or Future) | Light Grey | #9E9E9E |
| Background | White | #FFFFFF |
| Primary text | Near-black | #212121 |
| Secondary text | Medium grey | #616161 |
| Table alternating row | Light grey | #F5F5F5 |

> **NOTE:** Do not use Army green (#4B5320 / OD Green) for status indicators. It is visually similar to amber when projected. Use the hex codes above, which are optimized for both screen and projector display.

**Typography Standards:**

| Element | Size | Weight |
|---|---|---|
| KPI tile status label | 28pt minimum | Bold |
| KPI tile value | 36pt minimum | Bold |
| Page title | 20pt | Bold |
| Section header | 16pt | Bold |
| Table header | 12pt | Bold |
| Table cell | 11pt | Regular |
| Footer / data-as-of | 10pt | Regular, italic |

### C-2. Layout Standards

**KPI Tiles:**
- Minimum height: 120px
- Display order (left to right): Overall Status, Schedule, Risk, Budget
- Each tile: Status label (top), value or count (center, large), trend indicator (bottom right, optional)
- Tile background: white with colored left border (5px, status color) OR solid status color tile

**Tables:**
- Maximum columns visible without horizontal scroll: 8
- Always include a "Last Updated" column
- Default sort: by status severity (Critical/RED first) or by date (soonest first)
- Alternate row shading: #F5F5F5 for even rows
- No column headers that require abbreviation to fit — resize columns or reduce column count

**Charts:**
- Timeline charts: baseline date shown as solid line, forecast as dashed line
- Bar charts: horizontal bars preferred over vertical for long labels
- No 3D chart styles — they distort values and are unreadable at distance
- All chart axes labeled with units
- All charts include a legend if more than one data series

### C-3. What Not to Include on Senior Leader Dashboards

The following elements degrade senior leader dashboard quality and must be excluded:

| Element | Reason |
|---|---|
| Decorative images, logos, clip art | Add cognitive load, waste screen space |
| Animated elements | Distracting, can cause display issues during brief |
| Dense prose blocks | Commanders do not read paragraphs on dashboards |
| More than 5 items in any list | If more than 5, create a drill-down page |
| Unexplained acronyms | Define on first use or in a visible legend |
| Data with no source attribution | Every figure needs a "Data as of [date]" anchor |
| Trend charts with fewer than 3 data points | Trends require data; 2 points is a line, not a trend |
| Raw IDs or system codes in primary display | Show human-readable names; IDs belong in drill-down |
| Grids or tables with more than 10 rows | Paginate or filter; commanders do not scroll |

---

## GLOSSARY

**Action (Foundry)** — A configured workflow in Foundry Ontology that allows users to create, edit, or update Object properties through a defined form interface. PM systems use Actions as the primary data update mechanism.

**Action Item** — A task assigned to a specific individual with a due date and completion criteria. Tracked as an Object Type in MSS PM systems.

**ADP 4-0** — Army Doctrine Publication 4-0, Sustainment. Doctrinal reference for logistics reporting (LOGREP, LOGSTAT) context.

**AIP Logic** — Palantir's AI workflow configuration tool within Foundry. Used in TM-40D for automated escalation notifications, anomaly detection alerts, and AI-assisted report generation.

**ASAT** — Automated Status and Accountability Tool. Army system for personnel accountability; PERSTAT data may originate from ASAT.

**Audit Trail** — A chronological record of all changes to a dataset or Object, including who made the change, when, and what the old and new values were. Required for financial and personnel data in PM systems.

**Baseline Schedule** — The approved project schedule with locked milestone dates used as the reference point for schedule variance calculation. Never modified without a formal rebaseline action.

**Billet** — An authorized position on a unit's Table of Distribution and Allowances (TDA) or Table of Organization and Equipment (TOE). Tracked in the Personnel Billet Object Type.

**C2DAO** — Command and Control Data Architecture Office. USAREUR-AF's data architecture governance authority. All shared Object Type changes and new shared data products require C2DAO coordination.

**Commander's Dashboard** — The Workshop application designed for senior leader consumption, optimized for brief-readiness and immediate status comprehension.

**Computed Property** — An Object Type property whose value is automatically derived from other properties (e.g., Schedule Variance = Forecast Date − Scheduled Date). Implemented via Functions on Objects (TypeScript, -40B) or pipeline transform.

**Contour** — Foundry's analytical workbench for pivot analysis, aggregation, trend analysis, and cross-dataset comparison. Primary tool for portfolio-level PM analysis.

**Contract Object Type** — MSS Object Type representing a contract action, tracking period of performance, value, obligation, COTR, and expiration status.

**CUI** — Controlled Unclassified Information. Designation for sensitive but unclassified information requiring specific handling. Budget data and personnel data in PM systems may carry CUI designation.

**Data Steward** — Individual responsible for the quality, accuracy, and governance of a specific data domain or dataset. The PM is the data steward for the PM tracking system.

**DTG** — Date-Time Group. Standard military time expression format (e.g., 111200ZMAR26). Used in SITREP and all automated reporting products.

**EDIPI** — Electronic Data Interchange Personal Identifier. DoD-standard unique identifier for individuals. Use EDIPI rather than names in system properties wherever possible to reduce PII exposure and enable cross-system linking.

**Escalation Flag** — A Boolean property on Risk or Action Item objects that triggers elevated visibility when automated threshold conditions are met.

**FM 6-0** — Field Manual 6-0, Commander and Staff Organization and Operations. Primary doctrinal reference for SITREP structure and staff reporting requirements.

**Foundry** — Palantir Foundry. The underlying platform for MSS. All MSS data products are built on Foundry infrastructure.

**GFEBS** — General Fund Enterprise Business System. Army financial management system. The authoritative source for obligation and expenditure data in PM funding tracking.

**GCSS-Army** — Global Combat Support System-Army. Army logistics information system. Authoritative source for equipment status and supply data in LOGREP tracking.

**Health Score** — A computed 0–100 composite score representing the overall health of a Program object, derived from weighted contributions of schedule, risk, budget, and personnel status.

**Idempotent Pipeline** — A data pipeline that produces the same correct output regardless of how many times it is run. PM reporting pipelines must be idempotent to support reruns without data corruption.

**IPPS-A** — Integrated Personnel and Pay System-Army. Army human resources system. Authoritative source for personnel data in PERSTAT tracking.

**Issue** — A risk that has been realized (has actually occurred and is causing program impact). Tracked separately from Risks in MSS PM systems.

**KPI** — Key Performance Indicator. Summarized metric displayed prominently in dashboard tiles for rapid status assessment.

**LOGREP** — Logistics Report. Standard Army report on equipment, supply, and logistics status. Required for sustainment programs.

**Link Type** — A defined relationship between two Object Types in Foundry Ontology. PM systems use Link Types to connect Programs to Milestones, Milestones to Risks, etc.

**Milestone** — A key program event with a defined date, completion criteria, and authority. The primary unit of schedule tracking in PM systems.

**MSS** — Maven Smart System. USAREUR-AF's enterprise AI/data platform, built on Palantir Foundry.

**Object Type** — A defined entity class in Foundry Ontology. PM systems define Object Types for Programs, Milestones, Risks, Resources, Personnel, and other trackable entities.

**Obligation Rate** — The percentage of authorized funding that has been legally committed (obligated) to date. Key financial health indicator for PM systems.

**Ontology** — Foundry's semantic data layer. The collection of Object Types, Link Types, and Actions that represent real-world entities and their relationships on MSS.

**OPDATA** — Operational Data. Umbrella term for data generated by and required for military operations. PM tracking data is a category of OPDATA.

**PERSTAT** — Personnel Status Report. Daily Army report on unit strength and duty status.

**Pipeline Builder** — Foundry's visual data pipeline design tool. Used for building scheduled transforms that generate PM reporting outputs.

**Portfolio** — A collection of related programs managed by a senior PM or G-staff officer. Portfolio analysis aggregates data across multiple programs.

**Program Manager (PM)** — Individual assigned responsibility for a specific program, with authority and accountability for program execution, reporting, and resource management.

**Rebaseline** — Formal process of resetting the baseline schedule dates for a program, typically requiring approval authority action. Must be tracked as a distinct event in the PM system, not a silent overwrite.

**Risk Register** — Structured record of all identified risks for a program, including likelihood, impact, scoring, mitigation status, and ownership.

**Schedule Variance (SV)** — The difference in days between a milestone's forecasted completion date and its baseline scheduled date. Positive SV indicates delay.

**SITREP** — Situation Report. Standard Army report on current status, significant activities, and near-term operations.

**TDA** — Table of Distribution and Allowances. Document defining authorized positions for a unit. Personnel Billet Object Types should align to TDA structure.

**UDRA** — Unified Data Reference Architecture. Army's federated data architecture framework, v1.1 published February 2025. Governs all MSS data product design.

**USR** — Unit Status Report. Monthly report on unit readiness across personnel, equipment, training, and supply categories, per AR 220-1.

**VAUTI** — Visible, Accessible, Understandable, Trustable, Interoperable. The five data quality criteria from DoD Data Strategy (2020). All MSS PM data products must meet VAUTI standards.

**Workshop** — Foundry's no-code application builder. Primary tool for PM dashboard and tracking application construction in TM-40D.

---

*TM-40D — Program Manager Technical Manual*
*Headquarters, United States Army Europe and Africa*
*Wiesbaden, Germany — 2026*
*DISTRIBUTION RESTRICTION: Approved for public release; distribution is unlimited.*

*For questions and corrections, contact the USAREUR-AF C2DAO at Wiesbaden.*
*Reference: learn-data.armydev.com*
