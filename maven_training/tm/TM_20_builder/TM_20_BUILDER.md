# TM-20 — MAVEN SMART SYSTEM (MSS)
## BUILDER TECHNICAL MANUAL

**HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA**
Wiesbaden, Germany

2026

**PREREQUISITE PUBLICATIONS:** TM-10, Maven User; ADRP 1, Data Literacy (recommended)

**DISTRIBUTION RESTRICTION:** Approved for public release; distribution is unlimited.

---

## SAFETY SUMMARY

Builders have elevated privileges on MSS. Errors in transforms, pipelines, or ontology configurations may affect downstream applications and other users. Before building, understand:

- Changes to shared datasets affect all downstream users
- Publishing broken transforms can corrupt operational data pipelines
- Incorrect ontology configurations affect all Workshop applications built on those objects

Review all CAUTIONS and WARNINGS in this manual before beginning build activities.

---

## TABLE OF CONTENTS

- Chapter 1 — Introduction to Building on MSS
- Chapter 2 — Setting Up Your Build Environment
- Chapter 3 — Data Ingestion and Pipeline Builder
- Chapter 4 — Python Transforms (Basic)
- Chapter 5 — The Ontology (Fundamentals)
- Chapter 6 — Building Workshop Applications
- Chapter 7 — Data Quality and Validation
- Chapter 8 — Builder Reference and Standards
- Appendix A — Python Quick Reference
- Appendix B — Workshop Widget Reference
- Appendix C — Builder Checklist
- Glossary

---

## CHAPTER 1 — INTRODUCTION TO BUILDING ON MSS

### 1-1. Purpose and Scope

This manual provides task-level instruction for personnel who build applications, data pipelines, and analytical products on the Maven Smart System (MSS). MSS is the USAREUR-AF enterprise AI/data platform, built on Palantir Foundry. All work described in this manual takes place inside the MSS environment at USAREUR-AF.

CAUTION: All datasets, pipelines, and applications built on MSS are subject to Army data governance policy (Army CIO Memorandum, April 2024). Builders must coordinate with their unit Data Steward and the USAREUR-AF C2DAO before ingesting new data sources or publishing applications with externally-shared data.

**What TM-20 covers:**
- Creating projects, repositories, and build environments
- Ingesting data using Pipeline Builder and Python transforms
- Modeling data in the Ontology (Object Types, Link Types)
- Building Workshop applications for unit use
- Applying data quality checks

**What TM-20 does NOT cover:**
- Basic navigation of MSS — see TM-10, Maven User
- Advanced transform development, Functions (TypeScript), AIP agents, or Ontology SDK — see TM-30, Advanced Builder

Complete TM-10 before beginning this manual. If you cannot navigate Compass, preview a dataset, or find an existing Workshop app, stop and complete TM-10 first.

---

### 1-2. USAREUR-AF Mission Context and the Builder's Role

United States Army Europe and Africa (USAREUR-AF) is the Army Service Component Command (ASCC) to United States European Command (USEUCOM), responsible for theater land operations across the European Area of Responsibility (AOR) and integration with NATO Allied command structures and Joint All-Domain Command and Control (JADC2). The command's major subordinate commands — V Corps, 21st Theater Sustainment Command (TSC), and 7th Army Training Command (ATC) — each generate and consume data that flows through MSS.

As a builder, the tools you create directly affect readiness visibility and decision-making across this formation. A Workshop application you build may display unit status to a V Corps G3 or track maintenance readiness for a 21st TSC logistics officer. A pipeline you author may be the authoritative source for a theater-level briefing. Understand the operational weight of what you are building before you begin.

Builders should understand where their work sits in the USAREUR-AF 5-Layer Data Stack. Most TM-20 work occurs at Layers 2 (Integration — transforms, pipelines) and 3 (Semantic — Ontology, Object Types). Workshop applications are built at Layer 4 (Analytics) and published to users at Layer 5 (Activation).

NOTE: Detailed architecture guidance, ontology modeling references, and data design patterns are available at learn-data.armydev.com. Key resources for builders include: Object Type Cookbook v2 (canonical ontology modeling reference), DDOF Playbook (data design patterns), and the Data Modeling Fundamentals course.

**TM-20 Activity to USAREUR-AF 5-Layer Data Stack Mapping:**

| TM-20 Activity | Stack Layer | Layer Name | Builder Creates |
|---|---|---|---|
| Data ingestion via Pipeline Builder | Layer 2 | Integration | Connectors, ingestion pipelines |
| Python transforms (raw → staging → curated) | Layer 2 | Integration | Connectors, ingestion pipelines |
| Data quality and validation checks | Layer 2 | Integration | Connectors, ingestion pipelines |
| Object Type and Link Type configuration | Layer 3 | Semantic (Ontology) | Object Types, Links, Actions, basic Functions |
| Actions (write-back) | Layer 3 | Semantic (Ontology) | Object Types, Links, Actions, basic Functions |
| Workshop application development | Layer 4 | Analytics | Workshop applications, basic dashboards |
| Dashboard design and data exploration | Layer 4 | Analytics | Workshop applications, basic dashboards |
| Publishing forms and action-enabled apps | Layer 5 | Activation | Forms, action-enabled apps |
| Dataset access controls and markings | Layer 1 | Infrastructure | (Administered by platform admin; builder requests) |

---

### 1-3. The Builder's Responsibility

When you receive builder-level access on MSS, you gain the ability to create and modify resources that other users depend on. This is a significant responsibility.


**Your actions affect others.** A transform that produces incorrect data will propagate errors into every Workshop application and report that consumes it. A broken Ontology configuration can disable live applications for an entire unit. A dataset without proper markings can expose data to personnel without appropriate access.

**Four rules every builder must follow:**

1. Always develop on a branch — never on the production dataset or Ontology
2. Test before you publish — verify output row counts, spot-check data values
3. Follow naming conventions — every resource you create must be named to standard
4. Document your work — every dataset and Object Type requires a description

Builders are accountable for the quality and security of what they publish.

USAREUR-AF data governance follows Army CIO guidance (April 2024). Builders are responsible for complying with USAREUR-AF C2DAO standards for dataset naming, access control, and data quality.

---

### 1-4. MSS Build Environment Overview

The MSS build environment consists of five interconnected components. Understand all five before building anything.

| Component | What It Is | Where to Find It |
|---|---|---|
| **Compass** | File/resource explorer — everything lives here | Top navigation |
| **Code Repositories** | Where Python transforms are written and built | Compass → your project |
| **Pipeline Builder** | Visual (no-code) ETL tool for ingestion and simple transforms | Compass → New → Pipeline |
| **Ontology Manager** | UI for defining Object Types, Link Types, and Actions | Left nav → Ontology |
| **Workshop** | Drag-and-drop application builder | Left nav → Workshop |

These components are not independent. You build in the order: data first, then Ontology, then applications. Skipping steps creates problems that are difficult to untangle.

---

### 1-5. The Three-Layer Architecture

MSS is organized in three layers. You must build bottom-up. You cannot build an application until the Ontology is configured. You cannot configure the Ontology until you have clean data.

```
┌──────────────────────────────────────────┐
│  LAYER 3: APPLICATIONS                   │  ← Workshop apps, dashboards, AIP agents
├──────────────────────────────────────────┤
│  LAYER 2: ONTOLOGY                       │  ← Object Types, Link Types, Actions
├──────────────────────────────────────────┤
│  LAYER 1: DATA (Datasets)                │  ← Raw → Staging → Curated datasets
└──────────────────────────────────────────┘
```

**Why this order matters:**

- Layer 1 (Data): Raw data in, cleaned data out. Transforms live here. The output of Layer 1 is a curated dataset ready for the Ontology.
- Layer 2 (Ontology): Translates tables into meaningful objects — a row is no longer just a row, it is a `UnitStatus` or a `SoldierReadiness` record. The Ontology is shared across all applications.
- Layer 3 (Applications): Workshop apps and reports read from the Ontology. They never read directly from raw or staging datasets.

**The data flow from source to user:**

```
External Source → [Raw Dataset] → [Staging Dataset] → [Curated Dataset]
                                                              ↓
                                                       [Object Type]
                                                              ↓
                                                    [Workshop App / Report]
```

Never let a Workshop application read from a raw dataset. Raw data is unstable, unvalidated, and may change schema without warning.

---

### 1-6. Prerequisites Before You Build

Complete all of the following before writing any code or creating any resources on MSS.

**Access requirements:**
- [ ] TM-10 (Maven User) completed
- [ ] Builder access request submitted and approved through your chain of command
- [ ] Editor role granted on your team's project folder in Compass
- [ ] Editor role granted on the ontology branch for your team
- [ ] Developer role granted on Code Repositories (if writing Python transforms)

**Orientation requirements:**
- [ ] Located your team's project folder in Compass
- [ ] Opened at least one existing transform and read it
- [ ] Previewed the output dataset of that transform
- [ ] Found the Object Type backed by that dataset in Ontology Manager
- [ ] Used the Workshop application built on that Object Type as an end user

Do not begin building until you have completed this orientation. You need to understand the existing system before you add to it.

---

### 1-7. Key Naming Conventions

All builders must follow these conventions. Non-compliant resources will be renamed or removed by the team lead. Consistent naming is essential for maintainability and data lineage.

| Resource Type | Convention | Example |
|---|---|---|
| Dataset — raw tier | `/Project/AOR/source_name/raw` | `/USAREUR-AF/EUCOM/sitrep_feed/raw` |
| Dataset — staging tier | `/Project/AOR/source_name/staging` | `/USAREUR-AF/EUCOM/sitrep_feed/staging` |
| Dataset — curated tier | `/Project/AOR/source_name/curated` | `/USAREUR-AF/EUCOM/sitrep_feed/curated` |
| Code Repository | `kebab-case` | `sitrep-transforms`, `unit-readiness-pipeline` |
| Transform function | `snake_case` | `raw_to_staging`, `compute_readiness_score` |
| Object Type | `PascalCase` singular noun | `UnitStatus`, `SoldierReadiness`, `LogisticsRecord` |
| Link Type | Verb phrase describing the relationship | `assignedTo`, `reportedBy` |
| Workshop App | Plain English, unit-appropriate | `EUCOM SITREP Dashboard`, `Personnel Tracker` |
| Ontology branch | `dev-[feature]` or `dev-[your-name]` | `dev-sitrep`, `dev-smith` |

NOTE: Dataset paths are permanent. You cannot rename a dataset path without breaking all downstream transforms and Ontology objects that reference it. Choose paths carefully before creating any dataset.

---

### 1-8. Getting Help

| Resource | Use For |
|---|---|
| Palantir Foundry documentation (in-platform help) | Official API reference, widget options, transform syntax |
| MAVEN_FIELD_MANUAL.md (team repo) | Team-specific patterns, MSS-specific guidance |
| data_skills/13_foundry_patterns/ | Python code examples for transforms and checks |
| Team lead / data engineer | Architecture decisions, access issues, naming questions |
| MSS support ticket | Platform errors, access not granted after 48 hours |

When escalating, always include: the resource RID, the error message (exact text), and the steps you took before the error occurred.

### 1-9. Governing References

The following documents govern MSS build activities and data handling policy in USAREUR-AF:

- **Army Data Plan (2022), Office of the Army Chief Information Officer** — Establishes the Army-wide framework for data management, governance, and analytics in support of Multi-Domain Operations.
- **DoD Data Strategy (2020)** — Establishes the VAUTI framework (Visible, Accessible, Understandable, Trustable, Interoperable) as the DoD standard for data quality and interoperability.
- **Army CIO Data Stewardship Policy (April 2, 2024)** — Establishes the data stewardship hierarchy (MADO, Data Steward, Functional Data Manager, C2DAO) and data chain of responsibility.

---

## CHAPTER 2 — SETTING UP YOUR BUILD ENVIRONMENT

### 2-1. Projects, Folders, and Repositories

Before creating any resource, understand how MSS organizes build assets.

| Container | What It Holds | Analogy |
|---|---|---|
| **Project** | A top-level grouping of all resources for one functional area | A SharePoint site |
| **Folder** | A subdirectory within a project — organize by layer or data source | A folder on a file server |
| **Code Repository** | A versioned code store for transforms (like a GitHub repo) | A Git repository |
| **Dataset** | A managed table — created by a transform or ingestion | A database table |
| **Pipeline** | A visual ETL flow (Pipeline Builder) | A workflow diagram |

Your team's project already exists. Do not create a new top-level project without approval. Add your work inside the existing project structure.

---

**TASK: CREATE A PROJECT**

**Conditions:** Builder access granted; no existing project for your functional area; team lead has authorized creation.

**Standards:** Project is created with the correct name format, appropriate permissions assigned, and folder structure established before any datasets are created inside it.

**Equipment:** MSS account with Owner or Admin role on the parent folder.

**Procedure:**
1. Navigate to Compass and find the parent folder where the project will live.
2. Select New → Project.
3. Name the project using the format: `[ORGANIZATION]-[FUNCTION]` (example: `21TSC-Logistics`).
4. Set the project description — describe what data and applications live here.
5. Under Permissions, add your team lead as Owner.
6. Add your team members as Editors.
7. Add end users (analysts, staff) as Viewers.
8. Create the following subfolders inside the project:
   - `data/raw`
   - `data/staging`
   - `data/curated`
   - `ontology`
   - `applications`
9. Confirm the project and folder structure appears in Compass before proceeding.

NOTE: Assign the most restrictive permissions necessary. Viewers can see but not modify. Editors can modify but not delete or grant access. Owners can do everything.

CAUTION: Do not grant Owner access to end users. Owner access allows permission changes that could expose data to unauthorized personnel.

---

**TASK: CREATE A CODE REPOSITORY**

**Conditions:** Project exists; builder has Editor or Owner role on the project; intent is to write Python transforms.

**Standards:** Repository is created, correctly named, connected to the project, and a README.md exists before any transform code is written.

**Equipment:** MSS account with Developer role on Code Repositories; project must exist first.

**Procedure:**
1. Navigate to your project folder in Compass.
2. Select New → Code Repository.
3. Select repository type: **Transforms (Python)**.
4. Name the repository using `kebab-case` (example: `sitrep-pipeline-transforms`).
5. Confirm the repository is created and the default branch (`master`) exists.
6. Open the repository. Verify the following default structure is present:
   ```
   transforms-python/
   └── src/
       └── myproject/
           └── __init__.py
   pipeline-spec.yml
   README.md
   ```
7. Edit `README.md` to describe the purpose of this repository, inputs, and outputs.
8. Commit the README change with message: `Initial repo setup — [purpose description]`.

NOTE: Code repositories use Git for version control. All changes are tracked. Never commit credentials, classification markings, or operational data payloads to a repository.

WARNING: Never store passwords, API tokens, or connection strings in repository code. Use environment variables or Foundry Secrets. Committing credentials to a repository is a security violation.

---

**TASK: SET UP FOUNDRY BRANCHING FOR DEVELOPMENT**

**Conditions:** Code repository exists; intent is to develop a new transform or modify an existing one.

**Standards:** A development branch is created from `master`, all development work occurs on the branch, and no direct commits are made to `master` during development.

**Equipment:** Existing code repository with `master` branch.

**Procedure:**
1. Open your code repository in Compass.
2. In the branch selector (top of the repository view), select Create New Branch.
3. Name the branch using the format: `dev-[feature-name]` (example: `dev-sitrep-normalization`).
4. Base the branch on `master`.
5. All development work — writing transforms, testing builds, fixing errors — happens on this branch.
6. When development is complete and output is verified, submit a Pull Request (PR) from `dev-[feature-name]` → `master`.
7. Assign at least one team member as reviewer.
8. After approval, merge the PR. Delete the feature branch.

NOTE: The same branching principle applies to datasets and the Ontology. Develop on a branch; merge to master only when verified.

CAUTION: Direct commits to `master` in a shared repository bypass the review process and can push untested code into production pipelines. This affects all downstream users immediately.

---

**TASK: REQUEST AND CONFIGURE DATA ACCESS**

**Conditions:** Builder needs to read from an existing dataset as input to a transform.

**Standards:** Access is requested through proper channels; input dataset is verified to have correct markings before use; access is the minimum necessary.

**Equipment:** MSS account; knowledge of which datasets are needed; team lead or data steward contact.

**Procedure:**
1. Identify the dataset you need. Copy its RID from Compass → dataset → three-dot menu → Copy RID.
2. Verify the dataset tier. Confirm you are requesting access to the staging or curated tier — not the raw dataset.
3. Submit an access request to the dataset owner (Compass → dataset → Permissions → Request Access). Include your justification and the RID.
4. After access is granted, open the dataset and verify you can preview it.
5. Check the dataset markings. Open the dataset → Info → Markings. Confirm your output dataset will carry the same or more restrictive markings.
6. Add the dataset as an `Input()` reference in your transform. Do not copy data out of MSS to verify access.

WARNING: Do not attempt to access datasets you have not been granted permission to use. Unauthorized access attempts are logged and may be reported to the chain of command. If you discover you can access a dataset you should not be able to see, report it to your team lead immediately.

CAUTION: If your input dataset carries a marking (classification or AOR restriction), your output dataset must carry the same marking. Markings do not transfer automatically — you must request them from the data steward.

---

### 2-2. Development Workflow Overview

All development on MSS follows the same cycle. Do not skip steps.

```
1. CREATE BRANCH (from master)
       ↓
2. WRITE / MODIFY (code, pipeline, ontology config)
       ↓
3. BUILD (run the transform, check output)
       ↓
4. VERIFY (row counts, spot-check values, check logs)
       ↓
5. PULL REQUEST (assign reviewer)
       ↓
6. REVIEW & MERGE (reviewer approves → merge to master)
       ↓
7. PRODUCTION BUILD (master branch runs, output goes live)
```

Never skip step 4. A build that completes without errors is not the same as a build that produced correct output.

---

## CHAPTER 3 — DATA INGESTION AND PIPELINE BUILDER

### 3-1. Overview of Data Ingestion

Data enters MSS in four ways:

| Method | Use Case | Who Configures |
|---|---|---|
| **Direct File Upload** | One-time or reference data (lookup tables, shapefiles) | Builder |
| **Pipeline Builder** | Scheduled file ingestion, basic transformations, no-code ETL | Builder |
| **Magritte Connector** | Automated pulls from approved external systems (databases, REST APIs) | Admin / Data Engineer |
| **Datasets API** | Programmatic ingestion from external scripts | Developer (TM-30) |

For most USAREUR-AF builders, Pipeline Builder covers the majority of ingestion needs. Use Magritte connectors when data arrives on a recurring schedule from an approved external system. Use direct upload for reference data that rarely changes.

---

### 3-2. Dataset Transactions: SNAPSHOT vs. APPEND

Every write to a Foundry dataset creates a transaction. Understanding transaction types prevents data loss and duplication.

| Transaction Type | Behavior | Use When |
|---|---|---|
| **SNAPSHOT** | Replaces the entire dataset with new data | Full refresh; reference tables; when history is not needed |
| **APPEND** | Adds new rows to existing data | Event logs; SITREPs; any data that accumulates over time |

CAUTION: Using SNAPSHOT on an append-intended dataset will delete all historical records every time the pipeline runs. Verify the correct transaction type before publishing any pipeline.

---

**TASK: INGEST A FILE USING PIPELINE BUILDER**

**Conditions:** A file (CSV, Excel, JSON) is available for upload; builder has Editor access to the target project folder.

**Standards:** File is uploaded, schema is verified, output dataset is created in the correct `raw` folder, and the dataset can be previewed successfully.

**Equipment:** MSS account with Editor access; source file under 500MB (for direct upload); target project folder exists.

**Procedure:**
1. Navigate to your project's `data/raw` folder in Compass.
2. Select New → Dataset → Upload File.
3. Select your file. MSS will auto-detect the format (CSV, Excel, Parquet).
4. Review the schema preview. Confirm column names and types look correct.
5. Name the dataset following the naming convention: `/Project/AOR/source_name/raw`.
6. Select Create Dataset.
7. After upload completes, open the dataset and select Preview.
8. Verify:
   - Row count matches the source file
   - No columns are missing
   - No data type errors (numbers showing as strings, dates as nulls)
9. Document the dataset: select Info → Edit Description. Describe the source, date received, and point of contact.

NOTE: Direct file upload creates a SNAPSHOT transaction. Each upload replaces the previous version. To preserve history, use APPEND mode or an incremental pipeline.

CAUTION: Do not upload files containing PII (Personally Identifiable Information) or data marked above UNCLASSIFIED without first confirming the dataset path and markings are configured for that classification level. Contact your data steward before uploading sensitive data.

---

**TASK: CREATE A BASIC DATA CONNECTION**

**Conditions:** An approved external data source exists (database, S3 bucket, REST API); admin or Magritte configuration access has been granted; recurring ingestion is required.

**Standards:** Connector is configured, test connection succeeds, sync schedule is set, and the output raw dataset receives data on first sync.

**Equipment:** Connection credentials stored in Foundry Secrets (never hardcoded); target raw dataset path established; admin approval for the external system.

**Procedure:**
1. Navigate to Data Connection (left nav) → New Connection.
2. Select the connector type matching your source system (JDBC, S3, REST API, etc.).
3. Enter the connection name in `kebab-case` format.
4. Configure credentials using Foundry Secrets — do not enter passwords directly in the connection fields.
5. Test the connection. Confirm success before proceeding.
6. Configure the sync target: select or create the raw dataset path.
7. Set the sync schedule (example: daily at 0600 UTC).
8. Enable the connection and confirm the first sync completes.
9. Preview the output dataset after the first sync.

WARNING: Connection credentials stored outside Foundry Secrets (hardcoded in config, in code, or in comments) are a security violation. All credentials must go through Foundry Secrets or an approved secrets management system.

---

**TASK: CONFIGURE A PIPELINE BUILDER FLOW**

**Conditions:** At least one input dataset exists (raw); output dataset path has been planned; builder wants to apply transformations without writing Python code.

**Standards:** Pipeline executes end-to-end without errors; output dataset contains expected rows; pipeline is scheduled or documented for manual execution.

**Equipment:** MSS account with Editor access; input dataset(s) available; target output folder exists.

**Procedure:**
1. Navigate to your project folder in Compass. Select New → Pipeline.
2. Name the pipeline using `kebab-case`: `[source]-[stage]-pipeline` (example: `sitrep-staging-pipeline`).
3. In the Pipeline Builder canvas, add an Input node. Connect it to your raw dataset.
4. Add transformation nodes as needed:
   - **Filter**: Remove rows where a required field is null
   - **Select Columns**: Remove columns not needed downstream
   - **Rename Columns**: Standardize column names to `snake_case`
   - **Derive Column**: Add computed fields (example: uppercase `unit_id`)
5. Add an Output node. Set it to your staging dataset path.
6. Set the transaction type: SNAPSHOT for full refresh, APPEND for accumulating data.
7. Run the pipeline manually using the Run button.
8. After completion, open the output dataset and Preview.
9. Verify row counts and spot-check at least 5 rows for accuracy.
10. If correct, configure the schedule: Pipeline → Schedule → set cron expression.

NOTE: Pipeline Builder is appropriate for straightforward transformations. When logic becomes complex (multi-table joins, conditional logic, custom business rules), switch to Python transforms. See Chapter 4.

---

**TASK: MONITOR A PIPELINE FOR ERRORS**

**Conditions:** A pipeline or transform has been configured; builder needs to confirm successful execution or investigate a failure.

**Standards:** Builder can locate build logs, identify the error type and line, and take corrective action within 30 minutes of a build failure notification.

**Equipment:** Access to the pipeline or code repository; Editor access on the resource.

**Procedure:**
1. Navigate to the pipeline or code repository in Compass.
2. Select Builds (top tab). The most recent build is listed first.
3. Identify the build status:
   - Green checkmark = Success
   - Red X = Failed
   - Orange clock = Running or queued
4. For a failed build, select the build record to open the logs.
5. For Python transform failures, look for the `Caused by:` line in the log output — this identifies the root error.
6. Common error types and actions:

| Error Type | Symptom in Log | Action |
|---|---|---|
| Syntax error | Fails immediately, Python line number shown | Fix syntax, rebuild |
| Missing column | `AnalysisException: cannot resolve column` | Verify input dataset schema |
| Schema mismatch | `Schema mismatch on write` | Delete output dataset and rebuild |
| Empty output | Build succeeds, zero rows in output | Check filter conditions — likely too restrictive |
| Memory error | `OutOfMemory` or container killed | Switch from `@lightweight` to `@transform_df` (Spark) |

7. After correcting the error, trigger a new build.
8. Verify the new build succeeds and output row count is non-zero and plausible.

---

### 3-3. When to Use Pipeline Builder vs. Python Transforms

| Situation | Recommended Tool |
|---|---|
| Simple column selection and renaming | Pipeline Builder |
| Filtering rows on a single condition | Pipeline Builder |
| File upload with basic cleanup | Pipeline Builder |
| Multi-table join with complex logic | Python Transform |
| Custom business rule (C-rating derivation, DTG parsing) | Python Transform |
| Deduplication with custom key | Python Transform |
| Incremental processing of large/growing datasets | Python Transform (`@incremental`) |
| Anything requiring custom Python libraries | Python Transform |

---

## CHAPTER 4 — PYTHON TRANSFORMS (BASIC)

### 4-1. What a Transform Is

A Python transform is code that reads one or more Foundry datasets, applies logic, and writes a new dataset. Foundry runs transforms on Apache Spark — a distributed compute engine — so transforms can process datasets of any size without memory limitations.

You write the logic. Foundry handles the infrastructure.

Every transform has:
- **Inputs**: One or more datasets the transform reads from
- **Computation**: Your Python/PySpark logic
- **Output**: One dataset the transform writes to

Transforms are triggered by Foundry when an input dataset changes, or on a configured schedule.

---

### 4-2. The Three Transform Types

| Decorator | Compute | Use When |
|---|---|---|
| `@transform_df` | Spark (distributed) | Standard batch processing; large datasets; most use cases |
| `@transform` | Spark (distributed) | Need fine-grained control over read/write; multiple outputs |
| `@lightweight_transform` | Python container (pandas) | Small datasets (<1M rows); complex Python logic; no Spark needed |

Start with `@transform_df`. It is the simplest syntax and handles the majority of use cases. Switch to `@transform` when you need multiple output datasets from one function. Use `@lightweight_transform` only for small reference tables or complex Python operations not available in PySpark.

NOTE: Foundry manages all Spark configuration. You do not configure executors, memory, or cluster settings. If a transform runs out of memory, the fix is to switch from `@lightweight_transform` to `@transform_df` — not to adjust Spark settings.

---

### 4-3. Code Repository Structure

```
sitrep-pipeline-transforms/
├── transforms-python/
│   └── src/
│       └── sitrep/
│           ├── __init__.py
│           ├── raw_to_staging.py       ← clean and normalize raw data
│           └── staging_to_curated.py  ← final prep for ontology backing
├── pipeline-spec.yml                   ← build and schedule config
└── README.md                           ← purpose, inputs, outputs
```

One Python file per logical stage of the pipeline. Each file contains one or more transform functions. Keep functions focused — one transform, one clear purpose.

---

**TASK: WRITE A BASIC @transform_df TRANSFORM**

**Conditions:** Code repository exists; input dataset is available and accessible; builder understands the data schema and the transformation required.

**Standards:** Transform builds without errors; output dataset contains expected rows; no hardcoded paths; function is documented with a docstring.

**Equipment:** Code repository with Developer access; input dataset with Viewer access; target output path planned.

**Procedure:**
1. Open your code repository. Switch to your development branch.
2. Navigate to `transforms-python/src/[your-project]/`.
3. Create a new Python file named for the transformation stage: `raw_to_staging.py`.
4. Write the transform using the `@transform_df` decorator. Minimum working example for a unit readiness pipeline:

```python
from transforms.api import transform_df, Input, Output
import pyspark.sql.functions as F

@transform_df(
    Output("/USAREUR-AF/EUCOM/unit_readiness/staging"),
    source=Input("/USAREUR-AF/EUCOM/unit_readiness/raw"),
)
def compute(source):
    """
    Clean and normalize raw unit readiness data.
    Drops records with null unit_id or readiness_pct.
    Standardizes unit_id to uppercase.
    """
    df = source

    # Remove records missing required fields
    df = df.filter(
        F.col("unit_id").isNotNull() &
        F.col("readiness_pct").isNotNull()
    )

    # Standardize unit_id: uppercase, strip whitespace
    df = df.withColumn("unit_id", F.upper(F.trim(F.col("unit_id"))))

    # Keep only columns needed downstream
    df = df.select("unit_id", "readiness_pct", "report_dtg", "aor")

    # Add pipeline metadata
    df = df.withColumn("_processed_at", F.current_timestamp())

    return df
```

5. Save the file.
6. In the repository, select Build → Build Now (on your dev branch).
7. Monitor the build log. Wait for completion.
8. Open the output dataset. Select Preview.
9. Verify: row count is reasonable, `unit_id` values are uppercase, no nulls in required fields.
10. Commit the file with a descriptive message: `Add raw_to_staging transform for unit readiness`.

CAUTION: Never hardcode dataset paths as plain strings inside your Python logic. All input and output paths must be declared as `Input()` and `Output()` in the decorator. Hardcoded paths break when the dataset is moved and cannot be tracked by Foundry's data lineage system.

---

**TASK: ADD DEPENDENCIES TO A TRANSFORM**

**Conditions:** Transform requires a Python library not available by default in Foundry's environment (example: `shapely`, `openpyxl`, a custom parsing library).

**Standards:** Dependency is declared in the repository configuration; transform builds successfully with the new library available; no library is installed via `pip install` inside transform code.

**Equipment:** Code repository; knowledge of the required package name and version.

**Procedure:**
1. Open your code repository.
2. Navigate to `transforms-python/`. Find or create the file `conda_recipe.yml` (for conda packages) or `requirements.txt` (for pip packages).
3. Add the required package:

```
# requirements.txt
pandas==2.1.0
openpyxl>=3.1.0
```

4. Save and commit the file.
5. Trigger a new build. Foundry will install the dependency before running your transform.
6. Verify the build succeeds and the library imports correctly in your transform.

NOTE: Only add dependencies you actually use. Each additional dependency increases build time. For standard data operations, PySpark's built-in functions cover most needs without additional libraries.

---

**TASK: BUILD AND RUN A TRANSFORM**

**Conditions:** Transform code is written and saved in the repository on a development branch.

**Standards:** Build completes without errors; output dataset is populated; builder has reviewed output data before considering the transform ready for merge.

**Equipment:** Code repository with at least one transform function; Developer access.

**Procedure:**
1. Confirm you are on your development branch (not `master`).
2. Save all changes in your Python files.
3. Select Build → Build Now from the repository view.
4. The build graph shows which transforms will run. Confirm the correct transforms are included.
5. Monitor the build. Progress is shown per-transform.
6. After completion, open each output dataset and:
   - Check the row count (Schema → Overview)
   - Preview a sample of rows
   - Verify expected columns are present with correct types
7. If the build succeeds and output looks correct, the transform is ready for code review and merge.

NOTE: A successful build only means the code ran without crashing. It does not mean the output is correct. Always spot-check the data.

---

**TASK: DEBUG A FAILED TRANSFORM**

**Conditions:** A transform build has failed; builder must identify and correct the error.

**Standards:** Root cause is identified from the build log; corrective action is taken; transform builds successfully on the next attempt.

**Equipment:** Code repository with a failed build; Editor access.

**Procedure:**
1. Open the repository. Select Builds. Select the failed build.
2. Read the log from the top. The first error is usually the root cause.
3. For Python errors, look for the traceback. The last line of the traceback identifies the error type and message.
4. For Spark execution errors, look for the `Caused by:` line — this is often deep in the log.
5. Match the error to the table below and take the indicated action:

| Error Message | Likely Cause | Fix |
|---|---|---|
| `SyntaxError` or `IndentationError` | Python syntax problem | Fix the indicated line |
| `AnalysisException: cannot resolve column` | Column name mismatch | Verify column names against input schema |
| `AnalysisException: schema mismatch` | Output schema changed from previous run | Delete the output dataset and rebuild |
| Build succeeds, zero output rows | Filter removed all data | Print row counts at each filter step; check filter conditions |
| `OutOfMemoryError` | `@lightweight_transform` on too much data | Switch to `@transform_df` |
| `ModuleNotFoundError` | Missing dependency | Add to `requirements.txt` |

6. Make the correction, save, and trigger a new build.
7. Repeat until the build succeeds and output is verified.

---

### 4-4. Basic PySpark Operations Reference

```python
import pyspark.sql.functions as F
from pyspark.sql.types import StringType, IntegerType, TimestampType

# Filter rows
df.filter(F.col("status") == "ACTIVE")
df.filter(F.col("unit_id").isNotNull())
df.filter(F.col("readiness_pct").between(0, 100))

# Select columns
df.select("unit_id", "readiness_pct", "report_dtg")

# Add or modify a column
df.withColumn("upper_unit", F.upper(F.col("unit_id")))
df.withColumn("processed_at", F.current_timestamp())

# Rename a column
df.withColumnRenamed("old_name", "new_name")

# Remove duplicates
df.dropDuplicates(["unit_id", "report_dtg"])

# Join two datasets
df1.join(df2, df1["unit_id"] == df2["id"], "left")

# Aggregate
df.groupBy("aor").agg(
    F.count("*").alias("unit_count"),
    F.avg("readiness_pct").alias("avg_readiness")
)

# Cast type
df.withColumn("count", F.col("count").cast(IntegerType()))

# Fill nulls
df.fillna({"status": "UNKNOWN", "count": 0})

# Parse DTG string to timestamp (military date-time groups)
df.withColumn("dtg_ts", F.to_timestamp(F.col("dtg_string"), "ddHHmm'Z' MMM yy"))
```

---

## CHAPTER 5 — THE ONTOLOGY (FUNDAMENTALS)

### 5-1. What the Ontology Is

The Ontology is the "meaning layer" of MSS. It translates flat dataset rows into meaningful real-world objects that applications can reason about.

Without the Ontology, MSS is a collection of tables. With the Ontology, those tables become **Soldiers**, **Units**, **Vehicles**, and **Missions** — objects with properties, relationships, and business logic attached to them.

Every Workshop application, AIP agent, and analytical tool built on MSS reads from the Ontology, not directly from datasets. This is why Ontology quality is critical: errors in the Ontology affect every application built on top of it.

---

### 5-2. Object Types vs. Datasets

| Concept | Datasets | Object Types |
|---|---|---|
| What it is | A table with rows and columns | A class of real-world things |
| How you access it | Preview, transform input/output | Search, Workshop widgets, AIP agents |
| Has relationships | No — just a table | Yes — linked to other object types |
| Has business logic | No | Yes — computed properties, functions |
| Can write back | No | Yes — via Actions |

A dataset is the storage layer. An Object Type is the semantic layer built on top of that storage.

---

### 5-3. Link Types

Link Types define how Object Types relate to each other. They are the connections in the Ontology graph.

Example relationships for a personnel readiness system:
- `Soldier` **assignedTo** `Unit` (many-to-one)
- `Unit` **submits** `SitrepReport` (one-to-many)
- `Vehicle` **assignedTo** `Unit` (many-to-one)

Link Types are bidirectional automatically. If `Soldier assignedTo Unit`, you can query from either direction.

---

**TASK: CREATE AN OBJECT TYPE**

**Conditions:** A curated dataset exists and is ready for Ontology backing; builder has Editor access on the Ontology branch; naming convention for the Object Type has been confirmed with team lead.

**Standards:** Object Type is created on the correct Ontology branch (not production), backed by the curated dataset, with primary key set, title property set, and a description written before any properties are added.

**Equipment:** Ontology Manager; curated dataset with Viewer access; Ontology branch (dev) checked out.

**Procedure:**
1. Navigate to Ontology Manager (left nav).
2. Confirm you are on a development branch, not the production Ontology. Check the branch selector at the top.
3. Select Object Types → New Object Type.
4. Enter the name: `PascalCase` singular noun (example: `UnitStatus`).
5. Write a description: describe what this object represents in one to two sentences.
6. Under Backing Dataset, select your curated dataset.
7. Set the Primary Key: select the column that uniquely identifies each row (example: `unit_id`).
8. Set the Title Property: select the column that will display as the object's name in search results (example: `unit_name`).
9. Save the Object Type.
10. Do not add properties yet — proceed to the next task.

CAUTION: Object Type creation on the production Ontology takes effect immediately and affects all live applications. Always create and test on a dev branch first.

---

**TASK: ADD PROPERTIES TO AN OBJECT TYPE**

**Conditions:** Object Type exists on a dev branch; curated dataset has been reviewed and columns to expose have been identified.

**Standards:** Only columns needed by applications are exposed as properties; all properties have display names in plain English; no raw/internal columns (prefixed with `_`) are added as properties.

**Equipment:** Ontology Manager; Object Type in edit mode.

**Procedure:**
1. Open the Object Type in Ontology Manager. Select Properties → Add Property.
2. For each property:
   a. Select the source column from the backing dataset.
   b. Set the API name (auto-generated from column name — verify it is `camelCase`).
   c. Set the display name (plain English, readable by end users — example: "Report Date").
   d. Confirm the property type (String, Integer, Timestamp, Boolean, GeoPoint, etc.).
3. Repeat for each column that applications will need.
4. Do not add columns prefixed with `_` (pipeline metadata columns).
5. Save the Object Type after adding all properties.
6. Navigate to Object Explorer and search for your Object Type. Verify objects appear and properties display correctly.

NOTE: Property type matters. A `Timestamp` field enables date-range filtering in Workshop. A `GeoPoint` field enables map display. Choose the correct type — it cannot be changed after publication without breaking downstream applications.

---

**TASK: CREATE A LINK TYPE**

**Conditions:** Two Object Types exist on the same Ontology branch; a documented relationship exists between them; the foreign key column is present in at least one of the backing datasets.

**Standards:** Link Type correctly represents the real-world relationship; cardinality is set accurately; link is verified to return objects from both directions in Object Explorer.

**Equipment:** Ontology Manager; both Object Types with Viewer access.

**Procedure:**
1. Navigate to Ontology Manager → Link Types → New Link Type.
2. Name the link using a verb phrase that describes the relationship (example: `assignedTo`).
3. Set Object Type A: the source object (example: `Soldier`).
4. Set Object Type B: the target object (example: `Unit`).
5. Set cardinality:
   - **One-to-Many**: one Unit has many Soldiers
   - **Many-to-One**: many Soldiers belong to one Unit
   - **Many-to-Many**: a Soldier can be assigned to multiple tasks and a task can have multiple Soldiers
6. Map the join key: select the column in Object Type A that matches the primary key of Object Type B (example: `unit_id` in Soldier matches `id` in Unit).
7. Save the Link Type.
8. In Object Explorer, open one Soldier object and verify the linked Unit appears in the Related Objects panel.

---

**TASK: PUBLISH OBJECTS TO THE ONTOLOGY**

**Conditions:** Object Type is correctly configured on a dev branch; all properties are verified; team lead has reviewed and approved the configuration.

**Standards:** Ontology branch is merged to production via Pull Request with reviewer approval; object count in production Ontology matches the curated dataset row count.

**Equipment:** Ontology Manager; PR reviewer assigned.

**Procedure:**
1. Verify the Object Type configuration on the dev branch is complete and tested.
2. Navigate to the Ontology branch manager. Create a Pull Request from your dev branch to the production Ontology branch.
3. Assign your team lead or a senior builder as reviewer.
4. After approval, merge the PR.
5. Navigate to the production Ontology. Open the newly published Object Type.
6. Verify the object count matches the expected row count from the curated dataset.
7. Open Object Explorer and search for several objects. Confirm properties display correctly.
8. Notify team lead that the Object Type is live and downstream applications can now be updated.

---

### 5-4. Naming Conventions for Ontology Resources

| Resource | Convention | Example |
|---|---|---|
| Object Type | `PascalCase` singular noun | `SoldierReadiness`, `UnitStatus`, `LogisticsItem` |
| Property API name | `camelCase` | `reportDate`, `unitId`, `readinessPct` |
| Property display name | Plain English, title case | "Report Date", "Unit ID", "Readiness %" |
| Link Type | `camelCase` verb phrase | `assignedTo`, `submittedBy`, `locatedIn` |
| Action Type | Verb + Noun, `PascalCase` | `UpdateUnitStatus`, `CreateSitrepEntry` |

---

### 5-5. Common Ontology Mistakes

| Mistake | Why It's a Problem | Prevention |
|---|---|---|
| Backing Object Type with staging dataset | Staging data is not final; schema changes break the Object Type | Only use curated tier datasets |
| Changing the primary key after publication | Destroys all existing object identities | Choose primary key before publishing; never change it |
| Exposing `_processed_at` and other pipeline columns as properties | Clutters the object model; confuses users | Only expose columns that represent real-world attributes |
| Adding properties without display names | Applications show the raw API name | Always set a plain-English display name |
| Modifying the production Ontology directly | Breaks live apps immediately, no review | Always use a dev branch; merge via PR |

CAUTION: Changes merged to the production Ontology take effect immediately for all active Workshop applications, reports, and AIP agents built on those objects. Coordinate with the team before any production Ontology change.

---

## CHAPTER 6 — BUILDING WORKSHOP APPLICATIONS

### 6-1. What Workshop Is

Workshop is MSS's drag-and-drop application builder. You arrange widgets on a canvas, connect them to Ontology objects, configure interactions, and publish an application — without writing frontend code.

Workshop is appropriate for:
- Dashboards displaying current operational status
- Search and filter interfaces for data exploration
- Forms for data entry tied to Ontology Actions
- Multi-page applications combining tables, charts, and maps

Workshop is not appropriate for:
- Applications requiring custom code logic in the UI (use Slate — TM-30)
- Data processing (use transforms)
- User authentication management (managed at the platform level)

---

### 6-2. Workshop Anatomy

| Concept | Meaning |
|---|---|
| **Application** | The top-level container — one deployable unit |
| **Module** | One page or screen within the application |
| **Widget** | A UI component (table, chart, form, button, map) |
| **Variable** | A shared value that widgets read and write — enables interactivity |
| **Object Set** | The data source for most widgets — a filtered group of Ontology objects |
| **Event** | An action triggered by user interaction (row click, button press) |

---

**TASK: CREATE A NEW WORKSHOP APPLICATION**

**Conditions:** Object Type(s) are published to the production Ontology; builder has Editor access on the target project folder; application purpose and intended users are defined.

**Standards:** Application is created, named correctly, linked to the correct Ontology, permissions are configured, and at least one module exists before any widgets are added.

**Equipment:** MSS account with Editor access; published Object Types; list of intended users.

**Procedure:**
1. Navigate to Workshop (left nav) → New Application.
2. Enter the application name: plain English, unit-appropriate (example: `EUCOM Personnel Readiness Dashboard`).
3. Write a brief description: who it is for and what it shows.
4. Select the Ontology the application will use (confirm with team lead if unsure).
5. In the Permissions panel:
   - Add team members as Editors
   - Add end users as Viewers
   - Do not add users as Owners unless they are responsible for maintaining the app
6. Create a first module: select New Module, name it (example: `Overview`).
7. Save the application before adding any widgets.

---

**TASK: ADD AND CONFIGURE A TABLE WIDGET**

**Conditions:** Workshop application and module exist; Object Type is published to the Ontology.

**Standards:** Table displays the correct Object Type, shows only relevant columns, is connected to an Object Set, and loads data when previewed in Edit mode.

**Equipment:** Workshop application in Edit mode; published Object Type.

**Procedure:**
1. Open the module in Workshop. Select Edit mode.
2. From the widget panel, drag an **Object Table** widget onto the canvas.
3. In the widget configuration panel (right side):
   a. Under Data Source, select Object Type and choose the relevant Object Type.
   b. Select columns to display — choose only properties relevant to the application's purpose.
   c. Set a default sort column (example: sort by `report_dtg` descending — most recent first).
4. Under Display, set column header labels if the default API name is not user-friendly.
5. Enable row selection if users will click rows to see detail (creates a Selected Object variable).
6. Preview the widget. Confirm data loads and columns are correct.
7. Save the module.

---

**TASK: ADD AND CONFIGURE A CHART WIDGET**

**Conditions:** Workshop module exists; Object Type has numeric or categorical properties suitable for charting.

**Standards:** Chart displays correct data, axes are labeled, chart type matches the data being shown, and the chart refreshes when applied filters change.

**Equipment:** Workshop application in Edit mode; Object Type with numeric properties.

**Procedure:**
1. In the module, drag a **Chart** widget onto the canvas.
2. Select the chart type:
   - **Bar Chart**: comparing values across categories (example: unit count by C-rating)
   - **Line Chart**: showing change over time (example: readiness % trend over 30 days)
   - **Pie/Donut**: showing proportion breakdown (example: FMC vs. PMC vs. NMC distribution)
3. Set the data source: select the Object Type.
4. Configure the axes:
   - X-axis: select the category or date property
   - Y-axis: select the numeric property or set as count
5. Set the aggregation method (sum, average, count).
6. Set axis labels in plain English.
7. Add a chart title.
8. Preview and verify the chart reflects the actual data.

---

**TASK: CREATE A FORM FOR DATA INPUT**

**Conditions:** An Action Type is published on the Ontology (defines what data can be written back); Workshop module exists.

**Standards:** Form fields match the Action Type parameters, validation rules are active, submit button is labeled clearly, and a test submission successfully creates or modifies the target object.

**Equipment:** Published Action Type; Workshop application in Edit mode.

**Procedure:**
1. In the module, drag an **Action Form** widget onto the canvas.
2. In widget configuration, select the Action Type to bind (example: `UpdateUnitStatus`).
3. The form auto-generates fields from the Action Type parameters. Review each field:
   - Confirm field labels are user-friendly
   - Set placeholder text where helpful (example: "Enter unit designation, e.g. 1-4 INF")
   - Mark required fields
4. For dropdown/select fields, confirm allowed values are populated from the Ontology or a static list.
5. Set the submit button label: use an action verb (example: "Submit Status Update", not just "Submit").
6. In Edit mode, test the form with sample data. Verify the object is updated in Object Explorer after submission.
7. Add a confirmation message widget that displays after successful submission.

NOTE: Action Forms require a published Action Type. If the Action Type does not exist yet, stop and create it in Ontology Manager before configuring the form. See Chapter 8, Actions in the Maven Field Manual, for Action Type creation steps.

---

**TASK: ADD FILTERS TO A DASHBOARD**

**Conditions:** Workshop module contains at least one table or chart widget; Object Type has filterable properties.

**Standards:** Filter widget is bound to a variable; the variable is connected to the table/chart data source; selecting a filter value changes the data displayed in dependent widgets within two seconds.

**Equipment:** Workshop module with data widgets; Object Type properties to filter on.

**Procedure:**
1. Create a variable to hold the filter value:
   - Variables panel → New Variable
   - Name it descriptively: `selectedAOR`, `statusFilter`
   - Set the type matching the filter property (String, Date, etc.)
2. Drag a **Dropdown** or **Search Box** widget onto the canvas.
3. Configure the filter widget:
   - Set input type to match the property being filtered
   - Set the variable it writes to: select `selectedAOR` or your named variable
   - For a Dropdown, populate the options from the Object Type property values or a static list
4. In the table or chart widget configuration, set a filter condition on the data source:
   - Property: `aor` equals variable `selectedAOR`
5. Preview the module. Select a filter value. Confirm the table or chart updates.
6. For cross-module filtering, pass variables as module navigation parameters.

---

**TASK: PUBLISH AND SHARE A WORKSHOP APP**

**Conditions:** Application is complete, tested, and reviewed; all widgets load data correctly; end users have been identified.

**Standards:** Application is published from the dev branch to main; end users have Viewer access; URL is shared with the unit through approved channels.

**Equipment:** Workshop application with Owner or Editor access; list of users to share with.

**Procedure:**
1. Before publishing, complete the pre-publish checklist in Appendix C.
2. In Workshop, open the application settings.
3. Select Publish. If developed on a branch, merge the application branch to the production branch first.
4. In Permissions, add all intended users or groups with Viewer access.
5. Copy the application URL from the address bar after publication.
6. Share the URL through approved channels (email, Teams, unit SharePoint) — not through external messaging.
7. Notify users of the application name and purpose.
8. After one week, check usage analytics (if available) to confirm the application is being used.

CAUTION: Publishing an application with incorrect data can mislead end users making operational decisions. Test the application with at least one non-developer user before publishing. Have them confirm the data looks correct against a known-good source.

---

### 6-3. Workshop Widget Selection Guide

| Use Case | Recommended Widget |
|---|---|
| Display multiple objects in a list | Object Table |
| Show all properties of one selected object | Object Detail |
| Show a count or summary metric | Metric Tile |
| Compare values across categories | Bar Chart |
| Show a trend over time | Line Chart |
| Show geographic locations | Map (requires GeoPoint property) |
| Filter by a single value | Dropdown |
| Search by text | Search Box |
| Filter by date range | Date Range Picker |
| Allow data entry / write-back | Action Form |
| Trigger an action with one click | Button |
| Display static instructions or context | Markdown Text |
| Highlight rows based on conditions | Object Table with Conditional Formatting |

---

### 6-4. Workshop Layout Best Practices

- Place filters at the top of the module, data widgets below
- Group related widgets visually using layout panels
- Use Metric Tiles to show key numbers at the top of a dashboard (total units, C1 count, etc.)
- Keep each module focused on one task or question — if a module has more than 8 widgets, split it
- Use Markdown widgets to provide context (module title, data source, as-of date)
- Test on a smaller screen — some users will access MSS on a laptop with limited screen space

---

## CHAPTER 7 — DATA QUALITY AND VALIDATION

### 7-1. Why Data Quality Matters for Builders

Every application and report your unit uses is only as accurate as the data behind it. As a builder, you are responsible for the data you publish. If your transform produces rows with null unit IDs, every Workshop app reading from that Object Type will display incomplete information to analysts making operational decisions.

Data quality checks are automated gate conditions that run after every build. A failing ERROR-level check blocks the pipeline from promoting output to downstream consumers. This protects users from bad data.

---

**TASK: WRITE A BASIC @check ON A TRANSFORM**

**Conditions:** A transform is written and builds successfully; output dataset has known quality requirements (no nulls on required fields, values within expected ranges).

**Standards:** At least one ERROR-level check is defined for each required field; checks run after every build; a failing check blocks downstream consumers; checks are documented with a clear message.

**Equipment:** Code repository; existing transform function.

**Procedure:**
1. Open the Python file containing your transform.
2. Add the check import and define quality rules. Example for a unit readiness staging dataset:

```python
from transforms.api import transform_df, Input, Output, Check
import pyspark.sql.functions as F

@transform_df(
    Output("/USAREUR-AF/EUCOM/unit_readiness/staging"),
    source=Input("/USAREUR-AF/EUCOM/unit_readiness/raw"),
    checks=[
        # Block pipeline if any unit_id is null
        Check(
            lambda df: df.filter(F.col("unit_id").isNull()).count() == 0,
            "unit_id must not be null",
            on_error=Check.FAIL
        ),
        # Block pipeline if readiness_pct is out of valid range
        Check(
            lambda df: df.filter(
                (F.col("readiness_pct") < 0) | (F.col("readiness_pct") > 100)
            ).count() == 0,
            "readiness_pct must be between 0 and 100",
            on_error=Check.FAIL
        ),
        # Warn (do not block) if more than 20% of units are C3/C4
        Check(
            lambda df: df.filter(
                F.col("c_rating_derived").isin("C3", "C4")
            ).count() / df.count() <= 0.20,
            "More than 20% of units are C3/C4 — review for data anomalies",
            on_error=Check.WARN
        ),
    ]
)
def compute(source):
    # ... transform logic ...
    return source.filter(F.col("unit_id").isNotNull())
```

3. Build the transform on the dev branch.
4. Verify that checks appear in the build log output.
5. Test that a failing check blocks the build by temporarily introducing bad data in a test run.
6. Commit the checks alongside the transform code.

NOTE: `Check.FAIL` blocks the pipeline — downstream datasets will not update. `Check.WARN` logs the issue but allows the pipeline to proceed. Use FAIL for conditions that make the data unusable. Use WARN for conditions that need monitoring but do not invalidate the data.

---

**TASK: VALIDATE DATA ON INGESTION**

**Conditions:** A Pipeline Builder flow or transform ingests data from an external source; data quality of the source is unknown or variable.

**Standards:** Ingestion transform or pipeline validates schema, required field presence, and basic range checks before writing to the staging dataset; invalid records are either rejected or flagged in a separate error dataset.

**Equipment:** Ingestion pipeline or transform; knowledge of the expected schema and valid value ranges.

**Procedure:**
1. Before writing any ingestion logic, document the schema contract: list every required field, expected type, and valid range.
2. In the ingestion transform, add validation as the first operation before any other logic:

```python
from transforms.api import transform_df, Input, Output
import pyspark.sql.functions as F

@transform_df(
    Output("/USAREUR-AF/EUCOM/sitrep/staging"),
    source=Input("/USAREUR-AF/EUCOM/sitrep/raw"),
)
def compute(source):
    df = source

    # Separate valid from invalid records
    valid = df.filter(
        F.col("unit_id").isNotNull() &
        F.col("report_dtg").isNotNull() &
        F.col("status").isin("ACTIVE", "INACTIVE", "PENDING")
    )

    # Log how many records were dropped
    # (In production, write rejected records to a separate error dataset)
    return valid
```

3. Consider writing rejected records to a separate error dataset for review by the data steward.
4. Add checks on the output as described in the previous task.

---

**TASK: PROFILE A DATASET BEFORE USE**

**Conditions:** A builder is preparing to use a dataset as input to a new transform or Ontology object, and has not used that dataset before.

**Standards:** Builder has reviewed row counts, null percentages on key fields, unique value counts on ID fields, and date range before writing any transform logic.

**Equipment:** Dataset with Viewer access; Foundry dataset preview and profiling tools.

**Procedure:**
1. Open the dataset in Compass. Select Preview.
2. Review the row count (Schema → Overview → Row Count).
3. For each critical field, note:
   - Null percentage (Profile tab, if available, or write a quick transform to count nulls)
   - Data type (matches what you expect?)
   - Sample values (any unexpected formats, extra spaces, mixed case?)
4. For ID fields (primary key candidates): verify uniqueness. A primary key field must have zero duplicates.
5. For date fields: check the date range. Confirm data is current and not stale.
6. Document your findings in a comment at the top of your transform file before writing any logic.

NOTE: This step prevents most common transform failures. Most errors in transform development are caused by assumptions about the input data that turn out to be wrong. Profile first; assume nothing.

---

### 7-2. Data Quality Dimensions

| Dimension | What It Means | How to Check |
|---|---|---|
| **Completeness** | Required fields are not null | Count nulls on critical columns |
| **Validity** | Values are within allowed ranges or sets | Check against valid value lists; check min/max |
| **Uniqueness** | ID fields have no duplicates | Count distinct vs. total rows on primary key |
| **Timeliness** | Data is current (not stale) | Check max `report_dtg` against current date |
| **Consistency** | Same concept expressed the same way | Normalize case, trim whitespace, standardize codes |

---

## CHAPTER 8 — BUILDER REFERENCE AND STANDARDS

### 8-1. Complete Naming Convention Reference

| Resource Type | Convention | Example |
|---|---|---|
| Dataset — raw | `/Project/AOR/source/raw` | `/USAREUR-AF/EUCOM/sitrep/raw` |
| Dataset — staging | `/Project/AOR/source/staging` | `/USAREUR-AF/EUCOM/sitrep/staging` |
| Dataset — curated | `/Project/AOR/source/curated` | `/USAREUR-AF/EUCOM/sitrep/curated` |
| Code repository | `kebab-case` | `sitrep-pipeline-transforms` |
| Transform function | `snake_case` | `raw_to_staging`, `compute_c_rating` |
| Object Type | `PascalCase` singular | `UnitStatus`, `SoldierReadiness` |
| Property API name | `camelCase` | `reportDate`, `unitId` |
| Link Type | `camelCase` verb phrase | `assignedTo`, `submittedBy` |
| Action Type | `PascalCase` verb + noun | `UpdateUnitStatus`, `CreateLogisticsEntry` |
| Workshop application | Plain English, unit context | `21TSC Readiness Dashboard` |
| Dev branch | `dev-[feature]` | `dev-sitrep-normalization` |

---

### 8-2. Build Quality Checklist

Before requesting a PR review and before merging any build to master, verify every item:

**Transforms:**
- [ ] Transform builds cleanly with zero errors and zero warnings
- [ ] Output dataset has non-zero row count
- [ ] Sample rows spot-checked against source data
- [ ] No hardcoded dataset paths — all paths in `Input()` / `Output()` decorators
- [ ] No credentials, tokens, or connection strings in code
- [ ] At least one ERROR-level `@check` on required fields
- [ ] `_processed_at` metadata column added
- [ ] Docstring describing transform purpose, input, and output
- [ ] Naming convention followed

**Ontology:**
- [ ] Object Type backed by curated dataset only
- [ ] Primary key verified as unique in backing dataset
- [ ] All properties have display names
- [ ] No pipeline metadata columns (`_`) exposed as properties
- [ ] Tested on dev branch before PR to production

**Workshop Applications:**
- [ ] Application tested by at least one non-developer user
- [ ] All widgets load data without errors
- [ ] Permissions set correctly (Viewers cannot edit)
- [ ] Application description written
- [ ] Tested on dev branch before publishing to production

---

### 8-3. Performance Guidelines

| Guideline | Rationale |
|---|---|
| Use `@incremental` transforms for datasets that grow over time | Full recompute on large datasets wastes compute and slows pipelines |
| Use `dropDuplicates()` before writing output | Duplicate rows in curated datasets corrupt Ontology objects |
| Avoid `SELECT *` — specify only needed columns | Reduces data volume through the pipeline |
| Partition large datasets by date or AOR | Enables Spark to skip irrelevant partitions during reads |
| Store DTGs as `TimestampType`, not strings | Enables date-range operations without parsing overhead |
| Break large transforms into stages | Smaller transforms are easier to debug and rebuild independently |

---

### 8-4. Documentation Requirements

Every resource you publish must have a description. This is not optional.

| Resource | Required Documentation |
|---|---|
| Dataset | Source system, data description, update frequency, point of contact |
| Code repository | Purpose, input datasets, output datasets, schedule |
| Transform function | Docstring: what it does, what it reads, what it produces |
| Object Type | What real-world thing it represents; which unit owns the data |
| Workshop application | Who it is for, what questions it answers, data sources |

Undocumented resources will be flagged in team reviews and may be removed if the owner cannot be identified.

---

### 8-5. Authorized vs. Unauthorized Builder Actions

| Action | Authorized | Notes |
|---|---|---|
| Create datasets in approved project folder | Yes | Follow naming conventions |
| Create Object Types on dev Ontology branch | Yes | Never directly on production |
| Write transforms reading from curated datasets | Yes | Never from raw datasets |
| Merge to master via PR with reviewer approval | Yes | Reviewer must not be the same person as author |
| Direct commit to master | No | Always use PR process |
| Modify production Ontology directly | No | Always use dev branch and PR |
| Create connections to unapproved external systems | No | Requires admin and security approval |
| Store credentials in code | No | Security violation |
| Access datasets without requested permissions | No | Unauthorized access is logged |
| Share MSS URLs with personnel outside the unit | No | Verify recipient has MSS access and appropriate clearance |

WARNING: Sharing direct links to MSS applications or datasets with personnel who do not have appropriate MSS access or data markings clearance is a security violation. Confirm recipient access level before sharing any MSS resource links.

---

### 8-6. Version Control and Commit Message Standards

Every commit to a code repository must have a meaningful message. Commit messages are the audit trail for all code changes on MSS.

**Commit message format:**

```
[Action]: [Brief description of what changed and why]

Examples:
Add: raw_to_staging transform for SITREP feed
Fix: null unit_id now filtered before output write
Update: add C-rating derivation logic to readiness transform
Remove: deprecated equipment_log ingestion pipeline
```

Do not commit:
- Large binary files (use Foundry dataset storage instead)
- Credentials or passwords (security violation)
- Operational data payloads (data lives in datasets, not repos)
- Commented-out blocks of old code (use version history)

---

### 8-7. Handoff Requirements

When transferring a build to another team member — rotation, reassignment, or extended absence — provide the following before departure:

1. **Resource inventory**: list all datasets, repositories, Object Types, and applications you own with their Compass paths and RIDs
2. **Architecture diagram or description**: how data flows from source to application
3. **Known issues**: any unresolved bugs, data quality problems, or pending work
4. **Schedule**: what runs, when, and how to verify it ran successfully
5. **Contacts**: data steward for each source dataset; point of contact for each connected external system
6. **Access transfer**: transfer Owner role on all resources to the incoming builder

Failure to provide a proper handoff leaves the incoming builder responsible for a system they do not understand. Schedule the handoff brief at least one week before departure.

---

## APPENDIX A — PYTHON QUICK REFERENCE

This is a quick reference for builders who have completed the Chapter 4 tasks. It is not a Python tutorial. For the annotated code examples referenced below, see `/home/dale/Desktop/claude/data_skills/13_foundry_patterns/`.

### Standard Transform Template

```python
from transforms.api import transform_df, Input, Output
import pyspark.sql.functions as F
from pyspark.sql.types import TimestampType, StringType, IntegerType

@transform_df(
    Output("/Project/AOR/source/staging"),
    source=Input("/Project/AOR/source/raw"),
)
def compute(source):
    """
    Transform: raw_to_staging
    Input:  /Project/AOR/source/raw
    Output: /Project/AOR/source/staging
    Purpose: Clean, validate, and standardize raw [SOURCE] data.
    """
    df = source

    # 1. Drop duplicates on primary key
    df = df.dropDuplicates(["primary_key_column"])

    # 2. Filter required fields
    df = df.filter(
        F.col("required_field").isNotNull()
    )

    # 3. Standardize text fields
    df = df.withColumn("unit_id", F.upper(F.trim(F.col("unit_id"))))

    # 4. Parse timestamps (DTG handling)
    df = df.withColumn("dtg", F.col("dtg_raw").cast(TimestampType()))

    # 5. Add pipeline metadata
    df = df.withColumn("_processed_at", F.current_timestamp())

    return df
```

### Multi-Input Transform Template

```python
from transforms.api import transform, Input, Output
import pyspark.sql.functions as F

@transform(
    output=Output("/Project/AOR/source/curated"),
    unit_data=Input("/Project/AOR/unit_readiness/staging"),
    personnel_data=Input("/Project/AOR/personnel/staging"),
)
def compute(output, unit_data, personnel_data):
    """Join unit readiness with personnel strength."""
    units = unit_data.dataframe()
    personnel = personnel_data.dataframe()

    merged = units.join(
        personnel.select("unit_id", "assigned_strength", "present_for_duty"),
        on="unit_id",
        how="left"
    )

    output.write_dataframe(merged)
```

### C-Rating Derivation (USAREUR-AF Standard)

```python
from pyspark.sql import functions as F
from pyspark.sql.types import StringType

def derive_c_rating(df, readiness_col="readiness_pct"):
    """Derive C-rating from readiness percentage per USAREUR-AF standards."""
    return df.withColumn(
        "c_rating_derived",
        F.when(F.col(readiness_col) >= 85, "C1")
         .when(F.col(readiness_col) >= 65, "C2")
         .when(F.col(readiness_col) >= 35, "C3")
         .otherwise("C4")
    )
```

### Incremental Transform Pattern

```python
from transforms.api import transform, Input, Output
import pyspark.sql.functions as F

@transform(
    output=Output("/Project/AOR/sitrep/processed"),
    source=Input("/Project/AOR/sitrep/raw"),
)
def compute(source, output):
    """
    Incremental SITREP processing.
    Foundry delivers only new rows since the last successful run.
    """
    # ctx.is_incremental is True when Foundry runs this incrementally
    new_df = source.dataframe(incremental=True)

    if new_df.rdd.isEmpty():
        return  # No new data — nothing to write

    processed = new_df.withColumn(
        "processed_at", F.current_timestamp()
    )

    output.write_dataframe(processed, output_mode="append")
```

### Common PySpark Patterns

```python
# Deduplicate — keep latest record per unit
from pyspark.sql.window import Window

window = Window.partitionBy("unit_id").orderBy(F.desc("report_dtg"))
df = df.withColumn("_rank", F.row_number().over(window))
df = df.filter(F.col("_rank") == 1).drop("_rank")

# Parse DTG string format: "151430Z MAR 26"
df = df.withColumn(
    "dtg_ts",
    F.to_timestamp(F.col("dtg_string"), "ddHHmm'Z' MMM yy")
)

# Handle nulls
df = df.fillna({"status": "UNKNOWN", "readiness_pct": 0})
df = df.dropna(subset=["unit_id", "report_dtg"])

# Conditional column value
df = df.withColumn(
    "mc_status",
    F.when(F.col("mission_capable") == True, "FMC")
     .when(F.col("partially_capable") == True, "PMC")
     .otherwise("NMC")
)
```

---

## APPENDIX B — WORKSHOP WIDGET REFERENCE

| Widget | Purpose | When to Use | Key Configuration |
|---|---|---|---|
| **Object Table** | Display multiple objects in rows | Primary data display; search results | Object Type, columns, sort order, row selection |
| **Object Detail** | Show all properties of one object | Detail panel after row selection | Object Set or variable binding |
| **Bar Chart** | Compare values across categories | C-rating distribution; unit counts by AOR | X-axis (category), Y-axis (value), aggregation |
| **Line Chart** | Show trend over time | Readiness trend; report submission rate | X-axis (date), Y-axis (metric), grouping |
| **Pie/Donut Chart** | Show proportional breakdown | FMC/PMC/NMC distribution | Category property, value property |
| **Map** | Display geographic locations | Unit positions; AOR coverage | GeoPoint property required |
| **Metric Tile** | Display a single key number | Total units; C1 count; % compliant | Aggregation function, label, color threshold |
| **Dropdown** | Single-value filter input | AOR filter; status filter | Options source, variable to write |
| **Search Box** | Text-based search/filter | Search by unit name or ID | Property to search on; output variable |
| **Date Range Picker** | Filter by date range | Report date range; DTG filter | Date property; start/end variables |
| **Action Form** | Multi-field data entry | Status update; SITREP submission | Action Type binding; field labels |
| **Button** | Trigger single action | One-click status change | Action Type; confirmation prompt |
| **Markdown Text** | Static text and formatting | Module title; instructions; as-of date | Markdown content; variable interpolation |
| **Conditional Formatting** | Color rows by value | Highlight C3/C4 units; flag late reports | Applied to Object Table; rule conditions |
| **Filter Panel** | Multi-property filter bar | Complex dashboards with many filter options | Properties to filter; variable bindings |

---

## APPENDIX C — BUILDER CHECKLIST

Use this checklist before publishing any build to production. All items must be checked before merging to master or publishing to the production Ontology.

### Transform Checklist

- [ ] Transform builds without errors on dev branch
- [ ] Output dataset row count is non-zero and plausible
- [ ] At least 10 rows spot-checked against source data
- [ ] All input paths use `Input()` decorator — no hardcoded strings
- [ ] All output paths use `Output()` decorator — no hardcoded strings
- [ ] No credentials or tokens in any Python file
- [ ] At least one `Check.FAIL` level check on required fields
- [ ] Transform has a docstring with purpose, input, and output
- [ ] Naming conventions followed for function and file names
- [ ] Commit message is descriptive

### Ontology Checklist

- [ ] Object Type backed by curated tier dataset
- [ ] Primary key field is unique in the backing dataset
- [ ] All properties have plain-English display names
- [ ] No `_` prefixed pipeline metadata columns exposed as properties
- [ ] Object count in dev Ontology matches expected dataset row count
- [ ] PR reviewed and approved by team lead before merge to production
- [ ] Downstream application owners notified of schema changes

### Workshop Application Checklist

- [ ] Application tested by at least one non-developer user
- [ ] All widgets load data without errors
- [ ] Filters function correctly — selections change displayed data
- [ ] Forms tested end-to-end: submission creates/modifies correct object
- [ ] Permissions reviewed: users have Viewer (not Editor) access
- [ ] Application description is written
- [ ] Application tested on a dev branch before publishing to production
- [ ] URL shared only with users who have appropriate MSS access

---

## GLOSSARY

Key terms for builders. For full definitions including user-level terms, see GLOSSARY_data_foundry.md.

| Term | Builder Definition |
|---|---|
| **@check** | Decorator that attaches data quality assertions to a transform; failing ERROR checks block the pipeline |
| **@incremental** | Transform decorator that processes only new rows since the last successful run |
| **@lightweight_transform** | Transform that runs in a Python container (pandas) rather than on Spark; use for small data only |
| **@transform** | Lower-level transform decorator; provides direct access to TransformInput and TransformOutput objects |
| **@transform_df** | Standard transform decorator; function receives and returns Spark DataFrames directly |
| **Action Type** | Template in Ontology Manager that defines a write-back operation (create, modify, delete an object) |
| **Backing Dataset** | The curated dataset an Object Type reads from to populate its objects |
| **Branch** | A versioned copy of a dataset, code repository, or Ontology — use for development; merge to master when ready |
| **Build** | Foundry running a transform and writing the output dataset |
| **Check** | An automated data quality assertion that runs after a transform build |
| **Compass** | Foundry's file and resource explorer — the primary navigation interface |
| **Computed Property** | An Object Type property whose value is calculated by code, not stored in the backing dataset |
| **Curated Dataset** | The final, clean, ontology-ready dataset in the data pipeline; the only tier that backs Object Types |
| **Data Lineage** | Foundry's graph showing how datasets and transforms connect — available on any dataset |
| **Input()** | Decorator parameter declaring a transform's input dataset by path |
| **Link Type** | A defined relationship between two Object Types in the Ontology |
| **Marking** | A data-level access control label applied to Object Types; limits visibility to users with the matching clearance |
| **Module** | One page or screen within a Workshop application |
| **Object Set** | A filtered group of Ontology objects used as a data source for Workshop widgets |
| **Object Type** | The blueprint for a real-world thing in the Ontology (e.g., UnitStatus, SoldierReadiness) |
| **Ontology** | MSS's semantic layer that translates dataset rows into meaningful objects with properties and relationships |
| **Ontology Manager** | The UI for creating and configuring Object Types, Link Types, and Action Types |
| **Output()** | Decorator parameter declaring a transform's output dataset by path |
| **Pipeline Builder** | Visual (no-code) ETL tool for ingestion and simple data transformation |
| **Primary Key** | The column that uniquely identifies each row in a backing dataset and each object in an Object Type |
| **RID** | Resource Identifier — the permanent unique ID of any Foundry resource; format: `ri.foundry.main.dataset.[UUID]` |
| **Raw Dataset** | Data exactly as received from the source system; never modified; never read by applications |
| **Staging Dataset** | Cleaned and validated data; intermediate layer between raw and curated |
| **Transaction** | A versioned write to a Foundry dataset; SNAPSHOT replaces all data, APPEND adds rows |
| **Variable** | A shared value in Workshop that enables widgets to communicate (example: selected row drives detail panel) |
| **Workshop** | MSS's drag-and-drop application builder; no frontend code required for standard applications |

---

*TM-20, Maven Smart System — Builder Technical Manual*
*Headquarters, United States Army Europe and Africa, Wiesbaden, Germany*
*UNCLASSIFIED — Approved for public release; distribution is unlimited.*
*Prerequisite: TM-10, Maven User*
