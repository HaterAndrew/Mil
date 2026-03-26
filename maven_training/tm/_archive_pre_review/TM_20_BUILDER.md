# TM-20 — MAVEN SMART SYSTEM (MSS)
## NO-CODE BUILDER TECHNICAL MANUAL

**HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA**
Wiesbaden, Germany

2026

**Version 1.0 | March 2026**

**APPLIES TO:** All USAREUR-AF military and Civilian personnel who build applications, pipelines, and analyses on MSS without writing code.

**PREREQUISITE PUBLICATIONS:** SL 1, Maven Smart System Operator Manual (required). Data Literacy Technical Reference (recommended).

**RELATED MANUALS:** SL 3, Advanced Builder/Developer (Python, PySpark, TypeScript, OSDK).

**DISTRIBUTION RESTRICTION:** DRAFT — Not yet approved for distribution.

---

## SAFETY SUMMARY

Builders have elevated privileges on MSS. Errors in pipelines, Ontology configurations, or published applications may affect downstream users and operational data. Before building, understand:

- Changes to shared datasets and Object Types affect all downstream applications and all users consuming them.
- Publishing a broken pipeline can corrupt operational data that units depend on for readiness reporting and command decisions.
- Incorrect Ontology configurations can disable live Workshop applications for an entire unit.
- Data ingested without coordination may introduce unauthorized or improperly marked data into the enterprise environment.
- Permissions assigned incorrectly can expose data to personnel without appropriate access.

**Read all WARNINGS and CAUTIONS before beginning any build activity.**

**If you are uncertain whether an action is authorized -- STOP. Contact your unit Data Steward or the USAREUR-AF C2DAO before proceeding.**

---

## TABLE OF CONTENTS

- Chapter 1 -- Introduction
- Chapter 2 -- Project Setup and Management
- Chapter 3 -- Data Ingestion with Pipeline Builder
- Chapter 4 -- Ontology UI Basics
- Chapter 5 -- Building Workshop Applications
- Chapter 6 -- Analysis with Contour and Quiver
- Chapter 7 -- Branching and Environment Management
- Chapter 8 -- Builder Standards and Governance
- Appendix A -- Pre-Publish Checklist
- Appendix B -- Common Pipeline Builder Patterns
- Glossary

---

# CHAPTER 1 -- INTRODUCTION

## 1-1. Purpose and Scope

**BLUF:** This manual teaches you to build applications, data pipelines, and analyses on MSS using only the graphical user interface -- no coding required.

This Technical Manual (TM) provides task-level instruction for USAREUR-AF personnel who build on the Maven Smart System (MSS) using no-code tools. It is written for all staff -- officer, warrant, NCO, Civilian -- who completed SL 1 and have been granted builder access. No programming background is required. If you can use a web browser and fill out forms, you can do everything in this manual.

> **NOTE:** Before beginning SL 2 work, verify you can independently perform the following SL 1 tasks without referencing the manual: Task 2-1 through 2-4 (account setup, MFA, access); Task 3-1 through 3-3 (navigation and resource discovery); Task 5-1 (dataset viewing); Chapter 7 (security markings and access controls). Builders must understand operator-level data security requirements before building. If you are uncertain about any SL 1 task, review SL 1 before proceeding.

**This manual covers:**

- Creating and managing projects via the Compass UI
- Building visual ETL pipelines using Pipeline Builder (drag-and-drop, no code)
- Connecting to data sources using pre-built UI connectors
- Creating Object Types and Link Types using the Ontology UI (form-based)
- Configuring basic Actions using form-based configuration (no code)
- Building Workshop applications with drag-and-drop widgets
- Publishing and sharing Workshop applications
- Building saved analyses in Contour
- Building basic dashboards in Quiver
- Managing project permissions and access via UI
- Using Foundry branching via the UI (no command line)
- Naming conventions and builder standards

**This manual does NOT cover:**

- Python, PySpark, or SQL transforms
- Code editors or code repositories
- TypeScript Functions or OSDK
- @incremental transform configuration
- AIP Logic configuration or Agent Studio
- Any task requiring writing or reading code

Those topics are in SL 3, Advanced Builder/Developer. If a task requires writing code, stop and contact your team's data engineer.

---

## 1-2. USAREUR-AF Mission Context and the Builder's Role

United States Army Europe and Africa (USAREUR-AF) is the Army Service Component Command (ASCC) to United States European Command (USEUCOM) and United States Africa Command (USAFRICOM), responsible for theater land operations across the European and African Areas of Responsibility (AOR) and integration with NATO Allied command structures. Major subordinate commands -- V Corps (forward deployed, Poland), 21st Theater Sustainment Command (TSC), and 7th Army Training Command (ATC) -- each generate and consume data that flows through MSS.

As a builder, the tools you create directly affect readiness visibility and operational decision-making across this formation. A Workshop application you build may display unit status to a V Corps G3 in Poznan or track logistics readiness for a 21st TSC officer in Kaiserslautern. A pipeline you configure may feed the data behind a theater-level briefing. Understand the operational weight of what you are building before you begin.

**Per ADP 3-13, information is combat power.** Builders are one of the primary means by which raw data becomes operationally useful information for commanders.

> **NOTE:** As a builder, understand the operator's perspective before you build. Refer to TM-10, Chapter 4 (Using Workshop Applications) to see how operators use the applications you create. Refer to TM-10, Chapter 5 (Working with Data) to understand what operators expect in terms of data quality and currency. Build with the operator experience in mind at all times.

---

## 1-3. The USAREUR-AF 5-Layer Data Stack

MSS is built around a five-layer data architecture. Understanding where your work fits in this stack is essential. SL 2 builders primarily operate at Layers 2, 3, and 4.

```
+----------------------------------------------------------+
|  LAYER 5: ACTIVATION                                     |
|  Published apps, forms, action-enabled workflows         |
|  (Users act on data, submit reports, trigger events)     |
+----------------------------------------------------------+
|  LAYER 4: ANALYTICS                                      |
|  Workshop applications, Contour analyses, Quiver         |
|  << SL 2 builds here (Workshop, Contour, Quiver)        |
+----------------------------------------------------------+
|  LAYER 3: SEMANTIC (ONTOLOGY)                            |
|  Object Types, Link Types, Actions, Properties           |
|  << SL 2 builds here (Ontology UI, no code)             |
+----------------------------------------------------------+
|  LAYER 2: INTEGRATION                                    |
|  Pipeline Builder, connectors, ingestion pipelines       |
|  << SL 2 builds here (Pipeline Builder, no code)        |
+----------------------------------------------------------+
|  LAYER 1: INFRASTRUCTURE                                 |
|  Raw data storage, connectors, access controls           |
|  (Administered by platform admin; builder requests)      |
+----------------------------------------------------------+
```

**SL 2 Activity to Layer Mapping:**

| SL 2 Activity | Stack Layer | Layer Name |
|---|---|---|
| Connect data sources via Pipeline Builder connectors | Layer 2 | Integration |
| Build visual ETL pipelines (Pipeline Builder) | Layer 2 | Integration |
| Schedule and monitor ingestion | Layer 2 | Integration |
| Create Object Types via Ontology UI | Layer 3 | Semantic |
| Create Link Types via Ontology UI | Layer 3 | Semantic |
| Configure Actions via form-based UI | Layer 3 | Semantic |
| Build Workshop applications | Layer 4 | Analytics |
| Build Contour saved analyses | Layer 4 | Analytics |
| Build Quiver dashboards | Layer 4 | Analytics |
| Publish Workshop apps, share with users | Layer 5 | Activation |

NOTE: Advanced transform development (Python/PySpark), OSDK, TypeScript Functions, and AIP Logic operate at Layers 2-3 but require code. Those are SL 3 topics. SL 2 covers only the no-code paths through Layers 2-4.

---

## 1-4. C2DAO Governance Chain

All builder activity on MSS is governed by the USAREUR-AF Data Governance chain. Know this chain before you build anything.

```
ARMY CIO
  |  Army Data Plan (2022); CIO Data Stewardship Policy (Apr 2024)
  v
USAREUR-AF C2DAO
  |  Theater-level data governance authority
  |  Approves new data sources, ontology changes, access policies
  v
UNIT DATA STEWARD
  |  Your unit's accountable data official
  |  First point of contact for any data question
  v
FUNCTIONAL DATA MANAGER
  |  Day-to-day oversight of a specific data domain
  v
BUILDER (YOU)
     Build within approved scope on approved data
```

**Key policy references:**

| Document | Governing Authority | Relevance to SL 2 Builders |
|---|---|---|
| Army Data Plan (2022) | Army CIO | Framework for data management, governance, analytics |
| DoD Data Strategy (2020) | OSD | VAUTI framework: Visible, Accessible, Understandable, Trustable, Interoperable |
| Army CIO Data Stewardship Policy (April 2, 2024) | Army CIO | Data stewardship hierarchy; data chain of responsibility |
| USAREUR-AF Data Governance SOP | C2DAO | USAREUR-AF-specific naming, access, and approval processes |

> CAUTION: Before ingesting any new data source, coordinate with your unit Data Steward and the USAREUR-AF C2DAO. Unauthorized ingestion of operational data -- even from Army systems -- may violate Army CIO policy and create compliance findings.

---

## 1-5. Builder Prerequisites

Complete all of the following before beginning any build activity on MSS.

**Access requirements:**

- [ ] SL 1 (Maven User) completed
- [ ] Builder access request submitted through chain of command and approved
- [ ] Editor role granted on your team's project folder in Compass
- [ ] Editor role granted on the Ontology branch for your team
- [ ] Workshop Builder permission granted

**Orientation requirements (complete before creating any resource):**

- [ ] Navigated to your team's project folder in Compass
- [ ] Opened and reviewed at least one existing Pipeline Builder pipeline
- [ ] Previewed the output dataset of that pipeline
- [ ] Found the Object Type backed by that dataset in Ontology Manager
- [ ] Opened and used (as an end user) the Workshop application built on that Object Type

Do not begin building until you understand the existing system. Adding to something you do not understand creates problems that are difficult to untangle.

---

## 1-6. Governing References

- Army Data Plan (2022), Office of the Army Chief Information Officer
- DoD Data Strategy (2020), Office of the Secretary of Defense
- Army CIO Data Stewardship Policy Memorandum, April 2, 2024
- USAREUR-AF C2DAO Data Governance SOP (current version)
- Palantir Foundry Product Documentation (in-platform Help)
- USAREUR-AF G6/Data: ontology design standards, doctrine-aligned Object Type patterns, data modeling guidance

---

## 1-7. Think Before You Build — The Builder's Design Framework

**BLUF:** The most common builder failure is building the wrong thing correctly. This section gives you a thinking framework to use before you open Pipeline Builder or Workshop. Spend time here before spending time on the platform.

Every build task starts with three questions. Answer them in order — do not skip ahead.

**Question 1: Who is my user and what decision are they making?**

The application or pipeline you build exists to help someone make a decision or take an action. If you cannot name that person and that decision before you start, you are not ready to build.

Examples of clear answers:
- "The S4 NCO in Graf needs to see which vehicles are deadlined, updated daily, so they can prioritize maintenance scheduling."
- "The battalion XO needs to see personnel readiness by company so they can report up to brigade before the Monday briefing."

Examples of answers that are too vague:
- "The S4 needs a readiness dashboard." (What kind of readiness? What does 'ready' mean? What action follows?)
- "G2 wants to see data about units." (Which units? What about them? For what purpose?)

If you have a vague answer, get a clearer requirement before you build. Building to a vague requirement produces something that looks complete but does not actually help anyone.

**Question 2: What data do I need, and where does it come from?**

Map the pipeline before you build it:

```
DECISION REQUIREMENT         DATA ELEMENTS NEEDED         SOURCE SYSTEM
"Which vehicles are   →   Equipment ID, status,    →   GCSS-A (via existing
 deadlined by fleet?"       class, location, date         ingestion pipeline)
```

Verify the data exists and is already in MSS before you design anything that depends on it. If the data does not exist, you have an ingestion problem — not a Workshop problem. Ingestion decisions require Data Steward coordination.

**Question 3: Where does my work fit in the 5-layer stack?**

Use the stack from paragraph 1-3 as a design checklist:

| Layer | Question to ask |
|---|---|
| Layer 2 (Integration) | Is the data I need already ingested? If not, can Pipeline Builder connect to the source? |
| Layer 3 (Ontology) | Is there an Object Type that represents the thing I'm building around? If not, does one need to be created (Data Steward coordination required)? |
| Layer 4 (Analytics) | What Workshop widgets best present the decision my user needs to make? |
| Layer 5 (Activation) | Does the user need to take an action — submit a form, trigger a workflow — or just view information? |

Build bottom-up. Do not start building a Workshop application until you have confirmed the data layer beneath it is solid. A beautifully designed Workshop app built on a broken pipeline is useless.

> **CAUTION:** A common mistake is building at Layer 4 (Workshop) while assuming the Layer 2 and Layer 3 problems will work themselves out. They will not. Verify your data exists, is clean, and is modeled correctly in the Ontology before you build the application that depends on it.

**The builder's minimum viable check before starting any task:**

- [ ] I can name the user and the decision they need to make.
- [ ] I know what data is needed and have confirmed it exists in MSS (or have a plan to get it there).
- [ ] I know which Object Type(s) my application will be built on.
- [ ] I have looked at the existing application (if any) before building something new.
- [ ] I have talked to the intended user — not just their supervisor — about what they need.

If any box is unchecked, do not build. Resolve it first.

---

# CHAPTER 2 -- PROJECT SETUP AND MANAGEMENT

## 2-1. MSS Resource Hierarchy

Before creating anything, understand how MSS organizes resources in Compass.

| Container | What It Holds | Managed By |
|---|---|---|
| **Project** | Top-level grouping for one functional area | Team lead / C2DAO approval |
| **Folder** | Subdirectory within a project | Builder |
| **Dataset** | A managed table produced by a pipeline | Builder (via Pipeline Builder) |
| **Pipeline** | A visual ETL flow (Pipeline Builder) | Builder |
| **Ontology** | Shared semantic layer -- Object Types, Links, Actions | Builder (via Ontology Manager) |
| **Workshop App** | A published application for end users | Builder |

**Your team's project already exists. Do not create a new top-level project without authorization from your unit Data Steward and C2DAO approval.**

---

## 2-2. Standard Folder Structure

Within an authorized project, create folders following this standard structure.

```
/[AOR]-[FUNCTION]/
+-- raw/               data as it arrives from source systems
+-- staging/           cleaned, validated, intermediate data
+-- curated/           publication-ready data, Ontology-backed
+-- pipelines/         Pipeline Builder definitions
+-- applications/      Workshop app definitions
```

**Example -- EUCOM SITREP project:**

```
/USAREUR-AF-SITREP/
+-- raw/
|   +-- sitrep_feed_raw
+-- staging/
|   +-- sitrep_feed_staging
+-- curated/
|   +-- sitrep_feed_curated
+-- pipelines/
|   +-- sitrep-ingestion-pipeline
+-- applications/
    +-- EUCOM SITREP Dashboard
```

NOTE: Dataset paths are permanent. You cannot rename a dataset path without breaking all downstream pipelines and Ontology objects. Plan folder and dataset names before creating any resource. When in doubt, ask your team lead.

> **NOTE:** The folder structure you create is what operators navigate using TM-10, Chapter 3 (Navigating the Platform), specifically Task 3-2 (Navigate Using Compass). Poor folder structure and unclear naming conventions create confusion for operators downstream. Test your folder organization by navigating it as an operator would before finalizing.

---

## 2-3. Naming Conventions

All resources must follow USAREUR-AF naming conventions. Non-compliant resources will be renamed or removed by the team lead.

| Resource Type | Convention | Example |
|---|---|---|
| Dataset -- raw tier | `[source]_raw` | `sitrep_feed_raw`, `gcss_a_maint_raw` |
| Dataset -- staging tier | `[source]_staging` | `sitrep_feed_staging` |
| Dataset -- curated tier | `[source]_curated` | `sitrep_feed_curated` |
| Pipeline Builder pipeline | `[function]-pipeline` | `sitrep-ingestion-pipeline` |
| Object Type | PascalCase, singular noun | `UnitStatus`, `SoldierReadiness`, `MaintenanceRecord` |
| Link Type | camelCase verb phrase | `assignedTo`, `reportedBy`, `locatedAt` |
| Workshop App | Plain English, unit-appropriate | `EUCOM SITREP Dashboard`, `Unit Readiness Tracker` |
| Ontology branch | `dev-[feature]` or `dev-[lastname]` | `dev-sitrep`, `dev-rodriguez` |
| Project folder | `[AOR]-[FUNCTION]` all caps | `USAREUR-AF-SITREP`, `VCORPS-READINESS` |

> CAUTION: Never use PII, classified nicknames, operational codenames, or system passwords in any resource name, description, or label. Resource names and descriptions are visible to all users with project access and appear in audit logs.

---

**TASK 2-1. CREATE A PROJECT**

**CONDITIONS:** Builder access granted; no existing project for your functional area; unit Data Steward and C2DAO have authorized project creation.

**STANDARDS:** The builder will create a project in Compass with the correct name and folder structure, assign appropriate initial permissions, and confirm the project is visible to authorized team members before creating any resources inside it.

**PROCEDURE:**

1. In Compass, click **New** (top right) and select **Project**.
2. Enter the project name following the `[AOR]-[FUNCTION]` convention (e.g., `VCORPS-READINESS`).
3. Enter a description: include the owning unit, functional area, data steward POC, and creation date.
4. Click **Create**.
5. Inside the new project, create subfolders: `raw`, `staging`, `curated`, `pipelines`, `applications`.
6. To create a folder: click **New** then **Folder**, enter name, click **Create**.
7. After folder structure is complete, set permissions (Task 2-3) before adding any data.

NOTE: Do not create datasets or pipelines before folder structure and permissions are set. Fixing structure after data is created requires migrating resources, which breaks downstream references.

---

**TASK 2-2. ADD TEAM MEMBERS TO A PROJECT**

**CONDITIONS:** Builder has Owner or Manager role on the project; team member has an active MSS account; team lead has authorized access.

**STANDARDS:** The builder will add the team member with the correct role. The new member can access the project at the appropriate permission level within 5 minutes. No member is assigned a role higher than required for their duties.

**PROCEDURE:**

1. Open the project in Compass.
2. Click the **Settings** icon (gear) in the upper right of the project view.
3. Select **Access and Sharing**.
4. Click **Add Member**.
5. Search for the team member by name or email.
6. Select the appropriate role from the dropdown (see role table below).
7. Click **Add**.
8. Verify the member appears in the member list with the correct role.
9. Notify the member that access has been granted.

**Role Reference Table:**

| Role | Can Do | Use For |
|---|---|---|
| **Viewer** | Read datasets, open Workshop apps | End users, consumers |
| **Editor** | Modify pipelines, datasets, Workshop apps | SL 2 builders |
| **Owner** | All Editor rights plus manage members, delete resources | Team leads |

NOTE: Assign the minimum role required. If a team member only consumes data in Workshop apps, assign Viewer -- not Editor. Follow least-privilege principles per Army CIO policy.

> CAUTION: Do not assign Owner role without authorization from your Data Steward. Owner access allows deletion of shared datasets and modification of permissions for all project members.

---

**TASK 2-3. SET PROJECT PERMISSIONS AND ACCESS CONTROLS**

**CONDITIONS:** Builder has Owner role on the project; unit Data Steward has provided an approved access list; classification and handling requirements are known.

**STANDARDS:** The builder will configure project permissions so that only authorized personnel have access, roles correctly match duties, and the Data Steward has reviewed and approved the configuration before any data is added.

**PROCEDURE:**

1. Open the project in Compass, click **Settings**, then **Access and Sharing**.
2. Review the current member list against the approved access list from the Data Steward.
3. Remove any members not on the approved list: click the three-dot menu next to their name then **Remove**.
4. Add authorized members not yet listed (see Task 2-2).
5. Verify each member's role against their duty position and adjust as needed.
6. Set the **Project Visibility**:
   - **Private** -- access by invitation only (default; use for all operational data projects)
   - **Organization** -- visible to all MSS users (use only for unclassified reference/training projects)
7. Click **Save**.
8. Send the finalized access list to your Data Steward for confirmation.

> CAUTION: Do not set any operational data project to Organization visibility without explicit C2DAO approval. This makes all datasets in the project readable by all MSS users.

---

# CHAPTER 3 -- DATA INGESTION WITH PIPELINE BUILDER

## 3-1. What Pipeline Builder Does

Pipeline Builder is MSS's visual, no-code ETL (Extract, Transform, Load) tool. Using a drag-and-drop interface, you build pipelines that pull data from a source, clean or reshape it, and write the result to a destination dataset -- no code required.

**Where Pipeline Builder fits in the 5-Layer Stack:** Layer 2, Integration. The output of every Pipeline Builder pipeline is a dataset that can be consumed at Layer 3 (Ontology) or Layer 4 (Analytics).

**What Pipeline Builder can do without code:**

- Connect to pre-configured data sources (files, shared datasets, approved connectors)
- Filter rows by value, date range, or condition
- Select, rename, and reorder columns
- Join two datasets on a shared key
- Aggregate data (count, sum, average, group by)
- Append (union) multiple datasets
- Deduplicate rows
- Schedule automatic refreshes

**What Pipeline Builder cannot do (requires SL 3/code):**

- Complex multi-step transformations
- Custom business logic
- Machine learning or statistical computation
- Writeback to external systems

> **NOTE:** The pipelines you build in Pipeline Builder become the data sources that operators access via TM-10, Task 5-1 (View and Read a Dataset) and in Workshop applications. Pipeline failures directly impact operators' ability to access operational data. Refer to TM-10, Chapter 8 (Troubleshooting and Support) to understand the operator experience when a pipeline fails — build your monitoring accordingly.

---

## 3-2. Pipeline Builder Interface Overview

| UI Area | Location | Purpose |
|---|---|---|
| **Canvas** | Center | Where you build -- drag nodes here and connect them |
| **Node Library** | Left panel | Available data sources, transforms, and outputs |
| **Node Properties** | Right panel | Configuration for the selected node |
| **Preview Pane** | Bottom panel | Live data preview -- shows first 100 rows of selected node output |
| **Build Log** | Bottom panel (tab) | Build status, errors, warnings |
| **Schedule** | Top toolbar | Configure automatic refresh |
| **Branch** | Top toolbar | Shows current branch; switch branch before editing |

Always work on a branch, not on the main/production pipeline. See Chapter 7 for branching.

---

**TASK 3-1. CREATE A PIPELINE BUILDER PIPELINE**

**CONDITIONS:** Builder has Editor access on the project; source dataset or connector is available; destination folder exists; working on a development branch (not main).

**STANDARDS:** The builder will create a Pipeline Builder pipeline in the correct project folder, connect a valid source, add at least one transform node, connect an output dataset, and confirm the pipeline builds successfully (green checkmark, no errors) before requesting a merge.

**PROCEDURE:**

1. In Compass, navigate to your project's `pipelines/` folder.
2. Click **New**, then **Pipeline**, then **Pipeline Builder**.
3. Name the pipeline following the convention `[source]-pipeline` (e.g., `sitrep-ingestion-pipeline`).
4. The Pipeline Builder canvas opens. Confirm the branch shown in the top toolbar is your development branch -- not `main`.
5. In the **Node Library** (left panel), expand **Sources**.
6. Drag the appropriate source node onto the canvas (see Task 3-2 for connecting sources).
7. Add transform nodes as needed (see Task 3-3).
8. Drag an **Output Dataset** node from the Node Library onto the canvas.
9. Connect nodes by clicking the output port of one node and dragging to the input port of the next.
10. Click the Output Dataset node. In the right panel, navigate to your project's appropriate folder and name the dataset.
11. Click **Build** (top toolbar). Wait for the build to complete.
12. If the build succeeds (green checkmark): click the Output node, then **Preview** (bottom panel), and verify the data looks correct.
13. If the build fails: read the error in the Build Log, fix the node configuration, and rebuild.

NOTE: A successful build means the pipeline ran without errors. It does not mean the data is correct. Always preview the output and spot-check values before declaring the pipeline complete.

---

**TASK 3-2. CONNECT A DATA SOURCE IN PIPELINE BUILDER**

**CONDITIONS:** Builder is in Pipeline Builder on a development branch; a pre-configured connector or source dataset exists; Data Steward has approved ingestion of this source.

**STANDARDS:** The builder will connect the data source, preview the incoming data to confirm schema and row count, and document the source name, expected row count, and refresh frequency in the pipeline's description field before proceeding.

**PROCEDURE:**

**Option A -- Connect to an existing MSS dataset:**

1. From the Node Library, drag **Dataset** (under Sources) onto the canvas.
2. In the right panel, click **Select Dataset**.
3. Browse Compass to the source dataset or search by name.
4. Click the dataset then **Confirm**.
5. Click the source node then **Preview** (bottom panel). Verify schema and row count.

**Option B -- Connect via a pre-built connector:**

1. From the Node Library, drag **Connector** onto the canvas.
2. In the right panel, click **Select Connector**.
3. From the list of authorized connectors, select the appropriate connector (e.g., GCSS-A feed, SharePoint file, SFTP source).
4. Configure the connection parameters (folder path, file pattern, authentication -- use values provided by your Data Steward; do not enter credentials from memory).
5. Click **Test Connection**. Verify the connection succeeds.
6. Click the connector node then **Preview**. Verify the incoming data schema.

> CAUTION: Before connecting any new data source, coordinate with your unit Data Steward and the USAREUR-AF C2DAO. Do not connect to a source that has not been explicitly approved for ingestion into MSS. This applies even if you personally have access to the source system.

NOTE: If the connector you need is not on the authorized list, submit a request to the C2DAO through your Data Steward. Do not attempt to work around missing connectors by manually uploading data files without approval.

---

**TASK 3-3. ADD TRANSFORM NODES TO A PIPELINE**

**CONDITIONS:** Builder is in Pipeline Builder on a development branch; a source node is connected; need to filter, reshape, or join data.

**STANDARDS:** The builder will add the correct transform nodes for the required operation, configure each node's properties accurately, and verify the output in the preview pane before connecting to the output dataset.

**PROCEDURE -- Filter rows:**

1. From Node Library, drag **Filter** onto the canvas between your source and output.
2. Connect: source to Filter, Filter to output.
3. In the right panel, click **Add Condition**.
4. Select the column to filter on from the dropdown.
5. Select the operator (equals, contains, greater than, is not null, etc.).
6. Enter the filter value.
7. For multiple conditions, click **Add Condition** again and select AND/OR logic.
8. Click the Filter node then **Preview** to confirm filtered row count.

**PROCEDURE -- Select and rename columns:**

1. Drag **Select Columns** onto the canvas.
2. In the right panel, check/uncheck columns to include or exclude.
3. To rename a column: click the column name in the right panel and edit the name.
4. Preview to confirm column list is correct.

**PROCEDURE -- Join two datasets:**

1. Drag **Join** onto the canvas.
2. Connect the first (left) dataset to the left input port; the second (right) dataset to the right input port.
3. In the right panel, select the **Join Type** (Inner, Left, Right, Full Outer).
4. Under **Join Keys**, select the matching column from the left dataset and from the right dataset.
5. Under **Output Columns**, select which columns to include from each side.
6. Preview to confirm joined row count and verify no unexpected row multiplication.

NOTE: A join that multiplies rows unexpectedly usually means the join key is not unique on one side. Check for duplicate keys in your source data before troubleshooting the join configuration.

**PROCEDURE -- Aggregate (group by/summarize):**

1. Drag **Aggregate** onto the canvas.
2. Under **Group By**, select the columns to group on (e.g., `unit_id`, `report_date`).
3. Under **Aggregations**, click **Add Aggregation**. Select the column and function (Count, Sum, Average, Min, Max).
4. Name the output column for each aggregation.
5. Preview to confirm row count is reduced (one row per unique group).

---

**TASK 3-4. SCHEDULE AUTOMATIC PIPELINE REFRESH**

**CONDITIONS:** Pipeline builds and produces correct output; builder has authorization from Data Steward to schedule automatic runs; the source data updates on a known schedule.

**STANDARDS:** The builder will configure a schedule that matches the source data refresh cadence, set appropriate alerting, and confirm the first scheduled run completes successfully.

**PROCEDURE:**

1. In the pipeline (after successful build), click **Schedule** in the top toolbar.
2. Click **Add Schedule**.
3. Select the frequency:
   - **Hourly** -- for near-real-time feeds (use sparingly; confirm with Data Steward)
   - **Daily** -- most common for SITREP, readiness, and logistics feeds
   - **Weekly** -- for slower-changing data
4. Set the start time. For daily feeds supporting morning briefings, schedule for 0300-0400 local to allow build time.
5. Under **On Failure**, configure email notification: enter your email and your team lead's email.
6. Click **Save Schedule**.
7. To manually trigger the first run: click **Build Now** and monitor the Build Log.
8. After the first run: preview the output dataset to confirm correct results.

NOTE: Schedule times are in UTC. USAREUR-AF is UTC+1 (CET) or UTC+2 (CEST in summer). A 0300 CET scheduled run should be entered as 0200 UTC in winter, 0100 UTC in summer.

> CAUTION: Do not schedule pipelines to run more frequently than the source data actually updates. Excessive builds consume platform resources and may cause rate-limiting on source connectors.

---

**TASK 3-5. MONITOR A PIPELINE AND RESPOND TO BUILD FAILURES**

**CONDITIONS:** Pipeline is scheduled and running; builder has received a failure alert or is performing routine monitoring.

**STANDARDS:** The builder will identify the failing node and error cause within 15 minutes of notification, take corrective action or escalate appropriately within 1 hour, and document the failure and resolution in the pipeline's description field.

**PROCEDURE:**

1. In Compass, open the pipeline.
2. Click the **Build Log** tab (bottom panel).
3. Find the failed build (red icon) -- note the timestamp.
4. Click the failed build entry to expand the error details.
5. Identify the failing node: Pipeline Builder highlights failing nodes in red on the canvas.
6. Click the failing node and read the error message in the right panel.

**Common failure causes and actions:**

| Error Type | Likely Cause | Action |
|---|---|---|
| Source dataset not found | Dataset was renamed or moved | Update the source node path |
| Column not found | Source schema changed | Update column names in affected transform nodes |
| Connection timeout | Source system unavailable | Check source system status; retry manually; alert Data Steward if persistent |
| Authentication failure | Connector credentials expired | Contact Data Steward -- do not attempt to update credentials yourself |
| Row count zero | Source has no data for this run | Investigate source; may be expected for some time windows |
| Build timed out | Pipeline too large for scheduled window | Escalate to data engineer (SL 3) |
| Output dataset missing / stale | Operator impact: TM-10, Task 5-1 | Check schedule; fix broken node; notify data steward |
| Schema mismatch after source change | Breaking change — operator impact | Escalate to SL 3 builder if multi-source; fix schema mapping |

> **NOTE:** When a pipeline fails, operators using TM-10, Task 5-1 see the failure in their data views and in Workshop applications. Fix pipeline issues promptly and document what failed and why. If the root cause is outside your SL 2 capability (e.g., requires @incremental logic, complex deduplication, Python transforms), escalate to a SL 3 builder or SL 4 developer.

7. After fixing the issue, click **Build Now** to confirm the fix resolves the failure.
8. Document the failure and fix in the pipeline's description field (right panel, **Edit Description**).
9. If the issue cannot be resolved at SL 2 level, escalate to your data engineer with the full error message, pipeline RID, and steps already attempted.

---

**TASK 3-6. DOCUMENT A PIPELINE**

**CONDITIONS:** Pipeline is building successfully; builder is preparing for branch merge or handoff.

**STANDARDS:** The pipeline description will include source name, output dataset path, refresh schedule, data steward POC, creation date, and a plain-English description of what the pipeline does. Known data quality limitations are noted.

**PROCEDURE:**

1. Open the pipeline in Pipeline Builder.
2. In the right panel (no node selected), click **Edit Description**.
3. Enter the required elements:

```
SOURCE: [name and system of origin]
OUTPUT: [Compass path of output dataset]
SCHEDULE: [frequency and UTC time]
DATA STEWARD: [name and unit]
CREATED: [date] by [name, unit]
LAST MODIFIED: [date] by [name, unit]

PURPOSE: [one to two sentence plain-English description of what this
pipeline does and why it exists]

KNOWN LIMITATIONS: [any data quality issues, gaps, or edge cases]
```

4. Click **Save**.

NOTE: Documentation is not optional. Pipelines without descriptions will be flagged during governance reviews. Your replacement needs to understand what you built without having to contact you.

---

# CHAPTER 4 -- ONTOLOGY UI BASICS

## 4-1. What the Ontology Is

The Foundry Ontology is the semantic layer of MSS -- it translates raw data tables into meaningful, interconnected objects. Instead of working with a table of rows and columns, users and applications work with Objects: a `UnitStatus` object, a `SoldierReadiness` object, a `MaintenanceRecord` object. Each Object Type has Properties (like fields), Link Types that connect it to other Object Types, and Actions that allow users to interact with it.

**Build the Ontology last, after your data is clean.** The Ontology reads from your curated dataset. If your curated dataset has schema issues, the Ontology configuration will fail or produce unreliable objects.

NOTE: Before creating any new Object Type, check the Ontology Manager to confirm no existing type already covers your use case. USAREUR-AF maintains established design patterns for common operational Object Types — consult your team lead or data steward before designing from scratch.

> **NOTE:** The Object Types and properties you configure in the Ontology become what operators see in Workshop applications and in Quiver (TM-10, Task 5-3, Use Quiver to Explore Ontology Objects). A poorly designed Object Type — unclear property names, missing properties, wrong cardinality — creates friction for every operator who uses it. Refer to TM-10, Chapter 4 and Task 5-3 to understand the operator experience of your Ontology design before publishing.

---

## 4-2. Ontology Manager Interface Overview

| UI Area | Location | Purpose |
|---|---|---|
| **Object Types panel** | Left sidebar | List of all Object Types in the Ontology |
| **Object Type editor** | Center | Configure properties, primary key, backing dataset |
| **Properties tab** | Center tab | Add/edit/remove properties (columns) |
| **Links tab** | Center tab | Configure Link Types to other Object Types |
| **Actions tab** | Center tab | Configure Actions (write-back operations) |
| **Branch selector** | Top toolbar | Current branch -- always verify before editing |
| **Publish button** | Top toolbar | Merges your branch changes to the main Ontology |

> CAUTION: The Ontology is shared across all Workshop applications in your environment. A change to a shared Object Type affects every Workshop app and every user who reads that Object Type. Always work on a development branch. Never edit the main Ontology branch directly. See Chapter 7 for branching.

---

**TASK 4-1. CREATE AN OBJECT TYPE VIA THE ONTOLOGY UI**

**CONDITIONS:** Builder has Editor access on the Ontology; a curated dataset backing the Object Type is published and has a stable schema; builder is working on a development branch.

**STANDARDS:** The builder will create an Object Type backed by the correct curated dataset, with a primary key configured, at least five meaningful properties added and named to standard, a plain-English description entered, and the Object Type previewing correctly (objects visible, properties show expected values) before the branch is submitted for merge.

**PROCEDURE:**

1. In the left navigation, open **Ontology Manager**.
2. Confirm the branch selector (top toolbar) shows your development branch -- not `main`.
3. Click **New Object Type** (top right of the Object Types panel).
4. Enter the Object Type name in PascalCase singular noun format (e.g., `UnitStatus`, `MaintenanceRecord`).
5. Enter a description: include what this object represents, which data source backs it, the owning unit, and the data steward POC.
6. Click **Create**.
7. The Object Type editor opens. Click the **Properties** tab.
8. Click **Link to Dataset** (or **Backing Dataset**).
9. Browse Compass to your curated dataset and click **Select**.
10. The platform reads the dataset schema and lists available columns. Map columns to properties:
    - To add a property: click **Add Property**, select the column from the dataset, enter a display name (plain English, e.g., "Unit Name" not "unit_nm"), and select the data type (String, Number, Boolean, Date, etc.).
    - Repeat for each column you want to expose as a property.
11. Configure the **Primary Key**: click on the property that uniquely identifies each object (e.g., `unit_id`) and toggle **Primary Key** to ON.
12. Click **Save**.
13. Click **Preview** to confirm objects are visible and property values are correct.

NOTE: The primary key must be unique per object. If your backing dataset has duplicate values in the primary key column, objects will not display correctly. Fix the dataset before configuring the Ontology.

> CAUTION: Do not expose columns containing PII, classified data, or data marked above the authorization level of intended users. Review the data with your Data Steward before configuring properties. Exclude sensitive columns by not adding them as properties.

---

**TASK 4-2. ADD AND CONFIGURE PROPERTIES ON AN OBJECT TYPE**

**CONDITIONS:** Object Type has been created; builder is on a development branch; additional properties need to be added or existing properties renamed.

**STANDARDS:** All added properties have plain-English display names, correct data types, and are formatted appropriately. Properties no longer needed are removed (not just hidden).

**PROCEDURE:**

**Add a new property:**

1. Open the Object Type in Ontology Manager (on your development branch).
2. Click the **Properties** tab.
3. Click **Add Property**.
4. Select the source column from the dataset column list.
5. Enter the display name (plain English, title case: "Report Date" not "rpt_dt").
6. Select the data type from the dropdown.
7. (Optional) Add a description for non-obvious fields.
8. Click **Save Property**.

**Rename a property:**

1. Click the property in the Properties tab.
2. Edit the **Display Name** field.
3. Click **Save**.

NOTE: Renaming a property changes what Workshop apps display -- it does not change the backing column name. Applications referencing the old display name may need updating.

**Remove a property:**

1. Click the property in the Properties tab.
2. Click **Delete Property** (three-dot menu or trash icon).
3. Confirm the deletion.

> CAUTION: Removing a property removes it from all Workshop apps that reference that Object Type. Check with your team lead and review all applications before removing any property from a shared Object Type.

---

**TASK 4-3. CREATE A LINK TYPE VIA THE ONTOLOGY UI**

**CONDITIONS:** Both Object Types to be linked exist and have primary keys configured; a foreign key relationship exists in the underlying data; builder is on a development branch.

**STANDARDS:** The builder will create a Link Type that correctly represents the relationship between the two Object Types, configured with the correct foreign key mapping, and verified by previewing linked objects before submitting for merge.

**PROCEDURE:**

1. Open the source Object Type in Ontology Manager (on your development branch).
2. Click the **Links** tab.
3. Click **Add Link Type**.
4. Enter a link name in camelCase verb phrase format (e.g., `assignedTo`, `reportedBy`, `locatedAt`).
5. Enter a description of the relationship (e.g., "Connects a SoldierReadiness record to the UnitStatus of the Soldier's parent unit").
6. Under **Target Object Type**, select the Object Type this link points to.
7. Under **Foreign Key Configuration**:
   - Select the column in this Object Type's dataset that contains the key linking to the target.
   - Select the primary key property of the target Object Type.
8. Set the **Cardinality**:
   - **Many-to-One** -- many source objects link to one target (most common; e.g., many soldiers in one unit)
   - **One-to-One** -- each source links to exactly one target
   - **Many-to-Many** -- requires a junction dataset; consult SL 3
9. Click **Save Link Type**.
10. Preview the source Object Type: click an individual object and verify linked objects appear in the Links section.

NOTE: If linked objects do not appear in preview, verify that foreign key values in the source dataset match primary key values in the target dataset. A mismatch in data types (integer vs. string) is a common cause of broken links.

NOTE: For complex relationship modeling, consult your team lead or data steward before building. Incorrect link configurations are difficult to fix after they are in production use.

> **NOTE:** If an Ontology design requires any of the following, it exceeds SL 2 scope and must be escalated to a SL 3 advanced builder: (1) Many-to-many Link Types with complex junction logic; (2) Multi-step Actions with conditional routing or approval chains; (3) Derived properties requiring formula logic beyond the basic UI; (4) Ontology models that feed coalition-facing or MPE data products. Refer to TM-30, Chapter 4 (Ontology Design Methodology) for the SL 3 design process, and to TM-30, Chapter 5 (Advanced Action Design via UI) for complex Action patterns.

---

**TASK 4-4. CREATE A BASIC ACTION VIA THE ONTOLOGY UI**

**CONDITIONS:** The target Object Type exists and is correctly configured; builder is on a development branch; the write-back dataset is prepared; Data Steward has approved write-back for this Object Type.

**STANDARDS:** The builder will create a form-based Action that allows authorized users to write a value back to the backing dataset, with required fields marked, input validation configured, and the Action tested end-to-end before requesting a merge.

**PROCEDURE:**

1. Open the target Object Type in Ontology Manager (on your development branch).
2. Click the **Actions** tab.
3. Click **New Action**.
4. Enter the Action name as a plain English verb phrase (e.g., "Submit SITREP Update", "Mark Maintenance Complete").
5. Enter a description: what does this Action do, who should use it, what does it write.
6. Under **Action Type**, select **Modify Object** (updating existing objects) or **Create Object** (creating new ones).
7. Under **Form Configuration**:
   - Click **Add Form Field** for each input the user needs to provide.
   - For each field: select the property it writes to, enter the field label, select the input type (text, dropdown, date picker, checkbox), and toggle **Required** if the field must not be blank.
   - For dropdown fields: enter the list of allowed values.
8. Under **Write Target**: confirm the backing dataset this Action writes to.
9. Under **Permissions**: select which Groups or Roles are allowed to execute this Action. Do not leave Actions open to all users unless explicitly authorized.
10. Click **Save Action**.
11. Test the Action: in the preview, find an object, click the Action name, complete the form, submit, then check the backing dataset to confirm the update was written.

> CAUTION: Actions that write to datasets affect all downstream applications. Before enabling a write-back Action in production, test it on a development branch with test data -- not with live operational records.

NOTE: Complex Action logic (conditional logic, computed fields, multi-step workflows, AIP integration) requires TypeScript and is covered in SL 3. If your Action needs more than a simple form-to-field write, escalate to your data engineer.

---

# CHAPTER 5 -- BUILDING WORKSHOP APPLICATIONS

## 5-1. What Workshop Is

Workshop is MSS's drag-and-drop application builder. Using Workshop, you assemble widgets -- tables, charts, filters, forms, maps -- into applications that end users interact with daily. No code is required.

Workshop applications read from the Ontology. They do not read directly from datasets. This means your Ontology must be correctly configured (Chapter 4) before you begin building in Workshop.

**The build order:**

```
Data (Pipeline Builder) -> Ontology (Object Types, Links, Actions) -> Workshop App
```

> **NOTE:** The Workshop applications you build are consumed by operators working from SL 1. Before building, read TM-10, Chapter 4 (Using Workshop Applications) — specifically Task 4-1 (Open and Orient to a Workshop Application), Task 4-3 (Apply Filters to a Dashboard), Task 4-4 (Navigate Between Modules/Pages), and Task 4-5 (Submit Data Using an Action Form). Build your application so an operator following those SL 1 tasks can use it without confusion.

---

## 5-2. Workshop Widget Library

| Widget | Use For | Key Configuration |
|---|---|---|
| **Table** | Display rows of Object data; sort, filter, select | Object Type source; columns to display; sort order |
| **Chart -- Bar** | Compare values across categories | X-axis (category property), Y-axis (numeric property) |
| **Chart -- Line** | Show trends over time | X-axis (date property), Y-axis (numeric property) |
| **Chart -- Pie/Donut** | Show proportion/composition | Segment property, value property |
| **Metric Tile** | Display a single KPI number | Aggregation (count, sum, avg) on a property |
| **Filter -- Dropdown** | Let users filter displayed data | Property to filter on; allowed values or dynamic |
| **Filter -- Date Range** | Filter by date window | Date property; default range |
| **Filter -- Search** | Free-text search across an Object Type | Property to search; Object Type |
| **Form** | Allow users to submit Actions | Action to invoke; fields from Action configuration |
| **Map** | Display objects at geographic coordinates | Latitude/longitude or address property |
| **Object Explorer** | Show properties of one selected object | Object Type; properties to display |
| **Rich Text** | Add labels, instructions, or context | Static or template-driven text |
| **Container** | Group and layout other widgets | Layout (horizontal, vertical, grid) |
| **Conditional Visibility** | Show/hide widgets based on filter state | Condition expression |

---

## 5-3. Workshop Interface Overview

| UI Area | Location | Purpose |
|---|---|---|
| **Canvas** | Center | Where you place and arrange widgets |
| **Widget Library** | Left panel | Available widgets -- drag to canvas |
| **Widget Properties** | Right panel | Configure the selected widget |
| **Variables panel** | Left panel (tab) | Define app-level variables and filters |
| **Preview mode** | Top toolbar toggle | Switch between edit and user view |
| **Publish button** | Top toolbar | Make the app available to users |
| **Branch selector** | Top toolbar | Confirm you are on a development branch |

> **NOTE:** When designing filter panels and navigation, test them from the operator's perspective. An operator following TM-10, Task 4-3 (Apply Filters to a Dashboard) expects predictable filter behavior and clear labeling. An operator following TM-10, Task 4-4 (Navigate Between Modules/Pages) expects consistent navigation. Test your application against TM-10 Chapter 4 tasks before publishing.

---

**TASK 5-1. CREATE A NEW WORKSHOP APPLICATION**

**CONDITIONS:** Builder has Workshop Builder permission; at least one Object Type exists and is correctly configured; builder is on a development branch; the application's purpose and intended users are defined.

**STANDARDS:** The builder will create a new Workshop application in the correct project folder, named to standard, connected to the appropriate Object Type, with a basic layout (at minimum a title and one data widget) that renders correctly in Preview mode.

**PROCEDURE:**

1. In Compass, navigate to your project's `applications/` folder.
2. Click **New**, then **Workshop Application**.
3. Enter the application name in plain English, unit-appropriate format (e.g., `EUCOM SITREP Dashboard`).
4. Click **Create**. Workshop editor opens.
5. Confirm the branch selector shows your development branch.
6. From the Widget Library (left panel), drag a **Container** widget onto the canvas for your header.
7. Inside the container, drag a **Rich Text** widget. Enter the application title and context text.
8. Drag a **Table** widget below the header container.
9. In the right panel under **Data Source**: click **Select Object Type**, browse to your Object Type, and confirm.
10. Under **Columns**: select the properties to display. Add only the columns end users need.
11. Click **Preview** (top toolbar) to switch to user view and confirm the table renders with data.
12. Switch back to **Edit** mode to continue building.

NOTE: Workshop apps built on development branches are only visible to team members with project access. They are not visible to end users until published (Task 5-6).

---

**TASK 5-2. ADD FILTERS TO A WORKSHOP APPLICATION**

**CONDITIONS:** A Workshop application exists with at least one data widget; the Object Type has filterable properties; builder is in Workshop edit mode on a development branch.

**STANDARDS:** The builder will add filters allowing end users to narrow data by at least two dimensions (e.g., unit and date range), and confirm that selecting a filter value updates all connected widgets in Preview mode.

**PROCEDURE:**

**Add a Dropdown Filter:**

1. From the Widget Library, drag **Filter -- Dropdown** onto the canvas.
2. In the right panel under **Object Type**: select the same Object Type as your data widget.
3. Under **Filter Property**: select the property to filter on (e.g., `unit_name`, `status`, `country_code`).
4. Under **Display Label**: enter a plain-English label (e.g., "Filter by Unit").
5. Under **Default Value**: set a default if appropriate, or leave blank for "Show All."
6. Connect the filter to the data widget: click the data widget, in the right panel click **Filters**, then **Add Filter**, and select the dropdown filter variable.
7. Preview: select a value in the dropdown filter and verify the table updates.

**Add a Date Range Filter:**

1. Drag **Filter -- Date Range** onto the canvas.
2. Select the Object Type and the date property to filter on (e.g., `report_date`).
3. Set a default range appropriate for the data's refresh cadence.
4. Connect to the data widget (same as above).
5. Preview: adjust the date range and verify the table updates.

NOTE: Filters work across all widgets connected to the same Object Type variable. If you want independent filtering per widget, create separate Object Type variables for each widget.

---

**TASK 5-3. ADD CHARTS TO A WORKSHOP APPLICATION**

**CONDITIONS:** A Workshop application exists; Object Type has appropriate numeric and categorical or date properties; builder is in edit mode on a development branch.

**STANDARDS:** The builder will add at least one chart that meaningfully visualizes a metric, correctly configured with labeled axes, and rendering with accurate data in Preview mode.

**PROCEDURE:**

**Add a Bar Chart:**

1. From the Widget Library, drag **Chart -- Bar** onto the canvas.
2. In the right panel under **Data Source**: select the Object Type.
3. Under **X-Axis**: select a categorical property (e.g., `unit_name`, `country`, `status_category`).
4. Under **Y-Axis**: select a numeric property or aggregation (e.g., Count of objects, Sum of `personnel_strength`).
5. Under **Color By** (optional): select a property to color-code bars (e.g., `readiness_status`).
6. Enter a **Chart Title** (e.g., "Readiness by Unit").
7. Connect any applicable filters.
8. Preview to confirm bars display with correct data.

**Add a Line Chart (trend over time):**

1. Drag **Chart -- Line** onto the canvas.
2. Data Source: your Object Type.
3. X-Axis: your date property. Enable **Date Grouping** if available.
4. Y-Axis: your numeric property or count.
5. Title: plain English (e.g., "Daily SITREP Submissions -- Last 30 Days").
6. Connect filters. Preview.

**Add a Metric Tile (single KPI number):**

1. Drag **Metric Tile** onto the canvas.
2. Data Source: Object Type.
3. Metric: select aggregation -- Count, Sum, or Average of a numeric property.
4. Label: plain English (e.g., "Total Units Reporting", "Average Readiness %").
5. (Optional) Configure conditional color: green/yellow/red thresholds.
6. Preview to confirm the value is correct.

---

**TASK 5-4. ADD A FORM (ACTION WIDGET) TO A WORKSHOP APPLICATION**

**CONDITIONS:** An Action is configured on the relevant Object Type (Task 4-4); builder is in Workshop edit mode on a development branch; intended users and permissions are confirmed.

**STANDARDS:** The builder will add a Form widget connected to the correct Action, with all required fields visible and labeled, and confirm that submitting a test entry through the form writes data to the backing dataset.

**PROCEDURE:**

1. From the Widget Library, drag **Form** onto the canvas.
2. In the right panel under **Action**: click **Select Action**, browse to the Object Type, and select the Action (e.g., "Submit SITREP Update").
3. The form fields defined in the Action configuration will appear automatically.
4. Review the field labels. If any are not user-friendly, update them in the Action configuration in Ontology Manager -- changes propagate automatically.
5. (Optional) Add a **Rich Text** widget above the form with instructions for the user.
6. Preview the application. Complete the form with test data and submit.
7. Open the backing dataset in Compass, click **Preview**, and confirm the test row was written correctly.
8. If the row did not appear: check the Action configuration for write target issues. Do not publish until write-back is confirmed working.

> CAUTION: Test Action forms with non-operational test data. Do not submit live operational data through an unvalidated form on a development branch.

---

**TASK 5-5. CONFIGURE LAYOUT AND ORGANIZE A WORKSHOP APPLICATION**

**CONDITIONS:** Core widgets are added; builder is in edit mode; layout needs to be organized for usability.

**STANDARDS:** The application will have a clear visual hierarchy (title, filters, data displays, forms), widgets sized appropriately and aligned, and the layout usable on standard government workstation screen sizes (1920x1080).

**PROCEDURE:**

1. In Workshop settings (gear icon), confirm the layout is set to **Fixed Width** (1200px or 1440px) for desktop use.
2. Use Container widgets for structure: group all filters in one horizontal container at the top; charts in a grid below; table beneath charts.
3. Resize widgets by clicking and dragging widget edges. Standard layout:
   - Header container: full width, 80px height
   - Filter row: full width, 60px height
   - Metric tiles row: full width, divided into 3-4 equal tiles
   - Charts: 50% width side-by-side, or full width for single chart
   - Table: full width, 400-600px height
4. Label all widgets: every chart and metric tile should have a title. Every filter should have a label.
5. Add a Rich Text header: include application name, classification/handling markings, owning unit, data steward POC, and "Data as of [date]."
6. Toggle Preview mode and review at 100% zoom. Check for overlapping widgets, cut-off text, or widgets too small to read.
7. Fix any layout issues before publishing.

NOTE: Test the application at 1920x1080 resolution -- the standard government workstation. Also check whether the layout is functional on tablet-size screens used in some TOC environments.

---

**TASK 5-6. PUBLISH AND SHARE A WORKSHOP APPLICATION**

> **CAUTION:** Before publishing, assess whether your application design is within SL 2 scope. If your design includes: multiple pages with conditional navigation between them; widgets that pass parameters to other widgets; role-based conditional layouts — your application is likely SL 3 scope. Refer to TM-30, Chapter 2 (Advanced Workshop Application Design), specifically Section 2-1 (The Multi-Page Application Model), to determine whether your design should be escalated to a SL 3 qualified builder before publication.

**CONDITIONS:** Workshop application is complete; all widgets render correctly in Preview; branch has been merged (Chapter 7); Data Steward has reviewed and approved publication; access list is defined.

**STANDARDS:** The builder will publish the application, configure access so only authorized users can open it, verify that a test user (View-only access) can access and use the application, and notify intended users.

**PROCEDURE:**

1. Confirm the branch has been merged to main (Chapter 7). You cannot publish from a development branch.
2. Open the Workshop application in Compass (on main branch).
3. Click **Publish** (top toolbar).
4. Review the publish summary: confirm the application name, version number, and Object Types it reads from.
5. Click **Confirm Publish**.
6. After publishing, click **Share** (or **Access Settings**).
7. Under **Who can access this application**:
   - Click **Add**, search for the Group or individual user.
   - Assign **View** access for end users.
   - Assign **Edit** access only to other builders who need to modify the application.
8. Set **Link Sharing** to **Off** unless C2DAO has specifically authorized link-based access.
9. Click **Save**.
10. Test access: ask a colleague with View-only access to confirm they can open and use the application.
11. Notify intended users via official channels. Include what the app shows and who to contact for issues.

> CAUTION: Do not publish applications containing data with markings above the access level of intended users. Confirm classification, handling, and need-to-know before publishing to any group.

NOTE: Compass links to Workshop applications are permanent once published. Do not delete or move a published application without notifying users and coordinating with your Data Steward.

---

# CHAPTER 6 -- ANALYSIS WITH CONTOUR AND QUIVER

## 6-1. Contour vs. Quiver -- When to Use Each

| Tool | Purpose | Best For | SL 2 Scope |
|---|---|---|---|
| **Contour** | Interactive analysis -- build and save views of data | Analysts exploring a dataset; saved analyses shared with a small audience | Build saved analyses using point-and-click interface |
| **Quiver** | Dashboard builder -- assemble charts and metrics into a shareable page | Quick executive dashboards; simple multi-chart views | Build basic dashboards with charts and metric tiles |

Use Contour when you need to explore a dataset, build a table/chart for analysis, and save that view for reuse.

Use Quiver when you need a simple, shareable dashboard with a few metrics and charts and do not need the full Workshop widget library or Action capability.

Use Workshop when you need a full interactive application with filters, forms, Actions, and complex layout.

> **NOTE:** Operators interact with Contour and Quiver using TM-10, Task 5-2 (Use Contour for No-Code Analysis) and Task 5-3 (Use Quiver to Explore Ontology Objects). When building saved analyses or Quiver configurations, understand the operator's analysis workflow from SL 1. Build analyses that support workflows operators actually perform. For advanced Contour capabilities (formula editor, multi-table aggregations, pivot analysis), refer to TM-30, Chapter 7 (Advanced Contour and Quiver).

---

## 6-2. Building Saved Analyses in Contour

**TASK 6-1. BUILD A SAVED ANALYSIS IN CONTOUR**

**CONDITIONS:** Builder has access to the target dataset or Object Type; the analysis purpose and intended audience are defined.

**STANDARDS:** The builder will create a saved Contour analysis answering a specific operational question, containing at least one table view and one chart, saved with a descriptive name, and shared with the intended audience.

**PROCEDURE:**

1. In the MSS left navigation, open **Contour**.
2. Click **New Analysis**.
3. Name the analysis (plain English, descriptive: e.g., `VCORPS SITREP Submission Rate -- Weekly`).
4. Under **Data Source**, click **Add Dataset or Object Type**. Search for and select your target.
5. Contour opens the data view with all columns visible.

**Build a Table View:**

6. The default view is a table showing all rows and columns.
7. To filter rows: click the column header, select **Filter**, then condition and value.
8. To select only needed columns: click **Columns** (top toolbar) and uncheck columns to hide.
9. To sort: click a column header, then **Sort Ascending/Descending**.
10. To group and aggregate: click **Group By**, select the grouping column, then click **Aggregate** and add an aggregation (Count, Sum, Average) on a numeric column.

**Build a Chart View:**

11. Click the **+** tab (next to the current view tab) to add a new view.
12. Select **Chart**.
13. Under **Chart Type**: select Bar, Line, or Pie.
14. Configure X-axis and Y-axis (same logic as Workshop charts -- see Task 5-3).
15. Add a title to the chart tab (double-click the tab name).

**Save and Share:**

16. Click **Save Analysis** (top toolbar).
17. Click **Share**, add authorized users or groups, and assign View access.
18. Copy the Contour analysis link and share with the intended audience via official channels.

NOTE: Contour analyses reflect current data when opened -- they are not live-updating dashboards. For a continuously updated operational view, use Workshop.

---

**TASK 6-2. ADD A PIVOT TABLE IN CONTOUR**

**CONDITIONS:** A Contour analysis exists; builder needs to summarize data across two dimensions (e.g., unit by month, status by country).

**STANDARDS:** The builder will configure a pivot table that correctly summarizes data across the intended dimensions and verify totals against the base table before saving.

**PROCEDURE:**

1. In the Contour analysis, click **+** to add a new view.
2. Select **Pivot Table**.
3. Under **Rows**: select the property to use as row labels (e.g., `unit_name`).
4. Under **Columns**: select the property to use as column headers (e.g., `report_month`, `country`).
5. Under **Values**: select the numeric property and aggregation function (Count, Sum, Average).
6. Review the pivot table. Verify row totals match the base table count for each unit.
7. Save the analysis.

---

## 6-3. Building Basic Quiver Dashboards

**TASK 6-3. BUILD A QUIVER DASHBOARD**

**CONDITIONS:** Builder has access to the target datasets or Object Types; intended dashboard audience is defined.

**STANDARDS:** The builder will create a Quiver dashboard with at least two charts and one metric tile, named correctly, and shared with the appropriate audience.

**PROCEDURE:**

1. In the MSS left navigation, open **Quiver**.
2. Click **New Dashboard**.
3. Name the dashboard (e.g., `USAREUR-AF Readiness Summary -- Weekly`).
4. Click **Add Widget**, then select **Chart**.
5. Configure the chart:
   - Under **Data Source**: select the dataset or Object Type.
   - Select Chart Type (Bar, Line, Pie).
   - Configure X-axis and Y-axis properties.
   - Enter a chart title.
6. Click **Add Widget** again, then select **Metric**.
7. Configure the metric tile:
   - Data source: Object Type.
   - Aggregation: Count, Sum, or Average.
   - Label: plain English name.
   - (Optional) Thresholds: set green/yellow/red values.
8. Arrange widgets by dragging. Resize by dragging widget edges.
9. Click **Save**.
10. Click **Share**, add authorized users, and assign View access.
11. Confirm a test user can open and view the dashboard.

NOTE: Quiver dashboards do not support Actions, complex filters, or form submission. Use Quiver for quick summary views; use Workshop for interactive operational applications.

---

**TASK 6-4. CONFIGURE AUTOMATIC REFRESH ON A QUIVER DASHBOARD**

**CONDITIONS:** Quiver dashboard exists; underlying data updates on a schedule; users need to see current data without manually refreshing.

**STANDARDS:** The builder will configure automatic refresh at an interval appropriate to the data's update cadence, and confirm the last-refreshed timestamp is visible to users.

**PROCEDURE:**

1. Open the Quiver dashboard in edit mode.
2. Click **Dashboard Settings** (gear icon, top right).
3. Under **Auto Refresh**: toggle ON.
4. Set the refresh interval to match or slightly exceed the pipeline schedule. Do not set refresh more frequently than the data actually updates.
5. Under **Show Last Refreshed Timestamp**: toggle ON.
6. Click **Save Settings**.

---

# CHAPTER 7 -- BRANCHING AND ENVIRONMENT MANAGEMENT VIA UI

## 7-1. Why Branching Matters

Branching is how MSS protects production data and applications from work-in-progress changes. Every resource in Foundry -- datasets, Ontology configurations, Workshop apps -- lives on a branch. The `main` branch is what users see and depend on. Your development branch is where you build and test.

**The rule: never edit main directly.** All SL 2 build work happens on a named development branch. When the work is tested and approved, you request a merge into main. A reviewer approves the merge and the changes go live.

Working without a branch is the equivalent of making changes to a live operational system without testing.

> **NOTE:** Operators (SL 1) work only with the main/production branch of MSS resources. They do not see development branches. When you merge your development branch to main, operators immediately see the changes in their next refresh. A faulty merge directly affects operational users. Refer to TM-10, Chapter 8 (Troubleshooting and Support) to understand what operators experience when a bad merge breaks an application. Treat every merge to main as a production release.

---

## 7-2. Foundry Branching Concepts

| Term | Meaning |
|---|---|
| **Branch** | An isolated copy of the Ontology where you can make changes without affecting main |
| **Main branch** | The production branch -- what all users see; never edit directly |
| **Development branch** | Your working branch -- named `dev-[feature]` or `dev-[lastname]` |
| **Check in** | Save your changes to the branch (versioned save with a message) |
| **Merge request** | A formal request to integrate your branch changes into main |
| **Review** | A team lead or designated reviewer approves the merge request |
| **Conflict** | Two branches have made changes to the same resource -- must be resolved before merging |

---

**TASK 7-1. CREATE A DEVELOPMENT BRANCH**

**CONDITIONS:** Builder has Editor access on the Ontology; a build task requires changes to Object Types, Link Types, or Actions.

**STANDARDS:** The builder will create a named development branch before making any Ontology changes, confirm the branch is active (shown in the branch selector), and not make any changes on the main branch.

**PROCEDURE:**

1. Open **Ontology Manager**.
2. In the top toolbar, click the **Branch Selector** (shows the current branch name).
3. Click **New Branch**.
4. Enter the branch name:
   - Feature-based: `dev-sitrep-objecttype`
   - Person-based: `dev-smith` (use only for short-lived personal branches)
5. Under **Branch From**: select `main` (or the base branch your team lead specifies).
6. Click **Create Branch**.
7. Confirm the branch selector now shows your new branch name.
8. Begin Ontology edits only after confirming the correct branch is active.

---

**TASK 7-2. CHECK IN (SAVE) CHANGES ON A BRANCH**

**CONDITIONS:** Builder has made changes to Object Types, Link Types, or Actions on a development branch and needs to save progress.

**STANDARDS:** The builder will check in changes with a descriptive message at logical intervals during the build.

**PROCEDURE:**

1. In Ontology Manager, with your development branch active, click **Check In** (top toolbar).
2. Enter a check-in message describing what you changed:
   - Good: "Add UnitStatus Object Type backed by sitrep_feed_curated; add unit_id primary key and 6 properties"
   - Poor: "changes" or "wip"
3. Click **Confirm Check In**.
4. Verify the changes are saved (the Check In button returns to inactive state).

NOTE: Check in frequently -- at minimum after completing each Object Type, Link Type, or Action configuration. Small, frequent check-ins make it easier to identify and revert specific changes if something breaks.

---

**TASK 7-3. REQUEST A MERGE INTO MAIN**

**CONDITIONS:** Build work on the development branch is complete; all changes have been checked in; builder has tested the changes; team lead is ready to review.

**STANDARDS:** The builder will submit a merge request with a complete description of all changes, dependencies or breaking changes noted, test results included, and the request directed to the correct reviewer. The builder will not approve their own merge request.

**PROCEDURE:**

1. In Ontology Manager, with your development branch active, click **Merge Request** (top toolbar).
2. Under **Merge Into**: confirm the target branch is `main`.
3. Under **Description**, fill in:

```
CHANGES: [list each Object Type, Link Type, Action, or pipeline modified/created]
REASON: [operational need driving this change]
TEST RESULTS: [what you tested and results]
DEPENDENCIES: [any datasets, pipelines, or resources this change depends on]
BREAKING CHANGES: [yes/no; if yes, describe impact on existing applications]
```

4. Under **Reviewer**: select your team lead or designated Ontology reviewer. Do not assign to yourself.
5. Click **Submit**.
6. Notify your reviewer via official channels that a merge request is pending.

> CAUTION: If your changes include modifications to an existing shared Object Type, call out any breaking changes explicitly in the merge request description. The reviewer needs to know whether downstream Workshop applications or analyses may be affected before approving.

---

**TASK 7-4. RESOLVE A BRANCH CONFLICT VIA UI**

**CONDITIONS:** A merge request has been flagged with a conflict; another branch modified the same resource before this merge was approved.

**STANDARDS:** The builder will identify the conflicting resource, understand what change the conflicting branch made, and resolve the conflict by selecting the correct version without discarding authorized changes made by another team member.

**PROCEDURE:**

1. Open the merge request in Ontology Manager.
2. Click **View Conflicts**. The UI shows which resources have conflicts.
3. For each conflicting resource, the UI displays two versions: **Your Changes** (your branch) and **Incoming Changes** (the other branch).
4. Review both versions. Understand what each change does.
5. Resolve the conflict:
   - If your change is correct: select **Keep My Version**.
   - If the incoming change is correct: select **Keep Incoming Version** and plan to redo your work.
   - If both changes are needed: contact your team lead -- multi-field conflicts may require a data engineer (SL 3).
6. After all conflicts are resolved, click **Mark as Resolved**.
7. Resubmit the merge request.

NOTE: When in doubt on a conflict, do not guess. Contact the team member whose branch created the conflict. Resolving a conflict incorrectly can delete another team member's work or produce an inconsistent Ontology state.

---

# CHAPTER 8 -- BUILDER STANDARDS AND GOVERNANCE

## 8-1. Overview

> **NOTE:** Builder standards exist because builders have elevated privileges that operators (SL 1) do not have. Before building, understand the security markings and access controls that govern operator data access (TM-10, Chapter 7, Security, Classification, and Markings). Your applications, pipelines, and Ontology configurations must respect those controls. For SL 3-level governance responsibilities on shared infrastructure, refer to TM-30, Chapter 8 (Data Governance and Stewardship).

Builder standards are not optional. They exist to maintain data quality, operational reliability, and security across the USAREUR-AF MSS environment. All SL 2 builders are accountable for the quality and compliance of everything they publish.

---

## 8-2. Naming Conventions (Consolidated)

See Chapter 2-3 for the full naming conventions table. Critical rules:

1. Dataset paths are permanent -- choose carefully before creating.
2. Object Type names are PascalCase singular nouns -- always.
3. Link Type names are camelCase verb phrases -- always.
4. Pipeline names use kebab-case -- always.
5. Workshop app names are plain English, unit-appropriate -- always.
6. Do not use PII, classified terms, or operational codenames in any resource name or description.

---

## 8-3. C2DAO Approval Triggers

The following actions require explicit C2DAO approval before proceeding. Formal approval must be documented. Do not proceed based on informal authorization.

| Action | Approval Required From | Documentation Required |
|---|---|---|
| Ingest a new external data source | C2DAO + Unit Data Steward | Data source registration form; data handling determination |
| Create a new top-level Project | C2DAO | Project authorization memo |
| Modify a shared Object Type used by multiple units | C2DAO + affected unit Data Stewards | Change notification; impact assessment |
| Publish a Workshop application to users outside your unit | C2DAO | Application publication request |
| Set Project Visibility to Organization-wide | C2DAO | Access policy waiver |
| Enable an Action (write-back) on a shared Object Type | C2DAO + Unit Data Steward | Write-back authorization |
| Schedule a pipeline pulling from a classified or sensitive source | C2DAO + security officer | Data handling certification |

> CAUTION: Proceeding without required approvals is a governance violation. It may result in revocation of builder access, a data incident report, and notification to your chain of command. When in doubt, ask your Data Steward before acting.

---

## 8-4. Data Quality Checklist

Before publishing any pipeline, Ontology configuration, or Workshop application, verify:

**Pipeline / Dataset:**

- [ ] Output dataset has a description (source, owner, refresh schedule, steward POC)
- [ ] Output row count is within expected range (checked against source)
- [ ] No unexpected null values in primary key column
- [ ] No unexpected duplicate rows
- [ ] Date columns contain valid date values (not string representations)
- [ ] Column names follow naming conventions (snake_case, no spaces, no special characters)
- [ ] Data contains no PII in columns not authorized for PII

**Ontology:**

- [ ] Object Type has a description
- [ ] Primary key is correctly configured (unique, non-null)
- [ ] All property display names are plain English
- [ ] Properties containing sensitive data are excluded or restricted appropriately
- [ ] Link Types are tested (linked objects appear in preview)
- [ ] Actions tested with test data (write-back confirmed working)

**Workshop Application:**

- [ ] Application has a title and data classification/handling marking
- [ ] All charts have titles
- [ ] All filters have labels
- [ ] Default filter state shows a useful, non-empty data view
- [ ] Form submissions tested with test data
- [ ] Application tested in Preview mode at 1920x1080
- [ ] Access permissions configured correctly
- [ ] Application tested by a user with end-user access (not builder access)

---

## 8-5. Builder Accountability

As a SL 2 builder, you are personally accountable for:

1. **What you publish.** If your application shows incorrect data to a commander, that is a data quality failure. Test thoroughly.
2. **Who you give access to.** If you assign permissions that allow unauthorized access to operational data, that is a security failure. Follow least-privilege principles.
3. **What you ingest.** If you connect a data source without C2DAO approval, that is a governance violation. Get approval first.
4. **How you document.** If you leave undocumented pipelines and Object Types that break when you PCS, that is a maintainability failure. Document everything.

**The four rules:**

1. Always work on a branch -- never on main/production directly.
2. Test before you publish -- verify data, spot-check values, test with end-user credentials.
3. Follow naming conventions -- every resource must be named to standard.
4. Document your work -- every resource requires a description.

---

# APPENDIX A -- PRE-PUBLISH CHECKLIST

Complete this checklist for every pipeline, Ontology change, and Workshop application before submitting a merge request or publishing.

---

## A-1. Pipeline / Dataset Pre-Publish Checklist

| # | Check | Verified |
|---|---|---|
| 1 | Pipeline name follows kebab-case convention | [ ] |
| 2 | Output dataset is in the correct folder (raw/staging/curated) | [ ] |
| 3 | Pipeline description includes: source, output path, schedule, steward POC, creator, date | [ ] |
| 4 | Pipeline builds successfully (green, no errors) | [ ] |
| 5 | Output row count matches expected range (verified against source) | [ ] |
| 6 | Primary key column has no null or duplicate values | [ ] |
| 7 | Date columns contain valid date values | [ ] |
| 8 | No PII in columns not authorized for PII | [ ] |
| 9 | Schedule is configured and tested (first run completed successfully) | [ ] |
| 10 | On-failure notification configured (builder + team lead) | [ ] |

- [ ] Pipeline complexity is within SL 2 scope (single data source, basic joins, standard transformations). If pipeline requires multi-source deduplication, @incremental patterns, custom Python transforms, or complex error-handling logic — escalate to SL 3 builder before proceeding (TM-30, Chapter 3).

---

## A-2. Ontology Pre-Publish Checklist

| # | Check | Verified |
|---|---|---|
| 1 | Object Type name is PascalCase singular noun | [ ] |
| 2 | Object Type description is complete (what, source, owner, steward, date) | [ ] |
| 3 | Primary key configured (unique, non-null, verified in preview) | [ ] |
| 4 | All property display names are plain English (not raw column names) | [ ] |
| 5 | Data types are correct for each property | [ ] |
| 6 | Sensitive columns excluded or restricted per Data Steward guidance | [ ] |
| 7 | Link Types tested (linked objects visible in preview) | [ ] |
| 8 | All Actions tested with test data (write-back confirmed working) | [ ] |
| 9 | Changes checked in with descriptive commit messages | [ ] |
| 10 | Merge request includes change description, test results, breaking changes noted | [ ] |
| 11 | Merge request assigned to correct reviewer (not yourself) | [ ] |

- [ ] Ontology design is within SL 2 scope (simple Object Types, one-to-one/one-to-many links, single-step Actions). If design requires many-to-many links, multi-step Actions, derived properties with complex logic, or coalition-facing access — escalate to SL 3 before proceeding (TM-30, Chapter 4).

---

## A-3. Workshop Application Pre-Publish Checklist

| # | Check | Verified |
|---|---|---|
| 1 | Application name is plain English, unit-appropriate | [ ] |
| 2 | Application header includes: title, classification/handling marking, owning unit, steward POC | [ ] |
| 3 | All charts have titles | [ ] |
| 4 | All filters have labels; default filter state shows useful data | [ ] |
| 5 | All Metric Tiles have labels and correct aggregations | [ ] |
| 6 | Form submission tested with test data; write-back confirmed | [ ] |
| 7 | Application renders correctly in Preview mode at 1920x1080 | [ ] |
| 8 | Application tested by a user with View-only access (not builder credentials) | [ ] |
| 9 | Access permissions configured per approved access list | [ ] |
| 10 | Link Sharing is OFF (unless C2DAO specifically authorized) | [ ] |
| 11 | Branch merged to main before publishing (not published from dev branch) | [ ] |
| 12 | Users notified of application publication via official channels | [ ] |

---

# APPENDIX B -- COMMON PIPELINE BUILDER PATTERNS

The following patterns address the most common USAREUR-AF data ingestion scenarios.

> **NOTE:** The design patterns in this appendix are SL 2 level — they use Pipeline Builder, Ontology Manager, and Workshop without code. As your data products grow in complexity, some patterns will need to evolve into SL 3 designs. If a pattern requires multi-step Actions, complex Link Type logic, or advanced transform rules, refer to TM-30, Chapter 4 (Ontology Design Methodology) and TM-30, Chapter 3 (Advanced Pipeline Builder) to assess whether SL 3 or SL 4 resources are needed.

---

## B-1. Standard SITREP Ingestion Pattern

**Use case:** Daily SITREP feed arrives as a structured file or shared dataset. Clean, deduplicate, and load to curated.

```
[Source: SITREP Feed]
       |
[Filter: Remove rows where unit_id IS NULL]
       |
[Select Columns: Keep unit_id, unit_name, report_date, status_code, remarks]
       |
[Rename Columns: status_code -> status, remarks -> sitrep_text]
       |
[Deduplicate: on unit_id + report_date (keep most recent)]
       |
[Output: sitrep_feed_curated]
```

**Schedule:** Daily at 0200 UTC.

**Notes:** Verify row count equals number of reporting units. Alert if row count drops below historical average -- this indicates missing unit reports.

---

## B-2. Multi-Source Readiness Consolidation Pattern

**Use case:** Readiness data arrives from multiple unit sources (VCORPS, 21st TSC, 7ATC). Standardize and combine.

```
[Source: VCORPS Feed]   [Source: 21TSC Feed]   [Source: 7ATC Feed]
         |                       |                       |
[Rename: standardize    [Rename: standardize   [Rename: standardize
 to common schema]       to common schema]      to common schema]
         |                       |                       |
         +---------------+-------+-----------------------+
                         |
               [Append (Union): combine all rows]
                         |
               [Deduplicate: on unit_id + report_date]
                         |
               [Output: readiness_consolidated_curated]
```

**Notes:** Each source feed may have slightly different column names. Rename/Select nodes before the Append must produce identical schemas. Verify column names and data types match across all three branches before connecting to the Append node.

---

## B-3. Snapshot-to-Current Join Pattern

**Use case:** A daily snapshot feed contains one row per unit per day. Show only the most recent status for each unit.

```
[Source: readiness_snapshot_raw]
       |
[Aggregate: Group By unit_id; Max(report_date) as latest_date]
       |
[Join: Join back to source on unit_id AND report_date = latest_date]
       |
[Select Columns: remove duplicate date columns from join output]
       |
[Output: readiness_current_curated]
```

**Notes:** If the pipeline runs before all units have reported, the latest date may not represent a complete dataset. Document this limitation in the pipeline description.

---

## B-4. Logistics Maintenance Tracking Pattern

**Use case:** GCSS-A maintenance data needs to be joined with unit assignment data to show which unit owns each item with open work orders.

```
[Source: gcss_a_maint_raw]         [Source: unit_assignment_curated]
         |                                       |
[Filter: status_code IN                [Select: unit_id, bumper_number,
 ('OPEN', 'IN_PROG')]                   unit_name, home_station]
         |                                       |
         +-----------------------+---------------+
                                 |
                   [Join: Inner Join on bumper_number]
                                 |
                   [Output: maint_open_work_orders_curated]
```

**Notes:** Bumper numbers must be formatted consistently in both datasets (case, leading zeros, spacing). Add a Rename node to standardize formatting before the join if source formats differ.

---

# GLOSSARY

**Action** -- A configured, form-based operation in the Foundry Ontology that allows authorized users to write data back to a backing dataset (e.g., submit a SITREP update, mark a maintenance record complete). Configured in Ontology Manager; invoked through Workshop form widgets.

**AOR** -- Area of Responsibility. The geographic and functional area within which a command has authority to act. USAREUR-AF's AOR covers the European theater.

**Backing Dataset** -- The curated dataset whose columns supply the property values for an Object Type in the Ontology. The Ontology reads from backing datasets; it does not store data independently.

**Branch** -- An isolated copy of the Foundry Ontology and associated resources in which a builder can make and test changes without affecting the production (main) environment.

**C2DAO** -- Command and Control Data Analytics Office. The USAREUR-AF organizational authority for data governance, data standards, and MSS build approval. Certain build actions require C2DAO approval before proceeding.

**Cardinality** -- The description of how many of one Object Type relate to another in a Link Type. Many-to-One: many Soldiers assigned to one unit. One-to-One: one readiness record per Soldier per day.

**Check In** -- The act of saving versioned changes to a Foundry branch. Always include a descriptive message explaining what was changed and why.

**Compass** -- The Foundry file and resource explorer. All MSS resources (datasets, pipelines, Workshop apps, Ontology) are navigated and managed through Compass.

**Connector** -- A pre-configured integration point between Foundry and an external data source (SharePoint file, SFTP feed, Army system). Connectors are authorized and managed by the C2DAO; builders select from an approved list.

**Contour** -- The Foundry interactive analysis tool. Allows analysts and builders to build table, chart, and pivot views of datasets and Object Types, saved as reusable analyses.

**Curated Dataset** -- A publication-ready dataset: cleaned, validated, and stable in schema. Ontology Object Types are backed by curated datasets. Never back an Object Type with a raw or staging dataset.

**Data Steward** -- The unit-level accountable official for a specific data domain. First point of contact for any data governance question. Must approve new data source connections and access changes.

**ETL** -- Extract, Transform, Load. The process of pulling data from a source, cleaning or reshaping it, and writing the result to a destination. Pipeline Builder is MSS's no-code ETL tool.

**Foreign Key** -- A column in one dataset that contains values matching the primary key of another dataset. Used to configure Link Types between Object Types.

**Foundry** -- The Palantir data platform on which MSS is built. All tools described in this manual (Pipeline Builder, Ontology Manager, Workshop, Contour, Quiver) are components of Palantir Foundry.

**Link Type** -- A configured relationship between two Object Types in the Foundry Ontology (e.g., a SoldierReadiness object linked `assignedTo` a UnitStatus object). Configured in Ontology Manager.

**Main Branch** -- The production branch of the Foundry Ontology. What all users see and depend on. SL 2 builders never edit main directly. All changes go through a development branch and merge request.

**Merge Request** -- A formal request to integrate changes from a development branch into the main branch. Requires a description of changes, test results, and approval from a designated reviewer.

**MSS** -- Maven Smart System. The USAREUR-AF enterprise AI/data platform, built on Palantir Foundry.

**Object Type** -- A defined class of entities in the Foundry Ontology. Examples: UnitStatus, SoldierReadiness, MaintenanceRecord. Named in PascalCase singular noun format.

**Ontology** -- The semantic layer of Foundry. Defines what the data means: Object Types (what things exist), Link Types (how they relate), and Actions (what users can do). Workshop applications read from the Ontology, not directly from datasets.

**Ontology Manager** -- The Foundry UI tool for creating and managing Object Types, Link Types, and Actions. No code required for SL 2-level configurations.

**Pipeline Builder** -- The Foundry visual, no-code ETL tool. Builders drag and drop source, transform, and output nodes onto a canvas to build data pipelines without writing code.

**Primary Key** -- The column (or combination of columns) that uniquely identifies each row in a dataset and each object in an Object Type. Must be unique and non-null.

**Project** -- The top-level organizational container in Foundry Compass. New projects require C2DAO authorization.

**Property** -- An attribute of an Object Type -- analogous to a column in a table. Configured in Ontology Manager and displayed to users in Workshop applications and Contour analyses. Display names must be plain English.

**Quiver** -- The Foundry quick dashboard builder. Assemble charts and metric tiles into a shareable page. Simpler than Workshop; no Actions or complex filters supported.

**Raw Dataset** -- Data as it arrives from a source system, before any cleaning or transformation. Not suitable for Ontology backing or direct application use.

**Readiness** -- Unit readiness: the assessed ability of a unit to execute its assigned mission. A primary operational data domain in USAREUR-AF MSS.

**Staging Dataset** -- Intermediate data between raw and curated. Cleaned but not yet fully validated or schema-stabilized. Not suitable for Ontology backing.

**USAREUR-AF** -- United States Army Europe and Africa. The Army Service Component Command to USEUCOM and USAFRICOM responsible for theater land operations across the European and African AOR.

**VAUTI** -- The DoD data quality framework: Visible, Accessible, Understandable, Trustable, Interoperable. The standard against which MSS data products are measured.

**Widget** -- A UI component in Workshop. Examples: Table, Chart, Filter, Form, Metric Tile, Map. Drag widgets from the Widget Library onto the Workshop canvas and configure them in the Widget Properties panel.

**Workshop** -- The Foundry drag-and-drop application builder. Builders assemble widgets into interactive applications for end users. Reads from the Ontology (Object Types). No code required for SL 2-level applications.

---

*TM 20-MSS-BLD*

*HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA, Wiesbaden, Germany*

*2026*

*By order of the Commander, United States Army Europe and Africa.*

*DISTRIBUTION RESTRICTION: DRAFT — Not yet approved for distribution.*
