# POST-TEST — TM-20: BUILDER
## Maven Smart System (MSS) — USAREUR-AF

| | |
|---|---|
| **Course** | TM-20: Builder |
| **Form** | Post-Test |
| **Level** | TM-20 (Intermediate) |
| **Audience** | All staff — prerequisite: TM-10 |
| **Time Allowed** | 45 minutes |
| **Passing Score** | 70% (42/60) |

---

## INSTRUCTIONS

This assessment evaluates mastery of course learning objectives. A passing score of 70% is required to receive credit. Complete independently without reference to training materials.

---

## SECTION 1 — MULTIPLE CHOICE

*Circle the letter of the best answer. (2 points each)*

**1. Per USAREUR-AF C2DAO naming conventions, a correct Foundry project name for 1st Cavalry Division's G4 logistics team would most closely follow which pattern?**

A. `CavalryDiv-G4-Logistics`
B. `1CD_G4_LOGISTICS_OPDATA`
C. `LogisticsProject_1CD`
D. `1st_Cav_G4`

**2. After ingesting a new file into Foundry, the FIRST data quality checks you should perform are:**

A. Schema validation, then immediately publish the dataset to the Ontology
B. Row count verification, data type validation, and null check on required fields
C. Export the dataset and open it in Excel to review visually
D. Run the dataset through a Pipeline Builder pipeline without reviewing it first

**3. In Pipeline Builder, you need to keep only records where the `unit` field equals "1-16 CAV". The correct step type is:**

A. Rename column
B. Calculated column
C. Filter rows
D. Type cast

**4. You are building a pipeline that joins a maintenance dataset to a vehicle roster on the `vehicle_id` field. Before executing the join, you notice that `vehicle_id` is stored as INTEGER in the vehicle roster but as TEXT in the maintenance dataset. You should:**

A. Proceed — Pipeline Builder automatically resolves type mismatches in joins
B. Cast both fields to the same data type in a type cast step before the join
C. Delete the maintenance dataset and re-ingest it with correct types
D. Contact the data steward and wait for the source data to be fixed before proceeding

**5. A Link Type in Foundry Ontology with cardinality ONE-TO-MANY between Unit and Vehicle means:**

A. Each Vehicle can belong to multiple Units, and each Unit can own multiple Vehicles
B. Each Unit can have many Vehicles, but each Vehicle belongs to exactly one Unit
C. Each Vehicle must be linked to exactly one Unit, and Units can only have one Vehicle
D. The relationship is optional — neither side is required to have a matching record

**6. When configuring an Ontology write step in Pipeline Builder, the field designated as the Primary Key:**

A. Must be named "id" in the source dataset
B. Determines how records are matched for upsert operations — matching records are updated, new records are inserted
C. Is used only for display purposes in Workshop and does not affect data storage
D. Must be a system-generated UUID and cannot be a business key from source data

**7. You are configuring an Action in Foundry. The Action requires a parameter for vehicle mileage that must be a positive integer. Where in the Action configuration do you enforce this constraint?**

A. In the Workshop widget that calls the Action
B. In the Pipeline Builder pipeline that processes the Action result
C. In the Action's parameter definition (type, validation rules, and description)
D. In the Ontology Manager's property definition for the mileage field

**8. In a Workshop application, you want a bar chart to only display data relevant to the unit selected in a dropdown filter widget. The correct configuration is:**

A. Build separate bar charts for each unit and hide/show based on the selection
B. Link the filter widget's output variable to the bar chart's filter input
C. Export the dropdown selection to a pipeline that regenerates the chart
D. Use conditional formatting on the chart to hide non-matching bars

**9. Your Workshop application has an Action button that submits a maintenance status update. To restrict this button so only Editors (not Viewers) can submit updates, you:**

A. Remove the button from the application layout when accessed by a Viewer
B. Configure the Action's access-control rule to require the Editor role
C. Add a password prompt to the Action form
D. Create two separate Workshop applications — one for Viewers and one for Editors

**10. You need to grant a new analyst read-only access to your unit's MSS project. The correct role to assign is:**

A. Owner
B. Editor
C. Viewer
D. Builder

**11. You have completed development of a new pipeline and Workshop application in your development environment. To promote these to production per USAREUR-AF C2DAO workflow, you must:**

A. Export the pipeline configuration and email it to the data steward for manual re-creation
B. Create a Foundry branch with your changes, write a promotion description, and submit for data steward review
C. Grant your account Owner access to the production environment and deploy directly
D. Submit a helpdesk ticket requesting a scheduled maintenance window for the deployment

**12. In Pipeline Builder, a "calculated column" step that produces a `readiness_pct` column by dividing `mission_ready` by `total_assigned` requires that `total_assigned`:**

A. Be stored as a text field
B. Never contain zero (to avoid division-by-zero errors)
C. Equal `mission_ready` for the calculation to be valid
D. Be rounded to the nearest integer before the division

**13. A Foundry dataset "ingest" operation that imports a CSV file into the platform will:**

A. Automatically apply all transforms from your pipeline to the raw data
B. Create a raw dataset containing the file's data, which then requires a pipeline to transform and clean it
C. Immediately publish the data to the Ontology as a new Object Type
D. Replace any existing dataset with the same name without warning

**14. You are building a Pipeline Builder pipeline that renames the column `veh_id` to `vehicle_id` to match the Ontology property name. The correct step type is:**

A. Filter rows
B. Rename column
C. Type cast
D. Calculated column

**15. Your Workshop application displays a table of open maintenance work orders. After submitting a new work order via an Action, the table does not update immediately. The MOST likely cause is:**

A. The Action failed silently and the submission was not recorded
B. The Workshop table refreshes on a schedule or requires a manual refresh — the submission was recorded but the view has not yet updated
C. The table is connected to the wrong dataset
D. The Action's access control prevents the new record from appearing for the submitting user

---

## SECTION 2 — SHORT ANSWER

*Answer in 2–5 sentences. (6 points each)*

**SA-1. You are building a pipeline to ingest a vehicle roster spreadsheet. The spreadsheet has a column called `mileage` that contains values like "12,500 miles" (text with commas and units). Describe the Pipeline Builder steps you would use to clean this column and produce a valid integer mileage value.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-2. Describe the correct USAREUR-AF branching and promotion workflow for deploying a new Workshop application to production. Include the role of the data steward in this process.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-3. Your S2 asks you to connect a personnel roster Object Type to an equipment tracker Object Type so analysts can see which Soldier is assigned to which vehicle. Describe the Ontology configuration steps required to establish this relationship.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-4. A Workshop application you built displays a metric widget showing "Total Vehicles: 0" even though the underlying dataset has 47 records. Describe two possible causes and how you would diagnose each.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-5. Explain the difference between the Viewer and Editor roles in a Foundry project. Give one concrete example of a task each role can perform, and one task that requires at least Editor access.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

---

## SCORING SUMMARY

| Section | Questions | Points Each | Total Points |
|---|---|---|---|
| Multiple Choice | 15 | 2 | 30 |
| Short Answer | 5 | 6 | 30 |
| **Total** | — | — | **60** |

Passing: 42/60 (70%) — Post-test only. Pre-test is diagnostic.

---

## ANSWER KEY — INSTRUCTOR USE ONLY

*Do not distribute to students.*

**Multiple Choice:**
1. B — C2DAO naming follows `ECHELON_OFFICE_FUNCTION_TYPE` uppercase pattern; Option B matches closest.
2. B — Row count, type validation, and null check are the three required post-ingest quality checks.
3. C — Filter rows is the correct step for keeping records matching a condition.
4. B — Type cast step before the join resolves the type mismatch; Pipeline Builder does not auto-resolve.
5. B — ONE-TO-MANY: one Unit has many Vehicles, each Vehicle belongs to one Unit.
6. B — Primary Key drives upsert logic — matching = update, new = insert.
7. C — Parameter-level type and validation rules are defined in the Action parameter configuration.
8. B — Linking filter widget output variable to chart filter input is the correct Workshop wiring.
9. B — Action access-control rule restricts execution to the required role.
10. C — Viewer is the read-only role; Editor allows building; Owner manages access.
11. B — Branch, write promotion description, submit for data steward review is the correct C2DAO workflow.
12. B — Division by zero is a pipeline error; zero in the denominator must be handled (COALESCE or filter).
13. B — Ingest creates a raw dataset; transforms are applied by a downstream pipeline.
14. B — Rename column is the correct step type for changing column names.
15. B — Workshop tables refresh on schedule or manually; Action submission is recorded but view may lag.

**Short Answer Guidance:**

SA-1. Full credit: calculated column step to strip commas (string replace "," with ""); calculated column to strip " miles" suffix (string replace or substring); type cast step to convert resulting text to INTEGER. Partial credit (3 pts) for identifying two of three steps. NOTE: order matters — strip text before casting.

SA-2. Full credit: create a branch in Foundry; make all changes (pipeline, Workshop) on the branch; write a promotion description explaining what changed and why; submit branch for data steward review; data steward reviews, may provide feedback, then approves and merges to main. Partial credit (3 pts) for correct overall flow without data steward role.

SA-3. Full credit: in Ontology Manager, define a Link Type between the Personnel (or Soldier) Object Type and the Vehicle Object Type; specify cardinality (likely ONE-TO-MANY if one Soldier assigned to one vehicle primary, or MANY-TO-MANY if multiple assignments); configure the Pipeline Builder Ontology write step to populate the link based on an assignment field. Partial credit (3 pts) for identifying Link Type without cardinality or pipeline write step.

SA-4. Full credit: two from — (1) metric widget is connected to the wrong dataset (check dataset binding); (2) the dataset is filtered before the metric widget and all records are filtered out (check upstream filters or variable connections); (3) the pipeline hasn't run yet and the dataset is empty (check pipeline last-run status); (4) the metric widget is configured with an incorrect aggregation field (check widget configuration). Each cause must include a diagnosis step for full credit.

SA-5. Full credit: Viewer = read-only access — can view Workshop applications and Contour analyses, cannot create or modify anything; Editor = can build and modify pipelines, Workshop apps, Object Types, and run Actions with appropriate configuration; task requiring Editor: creating a Pipeline Builder pipeline, modifying an Object Type, building a Workshop application. Partial credit (3 pts) for correct definition of one role without example.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*TM-20 Post-Test | Version 1.0 | March 2026*
