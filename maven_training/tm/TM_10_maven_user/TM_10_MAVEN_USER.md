```
TM-10 — MAVEN SMART SYSTEM (MSS)
OPERATOR TECHNICAL MANUAL

HEADQUARTERS
UNITED STATES ARMY EUROPE AND AFRICA
Wiesbaden, Germany

2026

PREREQUISITE PUBLICATIONS: ADRP 1, Data Literacy (recommended prior reading)
DISTRIBUTION RESTRICTION: Approved for public release; distribution is unlimited.
```

---

## SAFETY SUMMARY

The Maven Smart System handles operational and potentially classified data. Improper use may result in:

- Unauthorized disclosure of sensitive or classified information
- Corruption or loss of operational data
- Unauthorized actions against live operational records

Read all WARNINGS and CAUTIONS in this manual before operating the system. If you are uncertain whether an action is authorized, STOP and consult your supervisor or data steward.

---

## TABLE OF CONTENTS

- [Chapter 1 — Introduction to the Maven Smart System](#chapter-1--introduction-to-the-maven-smart-system)
- [Chapter 2 — Getting Started: Accessing and Navigating MSS](#chapter-2--getting-started-accessing-and-navigating-mss)
- [Chapter 3 — Using Workshop Applications](#chapter-3--using-workshop-applications)
- [Chapter 4 — Understanding and Working with Data](#chapter-4--understanding-and-working-with-data)
- [Chapter 5 — Using AIP and AI Tools](#chapter-5--using-aip-and-ai-tools)
- [Chapter 6 — Data Security and Classification Handling in MSS](#chapter-6--data-security-and-classification-handling-in-mss)
- [Chapter 7 — Troubleshooting](#chapter-7--troubleshooting)
- [Chapter 8 — Operator Maintenance](#chapter-8--operator-maintenance)
- [Appendix A — Quick Reference Card](#appendix-a--quick-reference-card)
- [Appendix B — Authorized Use Policy Summary](#appendix-b--authorized-use-policy-summary)
- [Glossary](#glossary)

---

# CHAPTER 1 — INTRODUCTION TO THE MAVEN SMART SYSTEM

**BLUF:** This manual tells you how to operate the Maven Smart System (MSS). It covers logging in, finding data, reading dashboards, submitting information, and staying within authorized boundaries. No technical background is required.

## 1-1. Purpose and Scope of This Manual

This Technical Manual (TM) provides operator-level instruction for the Maven Smart System (MSS). It is written for all Army and civilian personnel assigned or attached to USAREUR-AF who require access to MSS in the course of their duties.

This manual covers what you need to know to use MSS safely and effectively. It does not cover how to build applications or modify data pipelines. Those tasks are covered in TM-20 (Workshop Builder) and TM-30 (Advanced Developer).

## 1-2. What the Maven Smart System Is

MSS is a secure, web-based platform where your unit's data lives and can be analyzed and acted upon. Think of it like a shared operations center for data: information from logistics, personnel, readiness, and other systems is collected, organized, and made accessible through applications your unit uses every day.

MSS is built on the Palantir Foundry platform, authorized for Army use under the Maven Smart System program. When you log into MSS, you are logging into Foundry with Army data and Army-approved access controls.

**What MSS does:**

- Stores data from Army systems in a single, organized location
- Makes that data visible through applications your unit can use without technical training
- Enables units to update records, report status, and track readiness through those same applications
- Provides analysis tools for personnel who need to examine data in more depth
- Supports AI-assisted analysis through authorized tools

**What MSS is not:**

- It is not a replacement for official Army systems of record (DCPDS, GCSS-A, MEDPROS, etc.)
- It is not a classified system by default — classification depends on the data and markings applied
- It is not a public system — access is controlled and audited

## 1-3. MSS in USAREUR-AF Context

Within USAREUR-AF, MSS supports the following mission areas:

| Mission Area | Example Use |
|---|---|
| Personnel Readiness | Viewing and reporting soldier readiness status |
| Logistics | Tracking equipment availability and maintenance status |
| Operational Reporting | Submitting and viewing SITREPs and operational updates |
| Intelligence Support | Viewing ISR-derived products (authorized users only) |
| Planning | Accessing order data, unit positions, and task organization |
| Command & Control | Tracking unit status across the AOR |

MSS users in USAREUR-AF range from unit S-shops to the theater staff. Your access level and the applications available to you depend on your role and assigned markings.

## 1-4. What This Manual Covers and Does NOT Cover

| This manual covers (TM-10) | Covered in other TMs |
|---|---|
| Logging in and navigating MSS | Building Workshop applications (TM-20) |
| Reading dashboards and reports | Creating or modifying data pipelines (TM-30) |
| Submitting data using forms | Writing transforms or code (TM-30) |
| Using AI tools as an end-user | Configuring AI agents or Logic workflows (TM-30) |
| Exporting data safely | Administering permissions and markings (Admin Guide) |
| Troubleshooting common issues | Ontology and dataset design (TM-30) |

If a task you need to perform is not covered in this manual, contact your unit data steward or MSS administrator before attempting it.

## 1-5. Prerequisites and Required Training Before Operating MSS

Before accessing MSS, you must complete the following:

1. **Annual Cyber Awareness training** — required for all DoD personnel with network access
2. **MSS User Onboarding Brief** — provided by your unit data steward or G6/S6
3. **Account request approval** — your account must be provisioned before you can log in

Recommended (not required) prior reading:
- ADRP 1 (The Army)
- Data Literacy for Army Leaders (DAU course or equivalent)

## 1-6. Security Responsibilities of Every MSS User

Every MSS user is personally responsible for the following:

1. Use only your own credentials. Do not share your CAC, PIN, or any access tokens.
2. Access only the data you are authorized to view. Do not attempt to access projects, datasets, or applications that have not been granted to you.
3. Report misrouted data immediately. If you see data at a higher classification level than your clearance, stop and report it. Do not attempt to read, copy, or act on that data.
4. Do not export data without authorization. Exports are logged. Downloading data you are not authorized to remove from the system is a security violation.
5. Log out when you are done. Do not leave an MSS session unattended on an unlocked workstation.
6. Report incidents. If you suspect a security violation, report it to your supervisor and unit security officer immediately.

WARNING: Unauthorized access to, disclosure of, or modification of data in MSS may constitute a violation of 18 U.S.C. § 1030 (Computer Fraud and Abuse Act) and applicable Army regulations. Violations may result in disciplinary action, loss of access, and criminal prosecution.

## 1-7. How to Get Access

Access to MSS is CAC-based. Your Common Access Card (CAC) is your login credential.

**Account Request Process:**

1. Contact your unit S6 or data steward to initiate an account request.
2. Your supervisor submits a request to the MSS administration team with your name, unit, role, and required access level.
3. The MSS admin team provisions your account and assigns appropriate markings and project access.
4. You will receive a notification when your account is active.
5. Log in using the MSS portal URL provided by your unit. Use your CAC and PIN.

NOTE: Account provisioning may take 3-5 business days. Plan accordingly before a deployment or exercise requiring MSS access.

**Account markings** are assigned based on your clearance level and mission role. Your assigned markings determine which data you can see. If you cannot see data you believe you should have access to, contact your unit data steward — do not attempt to work around access controls.

## 1-8. How to Report Problems

Report system problems through the following channels:

| Problem Type | Who to Contact |
|---|---|
| Cannot log in | Unit S6 or MSS Help Desk |
| Cannot access a project | Unit data steward |
| Data appears incorrect | Unit data steward (do not correct it yourself) |
| System error or crash | MSS Help Desk (provide error code and screenshot) |
| Security incident | Supervisor and unit security officer immediately |
| Application not working | MSS Help Desk |

**Before calling for help, collect:**
- Your username
- The name of the application or dataset
- The error message (exact text or screenshot)
- The time the error occurred
- Steps that led to the error

---

# CHAPTER 2 — GETTING STARTED: ACCESSING AND NAVIGATING MSS

**BLUF:** This chapter walks you through logging in, orienting yourself on the home screen, and finding your unit's data.

---

**TASK: ACCESS THE MAVEN SMART SYSTEM**

**Conditions:** Operator has a provisioned MSS account, a CAC reader, and access to an approved workstation with an approved web browser (Chrome or Firefox recommended).

**Standards:** Operator successfully authenticates with CAC, reaches the MSS home screen, and can identify the main navigation elements.

**Equipment:** CAC, CAC reader, approved workstation, MSS portal URL (provided by unit S6).

**Procedure:**

1. Insert your CAC into the CAC reader.
2. Open an approved web browser.
3. Navigate to the MSS portal URL provided by your unit S6.
4. The browser will prompt you to select a certificate. Select your authentication certificate (not your email certificate).
5. Enter your CAC PIN when prompted.
6. The MSS home screen loads. You are now logged in.

NOTE: If the browser does not prompt for a certificate, ensure your CAC reader drivers are installed and the CAC is seated properly. Contact your S6 if the issue persists.

CAUTION: Do not save your PIN in the browser. Do not allow the browser to remember your login. MSS sessions may contain sensitive information.

---

**TASK: NAVIGATE THE MSS HOME SCREEN**

**Conditions:** Operator is logged into MSS.

**Standards:** Operator can identify all major navigation elements and locate the search function, notifications, and user profile.

**Equipment:** Active MSS session.

**Procedure:**

1. Observe the top navigation bar. It contains: the MSS logo (home button), a search bar, notification bell, and your user profile icon.
2. Observe the left sidebar. It contains navigation links to: Home, Projects (Compass), and any pinned applications.
3. The main area of the home screen displays: recently visited resources, pinned projects, and notifications.
4. To access your user profile: click your profile icon in the upper right corner.
5. To view notifications: click the bell icon.
6. To return to the home screen from anywhere: click the MSS logo in the upper left.

**Table 2-1. MSS Navigation Elements**

| Element | Location | Purpose |
|---|---|---|
| Search bar | Top center | Find datasets, applications, and projects |
| Notification bell | Top right | System alerts, workflow updates |
| User profile icon | Top right | Account settings, markings, logout |
| Compass (file explorer) | Left sidebar | Browse all MSS resources |
| Home button (logo) | Top left | Return to home screen |
| Pinned items | Home screen main area | Shortcuts to frequently used resources |
| Recent activity | Home screen main area | Recently visited datasets and apps |

**Table 2-2. Common MSS Icons**

| Icon | Meaning |
|---|---|
| Folder icon | Project or directory |
| Table/grid icon | Dataset |
| Application window icon | Workshop application |
| Lock icon | Access restricted — you may not have permission |
| Star icon | Bookmarked/pinned item |
| Clock icon | Scheduled update or last-updated timestamp |
| Warning triangle | Data quality alert or system warning |
| Chain link icon | Data lineage — source/dependency information |

---

**TASK: LOCATE A PROJECT**

**Conditions:** Operator is logged into MSS and has been assigned to a unit project.

**Standards:** Operator navigates to their unit's project space and identifies its contents.

**Equipment:** Active MSS session, knowledge of unit project name (provided by data steward).

**Procedure:**

1. Click **Compass** in the left sidebar. The file explorer opens.
2. Compass displays folders organized by organization and project. Navigate the folder tree to find your unit's project.
3. Alternatively, use the search bar: type your unit name or project name and press Enter.
4. Click the project folder to open it. You will see subfolders for datasets, applications, and other resources.
5. Note what you can see — your access is limited to resources your account has been granted.

NOTE: If you cannot find your unit's project, your account may not have been granted access yet. Contact your data steward. Do not attempt to access other units' projects.

---

**TASK: SEARCH FOR A DATASET OR RESOURCE**

**Conditions:** Operator is logged into MSS and needs to locate a specific dataset or application.

**Standards:** Operator uses the search function to locate a named resource and opens it.

**Equipment:** Active MSS session.

**Procedure:**

1. Click the search bar at the top of the screen.
2. Type the name or partial name of the dataset or application. MSS searches as you type.
3. Results appear below the search bar. Results include datasets, applications, projects, and other resources.
4. Use the filter options (left side of results) to narrow by type (Dataset, Application, Project).
5. Click the result to open it.

NOTE: Search results only show resources you have permission to see. If you expect to find something but it does not appear, you may not have access. Contact your data steward.

---

**TASK: OPEN AND READ A DATASET**

**Conditions:** Operator has located a dataset in MSS and has Viewer access to it.

**Standards:** Operator opens the dataset preview, reads column headers, understands data types, and locates the last-updated timestamp.

**Equipment:** Active MSS session, Viewer access to the target dataset.

**Procedure:**

1. Locate the dataset using search or Compass navigation.
2. Click the dataset name to open it.
3. The dataset preview shows the first rows of data in a table format. Each column has a header (column name) and a data type indicator.
4. Scroll right to see additional columns. Scroll down to see more rows.
5. Look for the metadata panel (usually on the right side or accessible via an "Info" tab). This shows: last updated time, number of rows, schema, and data lineage.
6. To sort by a column: click the column header. Click again to reverse the sort.
7. To filter rows: use the filter bar above the preview table.

CAUTION: You are viewing a preview of the dataset. Do not attempt to edit data directly in the preview. If you need to correct data, use the designated Workshop application for that data type or contact your data steward.

---

# CHAPTER 3 — USING WORKSHOP APPLICATIONS

**BLUF:** Workshop applications are the primary interface for most MSS users. They display your unit's data in dashboards, forms, and reports. This chapter covers opening, reading, and using Workshop applications.

Workshop is Foundry's application layer. A developer has built an application — a dashboard, a form, a report — and made it available to your unit. You interact with that application the same way you would interact with any web application: clicking, filtering, filling out forms. You do not need to understand how the application was built.

---

**TASK: OPEN A WORKSHOP APPLICATION**

**Conditions:** Operator is logged into MSS and has access to a Workshop application.

**Standards:** Operator locates and successfully opens a Workshop application.

**Equipment:** Active MSS session, Viewer access to the target application.

**Procedure:**

1. Locate the application using search or Compass navigation (applications appear with an application window icon).
2. Click the application name to open it.
3. The application loads in the browser. Wait for all widgets to finish loading (loading spinners will disappear).
4. Review the application layout: it will typically have a header or title, navigation tabs or modules, and data displays.
5. If the application has multiple modules (pages), they appear as tabs or a sidebar navigation within the application.

NOTE: Workshop applications are read-only unless they include a form or action button. The presence of a form or button means you are authorized to submit data through that interface.

---

**TASK: READ A DASHBOARD**

**Conditions:** Operator has a Workshop application open that includes a dashboard view.

**Standards:** Operator correctly interprets charts, tables, KPIs, and status indicators displayed in the dashboard.

**Equipment:** Active MSS session, Workshop application open.

**Procedure:**

1. Identify the dashboard elements: charts (bar, line, pie), tables (rows and columns of data), metric tiles (large single numbers), and status indicators (colored icons or badges).
2. Read metric tiles first — they show the most important summary numbers (e.g., total units reporting, readiness percentage).
3. Read charts: check the title, axis labels, and legend before interpreting values.
4. Read tables: column headers identify what each column contains. Sort by clicking column headers.
5. Look for color coding: green typically indicates acceptable status, yellow indicates caution, red indicates a problem or threshold exceeded. Verify the legend — color meanings vary by application.
6. Check the last-updated timestamp if visible. If data appears outdated, note it and report to your data steward.

NOTE: Dashboard data reflects the last time the underlying data pipeline ran. It is not necessarily real-time. Know your pipeline's update frequency — ask your data steward if you are unsure.

---

**TASK: FILTER AND QUERY DATA IN A DASHBOARD**

**Conditions:** Operator has a dashboard open that includes filter controls.

**Standards:** Operator applies filters to narrow displayed data to a specific unit, date range, or status, and reads the filtered results.

**Equipment:** Active MSS session, Workshop application with filter controls.

**Procedure:**

1. Locate the filter panel. It is typically on the left side or top of the dashboard. Filter controls include: dropdown menus, date pickers, search boxes, and toggle switches.
2. Select the desired filter value from the dropdown (e.g., select your brigade from a unit filter).
3. To filter by date: click the date picker, select the start date, then the end date.
4. Charts and tables on the dashboard update automatically to reflect your filters.
5. To clear a filter: click the "X" next to the filter value or select "All" from the dropdown.
6. To clear all filters: look for a "Reset Filters" or "Clear All" button.

NOTE: Filters only affect what you see in your current session. They do not change the underlying data and do not affect what other users see.

---

**TASK: SUBMIT DATA USING A FORM**

**Conditions:** Operator has a Workshop application open that includes a data entry form, and is authorized to submit data through that form.

**Standards:** Operator correctly completes all required fields and successfully submits the form with confirmation.

**Equipment:** Active MSS session, Workshop application with an Action Form widget, authorization to submit data.

**Procedure:**

1. Locate the form within the application. Forms include labeled input fields (text boxes, dropdowns, date pickers) and a Submit button.
2. Required fields are marked with an asterisk (*) or highlighted. You must complete all required fields before the form will accept submission.
3. Complete each field according to the field label. Enter accurate information — you are writing to a live operational record.
4. For dropdown fields: click the dropdown and select the correct value. Do not type a value not on the list.
5. For date fields: use the date picker. Do not manually type dates unless instructed — format errors will cause submission to fail.
6. Review all entries before submitting.
7. Click the Submit button.
8. Wait for the confirmation message. A success message confirms the record was written. An error message describes what went wrong.
9. If submission fails: read the error message, correct the identified field, and resubmit.

CAUTION: Data submitted through a form writes directly to operational records. Verify all information before submitting. Incorrect submissions may require a data steward to correct.

WARNING: Do not submit data on behalf of another Soldier without authorization. Actions are logged with your user identity. Submitting data under your credentials that belongs to another Soldier or unit is a records integrity violation.

---

**TASK: EXECUTE AN ACTION**

**Conditions:** Operator has a Workshop application open that includes an action button (e.g., "Mark Complete," "Approve," "Close Report"), and is authorized to execute that action.

**Standards:** Operator identifies the action, reviews the confirmation prompt, and successfully executes the action with awareness of what it changes.

**Equipment:** Active MSS session, Workshop application with action button, authorization to execute the action.

**Procedure:**

1. Locate the action button. Buttons are labeled with their function (e.g., "Update Status," "Submit SITREP," "Mark Ready").
2. Before clicking: read the button label and any surrounding text to understand what the action does.
3. If a record must be selected before executing the action (e.g., select a unit from a table, then click "Update Status"), make that selection first.
4. Click the action button.
5. A confirmation dialog will appear describing the action and its effect. Read it carefully.
6. Click "Confirm" to proceed or "Cancel" to abort.
7. Wait for the success or error message.
8. Verify the result: if the action updated a record, check that the relevant field or status changed as expected.

CAUTION: Actions change live operational data. Some actions cannot be undone. If you are unsure what an action does, do not execute it. Ask your supervisor or data steward.

---

**TASK: EXPORT DATA FROM A WORKSHOP APPLICATION**

**Conditions:** Operator has a Workshop application open with export functionality, is authorized to export the data, and the data marking permits export.

**Standards:** Operator exports data to the correct format, verifies the export does not exceed authorized marking level, and handles the exported file IAW data handling requirements.

**Equipment:** Active MSS session, Workshop application with export button, authorized destination for the exported file.

**Procedure:**

1. Locate the export button. It is typically labeled "Export," "Download," or represented by a download arrow icon.
2. Before clicking: verify you are authorized to export this data and that your destination (laptop, shared drive) is approved for the data's classification level.
3. Click the export button.
4. Select the format (CSV or Excel) if prompted.
5. The file downloads to your default download directory.
6. Handle the downloaded file IAW the data's marking level. Do not place it in an unauthorized location.

WARNING: Exported data retains its classification and handling requirements outside of MSS. Placing classified or CUI data in an unauthorized location is a security violation. If you are uncertain whether an export is authorized, do not export. Contact your data steward.

NOTE: Not all Workshop applications have export functionality. Absence of an export button means export is not authorized for that application or dataset.

**Table 3-1. Common Workshop Interface Elements**

| Element | Description | Operator Action |
|---|---|---|
| Object Table | Rows and columns of records | Click to select a row; sort by column header |
| Chart | Visual data representation (bar, line, pie) | Read title and legend; hover for values |
| Metric Tile | Single large number (KPI) | Compare to threshold/standard |
| Filter Panel | Dropdown, date picker, search box | Select values to narrow displayed data |
| Action Button | Labeled button that changes data | Read label; confirm before executing |
| Action Form | Multi-field data entry form | Complete all required fields; submit |
| Map Widget | Geographic display of data | Click objects on map for detail |
| Status Badge | Colored indicator (green/yellow/red) | Check legend for threshold meanings |
| Search Box | Text input to filter displayed records | Type to filter; clear to reset |
| Pagination | Page navigation at bottom of tables | Use to see additional records |

NOTE: Operators are authorized to VIEW data, FILTER data, SUBMIT forms, and EXECUTE actions in Workshop — but only within applications they have been granted access to. Operators are NOT authorized to edit application layouts, add or remove widgets, or modify data outside of designated forms and actions. If you see an "Edit" mode in Workshop, do not enter it unless you are a designated builder. Report any accidental edits to your data steward immediately.

---

# CHAPTER 4 — UNDERSTANDING AND WORKING WITH DATA

**BLUF:** MSS stores data as structured tables. This chapter explains how to read that data, perform no-code analysis, verify data quality, and report problems.

## 4-1. Data Basics

Data in MSS is organized into **datasets** — structured tables with rows and columns, similar to a spreadsheet. Each column has a name and a data type (text, number, date, etc.). Each row is one record (one Soldier, one vehicle, one report).

Data in MSS flows through layers before you see it:

- Raw data comes in from Army systems (GCSS-A, DCPDS, unit feeds, etc.)
- It is cleaned and standardized by data engineers
- The cleaned data backs the applications and analysis tools you use

You interact with the curated, cleaned layer. You do not see raw data in operational applications.

---

**TASK: READ AND INTERPRET A DATASET**

**Conditions:** Operator has located a dataset in MSS and has Viewer access.

**Standards:** Operator correctly identifies column names, data types, and the meaning of at least five columns in a sample dataset within 5 minutes of opening it.

**Equipment:** Active MSS session, Viewer access to target dataset.

**Procedure:**

1. Open the dataset in Compass by clicking its name.
2. The preview shows the first 100 rows. Read the column headers across the top.
3. Look at the data type indicator below each column header (text, integer, timestamp, boolean).
4. Read several rows to understand the range of values in each column.
5. Use the sort function (click a column header) to see the highest and lowest values in a column.
6. Use the filter bar to narrow to a specific value (e.g., filter the "unit" column to your brigade).
7. Check the metadata panel for: total row count, last updated time, and schema (full column list with types).

---

**TASK: USE CONTOUR FOR NO-CODE ANALYSIS**

**Conditions:** Operator has access to a dataset and the Contour analysis tool.

**Standards:** Operator opens Contour, loads a dataset, performs a basic aggregation (count or sum by group), and creates a chart.

**Equipment:** Active MSS session, Viewer access to target dataset, access to Contour.

**Procedure:**

1. Open the target dataset in Compass.
2. Click the **Analyze in Contour** button (or navigate to Contour from the left sidebar and open a new analysis).
3. In Contour, the dataset appears as a source. Click it to load a preview.
4. To aggregate data: click **Group By** and select the column you want to group on (e.g., "unit").
5. Add an aggregation: click **Aggregate** and select the function (Count, Sum, Average) and the column to aggregate.
6. The result table updates to show one row per group with the aggregated value.
7. To create a chart: click **Visualize** and select a chart type (Bar, Line, Pie).
8. Map the X axis to your group column and the Y axis to your aggregated value.
9. The chart renders in the analysis panel.
10. Save the analysis by clicking **Save** and naming it.

NOTE: Contour analyses are saved to your personal space or a shared project folder. Save analyses to the correct location — personal analyses in your workspace, unit analyses in the unit project folder.

CAUTION: Contour analysis operates on live data. Do not share Contour outputs without verifying that the output does not reveal data at a higher classification level than intended recipients are cleared for (aggregation risk — see Section 6-5).

---

**TASK: USE QUIVER FOR ONTOLOGY ANALYSIS**

**Conditions:** Operator has access to Quiver and the relevant object types in MSS.

**Standards:** Operator opens Quiver, selects an object type, applies a filter, and views properties of selected objects.

**Equipment:** Active MSS session, access to Quiver, access to target object types.

**Procedure:**

1. Navigate to **Quiver** from the left sidebar or application menu.
2. In Quiver, select an object type from the catalog (e.g., "UnitStatus," "SoldierReadiness").
3. The object list loads showing all objects you have access to.
4. Apply filters using the filter panel on the left: select a property and enter a filter value.
5. Click an object in the list to view its full property set in the detail panel.
6. Use the **Related Objects** panel to navigate to linked objects (e.g., from a Unit to its assigned Soldiers).

NOTE: Quiver shows data from the Ontology — the structured, semantic layer of MSS. Objects in Quiver are the same objects that power Workshop applications. Changes made through authorized actions in Workshop are reflected here.

---

**TASK: VERIFY DATA CURRENCY AND PROVENANCE**

**Conditions:** Operator has a dataset or Workshop application open and needs to verify data is current.

**Standards:** Operator locates the last-updated timestamp and the data source, and determines whether the data meets currency requirements for the intended use.

**Equipment:** Active MSS session.

**Procedure:**

1. For a dataset: open the metadata panel (click the "Info" or "Details" tab). Find the **Last Updated** timestamp.
2. For a Workshop application: look for a data timestamp displayed in the app header or footer. If not visible, hover over a chart — the tooltip may show a data-as-of date.
3. Compare the last-updated time to your mission's data currency requirement. For most readiness reporting, data older than 24 hours requires verification.
4. To check provenance: open the dataset and click **Lineage** (if available). The lineage view shows where the data came from and what transformations it went through.
5. If the data is older than expected: contact your data steward. Do not use stale data for operational decisions without acknowledging the currency limitation.

## 4-2. How to Know if Data Is Current vs. Stale

| Indicator | Meaning | Action |
|---|---|---|
| Last updated less than scheduled interval | Data is current | Proceed normally |
| Last updated significantly past scheduled interval | Pipeline may have failed | Report to data steward |
| "No data available" message in dashboard | Data feed may be down | Report to data steward |
| Data values are unchanged for an unusually long period | Possible stale data | Verify with source unit |
| Warning triangle icon on dataset | Data quality alert | Read alert; report to data steward |

## 4-3. What to Do When Data Looks Wrong

Do not attempt to correct data yourself unless you are using an authorized Action or form designed for that purpose.

If you see data that appears incorrect:

1. Note the specific record: dataset name, row identifier, incorrect field, and the value you expected.
2. Do not share or act on the incorrect data operationally.
3. Contact your unit data steward with the specifics.
4. The data steward will determine the source of the error and coordinate the correction.

CAUTION: Guessing at data corrections, manually editing records outside of authorized interfaces, or working around incorrect data without reporting it degrades data integrity for everyone who uses the same data.

**Table 4-1. Data Quality Indicators**

| Indicator | What It Means | Operator Action |
|---|---|---|
| Green checkmark | Data passed quality checks | Use normally |
| Yellow warning | Data passed minimum checks but has anomalies | Review data before using; flag to steward |
| Red X | Data failed quality check | Do not use; report to data steward |
| "Null" or blank field | No data recorded for that field | Treat as unknown; do not infer a value |
| "UNKNOWN" value | Data was present but could not be determined | Treat as unknown; investigate if operationally significant |
| Duplicate rows | Same record appears more than once | Report to data steward; do not count duplicates as separate events |

---

# CHAPTER 5 — USING AIP AND AI TOOLS

**BLUF:** MSS includes AI-assisted tools under the Artificial Intelligence Platform (AIP). These tools can help you find information and summarize data faster. They require human review before any output is used operationally.

## 5-1. What AIP Is and What It Is Authorized for in USAREUR-AF

AIP (AI Platform) is MSS's AI layer. It connects large language models (LLMs) — AI systems that understand and generate natural language — to your unit's data in MSS. This allows you to ask questions about data in plain English and receive summaries, analyses, and recommendations.

In USAREUR-AF, AIP tools are authorized for:

- Summarizing readiness data across units
- Drafting SITREP text based on structured data
- Answering questions about data in MSS using natural language
- Surfacing patterns or anomalies in operational data

AIP tools are NOT authorized for:
- Making final operational decisions
- Generating official orders, directives, or legal documents without human review
- Accessing classified data without appropriate authorization
- Connecting to external systems or the public internet

## 5-2. CRITICAL NOTICE — AI Output Requires Human Review

WARNING: AI-generated content in MSS is NOT authoritative. AI tools can produce plausible-sounding but incorrect information. All AI outputs must be reviewed by a qualified human before being used to make operational decisions, submit reports, or brief commanders. The human operator is responsible for the accuracy of any AI-assisted product.

---

**TASK: USE AN AIP LOGIC WORKFLOW**

**Conditions:** Operator has access to an AIP Logic workflow embedded in a Workshop application.

**Standards:** Operator understands what the workflow does, reviews its output, and applies appropriate judgment before acting on the result.

**Equipment:** Active MSS session, Workshop application with AIP Logic workflow.

**Procedure:**

1. AIP Logic workflows appear in Workshop applications as automated process steps — they may show as status indicators, recommendations, or automated alerts (e.g., "Unit XYZ readiness has dropped below threshold — review recommended").
2. Read the workflow output displayed in the application.
3. Identify what data the workflow acted on (usually shown as a reference or detail link).
4. Verify the underlying data by clicking through to the source record.
5. Apply your own judgment to the recommendation before taking action.
6. If the recommendation is to execute an action (e.g., escalate a report), confirm it is appropriate based on your review of the underlying data before proceeding.

NOTE: AIP Logic workflows are automated rules your unit's data engineers configured. They are not infallible. Report unexpected or incorrect workflow outputs to your data steward.

---

**TASK: INTERACT WITH AN AIP AGENT**

**Conditions:** Operator has access to an AIP Agent embedded in a Workshop application or accessible through Agent Studio.

**Standards:** Operator successfully enters a natural language query, receives a response, and critically evaluates the response before using it.

**Equipment:** Active MSS session, access to AIP Agent interface.

**Procedure:**

1. Locate the Agent chat interface. It appears as a chat panel within a Workshop app or as a standalone Agent Studio interface.
2. Type your question in plain English in the chat input box. Be specific: instead of "how are we doing," type "what is the current readiness rate for units in 21st TSC?"
3. Press Enter or click Send.
4. The agent retrieves data from MSS and responds in the chat panel. The response may include text summaries, data tables, or links to source records.
5. Read the response carefully.
6. Verify key facts: click through to any source records the agent references to confirm the data is accurate.
7. If the response includes charts or tables, compare them to what you would see if you navigated to the data directly.
8. If the response is unexpected or appears incorrect, type a follow-up question or navigate to the data directly to verify.
9. Do not copy the AI response verbatim into an official document without verification.

NOTE: AIP Agents only have access to data within MSS that you are authorized to see. An agent cannot see data outside your access level. If an agent says it cannot find information, the data may not exist in MSS or you may not have access.

## 5-3. What AI Tools Cannot Do

| AI tools CANNOT... | Why it matters |
|---|---|
| Make binding operational decisions | Decisions require a human commander or responsible officer |
| Access data you are not authorized to see | Access controls are enforced regardless of how the query is made |
| Guarantee accuracy | LLMs can produce incorrect outputs ("hallucinate") |
| Modify data | Agents read data; only authorized Actions can write data |
| Access the public internet or external systems | AI operates within the MSS boundary |
| Override classification markings | Markings are enforced at the data level, not bypassed by AI |

## 5-4. Reporting AI Errors or Unexpected Outputs

If an AIP agent or workflow produces output that appears incorrect, unexpected, or potentially harmful:

1. Do not act on the output.
2. Document the query you entered and the output you received (screenshot).
3. Report to your unit data steward with the documentation.
4. The data steward will escalate to the MSS team for investigation.

---

# CHAPTER 6 — DATA SECURITY AND CLASSIFICATION HANDLING IN MSS

**BLUF:** MSS enforces data security through markings — labels on data that restrict who can see it. This chapter explains what those markings mean and what you must do to handle data properly.

## 6-1. Markings in MSS — What They Look Like and What They Mean

Markings in MSS appear as colored labels or badges on datasets, applications, and objects. They indicate classification level and handling requirements.

| Marking Label | Meaning |
|---|---|
| UNCLASSIFIED | No classification — still may have handling restrictions |
| CUI | Controlled Unclassified Information — requires protection but not classified |
| FOUO | For Official Use Only — subcategory of CUI |
| SECRET | Requires SECRET clearance to access |
| [AOR Label] | Data restricted to users with access to a specific area of responsibility |
| [Role Label] | Data restricted to users with a specific role marking (e.g., S2-only) |

NOTE: Markings are applied to data, not just documents. A dataset marked SECRET means every row in that dataset is at the SECRET level. If you can see it in MSS, your clearance and markings authorize you to see it.

## 6-2. What to Do if You See Data at a Higher Classification Than Your Clearance

If you navigate to data that appears to be at a classification level above your clearance:

1. STOP. Do not read, copy, screenshot, or act on the data.
2. Close the browser tab or navigate away immediately.
3. Do not discuss the content of the data with others.
4. Report the incident to your supervisor and unit security officer within one hour.
5. Document: what you accessed, when, how you got there, and that you did not read the content.

WARNING: This is a potential security incident. Report it immediately regardless of whether you think the data was misrouted or accessible in error. The security officer will determine the appropriate response. Failure to report is itself a security violation.

## 6-3. Authorized vs. Unauthorized Actions

| Action | AUTHORIZED | NOT AUTHORIZED |
|---|---|---|
| View data at your clearance level | Yes | — |
| Export data IAW handling requirements | Yes, with authorization | Without authorization |
| Share an MSS link with a colleague who has access | Yes | With someone who does not have access |
| Screenshot a dashboard | Only if approved for data level | Screenshots of classified data on unclassified systems |
| Submit data through authorized forms | Yes | Outside of designated forms |
| Discuss MSS data in open channels | Only UNCLASSIFIED data | CUI or above in unencrypted communications |
| Access another user's account | Never | — |
| Attempt to access restricted projects | Never | — |

---

**TASK: VERIFY YOUR ACCESS LEVEL AND MARKINGS**

**Conditions:** Operator is logged into MSS and wants to verify what access level and markings are assigned to their account.

**Standards:** Operator locates the profile page, identifies assigned markings, and understands what each marking grants access to.

**Equipment:** Active MSS session.

**Procedure:**

1. Click your profile icon in the upper right corner.
2. Select **Profile** or **Account Settings** from the dropdown.
3. In your profile, locate the **Markings** or **Access** section. This lists all markings assigned to your account.
4. Compare your markings to the data you need to access. If a required marking is absent, contact your data steward to request it.
5. Note your account's role assignments (Viewer, Editor) on the relevant projects.

NOTE: You cannot grant yourself markings or roles. Requests must go through your supervisor and the MSS administration team.

## 6-4. Aggregation Risk

CAUTION: Combining multiple pieces of unclassified or lower-classification data can produce a product that is classified at a higher level. This is called aggregation risk.

Example: Combining unit locations, readiness status, and personnel numbers — each individually UNCLASSIFIED — may produce a product classified at a higher level because it reveals combined operational capability.

Before exporting, sharing, or publishing any analysis that combines multiple data elements, have a security officer or data steward review the product.

## 6-5. Proper Procedures for Screenshots, Exports, and Sharing MSS Content

- **Screenshots:** Only take screenshots of data you are authorized to share. Screenshots inherit the classification of the data they contain.
- **Exports:** Export only through authorized export functions in Workshop. Do not use screen capture to export tabular data.
- **Sharing:** Share MSS links only with users who have access to the resource. Do not share data files via email or unencrypted channels unless the data marking permits it.
- **Printing:** Printed MSS output must be handled IAW the classification of the data. Print to approved printers only. Mark the printed document IAW Army marking requirements.

## 6-6. Incident Reporting Procedures

| Incident Type | Report To | When |
|---|---|---|
| Data at higher classification than clearance | Supervisor and unit security officer | Within 1 hour |
| Unauthorized access by another user | Supervisor and unit security officer | Immediately |
| Accidental data export to unauthorized location | Supervisor and unit security officer | Immediately |
| Lost or stolen device with MSS data | Supervisor, security officer, and S6 | Immediately |
| Suspected account compromise | Unit S6 and MSS admin | Immediately |

---

# CHAPTER 7 — TROUBLESHOOTING

**BLUF:** Most MSS problems can be resolved by the operator or escalated with the right information. Do not guess at fixes that might affect operational data. Follow the table below.

## 7-1. Common Problems and Actions

| Problem | Likely Cause | Operator Action |
|---|---|---|
| Cannot log in — browser does not prompt for certificate | CAC reader issue or browser configuration | Check CAC is inserted; restart browser; contact S6 |
| Cannot log in — PIN rejected | Incorrect PIN or locked CAC | Re-enter PIN carefully; if locked, contact S6 for CAC unlock |
| Cannot log in — account not found | Account not provisioned | Contact data steward to confirm account was created |
| Can log in but cannot see a project | Account not granted access to project | Contact data steward to request access |
| Dashboard shows no data | Filter returns zero results, or data pipeline failed | Clear all filters first; if still empty, contact data steward |
| Data in dashboard is stale | Pipeline has not run or failed | Contact data steward; note last-updated timestamp |
| Application fails to load | Browser or network issue | Refresh page; try a different browser; contact help desk |
| Form submission fails | Required field missing, or validation error | Read error message; correct identified field; resubmit |
| Action fails with an error | Permissions issue or data conflict | Note error message; contact data steward |
| Contour analysis returns unexpected results | Incorrect grouping or filter | Review analysis configuration; consult data steward |
| AIP agent gives wrong answer | AI error or data not in MSS | Verify data directly; report agent error to data steward |
| "Access Denied" on a resource | You do not have permission | Contact data steward — do not attempt to work around |

## 7-2. When to Self-Help vs. When to Escalate

**Self-help:**
- Browser and CAC issues not related to your account
- Clearing filters and refreshing the page
- Re-reading instructions and verifying field entries before form resubmission

**Escalate to data steward:**
- Any data quality or accuracy issue
- Missing access to a project or dataset
- Pipeline appears to have stopped running
- You cannot determine whether data is correct

**Escalate to security officer:**
- Any suspected security incident
- Data at wrong classification level
- Unauthorized access or account compromise

**Escalate to help desk:**
- System errors with error codes
- Application will not load after refresh
- Cannot access the MSS portal at all

## 7-3. Information to Collect Before Calling for Help

Before contacting the help desk or data steward, collect the following:

1. Your username (as shown in your profile)
2. The name and URL of the application or dataset
3. The exact error message text (screenshot is best)
4. The time the error occurred
5. Steps you took that led to the error
6. Whether the problem is consistent or intermittent
7. Your browser type and version (Help → About in your browser)

## 7-4. MSS Support Contacts and Escalation Path

| Issue Type | Point of Contact |
|---|---|
| Account access | Unit data steward → MSS admin team |
| Data quality | Unit data steward |
| System outage | MSS Help Desk |
| Security incident | Unit security officer → chain of command |
| Application bug | MSS Help Desk (reference application name and RID) |

NOTE: Contact information for your unit's data steward and the MSS Help Desk is maintained by your unit S6. This manual does not list specific phone numbers or email addresses, as they are subject to change. Obtain current contact information from your S6 or unit SOPs.

---

# CHAPTER 8 — OPERATOR MAINTENANCE

**BLUF:** For a software system, "operator maintenance" means keeping your account, settings, and access current. This chapter covers account hygiene tasks every MSS user should perform regularly.

---

**TASK: MANAGE YOUR USER PROFILE AND SETTINGS**

**Conditions:** Operator is logged into MSS.

**Standards:** Operator updates display name (if incorrect), sets notification preferences, and verifies profile information is accurate.

**Equipment:** Active MSS session.

**Procedure:**

1. Click your profile icon in the upper right corner and select **Profile** or **Settings**.
2. Verify your display name and email address are correct. If incorrect, contact your unit S6 or MSS admin to update.
3. Navigate to **Notification Preferences**.
4. Enable notifications for workflows or applications relevant to your role (e.g., SITREP submission confirmations, readiness threshold alerts).
5. Disable notifications that are not relevant to your role to avoid alert fatigue.
6. Save changes.

NOTE: Some profile fields (name, email, clearance level) are managed by MSS administrators and cannot be self-edited. Contact your data steward for corrections.

---

**TASK: BOOKMARK FREQUENTLY USED RESOURCES**

**Conditions:** Operator is logged into MSS and has identified resources they access regularly.

**Standards:** Operator stars at least two frequently used projects or applications for quick access from the home screen.

**Equipment:** Active MSS session.

**Procedure:**

1. Navigate to the dataset, application, or project you want to bookmark.
2. Click the **Star** icon next to the resource name (in Compass or in search results).
3. The resource now appears in your **Starred** or **Pinned** list on the MSS home screen.
4. To remove a bookmark: click the star again to toggle it off.

NOTE: Bookmarks are personal — they affect only your view. They do not change any permissions or make the resource more visible to others.

---

**TASK: REVIEW YOUR ACTIVE SESSIONS AND ACCESS**

**Conditions:** Operator is logged into MSS as part of a periodic security hygiene check.

**Standards:** Operator reviews active sessions, verifies no unexpected sessions are present, and reviews their current project and marking assignments.

**Equipment:** Active MSS session.

**Procedure:**

1. Click your profile icon and select **Profile** or **Security Settings**.
2. Locate the **Active Sessions** panel. It lists all current login sessions with timestamps and browser/IP information.
3. Review the list. If you see any session you do not recognize (unexpected browser, location, or time), report it to your unit security officer immediately.
4. Review your current project access list and markings. Confirm they match your current role and assignment.
5. If you have access to projects or data no longer relevant to your current assignment, notify your data steward to remove that access.

NOTE: Perform this check at least monthly, or whenever you change assignment, complete a TDY, or return from leave.

## 8-4. Account Deactivation Procedures

When you PCS, separate, retire, or no longer require MSS access for your current role:

1. Notify your unit data steward at least 5 business days before your departure or role change.
2. The data steward initiates account deactivation with the MSS admin team.
3. Transfer any saved analyses, bookmarks, or work products to the unit project folder before your access is removed. Personal workspace items may be deleted with the account.
4. If you are moving to a new unit that also uses MSS, a new account request must be submitted by your gaining unit.

CAUTION: Accounts that are not deactivated promptly after departure represent a security risk. Supervisors are responsible for ensuring departing personnel's accounts are deactivated in a timely manner.

---

# APPENDIX A — QUICK REFERENCE CARD

*Print and retain. Reference during initial MSS operations.*

---

**MAVEN SMART SYSTEM (MSS) — OPERATOR QUICK REFERENCE**

**1. LOG IN**
- Insert CAC → open browser → navigate to MSS portal URL
- Select authentication certificate → enter PIN
- Home screen loads = successful login

**2. FIND YOUR DATA**
- Use Search bar (top center) → type dataset or application name
- OR → Compass (left sidebar) → navigate to your unit's project folder

**3. OPEN A WORKSHOP APPLICATION**
- Search or Compass → click application name → wait for load
- Read dashboard → apply filters to narrow data → check data timestamp

**4. SUBMIT DATA**
- Locate form in application → complete all required fields (*)
- Verify accuracy → click Submit → wait for confirmation
- If error → read message → correct field → resubmit

**5. EXPORT DATA**
- Locate Export button in application → verify authorization
- Select format (CSV/Excel) → file downloads
- Handle file IAW data marking (classification level)

**6. REPORT PROBLEMS**
- Data issue → unit data steward
- Login/system issue → unit S6 or MSS Help Desk
- Security incident → supervisor + security officer IMMEDIATELY

**7. SECURITY RULES (ALWAYS)**
- Use only your own CAC and PIN
- Access only data you are authorized to see
- Log out when leaving your workstation
- Report stale, incorrect, or misrouted data — do not fix it yourself
- AI output requires human review before operational use

---

# APPENDIX B — AUTHORIZED USE POLICY SUMMARY

| AUTHORIZED | NOT AUTHORIZED |
|---|---|
| Log in using your own CAC | Log in using another person's credentials |
| View data you are cleared and marked for | Attempt to access data above your clearance or markings |
| Filter and sort data in dashboards | Edit data outside of authorized forms and actions |
| Submit data through authorized forms | Modify records outside designated interfaces |
| Execute actions in applications you are authorized to use | Execute actions without reading the confirmation |
| Export data IAW handling requirements | Export data without authorization or to unauthorized locations |
| Share MSS links with authorized users | Share MSS links or data with unauthorized users |
| Take screenshots of UNCLASSIFIED MSS content | Screenshot classified data on an unclassified device |
| Use AIP agents to query and summarize data | Use AI output as authoritative without human review |
| Report data quality issues to the data steward | Correct data errors yourself outside of authorized interfaces |
| Report security incidents immediately | Delay reporting or attempt to self-resolve security incidents |
| Bookmark and save personal views | Modify application layouts (builder access only) |
| Log out when finished | Leave an active MSS session unattended on an unlocked workstation |

---

# GLOSSARY

| Term | Definition |
|---|---|
| **Action** | A button or form in a Workshop application that writes data back to MSS. Submitting a SITREP or updating a unit status are examples of actions. |
| **AIP** | Artificial Intelligence Platform. The AI layer of MSS that enables natural language queries and automated workflows using approved AI models. |
| **AOR** | Area of Responsibility. In MSS, an AOR marking restricts data visibility to users assigned to that area. |
| **Bookmark (Star)** | A saved shortcut to a frequently used resource in MSS. Affects only your personal view. |
| **CAC** | Common Access Card. Your login credential for MSS. |
| **Compass** | MSS's file explorer. Displays all resources (datasets, applications, projects) organized by folder. |
| **Contour** | MSS's no-code analysis tool. Allows users to aggregate, filter, and chart data without writing code. |
| **CUI** | Controlled Unclassified Information. Data that requires protection but is not classified. |
| **Dashboard** | A visual display of data in a Workshop application. Includes charts, tables, and metric tiles. |
| **Dataset** | A structured table of data in MSS. Has columns (fields) and rows (records). |
| **Data Steward** | The person responsible for a dataset or application. First point of contact for data quality issues and access requests. |
| **DTG** | Date-Time Group. Military timestamp format (e.g., 111830Z MAR 26). |
| **Filter** | A control in a dashboard that narrows displayed data by a selected value (unit, date range, status). |
| **Foundry** | The Palantir platform on which MSS is built. Maven Smart System runs on Palantir Foundry. |
| **Lineage** | The record of where a dataset came from and what transformations it went through before reaching you. |
| **Marking** | A label applied to data in MSS that restricts who can see it. Based on classification level and role. |
| **Module** | One page or screen within a Workshop application. Applications can have multiple modules (e.g., Overview, Detail, Map). |
| **MSS** | Maven Smart System. The Army's operational data platform, built on Palantir Foundry. |
| **Object** | A record in the MSS Ontology representing a real-world thing — a Soldier, a unit, a vehicle, a report. |
| **Ontology** | The semantic layer of MSS. Defines what data represents in terms of real-world things and their relationships. |
| **Project** | A workspace in MSS containing related datasets, applications, and resources for a specific unit or mission area. |
| **Quiver** | MSS's ontology analysis tool. Allows users to explore objects and their relationships. |
| **RID** | Resource Identifier. A unique permanent ID for any resource in MSS (dataset, application, object). Useful when reporting problems. |
| **SITREP** | Situation Report. A standard format for reporting unit operational status. |
| **Workshop** | MSS's application layer. The interface most users see — dashboards, forms, maps, and reports built by developers. |

---

*TM-10 — Maven Smart System (MSS) Operator Technical Manual*
*HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA, Wiesbaden, Germany*
*UNCLASSIFIED — Approved for public release; distribution is unlimited.*
*For updates or corrections, contact the USAREUR-AF Operational Data Team.*
