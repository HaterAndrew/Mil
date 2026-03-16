# TRAINING AND EVALUATION OUTLINES (T&EO)
## Maven Smart System (MSS) Training Program
### USAREUR-AF Operational Data Team — C2DAO

---

| | |
|---|---|
| **Document** | Training and Evaluation Outlines |
| **Proponent** | USAREUR-AF C2DAO |
| **Reference POI** | POI-MSS-001 |
| **Reference MTP** | MTP-MSS-001 |
| **Effective Date** | March 2026 |
| **Classification** | UNCLASSIFIED |

---

## HOW TO USE T&EOs

Each T&EO defines the conditions and standards for a specific evaluated task. The evaluator uses these outlines to:
1. Brief the trainee on the task conditions before the evaluation
2. Score each performance measure as GO or NO-GO
3. Determine overall task result

**Scoring:**
- Any step marked **[CRITICAL]** = automatic NO-GO if failed, regardless of other performance
- All other steps: the evaluator applies GO/NO-GO holistically, considering whether the trainee can perform the task to standard independently

---

## Authoritative References

| Publication | Title | Relevance |
|---|---|---|
| AR 350-1 | Army Training and Leader Development | Master regulation for Army training policy; governs evaluation standards and training records |
| TR 350-70 | Army Learning Policy and Systems | TRADOC master regulation governing training evaluation methodology and assessment design |
| ADP 7-0 | Training | Army training doctrine; establishes principles for task-condition-standard evaluation |
| FM 7-0 | Training | Unit training management procedures; provides guidance on GO/NO-GO evaluation and remediation |

> **NOTE:** TR 350-70 is published by TRADOC at adminpubs.tradoc.army.mil, not DA APD.

---

# PART I — TM-10: MAVEN USER T&EOs

---

## T&EO TM10-01: Log In and Navigate to Designated Application

**Task:** Authenticate to MSS Training Environment and navigate to a designated Workshop application.

**Conditions:** Given a government workstation with CAC reader and network access to the MSS Training Environment; trainee has an active account in the Training Environment. The evaluator specifies the name of the target Workshop application.

**Standards:** The trainee will authenticate using CAC/PIV PIN and navigate to the designated Workshop application — without instructor assistance — within 5 minutes of the task being assigned.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Opens browser and navigates to the MSS Training Environment URL (not production MSS) | Navigates directly to correct URL | Opens production MSS; requires correction |
| 2 | Selects correct certificate (PIV Authentication) | Selects correct cert | Selects wrong cert; authentication fails |
| 3 | Enters PIV PIN when prompted | PIN entered correctly | Fails PIN entry; requires reset |
| 4 | Confirms Training Environment landing page is displayed | Training Environment confirmed | Navigates to production environment |
| 5 | Navigates to designated Workshop application using Projects or Compass | Application open within 5 minutes | Requires instructor guidance; exceeds 5 minutes |
| [CRITICAL] 6 | Does not attempt to access the production MSS environment during the task | Training Environment confirmed | Navigates to production |

---

## T&EO TM10-02: Filter Table to Identify Missing Submissions

**Task:** Apply a date filter to a SITREP submission table and identify units with missing submissions.

**Conditions:** Given an open Workshop application containing a SITREP submission table with at least 20 records spanning multiple weeks; the evaluator specifies the filter condition ("filter to last 7 days") and the unit list (15 units expected).

**Standards:** The trainee will apply the correct filter and correctly identify all units with missing submissions — without assistance — within 5 minutes.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Locates the filter control for the date column | Identifies correct filter | Cannot locate filter without assistance |
| 2 | Applies "last 7 days" filter condition | Filter applied; row count reduces | Incorrect filter applied; incorrect row count |
| 3 | Identifies the number of submissions in the filtered view | States correct count | States incorrect count |
| 4 | Correctly identifies missing unit(s) by comparing submission list to provided unit roster | All missing units named | Misses a missing unit or incorrectly identifies a present unit as missing |

---

## T&EO TM10-03: Execute an Authorized Action

**Task:** Execute a status update Action on a specified record in a Workshop application.

**Conditions:** Given a Workshop application with a SITREP status table and an "Update SITREP Status" Action; the evaluator specifies the target record (by name or ID) and the new status value to set.

**Standards:** The trainee will locate the target record, execute the Action with the correct parameters, and verify the status updated — without assistance — within 3 minutes.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Locates the target record in the table (by filtering or scrolling) | Record located | Cannot locate record; requires assistance |
| 2 | Activates the Action button (selects record first if required) | Action button activated | Action button remains grayed; trainee does not diagnose |
| 3 | Completes the Action parameter form with the specified new status | Correct status value entered | Incorrect status entered |
| 4 | Confirms the Action execution when prompted | Executes Action | Dismisses confirmation without executing |
| 5 | Verifies the record status updated in the table | Confirms updated status visible | Does not verify; states "it worked" without confirmation |
| [CRITICAL] 6 | Does not execute the Action on the wrong record | Target record status updated | Wrong record status updated |

---

## T&EO TM10-04: Export Filtered Table to CSV

**Task:** Export a filtered Workshop table to CSV with correct classification labeling.

**Conditions:** Given a filtered Workshop table (filter previously applied); the evaluator specifies the export destination (a designated training output folder).

**Standards:** The trainee will export the filtered table to CSV, confirm row count matches the filtered view, and label the file with the correct classification marking.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Locates the export function for the table widget | Export function found | Cannot locate; requires assistance |
| 2 | Selects CSV as export format | CSV selected | Incorrect format selected |
| 3 | Exports to the designated training output folder (not personal downloads, cloud storage) | Exported to authorized location | Exported to unauthorized location |
| 4 | Confirms exported row count matches filtered table row count | Row count verified | Row count not verified; or count does not match |
| [CRITICAL] 5 | Labels the exported file with the classification marking (UNCLASSIFIED in training) | File labeled | File not labeled; or incorrect label |

---

## T&EO TM10-05: Build a Basic Contour Chart

**Task:** Build a bar chart in Contour from a provided dataset.

**Conditions:** Given access to Contour and a specified dataset (equipment readiness by unit) in the Training Environment; the evaluator specifies the chart type (bar chart), X axis field (unit), and Y axis field (equipment_count); a filter condition is also specified (c_rating IN ['C3','C4']).

**Standards:** The trainee will open the dataset in Contour, build the specified bar chart, apply the specified filter, and describe what the chart shows — without assistance — within 10 minutes.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Opens the specified dataset in Contour | Dataset open in Contour | Cannot open; navigates to wrong dataset |
| 2 | Selects correct X axis field (unit) | Correct field on X axis | Incorrect field; chart does not show unit distribution |
| 3 | Selects correct Y axis field (equipment_count or equivalent) | Correct field on Y axis | Incorrect field |
| 4 | Applies specified filter (c_rating IN ['C3','C4']) | Filter applied; data narrows | Filter not applied or incorrect |
| 5 | Saves the Contour analysis with a descriptive name | Analysis saved with descriptive name | Not saved; or named with default/non-descriptive label |

---

## T&EO TM10-06: Identify Classification Marking and State Authorized Export Procedure

**Task:** Locate the classification marking of a specified dataset and state the authorized export procedure.

**Conditions:** The evaluator identifies a dataset by name; the trainee must locate the classification marking in the dataset properties and state the authorized export destination and handling requirements for that classification level.

**Standards:** The trainee will locate the classification marking in the dataset Properties panel and correctly state the authorized distribution and export procedure — without reference to notes.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Opens the dataset Properties panel | Properties panel open | Cannot locate Properties panel |
| 2 | Reads the classification marking from the Properties panel | Reads marking aloud | States a marking without reading it from the Properties panel |
| [CRITICAL] 3 | States the correct authorized distribution for the marking | Correct distribution stated | States incorrect distribution (e.g., "FOUO data can go to personal email") |
| [CRITICAL] 4 | States the authorized export destination (government systems for FOUO/CUI; no personal cloud storage, no personal email) | Correct destination stated | States an unauthorized destination |
| 5 | States the correct file labeling requirement for the export | Correct labeling stated | No labeling requirement stated |

---

# PART II — TM-20: BUILDER T&EOs

---

## T&EO TM20-01: Create a Foundry Project to Standard

**Conditions:** Given the C2DAO Naming and Governance Standards; a specified project name, classification, and folder structure.

**Standards:** Create a correctly named, marked, and structured project — independently.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Project name follows C2DAO naming convention (unit_description_env format) | Correct name | Spaces, special chars, or format violation |
| [CRITICAL] 2 | Classification marking set | Marking set | No marking |
| 3 | All four required folders created (Datasets, Pipelines, Ontology, Applications) | All four present | Any folder missing |

---

## T&EO TM20-02: Ingest Files and Verify Data Quality

**Conditions:** Two provided files (CSV and XLSX); trainee's Foundry project.

**Standards:** Ingest both files; verify row counts; identify at least one data quality observation per file.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Both files ingested to correct project folder | Both files in Datasets folder | File in wrong location or not ingested |
| 2 | Row count verified for each file (matches source) | Both row counts confirmed | Row count not checked |
| 3 | At least one data quality observation noted per file | Observation documented | No observation documented |

---

## T&EO TM20-03: Build a Clean-and-Transform Pipeline

**Conditions:** Two ingested datasets (equipment and unit lookup); trainee's project.

**Standards:** Build a pipeline that validates, cleans, type-casts, and joins the two datasets; pipeline runs to completion without error; output row count matches expected.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Pipeline has Filter step removing null or invalid rows | Filter step present and configured | No filter; nulls present in output |
| 2 | Pipeline has Rename step with C2DAO-compliant column names | All output columns follow convention | Any column with non-compliant name |
| 3 | Pipeline has CAST steps correcting type errors identified in profiling | Types correct in output | Type mismatch in output |
| 4 | Pipeline has a Join step on `unit_id` producing a joined output | Join step present; correct key | No join; or wrong key; or 0-row output |
| [CRITICAL] 5 | Date column(s) have a computed DATEDIFF column where applicable | Date computation present and correct | Date computation absent or incorrect |
| [CRITICAL] 6 | Pipeline runs to completion without error | No errors in pipeline log | Pipeline errors present (even if output appears) |
| 7 | Output row count matches expected (no unexplained fan-out) | Row count matches | Row count unexplainably inflated (fan-out) |

---

## T&EO TM20-04: Create an Object Type

**Conditions:** Pipeline output dataset with at least 5 columns of different types.

**Standards:** Create an Object Type with all specified properties correctly typed, a Primary Key, and a display name expression.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Object Type created with all required properties | All properties present | Any required property missing |
| [CRITICAL] 2 | All property types correct (STRING, INTEGER, DATE, etc.) | All types correct | Any type incorrect |
| [CRITICAL] 3 | Primary Key property designated | Primary Key set | No Primary Key |
| 4 | Display name expression configured | Display name expression set | No display name expression |
| 5 | Object Type naming follows C2DAO convention | Compliant name | Non-compliant name |

---

## T&EO TM20-05: Create a Link Type

**Conditions:** Two existing Object Types (Equipment and Unit).

**Standards:** Create a Link Type connecting the two Object Types with correct cardinality and directionality.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Link Type created between correct Object Types | Equipment links to Unit | Wrong Object Types |
| 2 | Cardinality set correctly (MANY_TO_ONE) | MANY_TO_ONE | Incorrect cardinality |
| 3 | Directionality correct (Equipment → Unit) | Correct direction | Reversed |

---

## T&EO TM20-06: Configure Ontology Write Step

**Conditions:** Existing Object Type; pipeline with output dataset.

**Standards:** Configure an Ontology write step with correct property mapping; run pipeline; verify Object count in Quiver matches source row count.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Ontology write step added to pipeline | Write step present | No write step |
| 2 | All required properties mapped (pipeline column → Object property) | All properties mapped | Any required property unmapped |
| [CRITICAL] 3 | Primary Key column mapped | PK mapped | PK not mapped (all objects overwrite) |
| [CRITICAL] 4 | Object count in Quiver matches source row count | Count matches | Count does not match (silent data loss) |

---

## T&EO TM20-07: Configure an Action

**Conditions:** Existing Object Type (Equipment).

**Standards:** Create an Action with a parameter, write rule, and Editor-only access restriction; test from Ontology Manager; confirm property updates.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Action created with named parameter | Parameter exists with name and type | No parameter |
| 2 | Write rule maps parameter to correct Object property | Write rule correct | Write rule missing or incorrect |
| [CRITICAL] 3 | Access restricted to Editor role (Viewer cannot execute) | Editor-only restriction set | No restriction; Viewer can execute |
| 4 | Action tested from Ontology Manager; property confirms updated | Property updated after test | Property did not update |

---

## T&EO TM20-08: Build a Workshop Application

**Conditions:** Object Type with at least 5 properties; existing Action.

**Standards:** Create a Workshop application with a table, filter widget, metric widget, and bar chart — each correctly bound to the Object Type.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Application named per C2DAO convention | Compliant name | Non-compliant name |
| 2 | Table widget bound to Object Type; displays required columns | Table shows live Ontology data | Table not bound; static or empty |
| 3 | Filter widget present and connected to table | Filter narrows table correctly | Filter present but not connected; or absent |
| 4 | Metric widget shows C1 count (or specified count) | Metric displays correct value | Metric absent or incorrect |
| 5 | Bar chart widget present with correct X and Y fields | Chart displays correct distribution | Chart absent; or wrong fields |

---

## T&EO TM20-09: Connect Action Button; Verify Execution

**Conditions:** Workshop application from T&EO TM20-08; Action from T&EO TM20-07.

**Standards:** Add an Action button; execute from a selected row; verify table refreshes with updated value.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Action button added to application | Button present | No button |
| 2 | Action executes when row is selected and button clicked | Action fires; confirmation appears | Action does not fire |
| [CRITICAL] 3 | Table refreshes to show updated property value after execution | Table refreshes with correct updated value | Table does not refresh; or wrong value |

---

## T&EO TM20-10: Configure Access Control

**Conditions:** Workshop application; test Viewer-role account provided by evaluator.

**Standards:** Grant Viewer access to test account; confirm Viewer can see application and data but cannot execute Editor-only Action.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Test Viewer account granted access | Access granted | Access not granted |
| 2 | Viewer account can open and view the application | Application visible to Viewer | Application not visible |
| [CRITICAL] 3 | Viewer account cannot execute the Editor-only Action | Action unavailable to Viewer | Viewer can execute Action (access misconfigured) |

---

## T&EO TM20-11: Create Branch and Submit Promotion Request

**Conditions:** Workshop application to modify (change application header text as the branch change).

**Standards:** Create a branch; make the change on the branch; verify branch-only; submit promotion request with complete description; respond to evaluator (as data steward) feedback.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| [CRITICAL] 1 | Branch created BEFORE making the change | Branch exists before change | Change made on main; branch created after |
| 2 | Change visible on branch; main is unchanged | Change is branch-only | Change appears on main |
| 3 | Promotion request submitted with complete description (what changed / why / downstream impact) | Description complete | Description empty or generic ("Updated application") |
| 4 | Evaluator feedback responded to within the evaluation period | Feedback addressed; revision submitted | Feedback ignored |

---

# PART III — TM-30: ADVANCED BUILDER T&EOs

---

## T&EO TM30-01: Design Ontology Schema

**Conditions:** A provided mission scenario description; 30 minutes design time before tool access; 6-item design rubric.

**Standards:** Produce a documented Ontology schema (Object Types with properties and types, Link Types with cardinality, Actions with access restrictions) scoring ≥75% on the rubric with no zero-score item.

| # | Rubric Item | GO | NO-GO |
|---|---|---|---|
| 1 | Domain entities correctly identified (no missing required entities, no phantom entities) | All required entities present | Required entity missing; or phantom entity with no data basis |
| 2 | Primary Keys appropriate (unique per entity, non-null, stable identifier) | PK choices justified | PK choice clearly wrong (name field, unstable ID) |
| 3 | Property types documented and correct | All types specified and correct | Missing types; or significant type errors |
| 4 | Link Type cardinality correct and justified | Cardinality correct; rationale stated | Cardinality wrong; or no rationale |
| 5 | Actions target correct properties with appropriate access control | All Actions have access restriction specified | Any Action with no access restriction |
| 6 | Naming follows C2DAO convention | All names compliant | >2 naming violations |

---

## T&EO TM30-02: Build Multi-Source Pipeline with Append Mode

**Conditions:** Two or three provided datasets; pipeline requirements specified in scenario.

**Standards:** Build a pipeline joining multiple sources; configure Append mode; run twice; verify two distinct snapshot records with different timestamps.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Join step on correct key; correct join type | Join correct | Wrong key; wrong join type; fan-out unresolved |
| [CRITICAL] 2 | Fan-out detected and corrected if present | Fan-out absent; or detected and documented | Fan-out present in output without detection |
| 3 | Append mode configured before first run | Append mode set; confirmed before run | Overwrite mode used; or Append set after first run |
| 4 | Snapshot timestamp column present in output | Timestamp column present | No timestamp |
| [CRITICAL] 5 | Two distinct snapshot records present after two runs | Two records with different timestamps | Only one record (Overwrite mode was used) |

---

## T&EO TM30-03: Configure Append Mode Snapshot Pipeline — *included in TM30-02 above*

---

## T&EO TM30-04: Build Multi-Page Workshop Application

**Conditions:** Existing Object Types from scenario; scenario specifying two pages with variable passing.

**Standards:** Build a multi-page application where Page 1 object selection drives a filtered view on Page 2; conditional formatting on at least one table.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Page 1 (portfolio) shows all units with correct status | Portfolio page correct | Portfolio page empty or incorrect |
| 2 | Object selection on Page 1 navigates to Page 2 | Navigation works | Navigation absent; or goes to wrong page |
| [CRITICAL] 3 | Page 2 content filtered by Page 1 selection | Page 2 shows correct unit's records | Page 2 shows all records regardless of selection |
| 4 | Conditional formatting present (status-based row coloring) | Formatting applied | No conditional formatting |

---

## T&EO TM30-05: Build Contour Workbook with Calculated Deviation Column

**Standards:** Build a Contour workbook showing readiness by battalion with a calculated deviation-from-standard column.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Correct dataset loaded | Correct dataset | Wrong dataset |
| 2 | Deviation column computed (actual - standard or equivalent) | Deviation column present and correct | Column absent or formula incorrect |
| 3 | Workbook saved with descriptive name | Saved with compliant name | Not saved |

---

## T&EO TM30-06: Execute Full C2DAO Promotion Workflow

**Standards:** Branch → change → complete description → submit → respond to steward feedback.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| [CRITICAL] 1 | Promotion description complete (what changed/why/downstream impact) | Complete description | Empty or generic description |
| [CRITICAL] 2 | Evaluator (data steward) feedback responded to | Feedback addressed; resubmission made | Feedback not addressed within evaluation |
| 3 | Change is on branch, not on main, at time of submission | Branch-only change | Change on main |

---

# PART IIIA — TM-40 WFF FUNCTIONAL TRACK T&EOs (TM-40A through TM-40F)

> WFF tracks share a common T&EO task structure. Scenario content (Object Type names, dataset fields, mission context) is adapted per WFF. Evaluators select the scenario package for the applicable WFF track.
>
> **Prerequisite reminder:** TM-40A–F require TM-10, TM-20, and TM-30 (all required).
> Evaluation: 6 tasks, all must pass (Go/No-Go); 3-hour evaluation window.

### WFF Track Scenario Packages

| Track | Course | Primary Domain Scenario | Key Object Types |
|---|---|---|---|
| TM-40A | Intelligence WFF | PMESII pattern analysis; ISR track management; threat object tagging | ThreatReport, ISRCollection, PMESIIObservation |
| TM-40B | Fires WFF | Target tracking pipeline; fire mission status; effects dashboard; CSR coordination | Target, FireMission, EffectsAssessment |
| TM-40C | Movement & Maneuver WFF | Maneuver unit readiness; route status; obstacle tracking; S3 planning dashboard | ManeuverUnit, Route, Obstacle, MovementOrder |
| TM-40D | Sustainment WFF | Class I–IX supply status; LOGSTAT pipeline; requisition tracking; S4 COP products | SupplyRequest, EquipmentReadiness, LOGSTATSubmission |
| TM-40E | Protection WFF | Force protection object types; AT data products; CBRN incident tracking; AMD status | ProtectionEvent, CBRNReport, FPStatusUpdate |
| TM-40F | Mission Command WFF | COP object types; CCIR threshold monitoring; SITREP submission; commander dashboard | SITREPSubmission, CCIRThreshold, COPObject |

> **NOTE:** All six WFF track evaluations use T&EO tasks 40WFF-01 through 40WFF-06. Evaluator selects the scenario package column matching the trainee's track. Critical performance measures for WFF tracks apply uniformly across all six scenario packages.

---

## T&EO 40WFF-01: Build a WFF Pipeline from Provided Exercise Data

**Task:** Ingest a provided WFF-specific dataset; build a Pipeline Builder pipeline that cleans, transforms, and outputs a typed, validated dataset ready for Ontology write.

**Conditions:** Given a provided synthetic WFF dataset (scenario-specific to the track); trainee's Foundry project in the MSS Training Environment.

**Standards:** Pipeline runs to completion without error; output schema is correctly typed; row count matches expected; output is written to the correct project folder.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Pipeline ingests the provided dataset without error | Ingestion completes; row count verified | Ingestion fails or row count not verified |
| 2 | Filter step removes null or invalid rows | Filter step present; nulls absent in output | No filter; nulls present in output |
| 3 | Column types correct (STRING, DATE, INTEGER as applicable) | All types correct | Any type mismatch in output |
| 4 | Computed column present (e.g., status flag, RAG value, DATEDIFF) | Computed column correct | Column absent or formula incorrect |
| [CRITICAL] 5 | Pipeline runs to completion without error | No errors in pipeline log | Pipeline errors present |
| 6 | Output dataset in correct folder with C2DAO-compliant name | Output in Datasets folder; compliant name | Output misplaced or non-compliant name |

---

## T&EO 40WFF-02: Create WFF Object Types and Populate via Pipeline

**Task:** Create the WFF-specific Object Types documented in the scenario and populate them via the pipeline Ontology write step.

**Conditions:** Pipeline output dataset from 40WFF-01; scenario specifying required Object Types and properties.

**Standards:** All required Object Types created with correctly typed properties; Primary Key designated; Object count in Quiver matches source row count.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | All required Object Types created | All Object Types present | Any required Object Type missing |
| [CRITICAL] 2 | All property types correct | All types correct | Any type incorrect |
| [CRITICAL] 3 | Primary Key designated for each Object Type | PK set | No PK (all objects overwrite) |
| 4 | Ontology write step configured; pipeline runs | Write step present; pipeline runs | Write step absent or pipeline fails |
| [CRITICAL] 5 | Object count in Quiver matches source row count | Count matches | Count does not match (silent data loss) |
| 6 | Object Type naming follows C2DAO convention | Compliant names | Non-compliant names |

---

## T&EO 40WFF-03: Configure a WFF Workshop Application

**Task:** Build a Workshop application displaying WFF data with appropriate filters and status indicators.

**Conditions:** Populated Object Types from 40WFF-02; scenario specifying required widgets and filter fields.

**Standards:** Application displays live Ontology data; all required filter widgets functional; status indicators present; classification marking displayed.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Application named per C2DAO convention | Compliant name | Non-compliant name |
| 2 | Table widget bound to correct Object Type; displays required columns | Table shows live Ontology data | Table not bound; static or empty |
| 3 | Filter widget(s) present and functional (narrows table correctly) | Filter narrows correctly | Filter absent or not connected |
| 4 | Status indicator present (conditional formatting or metric widget) | Status indicator functional | Status indicator absent |
| [CRITICAL] 5 | Classification marking present on the application | Marking displayed | Marking absent |

---

## T&EO 40WFF-04: Configure a WFF Action

**Task:** Create an Action to support a WFF workflow (e.g., status update, submission trigger).

**Conditions:** Existing WFF Object Type; scenario specifying the Action type and access restriction.

**Standards:** Action created with correct parameter, write rule, and access restriction; test execution confirms property updates.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Action created with named parameter | Parameter exists with name and type | No parameter |
| 2 | Write rule maps parameter to correct Object property | Write rule correct | Write rule missing or incorrect |
| [CRITICAL] 3 | Access restricted per scenario spec (Editor-only or specified role) | Access restriction set | No restriction; unauthorized role can execute |
| 4 | Action tested; property confirms updated | Property updated after test | Property did not update |

---

## T&EO 40WFF-05: Build a Multi-Page WFF Dashboard

**Task:** Build a multi-page Workshop application where a Page 1 selection drives a filtered detail view on Page 2.

**Conditions:** Object Types populated from 40WFF-02; scenario specifying Page 1 (summary) and Page 2 (unit/element detail) requirements.

**Standards:** Page 1 shows all records with correct status; selecting a record on Page 1 navigates to Page 2 and filters Page 2 data to the selected record's context.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Page 1 (summary/portfolio view) displays all records with correct status | Summary page correct | Summary page empty or incorrect |
| 2 | Selecting a record on Page 1 navigates to Page 2 | Navigation works | Navigation absent or goes to wrong page |
| [CRITICAL] 3 | Page 2 content is filtered by Page 1 selection | Page 2 shows correct record's data | Page 2 shows all records regardless of selection |
| 4 | Conditional formatting present on at least one table (status-based) | Formatting applied | No conditional formatting |

---

## T&EO 40WFF-06: Apply C2DAO Governance (Naming, Marking, Branch, Promotion)

**Task:** Demonstrate compliance with C2DAO data governance requirements for a WFF data product.

**Conditions:** Workshop application from 40WFF-03/05; evaluator will review naming, markings, and require a branch/promote workflow.

**Standards:** Product meets C2DAO naming convention; classification marking present; branch created before change; promotion request submitted with complete description.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Dataset, pipeline, and application names follow C2DAO convention | All names compliant | Any non-compliant name |
| 2 | Classification marking present on dataset and application | Markings present | Any marking absent |
| [CRITICAL] 3 | Branch created BEFORE making the specified change | Branch exists before change | Change made on main; branch created after |
| 4 | Change is on branch only; main is unchanged | Change is branch-only | Change appears on main |
| [CRITICAL] 5 | Promotion request submitted with complete description (what/why/downstream impact) | Description complete | Description empty or generic |

---

# PART IV — TM-40 SPECIALIST TRACK T&EOs

> T&EOs for TM-40 specialist tracks are structured around the practical exercise tasks in each course syllabus.
> Evaluators should refer to the applicable course syllabus for the full Go standard and hard No-Go items.
> Critical items from each track are listed below.

---

## TM-40G (ORSA) — Critical Performance Measures

| Task | Critical Performance Measure | Hard NO-GO |
|---|---|---|
| Time series forecast | 90% confidence intervals present on forecast output | Yes — point estimate without bounds |
| Monte Carlo simulation | ≥1,000 trials; seed set for reproducibility | Yes — fewer than 1,000 trials; no seed |
| Commander brief | Every estimate presented with confidence range | Yes — point estimate without bounds in brief |
| Monte Carlo reproducibility | Evaluator re-runs simulation; output matches | Yes — simulation is not reproducible |

---

## TM-40H (AI Engineer) — Critical Performance Measures

| Task | Critical Performance Measure | Hard NO-GO |
|---|---|---|
| Human review gate | No AIP workflow write occurs without human checkpoint | Yes — write bypasses checkpoint |
| Authorization Checklist | Checklist complete and honest | Yes — checklist misrepresents workflow |
| Evaluator bypass attempt | Evaluator attempts to bypass review gate; trainee's workflow prevents it | Yes — bypass succeeds |

---

## TM-40I (ML Engineer) — Critical Performance Measures

| Task | Critical Performance Measure | Hard NO-GO |
|---|---|---|
| Model calibration | Calibration check performed; documented | Yes — calibration skipped |
| Governance document | Model card includes: assumptions, training data description, limitations, intended use restrictions | Yes — required section missing |
| Drift detection | Evaluator-seeded drift event detected by monitoring pipeline | Yes — drift not detected |

---

## TM-40J (Program Manager) — Critical Performance Measures

| Task | Critical Performance Measure | Hard NO-GO |
|---|---|---|
| Dashboard data-as-of timestamp | Present on every commander-facing dashboard | Yes — absent |
| Append mode pipeline | Two distinct snapshot records after two runs | Yes — only one record |
| Contour portfolio sort | RED items sort to top (`overall_status` ascending) | No (affects task score, not hard No-Go) |

---

## TM-40K (Knowledge Manager) — Critical Performance Measures

| Task | Critical Performance Measure | Hard NO-GO |
|---|---|---|
| AIP review gate | No AIP-generated lesson published without human review | Yes — auto-publish occurs |
| PCS transfer package | Names specific Foundry project, Object Types, pipelines, contacts | Yes — generic boilerplate |

---

## TM-40L (Software Engineer) — Critical Performance Measures

| Task | Critical Performance Measure | Hard NO-GO |
|---|---|---|
| Credential security | No hardcoded credentials in application code | Yes — any hardcoded credential |
| Validator test suite | All 8 test cases pass against trainee's actual code | Yes — any test case fails |
| Pagination | OSDK query iterates all pages (not just page 1) | No (affects task score) |
| Slate error states | Application displays useful error message on Action failure | No (affects task score) |

---

## APPENDIX A — T&EO SCORING SHEET TEMPLATE

```
=========================================================
MSS TRAINING T&EO SCORING SHEET
=========================================================
Trainee Name:        _______________________________________
Course:              _______________________________________
Task/T&EO:           _______________________________________
Evaluation Date:     _______________________________________
Evaluator:           _______________________________________
=========================================================

PERFORMANCE MEASURES

Step | Description                          | GO | NO-GO | N/A | Notes
-----|--------------------------------------|----|-------|-----|------
1    |                                      | [] | []    | []  |
2    |                                      | [] | []    | []  |
3    | [CRITICAL]                           | [] | []    | []  |
4    |                                      | [] | []    | []  |
5    |                                      | [] | []    | []  |

HARD NO-GO ITEMS VIOLATED (if any):
_____________________________________________________________

OVERALL TASK RESULT:  [ ] GO     [ ] NO-GO

EVALUATOR NOTES:
_____________________________________________________________
_____________________________________________________________

EVALUATOR SIGNATURE:  _______________________________________
DATE:                 _______________________________________
=========================================================
```

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*T&EO MSS-TEO-001 | Version 1.0 | March 2026*
