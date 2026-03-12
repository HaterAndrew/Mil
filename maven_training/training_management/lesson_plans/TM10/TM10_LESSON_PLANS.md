# LESSON PLANS — TM-10 MAVEN USER
## Maven Smart System (MSS) Training Program
### USAREUR-AF Operational Data Team — C2DAO

**Course:** TM-10 — Maven User
**Course Duration:** 1 day (8 hours)
**All 9 lesson plans contained in this file.**

---

# BLOCK 1 — MSS OVERVIEW AND DATA LITERACY FUNDAMENTALS

| Field | Value |
|---|---|
| **Course** | TM-10 Maven User |
| **Lesson Title** | MSS Overview and Data Literacy Fundamentals |
| **Block Number** | Block 1 |
| **POI Reference** | TM-10 Block 1 |
| **Hours** | 1.0 |
| **Method** | Lecture |
| **Time** | 0800–0900 |
| **Version** | 1.0 — March 2026 |

## Purpose

This block establishes why MSS exists, what it replaces, and what the trainee's relationship to it is. Before trainees touch the keyboard, they need a mental model: MSS is not a website — it is a platform with a data model, access controls, and governance. This block prevents the first-day confusion that comes from trainees treating Foundry like SharePoint or a reporting portal.

## Learning Objectives

**TLO:** Given an overview of the MSS platform, the trainee will correctly describe the purpose of MSS, its relationship to USAREUR-AF operational requirements, and the roles defined in the training progression — without reference to notes — to the satisfaction of the evaluator.

| # | ELO | Assessment |
|---|---|---|
| 1 | State what MSS replaces in the unit data workflow (manually updated PowerPoints, emailed spreadsheets, stovepiped reporting) | Verbal check on learning |
| 2 | Describe the four-tier training progression and state which tier applies to them | Verbal check on learning |
| 3 | Identify three USAREUR-AF use cases for MSS (readiness tracking, logistics, SITREP, personnel accountability) | Verbal check on learning |
| 4 | State the difference between consuming a data product (TM-10) and building one (TM-20+) | Verbal check on learning |

## Resources

**Instructor:** TM-10 presentation slides, Block 1 deck; Data Literacy Technical Reference Chapter 1 (supporting reference)
**Student:** TM-10, Chapter 1 (pre-read, should be complete)
**Aids:** Projector; MSS screenshots embedded in slides (no live demo this block)

## Safety and Security

No live system interaction this block. No data handling risks. The instructor should emphasize during this block that the production MSS environment is never used for training — all labs are in the Training Environment.

## Introduction

**ATTENTION:** "How many people here have updated a slide deck the night before a brief because the data changed? Or gotten a spreadsheet emailed from three different people with three different numbers? That is the problem MSS solves. After today you will never need to ask someone to send you the current readiness data — it is live, it is always current, and it is in MSS."

**MOTIVATION:** Every Soldier on the data team uses MSS. Your S3, your G4, your commander — they are reading dashboards that someone built on this platform. After today you can navigate those dashboards, execute authorized actions on the data, and handle a data export without accidentally violating classification procedures. These are not optional skills — they are required to do your job on this team.

**OVERVIEW:**
1. What MSS is and what it replaced in the unit workflow (10 min)
2. The Foundry data model: datasets → pipelines → Ontology → applications (15 min)
3. USAREUR-AF use cases — what is running on MSS right now (15 min)
4. Training progression: TM-10 through TM-40, and where you are (10 min)
5. Check on learning and transition to Block 2 (10 min)

## Body

### Sub-Topic 1: What MSS Is — 10 minutes

**Instructor Notes:**
Lead with the operational problem, not the technology. MSS exists because units were managing operational data through emailed Excel files, manually updated PowerPoint slides, and informal tracking systems that only one person understood. When that person PCSed, the data went with them.

MSS centralizes operational data on a governed platform. It is not a website or a reporting tool — it is a data platform with a structured data model, access controls, pipelines, and applications built on top of shared data. The analogy that works for most trainees: MSS is to operational data what a COP is to a common operational picture. Everyone sees the same data, it is authoritative, and changes are visible to everyone with access.

Reference Slide 2 (What is MSS diagram). Walk through: data sources → ingestion → Ontology → applications layer.

**Student Activity:** Trainees listen and take notes. Ask them to note what tool or process in their own unit they believe MSS would replace. This becomes a discussion prompt.

**Check on Learning:**
- Q: "What is the primary problem MSS is designed to solve?"
- A: Fragmented, non-authoritative data management — multiple versions of truth, manual updates, knowledge walking out with personnel.
- If unclear: Return to the "version of truth" framing. The key insight is single source of truth + live data.

---

### Sub-Topic 2: The Foundry Data Model — 15 minutes

**Instructor Notes:**
Trainees do not need to understand Foundry architecture deeply at TM-10 — but they need a mental model that prevents confusion during labs. Introduce the four layers:

1. **Datasets** — raw data ingested into Foundry (CSV, Excel, database feeds). The raw material.
2. **Pipelines** — transforms that clean, join, and compute on datasets. The manufacturing step.
3. **Ontology** — the semantic layer. Datasets become Objects (Equipment, Unit, Personnel) with properties. This is what makes MSS "smart" — data has meaning, not just rows and columns.
4. **Applications** — Workshop apps, Contour analyses, Quiver views built on top of the Ontology. What the user sees.

TM-10 trainees only interact with layer 4 (applications) and occasionally layer 3 (Quiver). They do not build layers 1-3 in this course.

Reference Slide 3 (Four Layers diagram). Use the analogy: datasets are the raw intel reports; the pipeline is the intel analyst who processes them; the Ontology is the common operational picture; applications are the brief.

**Student Activity:** Trainees sketch the four layers from memory on paper. 2-minute exercise.

**Check on Learning:**
- Q: "In which layer would you find a live status update that an S3 NCO just submitted?"
- A: Ontology layer (it is a property of an Object, updated via an Action).
- If unclear: Emphasize that the Ontology is where meaning lives. The Action updated an Object property, which is in the Ontology.

---

### Sub-Topic 3: USAREUR-AF Use Cases — 15 minutes

**Instructor Notes:**
Make it real. Describe three to five actual categories of data products running on USAREUR-AF MSS. Do not describe classified products by name — use categories:

- **Unit readiness tracking:** Equipment C-ratings by unit, personnel fill rates, maintenance status dashboards refreshed on schedule.
- **SITREP management:** Structured SITREP submissions via Workshop applications replacing emailed and faxed reports. S3 shops can see submission status across the formation.
- **Logistics:** Class IX consumption tracking, stockage-level visibility, depot shipment status. G4 dashboards showing obligation rates.
- **Personnel accountability:** Roll-up of personnel status by unit, deployment tracking, skills inventory.

Reference Slides 4–5 (use case examples — screenshots of anonymized Training Environment examples).

Ask trainees which of these categories their unit needs. This activates prior experience and builds motivation.

**Student Activity:** Quick show of hands — which of these categories is relevant to your section? (Note the spread — makes clear this is not theoretical.)

**Check on Learning:**
- Q: "If an S4 NCO wanted to see real-time Class IX consumption without emailing anyone, which layer of MSS would they interact with?"
- A: Applications layer (a Workshop dashboard or Quiver view built on logistics data).

---

### Sub-Topic 4: Training Progression — 10 minutes

**Instructor Notes:**
Explain the progression clearly. Reference POI Course Summary table.

- **TM-10 (this course):** All personnel. Consume data products, execute authorized actions, handle exports. No building.
- **TM-20:** All staff who need to build data products. Visual, no code.
- **TM-30:** Data-adjacent specialists (17/25-series, S6, G2/G9). Advanced building, Ontology design, analytics.
- **TM-40A–F:** Role-specific specialist tracks for ORSA, AI engineers, ML engineers, PMs, KMs, and software engineers.

Emphasize: TM-10 is the foundation for all higher training. There are no waivers. Senior personnel sometimes push back on this — have a clear, brief response: "The evaluation confirms you can navigate MSS and handle classification procedures correctly. Passing TM-10 is required for TM-20 enrollment. There are no exceptions."

**Student Activity:** Each trainee identifies on their copy of the syllabus which TM level is their likely terminal level based on their role.

**Check on Learning:**
- Q: "An S3 NCO who will maintain the unit SITREP tracker and add new fields to the Workshop application — which TM level do they need to complete?"
- A: TM-20 (Builder). Workshop application maintenance requires the Builder skill set.

## Summary

**SUMMARY:**
- MSS is a data platform — not a reporting tool. It provides a single source of truth for operational data.
- The four layers are datasets, pipelines, Ontology, and applications. TM-10 users work in applications.
- Real USAREUR-AF data products — readiness, SITREPs, logistics, personnel — run on MSS.
- Your training level determines what you can do: TM-10 = consume and act on data; TM-20+ = build.

**REMOTIVATION:** You are about to log in to the platform that your unit S3, G4, and commander use to make decisions. After the next eight blocks today, you will be able to navigate it, use it, and handle its data correctly. This is not classroom theory — this is the operational tool.

**CLOSE:** Next block, you will log in for the first time. Know your PIV PIN before we start — if you don't know it, figure it out right now during the 5-minute break. We will not wait for PIN resets in Block 2.

## Assessment

This block is assessed through verbal check on learning questions during the lesson and by evaluator observation during Block 9 (Practical Exercise). No separate Block 1 evaluation.

## Assignment

No assignment — this is Block 1 of a 1-day course. Students should ensure TM-10 Chapter 1 is reviewed during the lunch break if not pre-read.

---

---

# BLOCK 2 — LOGIN AND NAVIGATION

| Field | Value |
|---|---|
| **Block Number** | Block 2 |
| **Hours** | 1.0 |
| **Method** | Lab |
| **Time** | 0900–1000 |

## Purpose

Login failure is the most common Day 1 delay. This block ensures every trainee has successfully authenticated via CAC, navigated to their unit's training project, and can find the resources they will use all day. A trainee who cannot log in cannot participate in any subsequent lab.

## Learning Objectives

**TLO:** Given an MSS-connected workstation with CAC reader, the trainee will successfully authenticate to the MSS Training Environment, navigate to the designated unit project, and locate specified resources using the navigation tools — to standard, without instructor assistance.

| # | ELO | Assessment |
|---|---|---|
| 1 | Authenticate via CAC + PIV PIN and confirm Training Environment access | Evaluator observation (Block 9) |
| 2 | Navigate the left-side navigation panel to locate a named project | Evaluator observation (Block 9) |
| 3 | Use Compass to search for a named dataset | Check on learning |
| 4 | Explain the difference between the Navigation Panel (Projects) and Compass (search) | Verbal check |

## Resources

**Instructor:** TM-10 Block 2 slides; instructor account in Training Environment; printed or digital TM-10 Chapter 2
**Student:** Workstation with CAC reader; network access to MSS Training Environment; TM-10 Chapter 2
**Datasets:** Training Environment pre-configured with unit training project

## Safety and Security

First live interaction with the system. Emphasize before the lab:
- Training Environment only — the URL should be the Training Environment URL, not production
- Do not navigate to production MSS if they have previously accessed it on this workstation
- If they accidentally see what appears to be real operational data, stop immediately and notify the instructor

## Introduction

**ATTENTION:** "If you don't know your PIV PIN, there is nothing we can do in this block. If that applies to you, see me now so we can figure out a plan. The rest of the class is moving forward in 60 seconds."

**MOTIVATION:** You will log into MSS before every brief, every morning when you check unit status, and every time you need to submit a status update. This needs to be automatic. By the end of this block, you will have done it three times.

**OVERVIEW:** Log in, navigate, explore. Three repetitions, each on a different scenario.

## Body

### Sub-Topic 1: CAC Authentication — 15 minutes

**Instructor Notes:**
Instructor authenticates live on the projector — walk through each step as you do it.

Steps:
1. Open browser (confirm MSS Training Environment URL — display on projector)
2. Insert CAC if not already in reader
3. Navigate to MSS URL
4. Select CAC certificate (correct certificate is government-issued; students should select the PIV Authentication certificate, not the email signing cert)
5. Enter PIV PIN when prompted
6. Confirm Training Environment landing page is displayed

Common failure: student selects the wrong certificate. Walk through certificate selection slowly.

**Student Activity:** All trainees attempt login simultaneously. Instructor walks the room. Students who succeed hold — wait for the group.

**Check on Learning:**
- Q: "If you get a 403 Forbidden error after successfully entering your PIV PIN, what does that mean and what do you do?"
- A: 403 = access exists but permissions are wrong. Not a login failure. Action: contact unit MSS Administrator for access provisioning. Do not retry login repeatedly.

---

### Sub-Topic 2: Navigation Panel and Projects — 20 minutes

**Instructor Notes:**
Once logged in, orient trainees to the interface. Cover:
- Left navigation panel: Home, Projects, Compass, Applications (Workshop), Contour, Quiver
- How to find a specific project by name using the Projects navigation
- Folder structure within a project: Datasets, Pipelines, Ontology, Applications

Instructor demo: navigate to the TM-10 Training Project. Show the folder structure. Open the README file if one exists.

Students will see their training project is pre-loaded with synthetic data. They should not modify anything in this block — just navigate.

**Student Activity:** Each trainee navigates to the TM-10 Training Project, finds the Datasets folder, counts how many datasets are present, and notes the name of the first dataset alphabetically. They will confirm this with the instructor.

**Check on Learning:**
- Q: "What is the difference between Projects and Compass in the left navigation?"
- A: Projects shows projects you have access to, organized hierarchically. Compass is a search tool across all resources you have access to — good for finding a dataset by name when you don't know which project it lives in.

---

### Sub-Topic 3: Compass Search — 15 minutes

**Instructor Notes:**
Compass is the "find anything" tool. Walk through:
- Opening Compass (Cmd+K or left nav Compass icon)
- Searching by resource name
- Filtering by resource type (Dataset, Object Type, Workshop Application)
- Opening a resource directly from Compass results

Important nuance: Compass only returns resources the trainee has access to. If they search for something and it doesn't appear, it's either named differently or they don't have access to it.

**Student Activity:** Trainees use Compass to find a named dataset ("SITREP_Training_Q1") and open it. Confirm they can see the dataset schema.

**Check on Learning:**
- Q: "You're looking for a Workshop application called 'Unit Readiness Dashboard' but you can't find it in your Projects. What tool do you use and what might be the reason you can't find it?"
- A: Compass. If it doesn't appear, either the application is in a project you don't have access to (ask unit MSS Administrator) or it's named differently.

---

### Sub-Topic 4: Second Repetition — 10 minutes

**Instructor Notes:**
Have trainees log out and log back in. This confirms the login process is internalized, not just completed once with instructor walking them through it. Students who struggled in Sub-Topic 1 should log in and navigate to the training project a second time without assistance.

**Student Activity:** Log out. Log back in. Navigate to training project. Confirm.

## Summary

**SUMMARY:**
- CAC + PIV PIN authentication — you should be able to do this without thinking
- Navigation Panel for projects you own/have access to; Compass for searching across all resources
- 403 = permissions issue, not a login failure; contact MSS Administrator, not IT helpdesk
- The Training Environment is your workspace today — do not navigate to production MSS

**CLOSE:** Next, we're going into Workshop — the application layer where most of your daily use of MSS will happen.

## Assessment

Assessed in Block 9 (Practical Exercise): Login and navigate to designated application (Task 1).

## Assignment

N/A (1-day course).

---

---

# BLOCK 3 — WORKSHOP APPLICATIONS

| Field | Value |
|---|---|
| **Block Number** | Block 3 |
| **Hours** | 1.0 |
| **Method** | Lab |
| **Time** | 1000–1100 |

## Purpose

Workshop is the primary interface most TM-10 trainees will use every day — it is how operational data products are surfaced to consumers. This block teaches the trainee to read, navigate, filter, and interpret a Workshop application so they can use what the unit data team has built.

## Learning Objectives

**TLO:** Given an operational Workshop application, the trainee will navigate between pages, apply table filters to locate specific records, interpret metric widgets, and describe how the data displayed connects to the Ontology layer — to standard, without reference to notes.

| # | ELO | Assessment |
|---|---|---|
| 1 | Navigate a multi-page Workshop application using the page navigation controls | Evaluator observation |
| 2 | Apply a table filter to reduce rows to a specified subset | Evaluated task (Practical Exercise Task 2) |
| 3 | Interpret a metric widget (describe what it shows and what it means operationally) | Check on learning |
| 4 | Distinguish between live data and a static screenshot of data | Verbal check |

## Resources

**Instructor:** TM-10 Block 3 slides; pre-built Training Workshop application with SITREP, readiness, and equipment data
**Student:** TM-10 Chapter 3; access to TM-10 Training Workshop Application
**Datasets/Apps:** Training Workshop Application pre-deployed in Training Environment with synthetic SITREP data

## Introduction

**ATTENTION:** "The S3's readiness dashboard is a Workshop application. The SITREP submission form your unit uses — that's a Workshop application. After this block, you can use them without someone walking you through it every time."

**MOTIVATION:** Workshop is what your commander sees. If you can't navigate it, you can't brief from it, you can't identify missing submissions, and you can't execute the status updates that maintain data accuracy. This is operational proficiency, not IT training.

## Body

### Sub-Topic 1: Workshop Interface Orientation — 15 minutes

**Instructor Notes:**
Open the pre-built Training Workshop Application. Walk through the interface:
- Page navigation (left sidebar or top tabs depending on application layout)
- Title bar and page description
- Widget types visible on the first page: table, metric, chart
- Application menu (top right) — settings visible to admin; not visible to standard Viewer

Point out: Workshop applications look different from each other — the builder designs the layout. There is no "standard" Workshop interface. What is standard is the widget behavior.

**Student Activity:** Trainees open the Training Workshop Application. Navigate to each page. Count how many pages exist. Note the page titles.

**Check on Learning:**
- Q: "Is the data in this Workshop application live or static?"
- A: Live — it is connected to the Ontology layer and refreshes as data changes. This is fundamentally different from a screenshot or an exported Excel file.

---

### Sub-Topic 2: Table Widgets and Filters — 25 minutes

**Instructor Notes:**
The table widget is the most common Workshop component. Cover:
- Clicking a column header to sort
- Using the filter controls (dropdowns, search boxes, date pickers) that the builder has configured
- Understanding that available filters are determined by the builder — a TM-10 user cannot add new filters that were not built in
- Selecting a row (object selection) — note that in some applications, selecting a row drives other widgets on the page

Lab step: find the SITREP submission table on the Submissions page. Apply a filter for "Last 7 Days" on the submission date column. Observe how the row count changes.

Common error: trainees try to type directly into a filter widget that only accepts dropdown selection. Clarify: the filter options depend on how the builder configured it — sometimes it is a dropdown, sometimes a search box.

**Student Activity:** Apply the "Last 7 Days" date filter. Identify how many SITREP submissions appear. Then clear the filter and note the total count. The difference is the number of submissions older than 7 days.

**Check on Learning:**
- Q: "You filter the SITREP table to last 7 days and see 12 submissions. Your unit has 15 subordinate elements. What does this tell you and what should you do?"
- A: Three elements have not submitted. You would look at which elements are missing (by filtering or scanning the Unit column) and follow up. MSS shows you the gap — the follow-up action is yours.

---

### Sub-Topic 3: Metric Widgets and Charts — 20 minutes

**Instructor Notes:**
Metric widgets show computed values: counts, sums, percentages, derived calculations. They are live — they recompute as the underlying Ontology data changes.

Walk through the metric widgets on the Readiness Summary page:
- "Total Units Reporting" — count of distinct unit objects with at least one readiness entry
- "C1 Equipment" — count or percentage
- "SITREP Compliance Rate" — derived calculation

Emphasize: metric widgets are as good as the data feeding them. If a unit hasn't submitted, the metric excludes them. "100% compliant" sometimes means "everyone who submitted is compliant" — not "all units submitted."

Charts (bar, line): same data source as tables. Changing a filter on the page may or may not affect the chart depending on how the builder connected them.

**Student Activity:** Read the Readiness Summary page metrics. Answer the check on learning questions using the displayed data.

**Check on Learning:**
- Q: "The C1 Equipment metric shows 87%. You need to brief this to the XO. What additional information do you need before you can use this number?"
- A: When was the data last updated? Which units have reported? Does this include all equipment types or a subset? The metric widget's label and the application documentation (if provided) should answer these — read it before briefing.

## Summary

**SUMMARY:**
- Workshop applications surface live Ontology data — not static reports
- Table filters let you narrow data to what you need; available filters are set by the builder
- Metric widgets show computed values that update as data changes
- Read the metric label carefully — understand what is included and when it was last computed

**CLOSE:** Tables and metrics let you read data. Next block: Actions, which let you write data — submit a status update, complete a form, record a change.

## Assessment

Assessed in Block 9 (Practical Exercise): filter table to last 7 days and identify missing submission (Task 2).

---

---

# BLOCK 4 — ACTIONS

| Field | Value |
|---|---|
| **Block Number** | Block 4 |
| **Hours** | 1.0 |
| **Method** | Lab |
| **Time** | 1100–1200 |

## Purpose

Actions are how authorized users write data back to the Ontology. An Action submits a status update, completes a form, records an event, or modifies an Object property. Most TM-10 trainees have exactly one or two Actions they are authorized to execute — this block teaches them to execute those correctly and understand what they are doing to the data.

## Learning Objectives

**TLO:** Given an authorized Action in an MSS Workshop application, the trainee will execute the Action correctly — providing required parameters, confirming the execution, and verifying the Ontology Object was updated — to standard, without instructor assistance.

| # | ELO | Assessment |
|---|---|---|
| 1 | Locate an Action button in a Workshop application | Evaluator observation |
| 2 | Execute an Action: complete the parameter form, confirm, and verify execution | Evaluated task (Practical Exercise Task 3) |
| 3 | Describe the result of executing an Action (what changed in the Ontology) | Check on learning |
| 4 | Explain why an Action may be grayed out or unavailable | Verbal check |

## Resources

**Instructor:** TM-10 Block 4 slides; Training Workshop Application with a pre-configured Action (UpdateSITREPStatus)
**Student:** TM-10 Chapter 4; access to Training Workshop Application

## Introduction

**ATTENTION:** "When you submit a SITREP through the unit's Workshop form, you are executing an Action. You just updated an Object in the Foundry Ontology. What the S3 sees on their dashboard changed in real time."

**MOTIVATION:** Actions are the feedback loop. Data products only stay accurate if authorized users update them. A readiness dashboard is only as good as the last Action executed by someone with your role.

## Body

### Sub-Topic 1: What Actions Are and How They Work — 15 minutes

**Instructor Notes:**
Actions are defined by the builder and authorized to specific roles. A TM-10 user can only execute Actions they are authorized for — they cannot create Actions or modify what an Action does.

Three things an Action typically does:
1. Presents a form with parameters (fields to fill in)
2. Validates the inputs (required fields, valid values)
3. Writes the result to one or more Object properties in the Ontology

Important: Actions are non-reversible in most configurations. There is no "undo." If you execute an Action with incorrect data, you need to execute the correction Action (if one exists) or contact the data steward.

Show the Action button location in the Training Workshop Application. Note: Action buttons may be labeled with operation names ("Submit SITREP", "Update Status", "Mark Complete") — not just "Action."

**Check on Learning:**
- Q: "An Action button is grayed out on your screen. What are two possible reasons?"
- A: (1) You don't have the access role required to execute it — the builder restricted it to a specific role (e.g., Editor only, or a specific unit role). (2) A required selection has not been made — some Actions require you to select an Object (click a row in a table) before the Action can run. If no row is selected, the Action may be inactive.

---

### Sub-Topic 2: Executing an Action — 35 minutes

**Instructor Notes:**
Live instructor demo first, then students execute independently.

Demo: locate the "Update SITREP Status" Action in the Training Workshop Application.
1. Select a record in the SITREP table (click a row to select it — the Action activates)
2. Click the "Update SITREP Status" Action button
3. The Action form appears — fill in parameters: Status (dropdown: Complete / Incomplete / Pending), Comments (text field), Submitted By (pre-filled from your account)
4. Review the completed form
5. Click Confirm/Submit
6. Observe: the confirmation toast appears; the row in the table updates to reflect the new status

Walk through this twice — once for the class, once where a student volunteers to do it while you narrate.

Then students execute independently on a designated training record.

Common error: student selects a record in one table but the Action still appears grayed out — they may have selected the row incorrectly (single click vs. double click, or clicked the wrong table). Demonstrate the correct selection behavior.

**Student Activity:** Each trainee executes the "Update SITREP Status" Action on their designated training record (instructor assigns record IDs so trainees are not editing the same record). Verify the status update appears in the table.

**Check on Learning:**
- Q: "You executed the Update SITREP Status Action and marked a record as 'Complete.' You then realize it should have been 'Pending.' What do you do?"
- A: Execute the Action again on the same record with the correct status — if the Action allows updates. If the Action only sets final status, contact the data steward or unit MSS Administrator for correction.

## Summary

**SUMMARY:**
- Actions write data to the Ontology — this is how authorized users update operational records
- Actions are non-reversible in most configurations — verify your inputs before confirming
- An Action may be grayed out if you lack the access role or have not selected a required Object
- What you see update on screen (row status change) reflects what the commander sees on their dashboard

**CLOSE:** After lunch, we shift from reading and writing data to building analysis. Contour lets you create your own charts and views on the fly.

## Assessment

Assessed in Block 9 (Practical Exercise): Execute the Status Update Action (Task 3).

---

---

# BLOCK 5 — CONTOUR

| Field | Value |
|---|---|
| **Block Number** | Block 5 |
| **Hours** | 1.0 |
| **Method** | Lab |
| **Time** | 1300–1400 |

## Purpose

Contour is the ad hoc analysis tool — it lets users build charts and filtered views on demand from datasets and Ontology data, without writing code and without waiting for a builder. A TM-10 trainee who can use Contour can answer a commander's question in five minutes rather than submitting an analysis request to the data shop.

## Learning Objectives

**TLO:** Given access to a Contour-accessible dataset, the trainee will build a basic bar chart, apply a column filter, and save or export the result — to standard, without instructor assistance.

| # | ELO | Assessment |
|---|---|---|
| 1 | Open a dataset in Contour from the MSS navigation | Check on learning |
| 2 | Select X and Y axis fields and generate a bar chart | Evaluated task (Practical Exercise Task 5) |
| 3 | Apply a filter to the Contour workspace to narrow the dataset | Evaluated task (Practical Exercise Task 5) |
| 4 | Export a Contour view or save it for sharing | Check on learning |

## Resources

**Instructor:** TM-10 Block 5 slides; Training Environment dataset suitable for Contour (equipment readiness by unit)
**Student:** TM-10 Chapter 5

## Introduction

**ATTENTION:** "The S3 calls you at 1400 and asks for a bar chart of C1 vs. C4 equipment by battalion for the 1600 brief. With Contour, you can build that in 4 minutes. Without Contour, you're in Excel for 45 minutes. Let's build it."

## Body

### Sub-Topic 1: Opening Contour and Loading Data — 15 minutes

**Instructor Notes:**
Navigate to Contour via left navigation. Open the pre-configured training dataset (equipment readiness).

Two ways to open data in Contour: (1) Open Contour directly and search for a dataset using Compass, (2) Open a dataset from the Projects view and select "Open in Contour."

Walk through the Contour canvas: left panel (field selector), main canvas (chart area), filter bar (top), view controls (right).

**Student Activity:** Open Contour and load the equipment readiness dataset. Confirm it shows column headers.

---

### Sub-Topic 2: Building a Bar Chart — 25 minutes

**Instructor Notes:**
Demo the chart build:
1. Drag "unit" field to X axis
2. Drag "equipment_count" field to Y axis
3. Change chart type to Bar (if not already bar)
4. Sort by Y descending
5. Add color coding: drag "c_rating" to Color channel

Explain: the chart is live — it updates as you change fields. You are not creating a static image; you are creating a view configuration that can be refreshed.

Apply a filter: add a filter on "c_rating" to show only C1 and C4 equipment. Observe how the chart narrows.

**Student Activity:** Build the same bar chart. Then change the filter to show only C3 and C4 equipment.

**Check on Learning:**
- Q: "What is the difference between a Contour analysis and a Workshop chart widget?"
- A: Contour is an ad hoc tool — you build what you need on demand. Workshop charts are pre-configured by the builder and embedded in an application. Contour is for exploration and one-off analysis; Workshop is for recurring operational use.

---

### Sub-Topic 3: Saving and Exporting — 20 minutes

**Instructor Notes:**
Saving a Contour analysis: top right "Save" button. Saved analyses appear in the Contour section of your project. Other project users can see saved analyses if the project is shared.

Exporting: "Export" option — CSV of the filtered data, or image export of the chart.

NOTE: Before exporting, confirm the classification marking of the dataset. The exported file inherits the classification. A FOUO or CUI dataset exported to an unsecured location is a spillage. This will be covered more in Block 8.

**Student Activity:** Save the Contour analysis with a descriptive name following naming conventions. Then export the chart as an image.

## Summary

**SUMMARY:**
- Contour is the ad hoc analysis tool — build charts and filtered views in minutes
- Bar charts: drag fields to X axis (categorical), Y axis (numeric), Color (optional grouping)
- Filters narrow the dataset to what you need without modifying the underlying data
- Before exporting, confirm the classification marking — the export inherits it

**CLOSE:** Contour is for building charts from datasets. Quiver is for exploring the Ontology — the Object layer. Different tool, different lens on the same data.

## Assessment

Assessed in Block 9 (Practical Exercise): Build a bar chart in Contour from provided dataset (Task 5).

---

---

# BLOCK 6 — QUIVER

| Field | Value |
|---|---|
| **Block Number** | Block 6 |
| **Hours** | 1.0 |
| **Method** | Lab |
| **Time** | 1400–1500 |

## Purpose

Quiver is the Object exploration tool — it surfaces the Ontology layer directly, allowing users to explore Objects (Equipment, Units, Personnel) with their properties, filter across objects, and see linked relationships. Where Contour is for tabular data analysis, Quiver is for navigating the semantic layer.

## Learning Objectives

**TLO:** Given access to an Object Type in Quiver, the trainee will open the Object set, apply filters, drill into an Object's properties, and export a filtered view — to standard, without instructor assistance.

| # | ELO | Assessment |
|---|---|---|
| 1 | Open an Object Type in Quiver from the MSS navigation | Check on learning |
| 2 | Apply a property filter to narrow the Object set | Evaluated task (Practical Exercise Task — not directly, but builds skill assessed in Task 4) |
| 3 | Click into a single Object and read its property values | Evaluator observation |
| 4 | Export a filtered Quiver view to CSV | Evaluated task (Practical Exercise Task 4) |

## Resources

**Instructor:** TM-10 Block 6 slides; Equipment Object Type pre-configured in Training Environment
**Student:** TM-10 Chapter 6

## Introduction

**ATTENTION:** "Contour shows you dataset rows. Quiver shows you Objects — the semantic layer. An Equipment Object doesn't have a 'row' — it has properties: equipment_id, unit, c_rating, last_maintenance, location. Quiver lets you explore Objects the way you'd look up a record."

## Body

### Sub-Topic 1: Opening an Object Type in Quiver — 15 minutes

**Instructor Notes:**
Navigate to Quiver from the Ontology section in the project, or directly from the left navigation.

Open the Equipment Object Type. Show the Object list view: each row is one Object (one piece of equipment). Columns are properties.

Note: Quiver looks similar to a table, but it is not a dataset — it is a live view of the Ontology. Objects can have Link Types to other Objects (Equipment → Unit). Quiver can show these relationships.

**Student Activity:** Open the Equipment Object Type in Quiver. Confirm the number of Objects displayed matches the known count the instructor provides.

---

### Sub-Topic 2: Filtering and Exploring Objects — 30 minutes

**Instructor Notes:**
Apply a filter in Quiver: filter Equipment by c_rating = "C3" or "C4". Observe the count narrows.

Click into a single Equipment Object: show the property panel — all properties for this Object. If Link Types are configured, show the linked Unit.

Quiver filter vs. Contour filter: both narrow what you see, but Quiver filters are on Object properties, and the results remain Objects (navigable, with links) — not just rows.

**Student Activity:** Filter to C3/C4 equipment. Click into one Object and note at least 3 of its properties. If a Link to the Unit Object is visible, click through to the linked Unit.

**Check on Learning:**
- Q: "You filtered to C4 equipment in Quiver. There are 7 Objects. One of them has a Link to a Unit Object. What does that Link tell you?"
- A: This equipment is associated with (assigned to, belongs to) a specific Unit. The relationship is part of the Ontology model — the builder linked Equipment to Unit. Clicking through shows you the Unit's properties.

---

### Sub-Topic 3: Exporting a Quiver View — 15 minutes

**Instructor Notes:**
Export the filtered view to CSV. Same classification rules as Contour exports — check the classification before exporting.

Show the Export button, select CSV, confirm the column selection. Exported file reflects the current filter state.

**Student Activity:** Export the filtered C3/C4 equipment view to CSV. Open the export and confirm the row count matches the filtered Quiver view.

**Check on Learning:**
- Q: "Is a Quiver export a one-time snapshot or does it stay current?"
- A: It is a snapshot of the data at the time of export. The export file is static. If you want to share live data, share the Quiver view or Workshop application, not an exported file.

## Summary

**SUMMARY:**
- Quiver surfaces the Ontology layer — Objects with properties and Links, not just rows in a table
- Filters narrow the Object set to what you need; click into any Object to see its full properties
- Link Types let you navigate between related Objects (Equipment → Unit, SITREP → Unit)
- Exports are snapshots — check classification before exporting, and don't treat the export as a live data source

**CLOSE:** Two short blocks remaining. AIP interface, then classification. Both are tested on the practical exercise.

## Assessment

Assessed in Block 9 (Practical Exercise): export filtered table to CSV (Task 4 — note: Task 4 is actually the Contour/Workshop export; Quiver skills are assessed through observation).

---

---

# BLOCK 7 — AIP INTERFACE

| Field | Value |
|---|---|
| **Block Number** | Block 7 |
| **Hours** | 0.5 |
| **Method** | Lab |
| **Time** | 1500–1530 |

## Purpose

AIP Logic and Agent Studio are AI-enabled tools in MSS. TM-10 users do not build AI workflows — they interact with them through Workshop applications or through the AIP interface directly. This block teaches the trainee to use an AIP interface correctly and, more importantly, to understand what AI outputs are and are not.

## Learning Objectives

**TLO:** Given an AIP Logic interface configured for TM-10 training, the trainee will submit a query, interpret the output, and correctly state the limitations and authorized uses of AIP-generated outputs — to standard.

| # | ELO | Assessment |
|---|---|---|
| 1 | Submit a query to an AIP Logic interface | Check on learning |
| 2 | Identify whether an AIP-generated output is authoritative or advisory | Verbal check |
| 3 | State two limitations of AIP outputs in operational contexts | Evaluated item (Practical Exercise conceptual question) |

## Resources

**Instructor:** TM-10 Block 7 slides; AIP Logic interface configured for training (document Q&A on synthetic SITREP data)
**Student:** TM-10 Chapter 7

## Introduction

**ATTENTION:** "AIP can read 200 SITREP documents and give you a summary in 10 seconds. That is real capability. But if you brief that summary to the G3 without reading the source documents, you are briefing an AI summary as if it were authoritative. That has a different name: a mistake."

## Body

### Sub-Topic 1: Using the AIP Interface — 20 minutes

**Instructor Notes:**
Open the Training AIP Interface (a pre-configured AIP Logic workflow exposing a Q&A interface over synthetic SITREP data).

Submit a query: "Which units had C-rating changes in the last 30 days?" — observe the output.

Walk through the output format: AIP returns a structured response, often with cited source Objects or documents.

**Key points:**
1. AIP outputs are advisory — they require human review. They are not authoritative.
2. AIP does not know things that are not in its context. If it confidently states something not in the data, that is a hallucination. This happens.
3. The human review gate exists for a reason — no AIP output should go directly into production data or into a commander's brief without review.

**Student Activity:** Submit two queries. Note whether the responses are clearly grounded in the data (cites source records) or appear to be general statements.

**Check on Learning:**
- Q: "AIP returns a response saying '4 units have C3 or C4 equipment.' You plan to brief this number to the S3. What should you do before briefing it?"
- A: Verify against the source data. Open the Equipment Object Type in Quiver or the Workshop readiness dashboard and confirm the count independently. AIP is a starting point, not the answer.

## Summary

**SUMMARY:**
- AIP interfaces are tools, not oracles. Outputs require human review.
- Always verify AIP-generated numbers or summaries against source data before using them operationally.
- AIP does not have context outside what is in its data source. Confident-sounding outputs can be wrong.

---

---

# BLOCK 8 — CLASSIFICATION MARKINGS AND EXPORT PROCEDURES

| Field | Value |
|---|---|
| **Block Number** | Block 8 |
| **Hours** | 0.5 |
| **Method** | Lecture |
| **Time** | 1530–1600 |

## Purpose

Data mishandling from MSS starts with not checking classification before exporting. This block is short and non-negotiable. It is directly evaluated in the practical exercise — trainees who cannot identify a classification marking or state the authorized export procedure will not pass.

## Learning Objectives

**TLO:** Given a description of an MSS dataset or export scenario, the trainee will correctly identify the classification marking, state the authorized distribution, and describe the correct export procedure — to standard, without reference to notes.

| # | ELO | Assessment |
|---|---|---|
| 1 | Locate the classification marking on a Foundry dataset | Evaluated task (Practical Exercise Task 6) |
| 2 | State the authorized distribution for a given marking (UNCLASSIFIED, FOUO/CUI) | Evaluated task (Practical Exercise Task 6) |
| 3 | Describe the authorized export procedure for each classification level | Evaluated task (Practical Exercise Task 6 — verbal) |

## Resources

**Instructor:** TM-10 Block 8 slides; examples of classification markings in the Training Environment
**Student:** TM-10 Chapter 8

## Introduction

**ATTENTION:** "This is the block that keeps you out of trouble. Classification markings are in MSS. Before you export any file, you check the marking. If you export FOUO data to your personal Google Drive, you have just committed a spillage. The practical exercise will ask you where to find the marking and what to do with the data."

## Body

### Sub-Topic 1: Where Classifications Live in Foundry — 10 minutes

**Instructor Notes:**
Classification markings are applied at the dataset level and at the application level. Where to find them:
1. Dataset properties panel (open a dataset → Properties → Classification)
2. Application header or documentation (if the builder included it)
3. Object Type properties (if configured)

In the Training Environment, all data is UNCLASSIFIED. But trainees must know the procedure for when they work with FOUO/CUI data in production.

Walk through: open a training dataset, locate the Properties panel, identify the classification field.

**Student Activity:** Locate the classification field on two different datasets. Note the marking.

---

### Sub-Topic 2: Authorized Export Procedures — 20 minutes

**Instructor Notes:**
Cover the three marking categories relevant to USAREUR-AF MSS:

| Marking | Authorized Export Destination | Distribution |
|---|---|---|
| UNCLASSIFIED | Approved government systems; NIPR | No restriction within authorized users |
| FOUO / CUI | Government systems only; no personal devices, no cloud storage (Google Drive, OneDrive personal) | Official use only; need-to-know |
| CLASSIFIED | Not applicable in MSS Training Environment; do not attempt to export from production classified systems without explicit authorization | Requires appropriate handling |

Procedure before any export:
1. Check the dataset classification marking
2. Confirm your export destination is authorized for that classification
3. Export using the MSS export function (not copy-paste)
4. Label the exported file with the classification marking

Common violations:
- Copy-paste data from MSS into an email or personal document
- Screenshot a classified field visible on screen and text-message it
- Export FOUO data to a personal Google Drive for "easier access"

**Check on Learning:**
- Q: "You export an Equipment readiness dataset and the Properties panel shows 'CUI//FOUO'. You want to email it to the S4 officer. Can you send it to their NIPR email? Can you put it on a USB drive? Can you send it to their personal email?"
- A: NIPR government email — Yes, with CUI marking in the subject. USB drive — only if authorized; most USAREUR-AF policy prohibits unapproved removable media. Personal email — No. Always.

## Summary

**SUMMARY:**
- Classification markings are in the dataset Properties panel — check before every export
- FOUO/CUI data stays on government systems; it does not go to personal devices or personal cloud storage
- Copy-paste is not an authorized export procedure — use the MSS export function
- Label exported files with the classification marking

**CLOSE:** One block left — the practical exercise. You have 60 minutes. The tasks cover login, Workshop, Actions, Contour, export, and classification. You may reference your TM-10 and this syllabus. No instructor assistance once the exercise begins.

## Assessment

Directly evaluated in Block 9 (Practical Exercise): state classification marking and authorized distribution for provided dataset (Task 6).

---

---

# BLOCK 9 — PRACTICAL EXERCISE (EVALUATED)

| Field | Value |
|---|---|
| **Block Number** | Block 9 |
| **Hours** | 1.0 |
| **Method** | Evaluation |
| **Time** | 1600–1700 |

## Purpose

The practical exercise confirms that the trainee can independently perform the six operational tasks that constitute TM-10 competency. The evaluator observes but does not assist.

## Scenario

**You are an S3 NCO. Your unit's SITREP tracker and readiness dashboard are in MSS. You have 60 minutes to complete all six tasks.**

## Pre-Exercise Brief (Delivered by Evaluator)

"You have 60 minutes. You may reference TM-10 and your course syllabus. You may not ask me for help — I will not answer questions about the tasks. If you have an access or system error that prevents completing a task, tell me immediately and I will document it. A system error that I document will not count against you. A wrong answer that you don't flag will.

The scenario and task instructions are in the envelope in front of you. You may begin."

## Evaluated Tasks

| Task | Description | Go Standard | Hard No-Go |
|---|---|---|---|
| 1 | Log in and navigate to the designated Workshop application | Successfully authenticated; application open without assistance | — |
| 2 | Filter the SITREP table to last 7 days; identify the unit(s) with missing submissions | Correct filter applied; correct unit(s) identified by name | — |
| 3 | Execute the Status Update Action to mark a specified record as "Complete" | Action executed; record shows updated status without error | — |
| 4 | Export filtered Workshop table to CSV | Export downloaded; row count matches filtered table; file labeled with classification marking | — |
| 5 | Build a bar chart in Contour from the provided readiness dataset | Chart built showing correct X and Y fields; filter applied as specified | — |
| 6 | State the classification marking and authorized distribution for the provided dataset (verbal or written) | Correct marking identified; correct authorized distribution stated | Incorrect classification = automatic No-Go |

## Evaluator Instructions

- Observe each task completion. Document time and result.
- Do not answer task questions. Do not provide hints.
- If a trainee makes a wrong action (e.g., selects wrong Action) and self-corrects before completing — that is still Go for that task.
- If a trainee selects wrong Action and completes it without self-correcting — that is No-Go for that task.
- At Task 6, the evaluator asks: "State the classification marking and authorized export destination for this dataset" — evaluator shows the dataset on screen. Trainee responds verbally or in writing.
- Document the evaluation on the Individual Training Record.

## Go Standard

All 6 tasks completed independently, to standard. Task 6 (classification) is a hard No-Go item — incorrect classification identification or authorization statement results in automatic No-Go regardless of performance on Tasks 1–5.

## No-Go Actions

If No-Go:
1. Evaluator provides written debrief within 1 duty day
2. Remediation: minimum 2 hours (self-study TM-10 + supervised lab)
3. Re-evaluation within 10 duty days using a different scenario

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*TM-10 Lesson Plans | Version 1.0 | March 2026*
