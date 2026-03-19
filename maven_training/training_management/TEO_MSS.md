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
| **Classification** | — |

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
| [CRITICAL] 3 | States the correct authorized distribution for the marking | Correct distribution stated | States incorrect distribution (e.g., "CUI data can go to personal email") |
| [CRITICAL] 4 | States the authorized export destination (government systems for CUI; no personal cloud storage, no personal email) | Correct destination stated | States an unauthorized destination |
| 5 | States the correct file labeling requirement for the export | Correct labeling stated | No labeling requirement stated |

---

## T&EO TM10-07: Explore an Object Type in Quiver

**Task:** Navigate to a specified Object Type in Quiver, apply a filter, and export the filtered view.

**Conditions:** Given access to Quiver in the MSS Training Environment; the evaluator specifies the Object Type name, a filter condition (e.g., status = 'RED'), and the export format.

**Standards:** The trainee will navigate to the specified Object Type in Quiver, apply the filter, confirm the filtered result set, and export the view — without assistance — within 5 minutes.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Opens Quiver and navigates to the specified Object Type | Correct Object Type open in Quiver | Cannot locate Object Type; opens wrong type |
| 2 | Identifies at least 3 properties displayed for the Object Type | Properties identified | Cannot describe Object properties |
| 3 | Applies the specified filter condition | Filter applied; result set narrows | Filter not applied or incorrect |
| 4 | States the count of objects matching the filter | Correct count stated | Incorrect count |
| 5 | Exports the filtered view to the designated format and location | Export completed | Export not completed; requires assistance |

---

## T&EO TM10-08: Submit a Query to an AIP Interface

**Task:** Submit a natural language query to a designated AIP interface and assess the output.

**Conditions:** Given access to a designated AIP Logic workflow or Agent interface in the Training Environment; the evaluator specifies the query to submit and the expected output domain.

**Standards:** The trainee will navigate to the AIP interface, submit the specified query, and state whether the output is reasonable or suspect — without assistance — within 5 minutes.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Navigates to the designated AIP interface | Interface open | Cannot locate; requires assistance |
| 2 | Submits the specified query in the input field | Query submitted | Query not submitted; or wrong interface used |
| 3 | Waits for and identifies the output | Output received and read | Navigates away before output appears |
| [CRITICAL] 4 | States that AIP outputs require human verification and should not be treated as authoritative without review | States verification requirement | Treats AIP output as authoritative without caveat |
| 5 | Identifies at least one limitation of AI-generated output (e.g., may hallucinate, may lack current data) | Limitation identified | Cannot state any limitation |

---

## T&EO TM10-09: Troubleshoot Common Access Issues

**Task:** Diagnose and state the resolution for pre-staged MSS access failures.

**Conditions:** The evaluator presents 2 access failure scenarios from the following set: wrong classification marking, no project access, dataset moved or renamed, certificate selection error, expired account. The trainee uses TM-10 troubleshooting procedures.

**Standards:** The trainee will correctly diagnose the root cause and state the correct resolution action for at least 2 of 2 scenarios — without reference to notes — within 5 minutes.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Correctly diagnoses the first access failure scenario | Root cause correctly identified | Incorrect diagnosis |
| 2 | States the correct resolution action for the first scenario | Correct resolution stated | Incorrect or no resolution stated |
| 3 | Correctly diagnoses the second access failure scenario | Root cause correctly identified | Incorrect diagnosis |
| 4 | States the correct resolution action for the second scenario | Correct resolution stated | Incorrect or no resolution stated |

---

## T&EO TM10-10: Request Access to a Missing Resource

**Task:** Submit a correct access request for a resource the trainee cannot currently access.

**Conditions:** The evaluator directs the trainee to access a dataset or application for which the trainee does not have permissions. The trainee must identify the access gap and submit a request to the unit MSS administrator.

**Standards:** The trainee will identify the access issue, determine the correct request recipient, and submit a correctly formatted access request — without assistance — within 5 minutes.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Identifies the access error (permission denied, not found, or equivalent) | Error correctly identified | Does not recognize access issue; assumes system is broken |
| 2 | States the correct recipient for the access request (unit MSS administrator) | Correct recipient identified | States incorrect recipient (e.g., C2DAO, help desk) |
| 3 | Includes required information in the request: resource name, project, and requested access level | All required information included | Missing resource name or requested access level |

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

## T&EO TM30-07: Build a Multi-Object Quiver Dashboard

**Task:** Build a Quiver dashboard with linked views across multiple Object Types.

**Conditions:** Given at least two populated Object Types with a Link Type between them; scenario specifying the required linked views and filter propagation behavior.

**Standards:** The trainee will build a Quiver dashboard with linked views where filters propagate across Object Types — without assistance — within 15 minutes.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Dashboard contains views for at least two Object Types | Both Object Types displayed | Any required Object Type missing |
| 2 | Views are linked via the defined Link Type | Link traversal functional | Views not linked; data not connected |
| [CRITICAL] 3 | Filters propagate correctly across linked views (filtering one view narrows the other) | Cross-filter propagation confirmed | Filters do not propagate; views are independent |
| 4 | Drill-down from one Object Type to related Objects functions correctly | Drill-down navigates to correct related Objects | Drill-down absent or navigates to wrong Objects |

---

## T&EO TM30-08: Configure an AIP Logic Workflow

**Task:** Configure an AIP Logic workflow with triggers, inputs, and outputs connected to the Ontology.

**Conditions:** Given an existing Object Type and a scenario specifying the workflow purpose (e.g., extract structured fields from text input); human review queue available in the Training Environment.

**Standards:** The trainee will configure the AIP Logic workflow with correct trigger, input binding, and output binding; route output to a human review queue — without assistance — within 20 minutes.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Workflow trigger configured correctly (manual or event-based per scenario) | Trigger fires as specified | Trigger absent or misconfigured |
| 2 | Input binding connects to correct Ontology Object or dataset field | Input binding correct | Input not bound or bound to wrong source |
| 3 | Output produces structured result (JSON or typed fields) | Structured output produced | Unstructured prose output only |
| [CRITICAL] 4 | Output routes to human review queue (not directly to production Objects) | Output enters review queue as Draft | Output writes directly to production without review |
| 5 | Workflow runs without error on provided test input | Successful test execution | Workflow errors on test run |

---

## T&EO TM30-09: Interpret a Data Lineage Graph

**Task:** Read a data lineage graph for a provided dataset and identify upstream sources, transforms, and downstream consumers.

**Conditions:** The evaluator presents a dataset's lineage graph in Foundry; the trainee must interpret the graph and answer questions about the data flow.

**Standards:** The trainee will correctly identify all upstream source datasets, the pipeline transforms applied, and the downstream consumers — without assistance — within 5 minutes.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Opens the lineage graph for the specified dataset | Lineage graph displayed | Cannot locate lineage view |
| 2 | Correctly identifies all upstream source datasets (by name) | All sources named | Any source missed or incorrect |
| 3 | Correctly describes the pipeline transforms applied (filter, join, etc.) | Transform types correctly described | Transforms misidentified or omitted |
| 4 | Correctly identifies downstream consumers (applications, dashboards, or other pipelines) | All consumers named | Any consumer missed |
| 5 | States how a change to an upstream source would propagate through the lineage | Propagation correctly described | Cannot describe downstream impact |

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

---

## TM-40G (ORSA) T&EOs

---

### T&EO 40G-01: Configure Code Workspace and Verify Foundry Connectivity

**Task:** Configure a Python/R Code Workspace with required packages and verify Foundry dataset read/write connectivity.

**Conditions:** Given a Foundry project with Code Workspace access and a test dataset; trainee's workspace in the MSS Training Environment.

**Standards:** Workspace configured with required packages; test dataset read successfully; test write transaction committed and verified.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Required packages installed (statsmodels, scipy, pandas, numpy, matplotlib) | All packages importable | Any required package fails to import |
| 2 | Test dataset read via Spark or pandas; schema and row count confirmed | Dataset read; schema matches | Dataset not readable; connection error |
| [CRITICAL] 3 | Write transaction test: output dataset written and committed | Write transaction committed; output dataset confirmed | Write transaction fails or uncommitted |
| 4 | Random seed set in workspace configuration | Seed set | No seed configured |

---

### T&EO 40G-02: Build and Validate a Regression Model

**Task:** Build a linear regression model for a provided readiness dataset with validation statistics and documented assumptions.

**Conditions:** Given a readiness dataset with at least 6 features; trainee's Code Workspace.

**Standards:** Model built, validated with residual analysis, and output written to Foundry with documented feature selection rationale and validation statistics.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Feature selection rationale documented (not just "best fit") | Rationale documented | No rationale for feature selection |
| 2 | Model trained with reproducible random seed | Seed set; split reproducible | No seed; results not reproducible |
| 3 | Validation statistics computed (R², RMSE, MAE at minimum) | All three statistics present | Any validation statistic missing |
| [CRITICAL] 4 | Residual analysis performed (residual plot or QQ plot) | Residual analysis present | No residual analysis |
| 5 | Model output written to Foundry curated dataset | Output in Foundry | Output not written to Foundry |
| 6 | Assumptions documented (linearity, independence, normality of residuals) | Assumptions listed | No assumption documentation |

---

### T&EO 40G-03: Build a Time Series Forecast with Confidence Bounds

**Task:** Build an ARIMA/SARIMA time series forecast with documented model selection rationale and 90% confidence intervals.

**Conditions:** Given a time series dataset (12+ months of readiness data); trainee's Code Workspace.

**Standards:** Forecast produced with documented stationarity test, model identification rationale, and 90% confidence intervals on all forecast values.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Stationarity test performed (ADF or equivalent) | Test performed; result documented | No stationarity test |
| 2 | Model order selection documented with ACF/PACF rationale | Selection rationale documented | No rationale; arbitrary order selection |
| [CRITICAL] 3 | 90% confidence intervals present on forecast output | Confidence intervals displayed | Point estimate without bounds |
| 4 | Out-of-sample forecast extends at least 6 periods forward | Forecast extends ≥6 periods | Fewer than 6 periods |
| 5 | Forecast plot includes historical data and confidence bounds | Plot with historical and bounds | Plot missing historical context or bounds |

---

### T&EO 40G-04: Run a Monte Carlo Simulation

**Task:** Run a Monte Carlo simulation for a COA comparison scenario with distribution selection rationale and reproducibility.

**Conditions:** Given a COA comparison scenario with defined operational thresholds; trainee's Code Workspace.

**Standards:** Simulation runs ≥1,000 trials with seed set; distribution selection justified; probability at operational threshold computed and reported.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| [CRITICAL] 1 | Minimum 1,000 trials executed | ≥1,000 trials | Fewer than 1,000 trials |
| [CRITICAL] 2 | Random seed set for reproducibility | Seed set; evaluator re-run matches | No seed; simulation not reproducible |
| 3 | Distribution selection justified from data or operational knowledge | Justification documented | No justification for distribution choice |
| 4 | Probability at operational threshold computed (e.g., P(readiness < 80%) at D+30) | Threshold probability computed | No threshold probability |
| 5 | Output distribution plotted with threshold marked | Distribution with threshold visible | No plot; or threshold not marked |

---

### T&EO 40G-05: Formulate and Solve a Linear Programming Problem

**Task:** Formulate and solve a resource allocation LP for a provided constraint scenario.

**Conditions:** Given a resource allocation scenario with defined constraints and objective; trainee's Code Workspace with scipy.

**Standards:** LP correctly formulated with documented constraints; solution computed; sensitivity analysis on binding constraints.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Objective function correctly formulated | Objective matches scenario | Objective incorrect |
| 2 | All constraints correctly formulated and documented | All constraints present | Any constraint missing or incorrect |
| 3 | Solution computed using scipy.optimize.linprog or equivalent | Solution produced | Solver fails or not attempted |
| 4 | Binding constraints identified | Binding constraints stated | Binding constraints not identified |
| 5 | Sensitivity analysis on at least one binding constraint | Sensitivity analysis present | No sensitivity analysis |

---

### T&EO 40G-06: Produce a Commander Brief with Uncertainty Bounds

**Task:** Produce a commander decision support brief from the practical exercise results.

**Conditions:** Results from T&EOs 40G-02 through 40G-05; evaluator plays the role of the commander.

**Standards:** Brief presents all estimates with confidence ranges; no point estimate without bounds; language appropriate for non-technical audience.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| [CRITICAL] 1 | Every estimate presented with confidence range or interval | All estimates bounded | Any point estimate without bounds |
| 2 | Language is appropriate for a non-technical commander audience | Clear, non-technical language | Methods-paper language; jargon-heavy |
| 3 | Assumptions stated for each analytical product | Assumptions communicated | No assumption communication |
| [CRITICAL] 4 | No unqualified predictions (e.g., "will" without a probability qualifier) | All predictions qualified | Unqualified prediction present |
| 5 | Recommendation is supported by the analytical evidence presented | Recommendation traceable to evidence | Recommendation exceeds analytical foundation |

---

## TM-40H (AI Engineer) T&EOs

---

### T&EO 40H-01: Author an AIP Logic Workflow

**Task:** Author an AIP Logic workflow with prompt engineering, conditional chain logic, and structured JSON output.

**Conditions:** Given a dataset with unstructured text records; scenario specifying required output fields; trainee's AIP Logic configuration access.

**Standards:** Workflow produces structured JSON output matching the specified schema; conditional chain handles multiple extraction paths; test run succeeds on provided data.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Prompt template includes explicit military terminology context | Military terminology defined in prompt | No terminology context; relies on LLM defaults |
| 2 | Workflow produces structured JSON output (not prose) | JSON output validated against schema | Unstructured prose output |
| 3 | Conditional chain present (different logic paths based on intermediate output) | Conditional logic functional | Linear workflow only; no conditional branching |
| 4 | Error handling configured (routes malformed output to review queue) | Error handling present | Silent failure on malformed output |
| [CRITICAL] 5 | Workflow runs without error on provided test input | Test run succeeds | Workflow errors on test run |

---

### T&EO 40H-02: Configure an AIP Agent Studio Agent

**Task:** Configure and test an Agent Studio agent with at least two tools and defined memory scope.

**Conditions:** Given existing Object Types and a defined scope of authorized queries; evaluator will test with 5 queries including out-of-scope queries.

**Standards:** Agent responds correctly to in-scope queries; refuses out-of-scope queries; tool calls are logged.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Agent configured with at least two tools | Two tools registered | Fewer than two tools |
| 2 | Agent responds correctly to 5 evaluator queries | Correct responses to in-scope queries | Incorrect response to in-scope query |
| [CRITICAL] 3 | Agent refuses out-of-scope queries | Out-of-scope queries refused | Agent responds to out-of-scope query |
| 4 | Tool calls are logged and visible | Tool call logs present | No logging of tool calls |
| 5 | Memory scope defined and enforced | Memory scope configured | No memory scope; unbounded context |

---

### T&EO 40H-03: Build an LLM Integration Pipeline with RAG

**Task:** Build a pipeline with ontology grounding and retrieval-augmented generation.

**Conditions:** Given a document corpus and Object Types in the Training Environment; scenario specifying retrieval requirements.

**Standards:** Pipeline retrieves correct ontology context for provided queries; output is grounded in retrieved content; evaluator validates grounding.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Retrieval mechanism configured (semantic search or keyword) | Retrieval functional | No retrieval; prompt-only generation |
| 2 | Retrieved context is from the correct Ontology Objects | Context grounded in correct Objects | Context from wrong Objects or fabricated |
| 3 | Output references retrieved content (grounding visible) | Grounding evident in output | Output not traceable to retrieved content |
| [CRITICAL] 4 | Output routed to human review queue before production write | Review queue integration present | Output writes directly to production |
| 5 | Pipeline runs without error on provided test queries | Test queries succeed | Pipeline errors on test queries |

---

### T&EO 40H-04: Implement Human-in-the-Loop Checkpoints

**Task:** Implement human review checkpoints for all write-capable Actions in an AIP workflow.

**Conditions:** Existing AIP Logic workflow with at least one Ontology write Action; evaluator will attempt to bypass the review gate.

**Standards:** No Action writes to production Objects without a visible human review/confirm step; evaluator bypass attempt is blocked.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| [CRITICAL] 1 | No AIP workflow write occurs without human checkpoint | All writes pass through checkpoint | Any write bypasses checkpoint |
| 2 | Review queue displays output for human inspection before write | Output visible in review queue | Review queue absent or empty |
| 3 | Reviewer can approve or reject each output | Approve/reject functional | No reject option available |
| [CRITICAL] 4 | Evaluator bypass attempt is blocked by workflow design | Bypass attempt fails | Bypass succeeds |

---

### T&EO 40H-05: Write Python Transforms for AIP Context

**Task:** Write Python transforms that extract and format Ontology data for AIP Logic context input.

**Conditions:** Given an Object Type with at least 5 properties; scenario specifying the context format required by the AIP Logic workflow.

**Standards:** Transform output matches expected schema; runs without error; military terminology is explicitly defined in context.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Transform extracts correct Object properties | All required properties extracted | Any required property missing |
| 2 | Output formatted to match AIP Logic input schema | Schema match confirmed | Schema mismatch |
| 3 | Military terminology definitions included in context output | Terminology defined | No terminology context; abbreviations unexplained |
| 4 | Transform runs without error | Successful execution | Runtime error |

---

### T&EO 40H-06: Complete the AIP Authorization Checklist

**Task:** Complete the AIP Authorization Checklist for a proposed workflow and identify prohibited use cases.

**Conditions:** Given a proposed AIP workflow design document; TM-40H Appendix A (Authorization Checklist) and Appendix B (Prohibited Use Cases).

**Standards:** Checklist complete and honest; at least 5 prohibited use cases identified by category.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | All checklist items completed | All items addressed | Any checklist item blank |
| [CRITICAL] 2 | Checklist responses are honest and accurate (evaluator verifies against workflow design) | Responses match actual workflow | Checklist misrepresents workflow capability or safety |
| 3 | At least 5 prohibited use cases identified from Appendix B | ≥5 prohibited uses identified | Fewer than 5 identified |
| 4 | Human-in-the-loop requirement documented for all Ontology write operations | HITL documented for all writes | Any write operation without HITL documentation |

---

## TM-40M (ML Engineer) T&EOs

---

### T&EO 40M-01: Configure Code Workspace with GPU and Verify Connectivity

**Task:** Configure a GPU-enabled Code Workspace with required packages and verify Foundry dataset read/write connectivity.

**Conditions:** Given a Foundry project with GPU Code Workspace access and a test dataset.

**Standards:** Workspace configured; GPU allocation confirmed; test dataset read and write transaction verified.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Required packages installed (scikit-learn, PyTorch or TensorFlow, pandas, numpy) | All packages importable | Any required package fails |
| 2 | GPU allocation confirmed (torch.cuda.is_available() or equivalent) | GPU available | GPU not allocated or not detected |
| [CRITICAL] 3 | Write transaction test: output dataset written and committed to Foundry | Write transaction committed | Write transaction fails |
| 4 | Random seed set for reproducibility | Seed set | No seed configured |

---

### T&EO 40M-02: Build a Feature Engineering Pipeline

**Task:** Build a feature engineering pipeline from a provided Foundry dataset meeting documented feature standards.

**Conditions:** Given a raw dataset with null values, type inconsistencies, and potential leakage features; trainee's Code Workspace.

**Standards:** Feature matrix output with nulls handled, encoding applied, scaling applied, and no feature leakage.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Null handling strategy applied and documented (impute, drop, or sentinel) | Nulls handled; strategy documented | Nulls present in output; or no documentation |
| 2 | Categorical encoding applied (one-hot or ordinal as appropriate) | Encoding applied | Raw categorical values in feature matrix |
| 3 | Numeric scaling applied (standard or min-max) | Scaling applied | Unscaled numeric features |
| [CRITICAL] 4 | Leakage audit performed: no feature derived from the label | Leakage audit documented; no leakage | Leakage detected; or audit not performed |
| 5 | Feature matrix written to Foundry curated dataset | Output in Foundry | Output not written |
| 6 | Each feature decision documented in writing | Feature documentation present | No documentation |

---

### T&EO 40M-03: Train and Evaluate a Supervised Model

**Task:** Train and evaluate a supervised model meeting defined accuracy, precision/recall, and calibration thresholds.

**Conditions:** Feature matrix from 40M-02; scenario specifying acceptance thresholds; trainee's GPU Code Workspace.

**Standards:** Model trained with cross-validation; evaluation metrics meet or are compared against acceptance thresholds; calibration check performed.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Train/test split with reproducible random seed | Split reproducible | No seed; not reproducible |
| 2 | Cross-validation performed (k≥5) | Cross-validation results reported | No cross-validation |
| 3 | Evaluation metrics computed (accuracy, precision, recall, ROC-AUC) | All metrics reported | Any metric missing |
| [CRITICAL] 4 | Calibration check performed and documented | Calibration check present | Calibration skipped |
| 5 | Model comparison: at least two models evaluated with documented selection rationale | Two models compared; winner justified | Single model with no comparison |

---

### T&EO 40M-04: Deploy a Model to a Serving Endpoint

**Task:** Deploy a trained model to a Foundry model serving endpoint and verify live inference.

**Conditions:** Trained model from 40M-03; model registry access.

**Standards:** Model deployed; inference endpoint returns predictions for test records; latency within specification.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Model registered in Foundry model registry with version | Model registered and versioned | Model not registered |
| 2 | Serving endpoint deployed and responding | Endpoint responds to inference request | Endpoint not deployed or not responding |
| [CRITICAL] 3 | Inference returns correct predictions for 10 test records | Predictions returned for all 10 records | Predictions fail or return errors |
| 4 | Latency within specification (scenario-defined threshold) | Latency within spec | Latency exceeds threshold |

---

### T&EO 40M-05: Implement a Drift Monitoring Pipeline

**Task:** Implement a monitoring pipeline with data drift detection and alert configuration.

**Conditions:** Deployed model from 40M-04; evaluator will seed a drift event into the monitoring dataset.

**Standards:** Pipeline detects evaluator-seeded drift event; alert routes correctly.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Drift detection method implemented (PSI, KS test, or equivalent) | Drift metric computed | No drift detection |
| 2 | Baseline distribution established from deployment-time data | Baseline documented | No baseline established |
| 3 | Alert threshold defined and documented | Threshold set with rationale | No threshold defined |
| [CRITICAL] 4 | Evaluator-seeded drift event detected by monitoring pipeline | Drift detected and flagged | Drift not detected |
| 5 | Alert routes to correct notification channel | Alert routed correctly | Alert not routed |

---

### T&EO 40M-06: Complete a Model Governance Document

**Task:** Complete a model governance document (model card) meeting USAREUR-AF documentation standards.

**Conditions:** Completed model from 40M-03 through 40M-05; TM-40M governance checklist.

**Standards:** Model card addresses all required sections; limitations are realistic and specific.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| [CRITICAL] 1 | Model card includes: assumptions, training data description, limitations, intended use restrictions | All four required sections present | Any required section missing |
| 2 | Limitations are specific and realistic (not generic boilerplate) | Specific limitations documented | Generic limitations (e.g., "may not be perfect") |
| 3 | Responsible AI declaration included | Declaration present | Declaration absent |
| 4 | Intended use restrictions clearly state when the model should NOT be used | Out-of-scope uses documented | No out-of-scope documentation |

---

## TM-40J (Program Manager) T&EOs

---

### T&EO 40J-01: Design a Program Data Architecture

**Task:** Design a program data architecture (4 Object Types) for a provided scenario.

**Conditions:** Given a program management scenario; 15 minutes design time on paper before building.

**Standards:** Design document covers Program, Milestone, Resource, and Risk Object Types with correct Link Types and properties.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | All four Object Types designed (Program, Milestone, Resource, Risk) | All four present | Any Object Type missing |
| 2 | Link Types specified with correct cardinality (Program → Milestone: ONE_TO_MANY, etc.) | Cardinality correct | Cardinality incorrect |
| 3 | Properties documented with types for each Object Type | Properties and types specified | Properties missing types |
| 4 | Design completed on paper before opening Ontology Manager | Paper design precedes build | Built without paper design |

---

### T&EO 40J-02: Build a Milestone Tracking Pipeline

**Task:** Build a pipeline from a provided IMS spreadsheet with DATEDIFF, milestone variance, and RAG status.

**Conditions:** Given an IMS Excel export with planned/actual completion dates; trainee's Foundry project.

**Standards:** Pipeline runs without error; DATEDIFF variance computed correctly; RAG status computed; data-as-of timestamp present.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | IMS Excel ingested; date columns correctly CAST before arithmetic | CAST applied; types correct | CAST not applied; DATEDIFF fails on text |
| 2 | DATEDIFF variance computed (planned_completion vs. actual_completion) | Variance column correct | Variance absent or incorrect |
| 3 | RAG status computed (RED >30 days late, AMBER >0, GREEN ≤0) | RAG logic correct | RAG absent or logic incorrect |
| [CRITICAL] 4 | Data-as-of timestamp column present (CURRENT_DATE) | Timestamp column present | No data-as-of timestamp |
| 5 | Pipeline runs without error | No errors | Pipeline errors present |

---

### T&EO 40J-03: Build a Milestone Dashboard with Data-As-Of Timestamp

**Task:** Build a Workshop milestone dashboard with RAG conditional formatting and data-as-of timestamp widget.

**Conditions:** Pipeline output from 40J-02; populated Milestone Object Type.

**Standards:** Dashboard displays milestone status with RAG formatting; data-as-of timestamp widget present and visible.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Table widget displays milestones with status | Table functional | Table empty or not bound |
| 2 | RAG conditional formatting applied (RED, AMBER, GREEN row coloring) | Formatting correct | No conditional formatting |
| [CRITICAL] 3 | Data-as-of timestamp widget present and displaying current date | Timestamp visible | No data-as-of timestamp on dashboard |
| 4 | Filter widget allows filtering by program or status | Filter functional | No filter |

---

### T&EO 40J-04: Build a Budget Execution Visualization

**Task:** Build a Quiver visualization showing obligation rate vs. quarterly target.

**Conditions:** GFEBS obligation data loaded; quarterly target specified by evaluator.

**Standards:** Chart displays obligation rate with reference line at quarterly target; at-risk programs identifiable.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Obligation rate chart displays correctly | Chart renders with correct data | Chart absent or incorrect data |
| 2 | Reference line at quarterly target (e.g., Q2 = 50%) | Reference line present at correct value | No reference line |
| 3 | At-risk programs identifiable from the visualization | At-risk programs visually distinguishable | Cannot identify at-risk programs |

---

### T&EO 40J-05: Configure a Snapshot Pipeline in Append Mode

**Task:** Configure an Append mode pipeline for historical trend analysis; run twice; verify cumulative records.

**Conditions:** Pipeline from 40J-02 or separate obligation pipeline; Append mode not yet configured.

**Standards:** Append mode configured before first run; two distinct snapshot records present after two runs.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Append mode configured before first run | Append mode set before run | Overwrite mode used; or Append set after first run |
| 2 | Snapshot timestamp column present | Timestamp column present | No snapshot timestamp |
| [CRITICAL] 3 | Two distinct snapshot records present after two runs | Two records with different timestamps | Only one record (Overwrite mode was used) |

---

### T&EO 40J-06: Produce an IPR Product Meeting PM Dashboard Standards

**Task:** Produce an IPR product from MSS meeting the PM Dashboard Standards Checklist.

**Conditions:** Dashboard from 40J-03; Contour portfolio view; PM Dashboard Standards Checklist.

**Standards:** Product meets all checklist items; Contour portfolio sorts RED to top; product is exportable.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Contour portfolio health matrix present | Portfolio view created | No portfolio view |
| 2 | Portfolio sorted by overall_status ascending (RED at top) | RED items at top | Not sorted; or sorted incorrectly |
| 3 | All PM Dashboard Standards Checklist items met | All items pass | Any checklist item fails |
| 4 | Product exportable as PDF for commander IPR | PDF export successful | Cannot export |

---

## TM-40K (Knowledge Manager) T&EOs

---

### T&EO 40K-01: Design a Knowledge Ontology

**Task:** Design a knowledge ontology (5+ Object Types) for a provided unit KM scenario.

**Conditions:** Given a unit KM scenario; knowledge architecture checklist provided.

**Standards:** Design covers all required Object Types with correct Link Types; evaluated against knowledge architecture checklist.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | All required Object Types present (Document, Lesson, AAR, SOP, ExpertiseProfile) | All five present | Any Object Type missing |
| 2 | Link Types specified between Object Types (Lesson → AAR, Lesson → Unit, SOP → Unit) | Links correct | Links missing or incorrect |
| 3 | Properties documented with types | All properties specified | Properties missing types |
| 4 | Design evaluated against knowledge architecture checklist | Checklist passes | Checklist fails |

---

### T&EO 40K-02: Configure an AAR Submission Form

**Task:** Configure a Workshop AAR submission form that writes to the AAR Object Type.

**Conditions:** Existing AAR Object Type from 40K-01.

**Standards:** Form writes correctly to AAR Object Type; required fields enforced; submission confirmation displayed.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Form includes all required fields (unit, date, event type, location, description, lesson, classification) | All required fields present | Any required field missing |
| [CRITICAL] 2 | Required-field validation fires on empty submission | Validation prevents empty submission | Empty submission accepted |
| 3 | Submission writes to AAR Object Type | Data confirmed in Object Type | Write fails or writes to wrong Object |
| 4 | Submission confirmation displayed to user | Confirmation visible | No confirmation |

---

### T&EO 40K-03: Configure a Lessons-Learned Pipeline

**Task:** Configure a lessons-learned intake pipeline with tagging and distribution logic.

**Conditions:** Provided test data for pipeline; tagging taxonomy specified by evaluator.

**Standards:** Pipeline applies tagging taxonomy; distribution routing logic functional; output reviewed for accuracy.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Tagging taxonomy applied to ingested lessons | Tags applied per taxonomy | No tagging |
| 2 | Deduplication logic present | Duplicate records removed or flagged | Duplicates pass through |
| 3 | Distribution routing logic functional (e.g., classification-based routing) | Routing logic correct | No routing; or routing incorrect |
| 4 | Pipeline runs without error on provided test data | No errors | Pipeline errors present |

---

### T&EO 40K-04: Configure an AIP Summarization Workflow with Review Gate

**Task:** Configure an AIP Logic summarization workflow for document intake with a human review gate.

**Conditions:** Given 5 provided documents; AIP Logic configuration access; human review queue available.

**Standards:** Workflow processes provided documents; output routed to review queue with Draft status; no auto-publish.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Workflow processes provided documents without error | All 5 documents processed | Any document fails processing |
| 2 | Output summaries are structured (not raw prose) | Structured output | Unstructured output |
| [CRITICAL] 3 | All AIP-generated lessons begin as Draft status | All outputs have Draft status | Any output published without review |
| 4 | Human review queue displays outputs for KM review | Review queue populated | Review queue empty |

---

### T&EO 40K-05: Build a Knowledge Browser Application

**Task:** Build a knowledge browser application with search, filter, and drill-down.

**Conditions:** Populated Knowledge Object Types from prior tasks; evaluator will submit 5 test queries.

**Standards:** Application returns correct results for all 5 evaluator test queries.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Search functionality present (keyword or semantic) | Search returns results | No search capability |
| 2 | Filter by tag, unit, and date functional | All three filters work | Any filter non-functional |
| 3 | Drill-down from search result to full lesson/AAR text | Drill-down functional | Drill-down absent |
| [CRITICAL] 4 | Application returns correct results for all 5 evaluator test queries | 5 of 5 queries return correct results | Any query returns incorrect results |

---

### T&EO 40K-06: Produce a PCS Knowledge Transfer Package

**Task:** Build and demonstrate a PCS knowledge transfer package for a specific role.

**Conditions:** Given a role description and TM-40K Ch 9 transfer package requirements.

**Standards:** Package contains all required documentation; names specific Foundry artifacts; not generic boilerplate.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Key person dependency analysis completed | Dependencies identified | No dependency analysis |
| [CRITICAL] 2 | Package names specific Foundry projects, Object Types, pipelines, and contacts | Specific artifacts named | Generic boilerplate ("see Foundry for details") |
| 3 | Data quality status documented for each artifact | Quality status present | No quality documentation |
| 4 | Package reviewed and approved by instructor | Instructor approval | Not reviewed |

---

## TM-40L (Software Engineer) T&EOs

---

### T&EO 40L-01: Authenticate and Execute a Paginated OSDK Query

**Task:** Authenticate to Foundry Ontology via OSDK and execute a paginated, filtered object query.

**Conditions:** Given an Object Type with >50 objects; evaluator specifies filter condition; trainee's OSDK development environment.

**Standards:** Query returns correct records; pagination handles all pages; no hardcoded credentials.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | OSDK client initialized with correct authentication | Client authenticated | Authentication fails |
| 2 | Filter applied as specified by evaluator | Correct records returned | Wrong records; filter not applied |
| [CRITICAL] 3 | Pagination iterates all pages (not just page 1) | All pages retrieved | Only page 1 retrieved; results truncated |
| [CRITICAL] 4 | No hardcoded credentials in application code | No credentials in code | Any hardcoded credential present |

---

### T&EO 40L-02: Execute an Action via OSDK with Validation

**Task:** Execute an Action via OSDK with full validation logic and structured error handling.

**Conditions:** Given an Action that writes to an Object Type; evaluator provides valid and invalid input scenarios.

**Standards:** Valid Action executes successfully; invalid input triggers correct structured error response.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Valid Action executes and returns success | Action succeeds on valid input | Action fails on valid input |
| 2 | Invalid input triggers validation error (not unhandled exception) | Structured error returned | Unhandled exception; or no validation |
| 3 | Error response includes specific field and message | Error identifies failing field | Generic error only |
| 4 | Async response pattern used (task ID polling for completion) | Async pattern implemented | Synchronous block; no polling |

---

### T&EO 40L-03: Build a TypeScript Function on Objects

**Task:** Build a TypeScript Function implementing a computed property.

**Conditions:** Given an Object Type with at least 5 properties; scenario specifying the computed property logic.

**Standards:** Computed property returns correct values for 10 test objects; edge cases handled.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Function compiles without TypeScript errors | No compilation errors | TypeScript errors present |
| 2 | Computed property returns correct values for 10 test objects | All 10 correct | Any incorrect value |
| 3 | Edge cases handled (null properties, boundary values) | Edge cases produce correct results | Edge case produces error or incorrect value |
| 4 | Bulk query pattern used (not per-object API calls) | Bulk pattern | N+1 query pattern present |

---

### T&EO 40L-04: Write and Test a TypeScript Action Validator

**Task:** Write a TypeScript Action validator with at least 3 distinct validation conditions and test with 8 test cases.

**Conditions:** Given an Action that writes to an Object Type; scenario specifying validation rules; 8 provided test cases (4 valid, 4 invalid).

**Standards:** Validator passes/blocks correctly in all 8 test cases; each test case paired with expected error message.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | At least 3 distinct validation conditions implemented | ≥3 conditions | Fewer than 3 conditions |
| 2 | Each condition produces a specific, descriptive error message | Specific error messages | Generic or missing error messages |
| [CRITICAL] 3 | All 8 test cases pass (4 valid accepted, 4 invalid blocked with correct errors) | 8 of 8 pass | Any test case fails |
| 4 | Cross-field validation present (e.g., if status=DEPLOYED, location must be non-null) | Cross-field logic present | No cross-field validation |

---

### T&EO 40L-05: Build a Slate Application with Live Ontology Data

**Task:** Build a Slate application integrated with the Foundry API displaying live ontology data.

**Conditions:** Given Object Types and Actions from prior tasks; scenario specifying UI requirements.

**Standards:** Application renders correctly; data refreshes on state change; error states display useful messages.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Application renders and displays live Ontology data | Data displayed | Application does not render; or static data |
| 2 | Data refreshes on state change (Action completion triggers refresh) | Refresh on state change | Manual refresh required |
| 3 | Error state displays useful error message on Action failure | Useful error message displayed | No error display; or generic "error occurred" |
| [CRITICAL] 4 | No hardcoded credentials in application code | No credentials in code | Any hardcoded credential present |

---

### T&EO 40L-06: Complete a C2DAO Code Review and Deployment Workflow

**Task:** Complete a code review and deployment workflow for a provided OSDK application.

**Conditions:** Given a completed application from prior tasks; C2DAO deployment checklist.

**Standards:** PR created; review comments addressed; deployment checklist completed end-to-end.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Pull request created with descriptive title and summary | PR created | No PR |
| 2 | Review comments addressed (evaluator provides at least 2 comments) | Comments addressed | Comments ignored |
| 3 | Deployment checklist completed end-to-end | All checklist items addressed | Any checklist item incomplete |
| [CRITICAL] 4 | No hardcoded credentials or tokens in committed code | No credentials | Credentials present in committed code |

---

## TM-40N (UI/UX Designer) T&EOs

---

### T&EO 40N-01: Produce a User Research Plan

**Task:** Produce a user research plan including research questions, target population, interview guide, and contextual inquiry protocol.

**Conditions:** Given a design scenario specifying the user population and operational context; SCD methodology reference.

**Standards:** Research plan is complete and actionable; interview guide uses SCD semi-structured questions; contextual inquiry protocol addresses operational environment constraints.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Research questions clearly defined and tied to design decisions | Questions defined | No research questions |
| 2 | Target user population identified with role, rank range, and operational context | Population specified | Generic or undefined population |
| 3 | Interview guide uses SCD semi-structured questions (not leading or yes/no) | SCD questions present | Leading or yes/no questions |
| 4 | Contextual inquiry protocol addresses operational environment (classification, lighting, noise, screen size) | Environment constraints addressed | No contextual inquiry protocol |

---

### T&EO 40N-02: Design an Information Architecture

**Task:** Design an information architecture for an MSS dashboard passing the "glance, scan, commit" test.

**Conditions:** Given a WFF scenario specifying the user's decision workflow; design tools available.

**Standards:** Design demonstrates decision-first hierarchy; passes 2-second (glance), 10-second (scan), and 30-second (commit) review levels.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Decision-first hierarchy documented (decision → supporting info → priority order → layout) | Hierarchy documented | No hierarchy; widget-palette-first design |
| [CRITICAL] 2 | Design passes glance test: overall status identifiable within 2 seconds | Status identifiable at glance | Status not identifiable without reading |
| 3 | Design passes scan test: areas needing attention identifiable within 10 seconds | Attention areas identifiable | Cannot identify attention areas within 10 seconds |
| 4 | Design passes commit test: drill-down to decision-supporting detail within 30 seconds | Detail accessible within 30 seconds | Detail requires >30 seconds to reach |

---

### T&EO 40N-03: Build an Interactive Prototype

**Task:** Build a clickable interactive prototype of a data entry workflow with all five states designed.

**Conditions:** Given a data entry scenario; design tools available.

**Standards:** Prototype is testable; all five states represented (default, loading, empty, error, success); user can walk through primary task flow without designer explanation.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Prototype is clickable and navigable (not static mockup) | Prototype navigable | Static mockup only |
| 2 | Default state displays correctly | Default state present | No default state |
| 3 | Loading, empty, and success states represented | All three states present | Any state missing |
| [CRITICAL] 4 | Error state displays useful feedback (not blank or generic) | Error state with feedback | No error state; or blank/generic error |
| 5 | User can complete primary task flow without designer explanation | Task flow completable independently | Requires explanation to navigate |

---

### T&EO 40N-04: Produce a Design Handoff Package

**Task:** Produce a design-to-development handoff package for a TM-40L SWE or TM-30 builder.

**Conditions:** Completed prototype from 40N-03; handoff template provided.

**Standards:** Package is implementation-ready; a SWE can implement without asking clarifying questions.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Annotated mockups present with widget specifications | Mockups annotated | No annotations |
| [CRITICAL] 2 | Data binding documentation present (widget → Object property mapping) | Data binding documented | No data binding documentation |
| 3 | Interaction specification covers all states (default, loading, empty, error, success) | All states specified | Any state unspecified |
| 4 | Accessibility requirements documented | Accessibility notes present | No accessibility documentation |

---

### T&EO 40N-05: Complete an Accessibility Audit

**Task:** Complete an accessibility checklist covering contrast, keyboard navigation, text alternatives, and screen reader compatibility.

**Conditions:** Prototype from 40N-03; MSS accessibility checklist.

**Standards:** Audit identifies at least 3 accessibility issues; WCAG 2.1 AA criteria applied.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Automated accessibility scan completed | Scan results documented | No scan performed |
| 2 | Manual keyboard navigation test completed | Keyboard test documented | No keyboard test |
| [CRITICAL] 3 | At least 3 accessibility issues identified with severity and WCAG criterion | ≥3 issues identified | Fewer than 3 issues; or no WCAG reference |
| 4 | Color-only encoding identified and flagged (redundant indicators required) | Color-only issues flagged | Color-only encoding not identified |

---

### T&EO 40N-06: Execute a Usability Test

**Task:** Execute a usability test with 5+ participants, documenting task completion rates and severity-rated findings.

**Conditions:** Prototype from 40N-03; 5 paired trainees serving as test participants.

**Standards:** Test executed with think-aloud protocol; task completion rates documented; findings severity-rated.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Think-aloud protocol used during test sessions | Think-aloud captured | No think-aloud; silent observation only |
| 2 | Task completion rates documented per task | Rates documented | No completion rates |
| 3 | Findings severity-rated (Critical, Major, Minor, Cosmetic) | Severity ratings applied | No severity ratings |
| [CRITICAL] 4 | Design recommendations proposed for Critical and Major findings | Recommendations present for Critical/Major | No recommendations for Critical/Major findings |

---

## TM-40O (Platform Engineer) T&EOs

---

### T&EO 40O-01: Deploy a Workload to Kubernetes

**Task:** Deploy a workload to a Kubernetes cluster with declarative manifests, resource management, and health checks.

**Conditions:** Given a container image and deployment requirements; training Kubernetes cluster.

**Standards:** Workload deployed; resource requests and limits configured; liveness and readiness probes functional.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Workload deployed using declarative YAML manifests (kubectl apply) | Deployment successful | Imperative deployment; or deployment fails |
| 2 | Resource requests and limits configured | Both requests and limits set | No resource configuration |
| [CRITICAL] 3 | Liveness and readiness probes configured and passing | Both probes configured and healthy | No health probes; or probes failing |
| 4 | Labels applied per standard (app, env, team at minimum) | All required labels present | Missing required labels |

---

### T&EO 40O-02: Configure a GitOps Workflow with Drift Detection

**Task:** Configure a GitOps controller, deploy by commit, and demonstrate drift detection and revert.

**Conditions:** Given a GitOps controller (ArgoCD or equivalent) and training cluster; evaluator will manually create drift.

**Standards:** Application deployed via Git commit; evaluator-created drift detected and reverted automatically.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | GitOps controller configured and syncing from Git repository | Controller synced | Controller not configured or not syncing |
| 2 | Application deployed by committing configuration to Git | Deployment via commit | Manual kubectl apply required |
| [CRITICAL] 3 | Evaluator-created drift detected and reverted by controller | Drift reverted automatically | Drift persists; controller does not revert |
| 4 | Drift alerts configured | Alert fires on drift | No drift alerting |

---

### T&EO 40O-03: Harden a Container Image

**Task:** Harden a container image starting from an Iron Bank base with multi-stage build, non-root execution, and capability dropping.

**Conditions:** Given an application requiring containerization; Iron Bank base images available.

**Standards:** Container passes vulnerability scan; runs as non-root; capabilities dropped.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Iron Bank base image used (not Docker Hub) | Iron Bank base | Docker Hub or unauthorized base |
| 2 | Multi-stage build: build tools not in production image | Multi-stage build confirmed | Build tools present in production image |
| [CRITICAL] 3 | Container runs as non-root user | Non-root execution confirmed | Container runs as root |
| 4 | Linux capabilities dropped (ALL dropped; required added back) | Capabilities dropped | No capability management |
| 5 | Vulnerability scan passes (no unpatched CRITICAL/HIGH) | Scan passes | CRITICAL/HIGH vulnerability with available fix |

---

### T&EO 40O-04: Build a CI/CD Pipeline with Security Gates

**Task:** Build a CI/CD pipeline with defined stages, security scanning gates, and artifact management.

**Conditions:** Given an application repository; CI/CD tooling available.

**Standards:** Pipeline includes security gates; a gate blocks deployment when vulnerability is detected.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Pipeline stages defined (build, test, scan, deploy) | All stages present | Any stage missing |
| 2 | Secrets detection gate present | Secrets scan configured | No secrets detection |
| [CRITICAL] 3 | Security gate blocks deployment when vulnerability detected (demonstrated) | Gate blocks on detected vulnerability | Gate does not block; security theater |
| 4 | Artifacts stored in artifact repository with version tags | Artifacts versioned | No artifact management |

---

### T&EO 40O-05: Implement a Deployment Strategy with Rollback

**Task:** Implement rolling update and blue/green deployment strategies; execute a rollback from each.

**Conditions:** Deployed workload from 40O-01; training cluster.

**Standards:** Both strategies demonstrated; rollback executed from each; rollback restores previous state.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Rolling update deployed with zero downtime | Rolling update succeeds | Downtime during rolling update |
| 2 | Rollback from rolling update restores previous version | Rollback successful | Rollback fails or does not restore |
| 3 | Blue/green deployment executed with traffic switch | Traffic switched to new version | Blue/green not implemented |
| [CRITICAL] 4 | Rollback from blue/green restores previous version | Rollback successful | Rollback fails |

---

### T&EO 40O-06: Deploy an Application Across an Air Gap

**Task:** Package and deploy an application to a simulated air-gapped cluster using bundled artifacts only.

**Conditions:** Simulated air-gapped training namespace (no external egress); bundling tools available.

**Standards:** Application deployed using bundled artifacts only; health checks pass; no external network access required.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Application bundled with all container images and configuration | Bundle complete | Bundle missing dependencies |
| 2 | Bundle imported to internal registry | Import successful | Import fails |
| [CRITICAL] 3 | Application deploys and health checks pass with no external network access | Application healthy | Deployment fails due to missing dependency |
| 4 | Deployment procedure documented for repeatable execution | Procedure documented | No documentation |

---

# PART V — TM-50 ADVANCED SPECIALIST TRACK T&EOs

> TM-50 T&EOs evaluate advanced competencies building on the corresponding TM-40 track. All TM-50 practical exercises include multi-part evaluations with product review components.
>
> **Prerequisite reminder:** Each TM-50 track requires the corresponding TM-40 track (e.g., TM-50G requires TM-40G).

---

## TM-50G (Advanced ORSA) T&EOs

---

### T&EO 50G-01: Implement a Bayesian Readiness Model

**Task:** Implement a Bayesian model with justified prior, posterior estimation, and 90% credible intervals.

**Conditions:** Given an operational readiness dataset; trainee's Code Workspace with PyMC or equivalent.

**Standards:** Prior selection justified and documented in assumption register; posterior with 90% credible interval computed.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Prior selection justified with documented rationale (not default uniform without justification) | Prior justified | No justification for prior |
| [CRITICAL] 2 | Posterior estimated with 90% credible interval | Credible interval present | Point estimate without bounds |
| 3 | Assumption register entry for the prior | Assumption documented | No assumption register entry |
| 4 | Hierarchical model applied if multi-echelon data present | Hierarchical approach used | Single-level model on multi-echelon data |

---

### T&EO 50G-02: Conduct Network Vulnerability Analysis

**Task:** Construct a supply chain network graph, compute centrality measures, and identify critical nodes.

**Conditions:** Given a logistics dataset with node/arc structure; trainee's Code Workspace.

**Standards:** Network graph constructed; betweenness centrality computed; top 3 critical nodes identified with operational risk translation.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Network graph constructed with correct nodes and arcs | Graph matches logistics data | Graph incorrect or incomplete |
| 2 | Betweenness centrality computed for all nodes | Centrality computed | No centrality computation |
| [CRITICAL] 3 | Top 3 critical nodes identified with operational risk rating | Critical nodes identified with risk | No operational risk translation |
| 4 | Node removal impact analysis performed (flow degradation measured) | Impact analysis present | No impact analysis |

---

### T&EO 50G-03: Compute Pareto Frontier for COA Comparison

**Task:** Formulate a two-objective optimization, compute the Pareto frontier, and name 3 COA points.

**Conditions:** Given a two-objective scenario (e.g., minimize cost vs. minimize risk); trainee's Code Workspace.

**Standards:** Pareto frontier computed and plotted; 3 COA points named with operational descriptions.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Both objectives quantified with formulas from operational data | Objectives quantified | Objectives vague or unquantified |
| 2 | Pareto frontier computed and plotted | Frontier plotted | No frontier computation |
| [CRITICAL] 3 | At least 3 COA points named with operational descriptions | 3 COAs named | Fewer than 3 COAs; or no operational naming |
| 4 | Recommendation stated with explicit assumption caveat | Recommendation with caveat | Recommendation without caveat |

---

### T&EO 50G-04: Produce a GO/SES-Ready Analytical Product

**Task:** Produce a complete analytical product meeting TM-50G product standards for GO/SES audience.

**Conditions:** Results from 50G-01 through 50G-03; TM-50G product standards checklist.

**Standards:** Product includes BLUF, uncertainty quantification, assumption register, limitations, and peer review signature block.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | BLUF present with result, confidence level, and key assumption | BLUF complete | BLUF missing or incomplete |
| [CRITICAL] 2 | Uncertainty quantified on all estimates (credible intervals, confidence ranges) | All estimates bounded | Any estimate without bounds |
| [CRITICAL] 3 | Assumption register present and complete | Assumption register present | No assumption register |
| 4 | Limitations register present with specific invalidation conditions | Limitations present | No limitations; or generic |
| [CRITICAL] 5 | Peer review signature block present and completed | Peer review block present | No peer review block |
| 6 | All models reproducible (seeds set, code runs without modification) | Reproducible | Not reproducible |

---

## TM-50H (Advanced AI Engineer) T&EOs

---

### T&EO 50H-01: Design an Enterprise RAG Pipeline Architecture

**Task:** Design a RAG pipeline architecture with chunking strategy, metadata schema, and retrieval evaluation harness.

**Conditions:** Given a document corpus and query set; training environment with embedding model access.

**Standards:** Architecture design justified; retrieval evaluation harness built and producing MRR scores.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Chunking strategy selected with documented tradeoff rationale | Strategy justified | No rationale for chunking choice |
| 2 | Metadata schema defined (source, date, section, classification) | Metadata schema present | No metadata schema |
| [CRITICAL] 3 | Retrieval evaluation harness built with ground truth query set | Harness produces MRR | No evaluation harness |
| 4 | OPSEC implications of embedding model addressed (external API vs. on-premises) | OPSEC addressed | OPSEC not considered |

---

### T&EO 50H-02: Design a Multi-Agent System

**Task:** Implement a multi-agent system with orchestrator, specialized workers, and failure recovery.

**Conditions:** Given at least three query types requiring different processing; training Agent Studio access.

**Standards:** Orchestrator routes correctly; failure recovery demonstrated; circular dependency prevention present.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Orchestrator routes queries to correct worker agents | Routing correct | Misrouted queries |
| 2 | At least two specialized worker agents with defined capabilities | Two workers present | Fewer than two workers |
| [CRITICAL] 3 | Failure recovery path implemented (timeout, fallback, dead-letter queue) | Recovery path functional | No failure recovery |
| 4 | Tool output schemas validated before hand-off | Schema validation present | No output validation |

---

### T&EO 50H-03: Design an AI Governance Framework

**Task:** Design a human-in-the-loop governance framework for a production AI system.

**Conditions:** Given a proposed production AI system design; governance framework template.

**Standards:** Human review gates placed on all consequential outputs; audit logging designed; rollback procedure documented.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| [CRITICAL] 1 | Human review gates placed on all consequential outputs (Ontology writes, commander products) | All consequential outputs gated | Any consequential output ungated |
| 2 | Audit log schema designed (query, output, reviewer, decision, timestamp) | Audit schema present | No audit logging |
| 3 | Rollback procedure documented (≤15 min recovery target) | Rollback documented | No rollback procedure |
| [CRITICAL] 4 | OPSEC classification handling addressed for AI system deployment | OPSEC addressed | Classification handling not addressed |

---

## TM-50M (Advanced ML Engineer) T&EOs

---

### T&EO 50M-01: Build a Drift Monitoring Pipeline

**Task:** Build a drift monitoring pipeline computing PSI and concept drift metrics with alert thresholds.

**Conditions:** Given a deployed model and monitoring dataset; evaluator will seed drift.

**Standards:** Pipeline computes drift scores; evaluator-seeded drift detected; alert routes correctly.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | PSI computed per feature with documented thresholds | PSI present with thresholds | No PSI computation |
| 2 | Baseline established from deployment-time data | Baseline documented | No baseline |
| [CRITICAL] 3 | Evaluator-seeded drift detected and flagged | Drift detected | Drift not detected |
| 4 | Alert routes to correct channel | Alert routed | Alert not routed |

---

### T&EO 50M-02: Implement Automated Retraining with Shadow Mode

**Task:** Implement an automated retraining trigger and shadow mode comparison before production promotion.

**Conditions:** Drift monitoring pipeline from 50M-01; model registry access.

**Standards:** Retraining trigger linked to drift alert; candidate model runs in shadow mode; human approval gate before promotion.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Retraining trigger linked to drift alert | Trigger configured | No automated trigger |
| 2 | Candidate model registered with CANDIDATE status | Model registered | No model registration |
| [CRITICAL] 3 | Shadow mode comparison produces output between candidate and production | Shadow comparison present | No shadow mode |
| 4 | Human approval gate before production promotion | Approval gate present | Automated promotion without human review |

---

### T&EO 50M-03: Conduct Fairness Evaluation and Produce Governance Package

**Task:** Conduct a fairness evaluation across subgroups and produce a complete model governance package.

**Conditions:** Deployed model with subgroup-identifiable data; governance checklist.

**Standards:** Fairness evaluation covers at least 2 subgroups; model card addresses all required sections; deprecation criteria defined.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Fairness evaluation computed across at least 2 subgroups | ≥2 subgroups evaluated | Fewer than 2 subgroups |
| 2 | Performance disparities identified and documented | Disparities documented | No disparity analysis |
| [CRITICAL] 3 | Model card includes: assumptions, training data, limitations, intended use, responsible AI | All sections present | Any section missing |
| [CRITICAL] 4 | Deprecation criteria explicitly defined | Deprecation criteria present | No deprecation criteria |
| 5 | Human review gate placed on consequential model outputs | Gate present | No gate on consequential outputs |

---

## TM-50J (Advanced Program Manager) T&EOs

---

### T&EO 50J-01: Build a Portfolio Health Dashboard

**Task:** Build a portfolio health dashboard covering all five required dimensions.

**Conditions:** Given portfolio data (or notional portfolio from scenario); MSS Training Environment.

**Standards:** Dashboard covers milestone adherence, dependency health, risk register, team velocity, and budget burn rate.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | All five portfolio dimensions present on dashboard | Five dimensions present | Any dimension missing |
| 2 | Milestone status uses GREEN/AMBER/RED with clear definitions | RAG applied | No RAG; or undefined thresholds |
| 3 | Dashboard readable by GO/SES audience in 60 seconds | Readable at 60 seconds | Requires explanation |
| 4 | Dependency health indicators present | Dependencies visible | No dependency view |

---

### T&EO 50J-02: Present a Technical Investment Brief

**Task:** Present a technical investment brief to a GO/SES audience (evaluator).

**Conditions:** Given a prepared case study; evaluator plays GO role; evaluator will inject a challenging question and a budget constraint mid-brief.

**Standards:** Brief uses BLUF; tradeoff table present; trainee adjusts recommendation in response to evaluator-injected constraint.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| [CRITICAL] 1 | BLUF present at start of brief | BLUF present | No BLUF |
| 2 | Tradeoff table with cost, schedule, performance, and risk ratings | Tradeoff table present | No tradeoff comparison |
| 3 | Challenging question handled without defensiveness | Question addressed substantively | Defensive or non-responsive |
| [CRITICAL] 4 | Recommendation adjusted in response to evaluator-injected constraint | Adjustment made | No adjustment; original recommendation unchanged |

---

### T&EO 50J-03: Respond to an Injected Portfolio Risk

**Task:** Update risk register, make escalation decision, and brief recommended response to an evaluator-injected portfolio risk.

**Conditions:** Portfolio dashboard from 50J-01; evaluator injects a portfolio risk during the evaluation.

**Standards:** Risk register updated; escalation decision made with rationale; recommended response briefed.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Risk register updated with the injected risk | Risk documented | Risk not documented |
| [CRITICAL] 2 | Escalation decision made (escalate or manage at portfolio level) with stated rationale | Decision made with rationale | No escalation decision |
| 3 | Recommended response briefed to evaluator | Response briefed | No response briefed |
| 4 | Cross-program dependency impact assessed | Dependency impact stated | No dependency assessment |

---

## TM-50K (Advanced Knowledge Manager) T&EOs

---

### T&EO 50K-01: Design a Multi-Domain Taxonomy

**Task:** Design a multi-domain controlled vocabulary with cross-domain linkages and governance process.

**Conditions:** Given a theater formation scenario covering 3 functional domains; taxonomy design template.

**Standards:** Taxonomy covers 3 domains; cross-domain linkages defined; vocabulary governance process documented.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Taxonomy covers 3 functional domains | All 3 domains present | Any domain missing |
| [CRITICAL] 2 | Cross-domain linkages defined (same concept mapped across domains) | Linkages present | No cross-domain linkage |
| 3 | Vocabulary governance process documented (who adds/modifies/deprecates terms) | Governance documented | No governance process |

---

### T&EO 50K-02: Build an AI-Augmented Tagging Pipeline with Review Gate

**Task:** Build an AIP Logic tagging pipeline with confidence threshold and human review gate.

**Conditions:** Given a document corpus and controlled vocabulary from 50K-01; AIP Logic access.

**Standards:** Pipeline auto-tags above confidence threshold; low-confidence tags route to human review; threshold basis documented.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Tagging pipeline processes documents without error | Pipeline runs | Pipeline errors |
| 2 | Confidence threshold defined with documented basis | Threshold documented | No threshold; or no basis |
| [CRITICAL] 3 | Low-confidence tags route to human review queue (not auto-applied) | Review queue receives low-confidence tags | Low-confidence tags auto-applied |
| 4 | High-confidence tags verified against gold-standard sample | Verification present | No verification |

---

### T&EO 50K-03: Evaluate Knowledge System Health

**Task:** Evaluate a provided knowledge system using the health metrics framework.

**Conditions:** Given a knowledge system with usage logs and content metadata; health metrics framework.

**Standards:** Evaluation covers zero-recall rate, content age, coverage gaps; prioritized remediation plan produced.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| [CRITICAL] 1 | Zero-recall rate computed with calculation shown | Zero-recall rate computed | No zero-recall analysis |
| 2 | Content age distribution analyzed | Age analysis present | No content age analysis |
| 3 | Top 3 coverage gaps identified | Gaps identified | Fewer than 3 gaps |
| 4 | Prioritized remediation plan produced | Remediation plan present | No remediation plan |

---

### T&EO 50K-04: Design a Unit Continuity Protocol

**Task:** Design a unit knowledge continuity system for a formation undergoing personnel rotation.

**Conditions:** Given a turnover scenario; TM-40K Ch 9 continuity procedures.

**Standards:** Handoff protocol, knowledge decay monitoring, and reactivation procedure designed.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Handoff protocol specifies knowledge transfer artifacts for departing personnel | Protocol present | No handoff protocol |
| 2 | Knowledge decay monitoring designed (flag artifacts with departed owners after 6 months) | Decay monitoring present | No decay monitoring |
| 3 | Reactivation procedure defined for dormant knowledge systems | Reactivation procedure present | No reactivation procedure |
| 4 | Protocol tested against the scenario's turnover case study | Applied to case study | Generic protocol not applied to scenario |

---

## TM-50L (Advanced Software Engineer) T&EOs

---

### T&EO 50L-01: Design an OSDK-First Object Type with Interface Contract

**Task:** Model an Object Type optimized for application consumption with interface contract documentation.

**Conditions:** Given a scenario specifying application query patterns; OSDK development environment.

**Standards:** Object Type queryable via OSDK; interface contract document covers queries, Actions, error types, and versioning policy.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Object Type designed for OSDK consumption (not just data storage) | OSDK query patterns considered | Data-centric design without query consideration |
| 2 | Primary key is stable and unique (not mutable business key) | PK stable | Mutable business key as PK |
| [CRITICAL] 3 | Interface contract document covers: queries, Action signatures, error types, versioning | Contract complete | Contract missing any required section |
| 4 | Top 5 OSDK queries documented before build | Queries documented | No pre-build query documentation |

---

### T&EO 50L-02: Implement Type-Safe TypeScript Function with Tests

**Task:** Implement a TypeScript Function with type-safe Action validation, discriminated union error types, and unit tests.

**Conditions:** Given an Object Type and Action requirements; TypeScript development environment.

**Standards:** Function compiles with no type errors; unit tests cover validation and error paths; all tests pass.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | TypeScript Function compiles with no type errors | No compilation errors | Type errors present |
| 2 | Discriminated union error types used for Action errors | Discriminated unions present | Generic error types |
| [CRITICAL] 3 | Unit tests cover validation and error paths; all pass | All tests pass | Any test fails |
| 4 | Input validation at Action boundary before OSDK write | Validation present | No input validation |

---

### T&EO 50L-03: Configure Enterprise CI/CD Pipeline with Contract Testing

**Task:** Configure a CI/CD pipeline with branch protection, contract testing, and promotion gate.

**Conditions:** Given an application repository; CI/CD tooling available.

**Standards:** Pipeline includes all required stages; contract test catches a breaking change; human approval gate before production.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Pipeline stages: unit test, integration test, contract test, security scan, promotion gate | All stages present | Any stage missing |
| 2 | Branch protection: no direct pushes to main; PR required | Branch protection configured | Direct push to main allowed |
| [CRITICAL] 3 | Contract test demonstrates catching a breaking change | Breaking change blocked | Breaking change not detected |
| 4 | Human approval gate before production promotion | Approval gate present | Automated promotion without review |

---

### T&EO 50L-04: Conduct Security Review and Fix Critical Findings

**Task:** Conduct a security review of a provided codebase and fix CRITICAL findings.

**Conditions:** Given an MSS application codebase with seeded vulnerabilities; TM-50L security review checklist.

**Standards:** Review covers all 5 checklist categories; CRITICAL findings identified and fixed.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Security review covers all 5 categories (input validation, credentials, OSDK handling, output encoding, access control) | All categories covered | Any category missed |
| 2 | Findings prioritized by severity (CRITICAL/HIGH/MEDIUM/LOW) | Severity ratings applied | No severity ratings |
| [CRITICAL] 3 | CRITICAL findings identified and fixed | CRITICAL findings fixed | CRITICAL finding not fixed |
| [CRITICAL] 4 | No OSDK credentials present in client-side code | No client-side credentials | Credentials in client-side code |

---

## TM-50N (Advanced UI/UX Designer) T&EOs

---

### T&EO 50N-01: Design a Design System Component

**Task:** Design a design system component with full documentation including variants, accessibility, and data binding.

**Conditions:** Given the MSS design system context; component design tools.

**Standards:** Component documentation is implementation-ready; accessibility notes present; do/don't examples included.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Component variants documented with visual examples | Variants present | No variant documentation |
| [CRITICAL] 2 | Accessibility notes present (contrast, keyboard, screen reader) | Accessibility documented | No accessibility documentation |
| 3 | Do/don't usage examples included | Examples present | No usage examples |
| 4 | Data binding patterns documented | Binding documented | No data binding documentation |

---

### T&EO 50N-02: Design a DDIL-Aware Application Pattern

**Task:** Design a DDIL-aware application pattern covering all four DDIL tiers with freshness indicators.

**Conditions:** Given an MSS application scenario; four-tier DDIL model.

**Standards:** All four tiers addressed; freshness indicators present; no blank screen at any tier.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | All four DDIL tiers addressed (Connected, Degraded, Intermittent, Disconnected) | All tiers present | Any tier missing |
| 2 | Data freshness indicators designed (age-based visual encoding) | Freshness indicators present | No freshness indicators |
| [CRITICAL] 3 | No blank screen at any DDIL tier | Content displayed at all tiers | Blank screen at any tier |
| 4 | Offline-first interaction pattern: writes queued for sync | Queue pattern designed | No offline write handling |

---

### T&EO 50N-03: Produce a Design Governance Proposal

**Task:** Produce a design governance proposal with review gates, deviation management, and quality metrics.

**Conditions:** Given the MSS design portfolio context; governance template.

**Standards:** Proposal includes review gates, deviation management process, and portfolio quality metrics.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Design review gates defined (when, who, criteria) | Gates defined | No review gates |
| [CRITICAL] 2 | Deviation management process present (how to deviate from design system) | Deviation process present | No deviation management |
| 3 | Quality metrics defined (consistency score, coverage rate, deviation rate) | Metrics defined | No quality metrics |

---

## TM-50O (Advanced Platform Engineer) T&EOs

---

### T&EO 50O-01: Design a Fleet Topology and Upgrade Strategy

**Task:** Design a fleet topology spanning hub and edge clusters with cluster templates and wave-based upgrade strategy.

**Conditions:** Given fleet requirements (regions, classification levels, workload profiles); fleet management tools.

**Standards:** Topology designed; cluster templates parameterized; upgrade strategy includes rollback procedures.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Fleet topology designed with hub and edge clusters | Topology designed | No fleet topology |
| 2 | Cluster templates parameterized for region, classification, and workload | Templates parameterized | Separate templates per cluster |
| 3 | Wave-based upgrade strategy documented (canary → production) | Wave strategy documented | No upgrade strategy |
| [CRITICAL] 4 | Rollback procedure documented for failed upgrades | Rollback procedure present | No rollback procedure |

---

### T&EO 50O-02: Define SLOs with Error Budgets

**Task:** Define SLOs and SLIs for MSS platform services with error budgets and budget-based decision policies.

**Conditions:** Given MSS platform service descriptions; SRE framework reference.

**Standards:** SLIs defined; SLOs set with error budgets; budget-based policy documented.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | SLIs defined for platform services (availability, latency, success rate) | SLIs defined | No SLIs |
| 2 | SLOs set with specific targets and measurement windows | SLOs with targets | Vague or unmeasurable SLOs |
| [CRITICAL] 3 | Error budgets computed from SLO targets | Error budgets computed | No error budgets |
| 4 | Budget-based decision policy documented (stop shipping when budget exhausted) | Policy documented | No budget-based policy |

---

### T&EO 50O-03: Build an Automated Compliance Pipeline

**Task:** Build a compliance pipeline generating RMF evidence from live system data with a compliance dashboard.

**Conditions:** Given STIG requirements and system configuration data; compliance tooling.

**Standards:** Pipeline produces evidence automatically; compliance dashboard displays pass/fail/exception; no manual evidence collection required.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Automated vulnerability scan results collected as evidence | Scan evidence present | Manual scan required |
| 2 | Configuration baseline comparisons automated | Baseline comparison automated | Manual baseline comparison |
| [CRITICAL] 3 | Compliance dashboard displays pass/fail/exception across STIG findings | Dashboard functional | No compliance dashboard; or manual collection required |
| 4 | Exception tracking with expiration dates | Exceptions tracked | No exception management |

---

### T&EO 50O-04: Configure Federated Observability with SLO-Based Alerting

**Task:** Configure cross-cluster metric federation and SLO-based alerting.

**Conditions:** Given two training clusters with Prometheus; alerting infrastructure.

**Standards:** Metrics federated across clusters; SLO-based alert fires when threshold breached.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Cross-cluster metric federation configured | Metrics visible across clusters | Federation not configured |
| 2 | Fleet-wide dashboard displays aggregated resource utilization and pod health | Dashboard present | No cross-cluster dashboard |
| [CRITICAL] 3 | SLO-based alert fires when fleet-wide SLI breaches threshold | Alert fires on breach | Alert does not fire |
| 4 | Cross-cluster correlation demonstrated (event on one cluster, metric impact visible fleet-wide) | Correlation demonstrated | No cross-cluster correlation |

---

# PART VI — T3-I: INSTRUCTOR CERTIFICATION T&EOs

---

## T&EO T3I-01: Deliver a Block of Instruction (Microteaching)

**Task:** Deliver a 20-minute block of instruction from a TM-10, TM-20, or TM-30 lesson plan.

**Conditions:** Given a classroom with projector and student workstations; published lesson plan for the selected block; classmates role-playing as trainees at the appropriate course level. The candidate has 20 minutes.

**Standards:** The candidate will deliver the block demonstrating satisfactory performance on at least 5 of 7 instructor observation criteria, with no unsatisfactory on Technical Accuracy or Evaluation Fidelity.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | **[CRITICAL]** Technical accuracy: content is correct; no uncorrected errors | Content correct throughout | Uncorrected technical error |
| 2 | Instructional clarity: explanations are clear and appropriately paced | Clear, well-paced | Confusing or inappropriate pace |
| 3 | Student engagement: students are actively engaged; instructor identifies stuck students | Students engaged | Students disengaged; stuck students ignored |
| 4 | Check on learning: at least 1 check-on-learning question used; questions require more than yes/no | Effective COL question(s) used | No COL questions; or yes/no only |
| 5 | Lab management (if applicable): lab runs on schedule; instructor manages errors without solving for students | Lab on schedule; appropriate assistance | Lab off schedule; instructor solves for student |
| 6 | **[CRITICAL]** Evaluation fidelity (if applicable): T&EO procedures followed; no assistance during eval | Procedures followed; no assistance | Procedures not followed; or assistance provided |
| 7 | Course materials currency: lesson plan is current; references correct platform version | Current materials | Outdated materials |

**Overall:** GO on 5/7 with no failure on critical items 1 or 6.

---

## T&EO T3I-02: Written Examination

**Task:** Complete a 20-question written exam on instructional methodology, T&EO structure, evaluation procedures, and instructor performance standards.

**Conditions:** Closed book, closed notes. 60 minutes. Exam administered by Senior or Master Instructor.

**Standards:** Score ≥ 80% (16 of 20 correct).

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Score ≥ 80% (16 of 20) | ≥ 16 correct | < 16 correct |

---

# PART VII — T3-F: MSC FORCE MULTIPLIER T&EOs

---

## T&EO T3F-01: Deliver a TM-10 Block (Teach-Back)

**Task:** Deliver a 15–20 minute block of instruction from the TM-10 lesson plans.

**Conditions:** Given a classroom with projector and workstations; published TM-10 lesson plan for the selected block; classmates role-playing as TM-10 trainees. The candidate has 15–20 minutes.

**Standards:** The candidate will deliver the block demonstrating satisfactory technical accuracy and materials use.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Technical accuracy: content is correct; platform features demonstrated correctly | Content correct | Technical error in content or demo |
| 2 | Materials use: follows published lesson plan; uses check-on-learning questions | Follows plan; uses COL | Deviates from plan; skips COL |

**Overall:** GO on both measures.

---

## T&EO T3F-02: Administer a TM-10 Go/No-Go Evaluation

**Task:** Administer 1 T&EO from TM10-01 through TM10-10 to a role-player and make the correct Go/No-Go decision.

**Conditions:** Given a T&EO scoring sheet, a role-player performing a predetermined scenario (Go or No-Go), and the candidate's instructor binder. The evaluator observes the candidate's administration.

**Standards:** The candidate will correctly score all performance measures, make the correct overall Go/No-Go decision, clearly announce the evaluation mode transition, provide no assistance during the evaluation, and properly document the result.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | **[CRITICAL]** Correct overall Go/No-Go decision (matches predetermined scenario) | Correct decision | Incorrect decision |
| 2 | All performance measures scored on the T&EO scoring sheet | All measures scored | Missing scores |
| 3 | Clear mode transition announcement ("We are now in the evaluation") | Announced clearly | No announcement or unclear |
| 4 | **[CRITICAL]** No assistance provided to role-player during evaluation | No assistance | Any assistance provided |
| 5 | Result properly documented on scoring sheet (including deficiency if No-Go) | Documented | Missing documentation |

**Overall:** GO on all critical items + GO on 4/5 total.

---

## T&EO T3F-03: Resolve Environment Issues

**Task:** Diagnose and resolve 3 pre-staged MSS environment failures.

**Conditions:** Given 3 workstations, each with a pre-staged failure from the set of 5 common issues. The candidate works independently. Time limits apply per issue type.

**Standards:** The candidate will correctly diagnose the root cause and resolve at least 2 of 3 issues within the prescribed time limits.

| # | Performance Measure | GO | NO-GO |
|---|---|---|---|
| 1 | Issue 1: correct diagnosis and resolution within time limit | Resolved | Not resolved |
| 2 | Issue 2: correct diagnosis and resolution within time limit | Resolved | Not resolved |
| 3 | Issue 3: correct diagnosis and resolution within time limit | Resolved | Not resolved |

**Overall:** GO on ≥ 2 of 3.

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

## T&EO SCORING SHEET — T3 COURSES (BLANK TEMPLATE)

```
=========================================================
T&EO SCORING SHEET — T3 COURSES
=========================================================
Trainee Name:     _______________________________________
Course:           [ ] T3-I    [ ] T3-F
T&EO Number:      _______________________________________
Task Title:       _______________________________________
Date:             _______________________________________
=========================================================

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

*USAREUR-AF Operational Data Team*
*T&EO MSS-TEO-001 | Version 2.0 | March 2026*
