```
TM-30 — MAVEN SMART SYSTEM (MSS)
ADVANCED BUILDER TECHNICAL MANUAL

HEADQUARTERS
UNITED STATES ARMY EUROPE AND AFRICA
Wiesbaden, Germany

2026

PREREQUISITE PUBLICATIONS: TM-10, Maven User; TM-20, Builder; ADRP 1, Data Literacy
DISTRIBUTION RESTRICTION: Approved for public release; distribution is unlimited.

---
SAFETY SUMMARY

Advanced builders have broad privileges on MSS production infrastructure. Actions
at this level can affect the entire formation's data environment.

Before operating at TM-30 level:
- Understand the full downstream impact of ontology changes, schema modifications,
  and incremental pipeline alterations
- Coordinate with data stewards before modifying shared production resources
- Never test in production — use Foundry branching for all development work
- AIP integrations require additional authorization review before deployment
```

---

## TABLE OF CONTENTS

- Chapter 1 — Introduction and Scope
- Chapter 2 — Advanced Python Transforms
- Chapter 3 — Incremental Transforms and Pipeline Patterns
- Chapter 4 — Advanced Ontology and Object Modeling
- Chapter 5 — Functions on Objects (FOO)
- Chapter 6 — Actions and Write-Back Patterns
- Chapter 7 — AIP Integration
- Chapter 8 — OSDK (Ontology SDK)
- Chapter 9 — Analytics: Quiver and Contour (Advanced)
- Chapter 10 — Data Lineage and CI/CD
- Appendix A — Advanced PySpark Reference
- Appendix B — Ontology Design Patterns
- Appendix C — AIP Authorization Checklist
- Appendix D — TM-30 Change Management Checklist
- Glossary

---

# CHAPTER 1 — INTRODUCTION AND SCOPE

## 1-1. TM-30 Scope vs. TM-20

TM-20 (Builder) qualified you to create datasets, write basic transforms, configure Object Types with standard properties, build Workshop applications, and configure Actions. That level covers the majority of day-to-day MSS development work.

TM-30 advances beyond builder fundamentals into production-grade capability. At this level you are responsible for:

- Authoring optimized PySpark transforms that execute efficiently at scale
- Designing and implementing incremental pipeline architectures
- Modeling complex ontology structures including Interfaces and derived properties
- Writing Functions on Objects (TypeScript) that compute against the Ontology at query time
- Building and deploying AIP Logic workflows and Agents
- Developing external applications via the Ontology SDK (OSDK)
- Managing production infrastructure through Foundry branching and CI/CD gates

Do not use this manual to re-learn baseline tasks. Reference TM-20 for Object Type creation, basic transforms, Workshop widget configuration, and basic Action setup. TM-30 assumes fluency in all TM-20 material.

## 1-2. Advanced Builder Responsibilities and Elevated Risk Profile

The advanced builder operates at the intersection of data engineering, software development, and operational architecture. Unlike a standard builder whose mistakes are typically scoped to one application or dataset, an advanced builder's actions touch shared infrastructure.

**What you own at TM-30 level:**

| Area | Your Responsibility |
|------|---------------------|
| Production pipelines | Correctness, performance, incremental behavior |
| Ontology structure | Interfaces, derived properties, link type design |
| Functions on Objects | TypeScript logic correctness and performance impact |
| AIP integrations | Authorization compliance, human review gates |
| OSDK applications | Auth model, token management, security review |
| CI/CD gates | Check definitions, test coverage, merge standards |

Every one of these areas, if misconfigured, can degrade the data environment for the entire formation — from battalion S2 analysts to G9 reporting. Own that risk.

## 1-3. Production vs. Development Discipline at TM-30 Level

> **CAUTION: Never develop directly on the production ontology or master branch. All development requires a feature branch. All merges to master require peer review and passing CI checks.**

The discipline standard at TM-30 is stricter than TM-20 because the blast radius is larger. Specific requirements:

1. All code changes start on a named feature branch (`feature/description-here`).
2. All branches must build cleanly before requesting review.
3. All transforms touching shared curated datasets require a second reviewer.
4. Ontology changes (new Object Types, Interface modifications, property additions/removals) require data steward coordination before merge.
5. AIP and OSDK deployments require command authorization review (see Appendix C).
6. No hotfixes to production without documented coordination. Use the emergency branch process if a production break requires immediate remediation.

## 1-4. Overview of TM-30 Capability Areas

| Capability Area | Chapter | Description |
|-----------------|---------|-------------|
| Advanced Python Transforms | 2 | Partitioning, schema enforcement, multi-input joins, lightweight pattern |
| Incremental Pipelines | 3 | @incremental decorator, watermark pattern, late-data handling |
| Advanced Ontology | 4 | Interfaces, derived properties, complex link types, Object Storage V2 |
| Functions on Objects (FOO) | 5 | TypeScript functions, computed properties, Workshop binding |
| Actions / Write-Back | 6 | Complex validation, batch actions, development testing workflow |
| AIP Integration | 7 | Logic, Agents, Code Workspaces, output integration |
| OSDK | 8 | External app development, object queries, Action invocation |
| Analytics (Advanced) | 9 | Quiver pivots, Contour multi-dataset joins, scheduled reports |
| Lineage and CI/CD | 10 | Lineage graph reading, branching workflow, automated checks |

## 1-5. Authorization Requirements for TM-30 Activities

Before performing TM-30 activities, confirm you hold the following:

- **Foundry role:** Editor on the production ontology branch and relevant code repositories
- **Team lead endorsement:** Written or tracked approval that you are operating at TM-30 level
- **AIP authorization:** Separate command approval required before any AIP Logic or Agent deployment to production (see Appendix C)
- **OSDK deployment authorization:** Security review required before deploying any OSDK-backed external application
- **Data steward coordination:** Required before modifying any shared Object Type, Interface, or curated dataset schema

If you do not hold these authorizations, build and test on your development branch. Do not promote to production.

## 1-6. Code Review and Change Management Requirements

All TM-30 production changes require:

1. Pull request (PR) opened against the `dev` integration branch
2. Passing CI build with no check failures
3. At least one peer review approval from another qualified builder
4. For ontology changes: data steward sign-off in PR comments
5. PR merged to `dev`, integration testing completed
6. Separate PR opened against `master`
7. Lead data engineer or team lead approval before merge to `master`

See Appendix D for the full TM-30 Change Management Checklist.

---

# CHAPTER 2 — ADVANCED PYTHON TRANSFORMS

## 2-1. Transform Optimization Principles

Foundry runs transforms on Apache Spark — a distributed compute engine. Spark's power comes from parallelism, but poorly written transforms waste that parallelism and consume excessive cluster resources, delaying the entire formation's data pipeline.

Three principles govern optimized transform authorship:

**a. Column Pruning.** Select only the columns you need before any join or aggregation. Every extra column carried through a shuffle adds memory and I/O cost.

**b. Predicate Pushdown.** Filter early. Apply `.filter()` before `.join()`, before `.groupBy()`, before any expensive operation. Spark can push predicates down to the source in many cases, avoiding full dataset reads.

**c. Partition Alignment.** When joining two large datasets, partition them on the join key first with `.repartition()`. Avoids expensive full shuffles at join time.

> **CAUTION: Calling `.count()`, `.collect()`, or `.toPandas()` on a large Spark DataFrame inside a production transform triggers a full materialization. Avoid these except in lightweight transforms or during development/debugging. Never leave `.show()` or `.collect()` calls in production code.**

---

### TASK 2-A: WRITE AN OPTIMIZED PYSPARK TRANSFORM

**CONDITIONS:** You have a large, growing unit readiness dataset with tens of millions of rows. A downstream analyst application requires a quarterly aggregated summary per unit. The full-scan version of this transform is taking over 20 minutes to build.

**STANDARDS:** Transform builds in under 5 minutes. Output schema is enforced. Only required columns are read. Filters are applied before aggregation.

**EQUIPMENT:** Foundry Code Repository (Transforms type), Editor role on input/output datasets.

**PROCEDURE:**

1. Open your Code Repository. Navigate to the appropriate transform file.
2. Import required modules:

```python
from transforms.api import transform, Input, Output
from pyspark.sql import functions as F
from pyspark.sql.types import (
    StructType, StructField, StringType, IntegerType, DoubleType, TimestampType
)
```

3. Define the output schema explicitly (step 4 will reference this):

```python
OUTPUT_SCHEMA = StructType([
    StructField("unit_id",         StringType(),    nullable=False),
    StructField("fy_quarter",      IntegerType(),   nullable=False),
    StructField("avg_personnel",   DoubleType(),    nullable=True),
    StructField("min_readiness",   DoubleType(),    nullable=True),
])
```

4. Write the transform with early filtering and column pruning:

```python
@transform(
    output=Output("/USAREUR-AF/operational/processed/unit_readiness_quarterly"),
    source=Input("/USAREUR-AF/operational/curated/unit_readiness"),
)
def compute_readiness_quarterly(ctx, source, output):
    df = source.dataframe()

    # Predicate pushdown: filter before any expensive operation
    df = df.filter(F.col("status").isin(["ACTIVE", "DEPLOYED"]))

    # Column pruning: select only what downstream needs
    df = df.select(
        "unit_id",
        "personnel_count",
        "readiness_level",
        "report_date",
    )

    # Derive partition column before groupBy
    df = df.withColumn("fy_quarter", F.quarter(F.col("report_date")))

    # Aggregation
    result = (
        df.groupBy("unit_id", "fy_quarter")
          .agg(
              F.avg("personnel_count").alias("avg_personnel"),
              F.min("readiness_level").alias("min_readiness"),
          )
    )

    # Enforce output schema — catches type drift before it breaks downstream
    result = ctx.spark_session.createDataFrame(result.rdd, OUTPUT_SCHEMA)

    output.write_dataframe(result)
```

5. Build on your feature branch. Verify output row count and schema match expectations.
6. Check build logs for shuffle read/write sizes. If shuffle reads exceed input size significantly, review join strategy.

---

### TASK 2-B: ENFORCE SCHEMA IN A TRANSFORM

**CONDITIONS:** A source feed intermittently delivers columns with wrong types (e.g., `personnel_count` arrives as string instead of integer). Downstream ontology-backed applications break when the schema drifts.

**STANDARDS:** Transform enforces output schema on every build. Type mismatches are caught at the transform layer, not downstream.

**PROCEDURE:**

1. Define `StructType` for the output:

```python
from pyspark.sql.types import (
    StructType, StructField, StringType, IntegerType, DoubleType, TimestampType
)

STAGING_SCHEMA = StructType([
    StructField("unit_id",          StringType(),    nullable=False),
    StructField("readiness_pct",    DoubleType(),    nullable=True),
    StructField("c_rating",         StringType(),    nullable=True),
    StructField("report_dtg",       TimestampType(), nullable=False),
    StructField("personnel_count",  IntegerType(),   nullable=True),
    StructField("_processed_at",    TimestampType(), nullable=False),
])
```

2. Cast columns explicitly in the transform body rather than relying on Spark inference:

```python
df = (df
    .withColumn("unit_id",         F.upper(F.trim(F.col("unit_id"))).cast(StringType()))
    .withColumn("readiness_pct",   F.col("readiness_pct").cast(DoubleType()))
    .withColumn("personnel_count", F.col("personnel_count").cast(IntegerType()))
    .withColumn("report_dtg",      F.to_timestamp(F.col("report_dtg_raw"), "ddHHmm'Z' MMM yy"))
    .withColumn("_processed_at",   F.current_timestamp())
)
```

3. Apply schema at write time:

```python
result = ctx.spark_session.createDataFrame(df.rdd, STAGING_SCHEMA)
output.write_dataframe(result)
```

4. If a cast fails (returns null for non-nullable field), Spark raises an exception at the `createDataFrame` step — the build fails cleanly rather than writing corrupt data.

> **CAUTION: Removing a column from STAGING_SCHEMA after objects are mapped to it in the Ontology will break the backing dataset and cause Object Type property resolution failures. Coordinate with data stewards before removing columns.**

---

### TASK 2-C: WRITE A MULTI-INPUT TRANSFORM

**CONDITIONS:** You need to join unit readiness data with personnel strength data to produce a combined curated dataset. Both inputs are maintained by different upstream teams.

**STANDARDS:** Join executes without full shuffle. Null handling on the left join is documented. Output is idempotent.

**PROCEDURE:**

```python
from transforms.api import transform, Input, Output
from pyspark.sql import functions as F

@transform(
    output=Output("/USAREUR-AF/operational/curated/unit_combined"),
    unit_data=Input("/USAREUR-AF/operational/processed/unit_readiness_clean"),
    personnel_data=Input("/USAREUR-AF/operational/processed/personnel_strength"),
)
def compute_unit_combined(ctx, unit_data, personnel_data, output):
    units = unit_data.dataframe()
    personnel = personnel_data.dataframe()

    # Column pruning on personnel before join
    personnel_slim = personnel.select(
        "unit_id",
        "assigned_strength",
        "present_for_duty",
        "mos_fill_pct",
    )

    # Left join: keep all units even if no personnel record exists
    # Repartition on join key to avoid full shuffle on large dataset
    joined = (
        units.repartition(200, "unit_id")
             .join(
                 personnel_slim.repartition(200, "unit_id"),
                 on="unit_id",
                 how="left",
             )
    )

    # Null-fill personnel columns for units with no personnel record
    joined = joined.fillna({
        "assigned_strength": 0,
        "present_for_duty":  0,
        "mos_fill_pct":      0.0,
    })

    # Deduplicate on primary key — idempotency guarantee
    result = joined.dropDuplicates(["unit_id", "report_dtg"])

    output.write_dataframe(result)
```

---

### TASK 2-D: USE @lightweight_transform FOR SMALL DATASETS

**CONDITIONS:** You need to process a lookup table or reference dataset (unit hierarchy, AOR boundaries, MOS codes) that is under 500,000 rows. The logic requires complex Python operations not easily expressed in PySpark.

**STANDARDS:** Transform runs in lightweight (non-Spark) container. Logic is correct. Pandas operations are used appropriately.

**WHEN TO USE:**
- Dataset is under 1 million rows
- Logic requires complex Python (custom parsers, ML inference, external lookups)
- Spark startup overhead is larger than actual compute time

**WHEN NOT TO USE:**
- Dataset grows over time (use `@transform` with Spark)
- Join with large datasets (Spark required)
- Memory requirements exceed lightweight container limits (~4 GB)

```python
from transforms.api import lightweight_transform, Input, Output
import pandas as pd

@lightweight_transform(
    output=Output("/USAREUR-AF/reference/mos_classification"),
    raw=Input("/USAREUR-AF/reference/mos_codes_raw"),
)
def compute_mos_classification(output, raw):
    df = raw.dataframe()  # Returns pandas DataFrame in lightweight context

    # Complex Python logic — not feasible in PySpark without UDFs
    df["branch"] = df["mos_code"].str[:2].map({
        "11": "Infantry",
        "13": "Field Artillery",
        "17": "Cyber",
        "25": "Signal",
        "35": "Military Intelligence",
        "88": "Transportation",
        "91": "Ordnance",
    }).fillna("Other")

    df["is_critical_mos"] = df["vacancy_rate"] > 0.20

    df["_processed_at"] = pd.Timestamp.utcnow()

    output.write_dataframe(df)
```

> **CAUTION: Do not use `@lightweight_transform` for datasets that are growing or will grow beyond 1 million rows. Lightweight containers have a fixed memory ceiling. A transform that works today on 200K rows will fail silently or OOM when the dataset grows to 2 million rows. Use `@transform` (Spark) for any dataset with ongoing operational growth.**

---

## 2-2. PySpark Advanced Operations Reference

| Operation | Pattern | Use Case |
|-----------|---------|----------|
| Window rank | `F.row_number().over(Window.partitionBy("unit_id").orderBy(F.desc("report_dtg")))` | Latest record per unit |
| Lag/lead | `F.lag("readiness_pct", 1).over(w)` | Period-over-period comparison |
| Running total | `F.sum("count").over(Window.partitionBy("aor").orderBy("report_dtg").rowsBetween(Window.unboundedPreceding, 0))` | Cumulative ops metrics |
| Explode array | `F.explode(F.col("equipment_list"))` | Flatten nested arrays |
| Struct extract | `F.col("location.grid_ref")` | Access nested struct fields |
| Pivot | `.groupBy("unit_id").pivot("c_rating").agg(F.count("*"))` | Cross-tab readiness by C-rating |
| Broadcast join | `df1.join(F.broadcast(small_df), "unit_id")` | Join large + small dataset |

## 2-3. Transform Performance Troubleshooting

| Symptom | Likely Cause | Resolution |
|---------|-------------|------------|
| Build takes >30 min | Full scan, no predicate pushdown | Add `.filter()` before join/agg |
| OOM error on Spark executor | Skewed join key or too-large partitions | Repartition on join key; use `salting` for skewed keys |
| Output schema changes break downstream | No schema enforcement | Define `StructType`, enforce at write |
| Incremental transform runs full scan | `require_incremental=True` missing | See Chapter 3 |
| Duplicate rows in output | Missing `dropDuplicates()` | Add dedup on primary key |
| Build succeeds but output is empty | Filter removes all rows | Check filter logic; add `.count()` test pre-filter |
| Lightweight OOM | Dataset exceeds container memory | Switch to Spark `@transform` |

---

# CHAPTER 3 — INCREMENTAL TRANSFORMS AND PIPELINE PATTERNS

## 3-1. Why Incremental Matters

Operational data in MSS grows continuously. SITREP feeds append new records every reporting cycle. Equipment maintenance logs grow daily. Personnel transactions accumulate over months. Full recompute on every pipeline trigger is neither efficient nor sustainable.

A transform that takes 45 seconds on one month of data takes 45 minutes on 60 months of data — with identical resource cost per run. Incremental transforms solve this by processing only data added since the last successful run. For high-frequency operational feeds, incremental is the only acceptable architecture at production scale.

## 3-2. The Watermark Pattern

A watermark is a stored marker indicating the last successfully processed state. On each run, the transform reads only data newer than the watermark, processes it, then advances the watermark.

Foundry manages the watermark automatically for transforms decorated with `@incremental` — it tracks transaction IDs on the source dataset. For pipelines external to Foundry (feeding data in via API), use an explicit watermark store. See `data_skills/13_foundry_patterns/incremental_transforms.py` for the `WatermarkPipeline` implementation pattern.

---

### TASK 3-A: WRITE AN INCREMENTAL TRANSFORM WITH @incremental

**CONDITIONS:** A SITREP feed dataset receives hundreds of new records per reporting cycle. The staging transform currently full-scans the input on every build. Build time exceeds the reporting cycle interval.

**STANDARDS:** Transform processes only new rows since last successful build. First run performs full snapshot. Output is append-only. Build completes within the reporting cycle interval.

**EQUIPMENT:** Foundry Code Repository, input dataset with Foundry transaction support.

> **CAUTION: `require_incremental=True` causes the transform to fail if the input dataset does not support incremental mode. Use this setting for production transforms to prevent silent fallback to full-scan. Omit it only on datasets where full-scan fallback is acceptable (e.g., small reference tables).**

**PROCEDURE:**

```python
from transforms.api import transform, Input, Output, incremental
from pyspark.sql import functions as F

@incremental(require_incremental=True)
@transform(
    output=Output("/USAREUR-AF/operational/processed/sitrep_normalized"),
    source=Input("/USAREUR-AF/operational/raw/sitrep_feed"),
)
def compute_sitrep_incremental(ctx, source, output):
    # Retrieve only rows added since last successful run.
    # On first run (no prior successful build), returns the full dataset.
    new_data = source.dataframe(ctx, "added")

    # Guard: no new data — nothing to do
    if new_data.rdd.isEmpty():
        return

    # Normalize and enrich
    processed = (
        new_data
        .withColumn("unit_id",       F.upper(F.trim(F.col("unit_id"))))
        .withColumn("processed_at",  F.current_timestamp())
        .withColumn("c_rating",
            F.when(F.col("readiness_pct") >= 85, "C1")
             .when(F.col("readiness_pct") >= 65, "C2")
             .when(F.col("readiness_pct") >= 35, "C3")
             .otherwise("C4")
        )
        .withColumn("is_late",
            (F.unix_timestamp(F.col("processed_at")) -
             F.unix_timestamp(F.col("report_dtg"))) / 3600 > 6
        )
    )

    # Append-only write — do not use output.write_dataframe() in incremental context
    output.set_mode("modify")
    output.write_dataframe(processed)
```

---

### TASK 3-B: IMPLEMENT A WATERMARK-BASED PIPELINE

**CONDITIONS:** You are building a pipeline that ingests data from an external system into Foundry via the Datasets API. The external system does not support transaction-level change tracking. You must track processed state yourself.

**STANDARDS:** Pipeline processes only records newer than last successful run. Watermark advances only after successful write. Pipeline is idempotent — running twice on the same data produces no duplicates.

**PROCEDURE:**

The `WatermarkPipeline` class in `data_skills/13_foundry_patterns/incremental_transforms.py` implements this pattern. For production use, the database path becomes a managed state store (SQLite for small-scale, or a Foundry dataset for production):

```python
from watermark_pipeline import WatermarkPipeline  # your local module
import pandas as pd
import os

PIPELINE_ID = "sitrep-external-feed"
STATE_DB = os.environ["PIPELINE_STATE_DB"]  # never hardcode

pipeline = WatermarkPipeline(db_path=STATE_DB)

def run_incremental_load(source_df: pd.DataFrame) -> None:
    """
    Load only new records from source_df into Foundry.
    Watermark tracks the maximum report_dtg seen in previous runs.
    """
    processed = pipeline.run(
        pipeline_id=PIPELINE_ID,
        source_df=source_df,
        timestamp_col="report_dtg",
    )

    if processed.empty:
        return  # No new data this cycle

    # Deduplicate on report_id before writing to Foundry
    processed = processed.drop_duplicates(subset=["report_id"])

    # Write to Foundry via Datasets API
    # (implementation uses foundry_client.datasets.upload_dataframe)
    write_to_foundry(processed)
    # Watermark already advanced inside pipeline.run() on success
```

---

### TASK 3-C: HANDLE LATE-ARRIVING DATA

**CONDITIONS:** Operational reports sometimes arrive hours or days after the event they describe. Your incremental pipeline has already processed the time window when the late data should have been included. The curated dataset now has gaps.

**STANDARDS:** Late-arriving data is detected and flagged. Reprocessing logic is documented. Pipeline does not silently discard late records.

**PROCEDURE:**

1. Store two timestamps on every record: `report_dtg` (when the event occurred) and `received_at` (when Foundry ingested it).

2. In your incremental transform, compute the lag:

```python
processed = processed.withColumn(
    "arrival_lag_hours",
    (F.unix_timestamp("received_at") - F.unix_timestamp("report_dtg")) / 3600
)
processed = processed.withColumn(
    "is_late_arrival",
    F.col("arrival_lag_hours") > 6.0  # 6-hour SLA for USAREUR-AF SITREP cycle
)
```

3. Route late arrivals to a separate output dataset for review:

```python
on_time  = processed.filter(~F.col("is_late_arrival"))
late     = processed.filter(F.col("is_late_arrival"))

output.set_mode("modify")
output.write_dataframe(on_time)

late_output.set_mode("modify")
late_output.write_dataframe(late)
```

4. For reprocessing, do not modify the watermark manually. Instead, trigger a full snapshot rebuild on the affected time window by temporarily setting `require_incremental=False`, running once, then restoring.

> **CAUTION: Do not advance the watermark past records you have not yet processed. A watermark that has moved ahead of actual data creates permanent gaps in your pipeline output. These gaps will not be caught until a downstream analyst notices missing data in a report.**

---

## 3-3. Incremental vs. Full-Recompute Decision Matrix

| Factor | Use Incremental | Use Full-Recompute |
|--------|-----------------|-------------------|
| Dataset row count | > 1 million and growing | < 1 million or static |
| Build time (full scan) | > 10 minutes | < 2 minutes |
| Data arrives in append-only fashion | Yes | No |
| Source supports transaction tracking | Yes | No |
| Late-arriving data requires reprocessing | Handle separately | Built-in |
| First build of new dataset | N/A | Yes — snapshot first |

## 3-4. Monitoring Incremental Pipelines

Configure these alerts in Foundry pipeline monitoring for every incremental production transform:

- **Build failure alert:** Immediate notification. A failed incremental build means data has stopped flowing.
- **No new data alert:** If new_data count = 0 for more than 2× the expected reporting cycle interval, the source feed may have stopped.
- **Late arrival rate:** Alert when `is_late_arrival` rate exceeds 15% — may indicate upstream system issues.
- **Watermark drift:** Alert when the watermark is more than 24 hours behind current time — indicates pipeline lag.

---

# CHAPTER 4 — ADVANCED ONTOLOGY AND OBJECT MODELING

## 4-1. Advanced Ontology Design Principles

The Ontology is the semantic core of MSS. At TM-20 level, you learned to create Object Types and link them. At TM-30 level, you design the ontology architecture itself.

**When to create a new Object Type:**
- The entity has its own lifecycle (created, modified, deleted independently)
- The entity has relationships to other objects
- Multiple applications need to query or display the entity
- The entity needs its own permissions or markings

**When to extend an existing Object Type:**
- You are adding properties to something already modeled
- The entity is simply additional detail on an existing object (add properties, not a new type)

**When to create an Interface instead:**
- Multiple Object Types share a common set of properties
- Applications need to query across multiple Object Types using a unified API
- You want to enforce a property contract (e.g., all "reportable" entities have `last_report_dtg`)

## 4-2. Interfaces — Shared Property Contracts

An Interface defines a set of properties that multiple Object Types must implement. It is analogous to an interface in TypeScript or an abstract base class in Python.

**Use case for USAREUR-AF:** Units, Personnel, and Equipment all have a `readiness_status`. Rather than defining the property three times with potentially inconsistent types, define an Interface `HasReadinessStatus` and implement it on all three Object Types.

---

### TASK 4-A: CREATE AN INTERFACE

**CONDITIONS:** Multiple Object Types in your ontology need to support readiness status tracking. Workshop applications and AIP agents need to query across these types using a unified property contract.

**STANDARDS:** Interface is defined with correct property types. All target Object Types implement the Interface. Interface properties are queryable from Workshop and OSDK.

**PROCEDURE:**

1. In Ontology Manager, navigate to **Interfaces** → **New Interface**.
2. Name the Interface: `HasReadinessStatus` (PascalCase, descriptive).
3. Add the following shared properties to the Interface:

| Property API Name | Type | Nullable | Description |
|-------------------|------|----------|-------------|
| `readinessStatus` | String | No | Current operational readiness status |
| `lastAssessedDtg` | Timestamp | Yes | When readiness was last assessed |
| `c_rating` | String | Yes | Army C-rating (C1–C4) |

4. Save and publish the Interface.
5. Open each target Object Type (e.g., `Unit`, `Personnel`, `EquipmentItem`).
6. Navigate to **Interfaces** tab → **Implement Interface** → select `HasReadinessStatus`.
7. Map each Interface property to the corresponding Object Type property.
8. Build and verify Interface resolution in Object Explorer.

> **CAUTION: Modifying or removing properties from a published Interface that is implemented by multiple Object Types will break all implementing types simultaneously. Treat Interface changes as a formation-wide schema change — coordinate with all affected teams before modifying.**

---

### TASK 4-B: CONFIGURE DERIVED PROPERTIES

**CONDITIONS:** You need to expose a property on `Unit` objects that represents the number of days since the last SITREP was submitted. This value changes daily without any data update. Storing it as a computed column in the transform would require a daily full-refresh.

**STANDARDS:** Property computes correctly at query time. Performance impact is understood and accepted. Backing function is tested on development branch.

**PROCEDURE:**

1. In Ontology Manager, open the `Unit` Object Type.
2. Navigate to **Properties** → **Add Property** → type: **Derived Property**.
3. Select the computation type:
   - **Formula-based:** For simple arithmetic (e.g., `TODAY() - lastSitrepDate`). No code required.
   - **Function-backed:** For complex logic. Requires a TypeScript Function (see Chapter 5).
4. For a formula-based derived property (`daysSinceLastSitrep`):
   - Formula: `DATEDIFF(NOW(), lastSitrepDtg, "days")`
   - Return type: Integer
5. Name the property, set display name, publish.

**Performance note:** Derived properties compute at query time — every time an object is loaded, the formula runs. For high-cardinality object sets (thousands of objects in a table), derived properties with expensive computations will noticeably slow Workshop application load time. If the value only needs to be current to within one reporting cycle, pre-compute it in the transform and store it as a regular property.

---

### TASK 4-C: MODEL COMPLEX LINK TYPES

**CONDITIONS:** Units have a many-to-many relationship with Personnel through assignments. An individual Soldier can be attached to multiple units (primary unit + OPCON attachment). You need to model this relationship with an assignment date on the link itself.

**STANDARDS:** Link type is correctly defined as many-to-many. Link property (assignment date) is accessible from both sides of the relationship.

**PROCEDURE:**

1. Ontology Manager → **Link Types** → **New Link Type**.
2. Configure:
   - **Name:** `personnel_assignment`
   - **Display name:** "Assignment"
   - **Object Type A:** `Personnel`
   - **Object Type B:** `Unit`
   - **Cardinality:** Many-to-Many
3. Add link properties (values stored on the link itself, not on either object):
   - `assignmentStartDtg` — Timestamp
   - `assignmentType` — String (PRIMARY, OPCON, TACON, ATTACHED)
4. Map the backing dataset — you need a junction dataset with columns for both primary keys plus the link properties.
5. Configure the backing dataset:
   - `personnel_id` (FK to Personnel)
   - `unit_id` (FK to Unit)
   - `assignment_start_dtg`
   - `assignment_type`
6. Publish the link type.
7. Verify traversal in Object Explorer: from a Personnel object, navigate to their assigned Units; from a Unit object, navigate to assigned Personnel.

---

### TASK 4-D: CONFIGURE OBJECT STORAGE V2

**CONDITIONS:** A high-cardinality Object Type (millions of Personnel objects) is experiencing slow search and filter performance in Workshop. Object Storage V2 provides indexing and property-level policy controls.

**STANDARDS:** Indexing configuration matches the most common query patterns. Property-level markings are applied correctly.

**PROCEDURE:**

1. Ontology Manager → Object Type → **Storage** tab.
2. Enable **Object Storage V2**.
3. Configure search indexing — index properties that are commonly used as filters:
   - `unit_id` — indexed (high-frequency filter in all applications)
   - `c_rating` — indexed
   - `aor` — indexed
   - `narrative` (free text) — indexed for full-text search if needed
4. Properties that do not need indexing (rarely filtered, large text, attachments) — leave unindexed to reduce storage cost.
5. Configure property-level policies:
   - Properties containing PII: add classification marking
   - Properties visible only to S2: apply appropriate marking
6. Publish and rebuild the Object Type.

> **CAUTION: Changing the indexing configuration on a high-cardinality Object Type triggers a full re-index. This can take hours on large datasets and temporarily degrades search performance. Schedule re-index operations during low-usage windows and notify application users.**

---

## 4-3. Ontology Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|-------------|-------------|------------------|
| One Object Type per data source | Fragments the semantic model; applications must know source, not concept | Model the concept; join sources in transforms |
| Derived properties for bulk displays | N+1 compute per object; table of 1000 objects = 1000 function calls | Pre-compute in transform; use derived only for per-object views |
| Link types without backing datasets | Relationships lost on rebuild | Always back link types with a persistent junction dataset |
| Removing properties without notification | Breaks all downstream applications using that property | Deprecate (mark nullable, stop writing); remove only after all consumers migrate |
| Storing raw dataset columns as Object properties | Exposes dirty/unstable data to applications | Always back Object Types with curated datasets only |

---

# CHAPTER 5 — FUNCTIONS ON OBJECTS (FOO)

## 5-1. What Functions on Objects Are

Functions on Objects (FOO) are TypeScript functions that execute against the Ontology at query time. They allow complex logic — including traversal of links to related objects, conditional scoring, and multi-object aggregations — to be encapsulated in the semantic model rather than duplicated across applications.

FOO functions live in a **Function Repository** (Code Repository, type: Functions). They are written in TypeScript and published to the Ontology, where they back computed properties or are called directly from Workshop widgets, AIP agents, and OSDK consumers.

## 5-2. When to Use FOO

| Use FOO | Use Transform-Computed Values | Use Derived Property Formula |
|---------|------------------------------|------------------------------|
| Logic requires traversing links to related objects | Value can be computed from columns in one dataset | Simple arithmetic on existing properties |
| Value must reflect current state of related objects | Value only needs to update on schedule | No TypeScript required |
| Complex scoring or classification logic | Bulk aggregation across millions of objects | Low query volume |
| Action side effects or validation | Static reference data enrichment | |
| Real-time queries requiring live data | | |

> **CAUTION: FOO functions are NOT suitable for bulk operations. If a Workshop table displays 10,000 objects and each has a FOO-backed computed property, the function executes 10,000 times on every page load. Pre-compute high-volume values in transforms. Use FOO for per-object detail views and low-volume computations.**

---

### TASK 5-A: WRITE A BASIC FUNCTION ON OBJECTS

**CONDITIONS:** You need to compute a composite readiness score for each Unit object that weights personnel fill and equipment serviceability. The formula is not expressible as a simple formula-based derived property.

**STANDARDS:** Function returns correct Integer result. Function is tested in development branch before publishing. Function is attached to Unit Object Type as a computed property.

**EQUIPMENT:** Foundry Function Repository (TypeScript), Editor role on Ontology.

**PROCEDURE:**

1. Create a new Code Repository (type: Functions) named `unit-readiness-functions`.
2. In `src/index.ts`:

```typescript
import { Function, Integer, Double } from "@palantir/functions-api";
import { Objects } from "@foundry/ontology-api";
import { Unit } from "@foundry/ontology-api";

export class UnitReadinessFunctions {

  /**
   * Composite readiness score: 60% personnel fill, 40% equipment serviceability.
   * Returns 0–100 integer. Returns null if data is insufficient.
   */
  @Function()
  public async getCompositeReadinessScore(unit: Unit): Promise<Integer | null> {
    const personnelFill = await unit.personnelFillPct;
    const equipmentSvc  = await unit.equipmentServiceablePct;

    // Guard: cannot compute without both inputs
    if (personnelFill == null || equipmentSvc == null) {
      return null;
    }

    const score = (personnelFill * 0.6) + (equipmentSvc * 0.4);
    return Math.round(score);
  }
}
```

3. Build the repository. Fix TypeScript compilation errors.
4. In Ontology Manager → `Unit` Object Type → Properties → Add Property → **Function-Backed Property**.
5. Select repository `unit-readiness-functions`, function `getCompositeReadinessScore`.
6. Map parameter `unit` to the current object.
7. Publish on development branch. Test in Object Explorer with known units.
8. After validation, merge to production via PR.

---

### TASK 5-B: BIND A FUNCTION TO A WORKSHOP WIDGET

**CONDITIONS:** A Workshop readiness dashboard needs to display the composite readiness score alongside standard properties in an Object Table.

**STANDARDS:** Function-backed property appears as a column in the Widget. Values load within acceptable latency for the table size.

**PROCEDURE:**

1. Open Workshop application → Module → Object Table widget.
2. In Columns configuration → **Add Column** → **Property** → select `compositeReadinessScore` (the function-backed property you published in Task 5-A).
3. Apply conditional formatting: green if > 80, yellow if 65–80, red if < 65.
4. Test with a small filtered object set (one brigade's units) before enabling for large object sets.
5. If load time is slow: move the table to a detail view (single object) rather than a bulk table display. See 5-2 for guidance on FOO performance limits.

---

### TASK 5-C: WRITE A FUNCTION WITH MULTIPLE OBJECT INPUTS AND LINK TRAVERSAL

**CONDITIONS:** You need to compute a unit's SITREP compliance rate — the percentage of expected SITREPs submitted on time over the past 30 days. This requires traversing the `Unit → Sitrep` link.

```typescript
import { Function, Double } from "@palantir/functions-api";
import { Unit } from "@foundry/ontology-api";

export class SitrepComplianceFunctions {

  @Function()
  public async getSitrepComplianceRate(unit: Unit): Promise<Double | null> {
    // Traverse the link to related SITREP objects
    const sitreps = await unit.sitreps.all();

    if (sitreps.length === 0) {
      return null;
    }

    // Filter to last 30 days
    const thirtyDaysAgo = new Date();
    thirtyDaysAgo.setDate(thirtyDaysAgo.getDate() - 30);

    const recent = sitreps.filter(s =>
      s.reportDtg != null && new Date(s.reportDtg) >= thirtyDaysAgo
    );

    if (recent.length === 0) {
      return 0.0;
    }

    // Compliance: on-time submissions / total submissions
    const onTime = recent.filter(s => s.isLate === false).length;
    return Math.round((onTime / recent.length) * 100) / 100;
  }
}
```

> **CAUTION: Link traversal functions (calling `.all()` on a link) load all related objects into memory. For Object Types with high-cardinality links (a unit with thousands of SITREPs), use `.filter()` before `.all()` to limit the set, or pre-aggregate in a transform and expose as a regular property.**

---

# CHAPTER 6 — ACTIONS AND WRITE-BACK PATTERNS

## 6-1. Actions Architecture

Reference TM-20 Chapter 8 for baseline Actions concepts. At TM-30 level, you design complex Actions with multi-field validation, conditional logic, and batch operations.

When a user executes an Action in Workshop:
1. Workshop validates the Action's parameters against the Action Type's validation rules.
2. If validation passes, Foundry submits the Action to the Ontology layer.
3. The Ontology layer applies the configured logic: creates, modifies, or deletes objects.
4. An audit record is written automatically — user, timestamp, parameters, outcome.
5. The backing dataset is updated; downstream transforms and Object Types refresh on next build cycle.

## 6-2. Action Types

| Type | Use Case | USAREUR-AF Example |
|------|----------|-------------------|
| Create Object | New record submission | Submit new SITREP, register new equipment item |
| Modify Object | Update existing record | Update unit readiness status, close an open event |
| Delete Object | Remove a record | Delete a duplicate SITREP (restricted — log carefully) |
| Batch | Operate on multiple objects at once | Bulk update status on all units in an AOR |

---

### TASK 6-A: CREATE A COMPLEX ACTION WITH VALIDATION

**CONDITIONS:** S6/G6 analysts need to submit updated unit readiness assessments via a Workshop form. The Action must enforce: `readinessPct` is 0–100, `cRating` matches the `readinessPct` range, `submittedBy` is present, and `assessmentDtg` is not in the future.

**STANDARDS:** All four validation rules enforce correctly. Invalid submissions are rejected with descriptive error messages. Valid submissions write correctly to the `Unit` Object Type.

**PROCEDURE:**

1. Ontology Manager → **Action Types** → **New Action Type** → type: **Modify Object** → target: `Unit`.
2. Define parameters:

| Parameter | Type | Required | Display Label |
|-----------|------|----------|---------------|
| `unitId` | String | Yes | Unit ID |
| `readinessPct` | Double | Yes | Readiness % (0–100) |
| `cRating` | String | Yes | C-Rating |
| `submittedBy` | String | Yes | Submitted By (name/rank) |
| `assessmentDtg` | Timestamp | Yes | Assessment DTG |
| `narrative` | String | No | Narrative |

3. Add validation rules:
   - `readinessPct >= 0 AND readinessPct <= 100` — message: "Readiness must be between 0 and 100."
   - Conditional: `IF readinessPct >= 85 THEN cRating == "C1"` — message: "C-Rating must be C1 for readiness >= 85%."
   - Conditional: `IF readinessPct >= 65 AND readinessPct < 85 THEN cRating IN ("C1", "C2")` — message: "C-Rating C2 or better required for this readiness range."
   - `assessmentDtg <= NOW()` — message: "Assessment DTG cannot be in the future."
4. Define logic: map each parameter to the corresponding `Unit` property.
5. Publish on development branch. Test with invalid inputs to verify each validation fires correctly.
6. Promote to production via PR after validation testing is complete.

> **CAUTION: Actions execute against the production Ontology when published. There is no "undo" — modified objects are modified, created objects exist. Test every validation rule exhaustively on a development branch before promoting. Confirm with the data steward that the Action modifies only the intended properties.**

---

### TASK 6-B: CREATE A BATCH ACTION

**CONDITIONS:** The G9 data team needs to bulk-update the `aorStatus` property on all units in a given AOR simultaneously when an AOR boundary changes. Updating hundreds of units individually is not operationally feasible.

**STANDARDS:** Batch Action operates on a filtered object set. User confirms the scope before execution. Audit trail captures all modified object IDs.

**PROCEDURE:**

1. Ontology Manager → **Action Types** → **New Action Type** → type: **Modify Object** → enable **Batch Mode**.
2. Define parameters:
   - `newAorStatus` — String (required)
   - `effectiveDtg` — Timestamp (required)
3. In Workshop, configure the Batch Action trigger:
   - Object Table widget → select rows → **Batch Action** button
   - Map `newAorStatus` and `effectiveDtg` from form inputs
   - Enable confirmation dialog: "You are updating [N] units. This cannot be undone. Confirm?"
4. Test on a small filtered subset (2–3 units) before running on the full AOR object set.

---

### TASK 6-C: TEST AN ACTION IN A DEVELOPMENT BRANCH

**PROCEDURE:**

1. Create a Foundry branch: `dev/action-test-[your-name]`.
2. In Ontology Manager, switch to the dev branch.
3. Publish your Action Type on the dev branch only.
4. Create a Workshop application on the same branch.
5. Execute the Action with valid and invalid test inputs.
6. Verify object modifications in Object Explorer on the dev branch.
7. After successful testing, open a PR to merge the Action Type definition to `dev` integration branch, then to `master`.
8. Production Workshop applications will see the Action after the `master` merge.

---

## 6-3. Action Security Model

Every Action execution is automatically logged with:
- User identity (Foundry principal)
- Timestamp (UTC)
- Action Type name
- Parameter values submitted
- Objects modified (by RID)
- Success/failure status

These logs are accessible in Foundry's audit trail and are retained per the MSS data retention policy. Do not create Actions that bypass required parameter fields to circumvent audit logging.

---

# CHAPTER 7 — AIP INTEGRATION

## 7-1. AIP Architecture Review

AIP (AI Platform) is the AI layer of MSS. It connects approved large language models (LLMs) to the Ontology, enabling natural-language querying, automated logic workflows, and AI-assisted analysis. AIP is not a standalone tool — it operates on top of the Ontology you have built.

| Component | Function |
|-----------|----------|
| AIP Logic | Event-driven automation on Ontology object changes |
| AIP Agent Studio | Conversational AI agents backed by Ontology tools |
| AIP Assist | In-app copilot widget for end users |
| Code Workspaces | Jupyter-based environment for model development against Foundry datasets |

## 7-2. Authorization Requirements

> **WARNING: AIP integrations require command authorization review before deployment to production. AI outputs, if acted upon without human review, can introduce errors into operational data. No AIP Logic or Agent may be deployed to production without: (a) command approval documented in writing, (b) human review gates built into the workflow, and (c) testing on a development branch with synthetic or historical data. See Appendix C for the full AIP Authorization Checklist.**

---

### TASK 7-A: BUILD AN AIP LOGIC WORKFLOW

**CONDITIONS:** When a `Unit` object's `cRating` property changes to `C3` or `C4`, the G3 requires an automatic notification object to be created in MSS for tracking.

**STANDARDS:** Logic fires correctly on the triggering condition. Notification object is created with correct properties. Logic does not fire on non-triggering changes. Human review gate is documented.

**PROCEDURE:**

1. AIP → **Logic** → **New Logic Workflow**.
2. Configure trigger:
   - Object Type: `Unit`
   - Property: `cRating`
   - Condition: `new value IN ["C3", "C4"]`
3. Add a **Function** node: call a TypeScript function that constructs the notification parameters.
4. Add an **Action** node: execute `create_readiness_notification` Action with the constructed parameters.
5. Add a **Human Review** gate: before the Action node, require a designated reviewer to approve notifications above a configured threshold (e.g., more than 5 units degraded in one cycle).
6. Test the workflow on a development branch by manually setting a Unit's `cRating` to `C3` via a test Action.
7. Review the Logic execution log. Verify the notification object was created with correct properties.
8. Submit for command authorization review (Appendix C) before promoting to production.

---

### TASK 7-B: CREATE AN AIP AGENT

**CONDITIONS:** G2 analysts need to query SITREP and unit readiness data using natural language rather than constructing Workshop filters manually.

**STANDARDS:** Agent answers questions accurately using Ontology data. Agent does not speculate beyond available data. Agent has restricted tool access (read-only, no Actions with write access). System prompt enforces operational scope.

**PROCEDURE:**

1. AIP → **Agent Studio** → **New Agent**.
2. Write the system prompt — this is the most critical configuration step:

```
You are a SITREP and readiness analysis assistant for USAREUR-AF.
You answer questions about unit readiness, SITREP compliance, and
equipment status using data from the MSS Ontology.

You have access to:
- Unit objects: readiness status, C-rating, AOR, personnel fill
- Sitrep objects: submission history, on-time/late status
- EquipmentItem objects: FMC/PMC/NMC status, maintenance dates

Rules:
- Only report what the data shows. Never estimate or speculate.
- Use military time (ZULU) for all timestamps.
- If data is unavailable, say so explicitly.
- Do not execute any Actions that write or modify data.
- Respond concisely. Use bulleted lists for multi-unit summaries.
```

3. Add tools (read-only):
   - Object Type: `Unit` — query, filter, summarize
   - Object Type: `Sitrep` — query, filter
   - Object Type: `EquipmentItem` — query, filter
   - Function: `getSitrepComplianceRate`
   - Function: `getCompositeReadinessScore`
4. Do not add Actions with write access until command authorization review is complete.
5. Test in the Agent Studio playground with representative queries.
6. Embed in Workshop: add an **Agent Widget** to your application module. Link to the published Agent.

---

### TASK 7-C: INTEGRATE AIP OUTPUT INTO A WORKSHOP APPLICATION

**PROCEDURE:**

1. In Workshop, open the module where AIP output will display.
2. Add an **AIP Widget** (type: Agent Chat or Logic Output, depending on your use case).
3. For Agent Chat: link to your published Agent. Configure the widget to pass the currently selected Object Set as context (e.g., selected unit or filtered set).
4. Add a clearly labeled **Human Review** section adjacent to AIP output:
   - Static text: "AI-generated output. Review before operational use."
   - Optionally: an Action button allowing the analyst to mark the output as "Reviewed" — this creates an audit record.
5. Never auto-populate operational fields from AIP output without explicit human confirmation.

> **WARNING: AI outputs require mandatory human review before operational use. Do not build Workshop workflows that automatically write AIP-generated values to production Object properties without an explicit human confirmation step. Automated action on AI output without review is prohibited.**

---

### TASK 7-D: USE CODE WORKSPACES FOR MODEL DEVELOPMENT

**CONDITIONS:** You need to develop and test a readiness forecasting model using historical SITREP data. Code Workspaces provide a Jupyter-based environment within the MSS boundary that can mount Foundry datasets directly.

**PROCEDURE:**

1. Navigate to **Code Workspaces** → **New Workspace**.
2. Select an appropriate compute profile (standard for EDA; GPU profile for model training if available and authorized).
3. Mount datasets:
   - Input dataset: `/USAREUR-AF/operational/processed/sitrep_normalized` (read-only)
   - Output dataset: `/USAREUR-AF/models/readiness_forecast_output` (write)
4. In the notebook, access datasets via the Foundry Python SDK:

```python
import foundry
import pandas as pd

# Authenticate via workspace token (auto-injected in Code Workspaces)
client = foundry.FoundryClient()

# Load dataset as pandas DataFrame
sitrep_df = client.datasets.read_table(
    dataset_rid="ri.foundry.main.dataset.XXXX",
    branch="master",
)

# EDA
print(sitrep_df.shape)
print(sitrep_df.dtypes)
print(sitrep_df["c_rating"].value_counts())
```

5. Develop and validate your model in the notebook.
6. Write outputs to the designated output dataset for downstream consumption by transforms or Workshop.
7. Do not store intermediate model artifacts containing real operational data outside the MSS boundary.

---

## 7-3. AIP Error Handling

| Error Type | Symptom | Response |
|------------|---------|---------|
| Model timeout | Agent returns no response | Reduce context size; limit object set passed to agent |
| Hallucinated data | Agent cites non-existent objects | Review system prompt; restrict tools to specific Object Types |
| Logic trigger loop | Logic fires repeatedly on same object | Add cooldown condition to Logic trigger; check for circular updates |
| Unexpected Action execution | Logic executes Actions not intended | Review Logic node configuration; add human review gate |

---

# CHAPTER 8 — OSDK (ONTOLOGY SDK)

## 8-1. What the OSDK Is

The Ontology SDK (OSDK) allows external applications — running outside the Foundry UI — to read and write MSS Ontology data programmatically. An external Python script, a REST API, a mobile application, or an automated reporting tool can all interact with MSS objects and execute Actions via the OSDK.

The OSDK is generated from your Ontology definition. It produces a strongly-typed client library in Python (or TypeScript) where every Object Type, property, and Action corresponds to a Python class or method.

## 8-2. OSDK vs. Direct Foundry Access

| Method | When to Use |
|--------|-------------|
| Workshop (UI) | Human users interacting with data directly |
| OSDK (Python/TypeScript) | Automated tools, external integrations, programmatic reporting |
| Foundry Platform SDK | Low-level dataset read/write; not Ontology-aware |
| REST API (Datasets API) | Raw dataset ingestion from external systems |

Use OSDK when the consumer is a program, not a human, and when the program needs to work with the semantic model (Objects, Actions) rather than raw datasets.

> **CAUTION: OSDK applications require an authorization review before deployment. OSDK tokens grant programmatic write access to the Ontology via Actions. A misconfigured or compromised OSDK application can modify production Ontology data at scale. Coordinate with security before deploying any OSDK-backed application to a network-connected system.**

---

### TASK 8-A: GENERATE OSDK CLIENT

**PROCEDURE:**

1. In Foundry, navigate to **Developer Console** → **SDK Generator**.
2. Select the Object Types to include in the generated SDK (principle of least privilege — include only what the application needs).
3. Select target language: Python or TypeScript.
4. Generate and download the SDK package.
5. Install in your application environment:

```bash
pip install ./foundry-sdk-usareur-af-0.1.0.tar.gz
```

6. Configure authentication via environment variable — never hardcode tokens:

```bash
export FOUNDRY_TOKEN="your-token-here"
export FOUNDRY_HOST="your-instance.palantirfoundry.com"
```

---

### TASK 8-B: READ OBJECTS VIA OSDK

**CONDITIONS:** An automated reporting script needs to query all units with C-rating of C3 or C4 and generate a daily readiness summary without human interaction.

**STANDARDS:** Query is correctly filtered. Results are paginated to handle large object sets. Credentials are managed via environment variables. No operational data is written to plaintext log files.

**PROCEDURE:**

```python
import os
from foundry import FoundryClient
from foundry.auth import UserTokenAuth

# Credentials from environment — never hardcode
client = FoundryClient(
    auth=UserTokenAuth(token=os.environ["FOUNDRY_TOKEN"]),
    hostname=os.environ["FOUNDRY_HOST"],
)

# Query degraded units (C3 or C4)
degraded_units = (
    client.ontology.objects.Unit
    .where(
        client.ontology.objects.Unit.c_rating.is_in(["C3", "C4"])
    )
    .order_by(client.ontology.objects.Unit.readiness_pct.asc())
)

# Paginate — never load all objects into memory at once
for unit in degraded_units.iterate():
    # Process each unit individually
    print(f"{unit.unit_id}: {unit.c_rating} ({unit.readiness_pct:.1f}%)")
    # Write summary to output — not raw operational data
```

> **CAUTION: Do not call `.all()` on large object sets. `.all()` loads every matching object into memory simultaneously. Use `.iterate()` for large queries. If you need aggregate statistics, use Contour or a pre-computed transform rather than iterating over thousands of objects in a script.**

---

### TASK 8-C: WRITE OBJECTS VIA OSDK (ACTIONS)

**CONDITIONS:** An automated pipeline needs to update `Unit` readiness status after processing an incoming data feed. Write-back is done by executing Actions, not by directly modifying datasets.

**STANDARDS:** Action execution is logged. Error handling covers API failures. Action parameters are validated before submission.

```python
import os
from foundry import FoundryClient
from foundry.auth import UserTokenAuth
import logging

logger = logging.getLogger(__name__)

client = FoundryClient(
    auth=UserTokenAuth(token=os.environ["FOUNDRY_TOKEN"]),
    hostname=os.environ["FOUNDRY_HOST"],
)

def update_unit_readiness(unit_id: str, readiness_pct: float, c_rating: str, submitted_by: str) -> None:
    """Execute the update_readiness_assessment Action via OSDK."""
    if not (0.0 <= readiness_pct <= 100.0):
        raise ValueError(f"readiness_pct out of range: {readiness_pct}")
    if c_rating not in {"C1", "C2", "C3", "C4"}:
        raise ValueError(f"Invalid c_rating: {c_rating}")

    try:
        client.ontology.actions.update_readiness_assessment(
            unit_id=unit_id,
            readiness_pct=readiness_pct,
            c_rating=c_rating,
            submitted_by=submitted_by,
        )
        logger.info(f"Action executed: update_readiness_assessment for {unit_id}")
    except Exception as e:
        logger.error(f"Action failed for {unit_id}: {e}")
        raise
```

---

## 8-3. Authentication and Token Management

| Requirement | Implementation |
|-------------|---------------|
| Token storage | Environment variables or secrets manager; never in code or config files checked into git |
| Token scope | Request minimum required permissions — read-only if application does not write |
| Token rotation | Rotate on personnel change or if token exposure is suspected |
| Token logging | Log token usage events (object count, Actions executed) but never log the token itself |
| Multi-environment | Separate tokens for dev and production environments |

---

# CHAPTER 9 — ANALYTICS: QUIVER AND CONTOUR (ADVANCED)

## 9-1. Advanced Quiver

Quiver is the MSS object-based analytics tool. It queries Object Types directly, respecting Ontology permissions and markings. At TM-30 level, you build reusable analyses with pivots and computed metrics that other analysts can clone and adapt.

Reference TM-20 for basic Quiver usage. This section covers advanced patterns.

---

### TASK 9-A: BUILD AN ADVANCED QUIVER ANALYSIS

**CONDITIONS:** The G3 needs a pivot analysis showing the distribution of units by C-rating across AORs, updated daily.

**STANDARDS:** Analysis uses a dynamic object set filter. Pivot table is correctly configured. Analysis is saved and shared with the G3 group. Auto-refresh is scheduled.

**PROCEDURE:**

1. Open **Quiver** → **New Analysis** → select Object Type `Unit`.
2. Apply base filter: status = ACTIVE or DEPLOYED.
3. Add metrics:
   - Count of units
   - Average readiness_pct
   - Minimum readiness_pct (worst unit in each group)
4. Configure pivot: Rows = `aor`, Columns = `c_rating`, Values = Count of units.
5. Add a secondary metric tile: total units at C3/C4 (computed metric: filter `c_rating IN ["C3","C4"]`, count).
6. Add conditional formatting: cells with count > 0 in C3/C4 columns highlighted red.
7. Save as "G3 Daily Readiness Pivot". Share with G3 Quiver group.
8. Schedule: Settings → **Auto-Refresh** → daily at 0700L (0600Z for USAREUR-AF).

---

### TASK 9-B: CREATE A CONTOUR ANALYSIS WITH JOINS

**CONDITIONS:** You need to join unit readiness data with SITREP compliance data to produce a combined analysis. The two datasets are backed by different Object Types. Contour operates at the dataset level and can join across sources.

**STANDARDS:** Join produces correct output. Aggregation matches expected counts. Analysis is exported as a reusable template.

**PROCEDURE:**

1. Open **Contour** → **New Analysis**.
2. Add first dataset: `/USAREUR-AF/operational/processed/unit_readiness_clean` (curated tier — never raw).
3. Add a **Join** step:
   - Join type: Left join
   - Second dataset: `/USAREUR-AF/operational/processed/sitrep_compliance_summary`
   - Join key: `unit_id`
4. Add **Aggregate** step: group by `aor`, `c_rating`; compute count of units, average compliance rate, average readiness_pct.
5. Add **Filter** step: remove units with `status = INACTIVE`.
6. Add a **Sort** step: sort by `c_rating` ascending, then `aor` ascending.
7. Preview the result. Verify row counts match expected unit counts per AOR.
8. Save as a reusable template: File → **Save as Template** → "Unit Readiness + SITREP Compliance".

---

### TASK 9-C: CREATE REUSABLE ANALYSIS TEMPLATES

**PROCEDURE:**

1. Complete the analysis to the point of a finalized, validated output.
2. Contour: File → **Save as Template**. Name with standard convention: `[AOR]-[subject]-[frequency]` (e.g., `EUCOM-readiness-daily`).
3. Quiver: **Save Analysis** → configure sharing: add all intended consumer groups.
4. Both tools: configure scheduled refresh aligned to the reporting cycle.
5. Document the template in your team's internal wiki: inputs required, expected output schema, refresh schedule, point of contact.
6. Share with your team lead for review before publishing broadly.

---

## 9-2. Tool Selection — Quiver vs. Contour vs. Workshop

| Need | Tool |
|------|------|
| Analyze objects with Ontology permissions applied | Quiver |
| Join raw/curated datasets without Ontology layer | Contour |
| Build an interactive application for end users | Workshop |
| Ad-hoc pivot analysis for analyst consumption | Quiver |
| Complex multi-dataset ETL result verification | Contour |
| Embed analysis in an operational application | Workshop (embed Quiver widget) |
| Share a reusable analysis template with a team | Quiver (save and share) or Contour (template) |

---

# CHAPTER 10 — DATA LINEAGE AND CI/CD

## 10-1. Reading the Lineage Graph

Foundry's Data Lineage tool shows the full directed acyclic graph (DAG) of data flow from ingestion through transforms to Ontology to applications. At TM-30 level, you read the lineage graph to:

- Understand the impact radius of a change before making it
- Debug unexpected data values by tracing upstream to the source of the error
- Identify orphaned datasets (no downstream consumers) for cleanup
- Verify that your changes rebuilt all dependent datasets

**How to read lineage:**
1. Open any dataset or Object Type in Compass.
2. Click the **Lineage** icon (three interconnected nodes).
3. The graph shows: upstream (left, what feeds this) and downstream (right, what this feeds).
4. Click any node to navigate to that dataset or transform.
5. Color coding: green = recently built successfully; yellow = stale (needs rebuild); red = build failure.

---

### TASK 10-A: TRACE DATA LINEAGE FOR A PRODUCTION DATASET

**CONDITIONS:** Analysts report that `Unit.readiness_pct` values appear incorrect. You need to trace the lineage from the Object Type back to the raw ingest to identify where the error was introduced.

**STANDARDS:** Root cause identified to a specific transform or source dataset. Impact on downstream consumers assessed before any fix is applied.

**PROCEDURE:**

1. Open `unit_readiness_clean` dataset in Compass → click **Lineage**.
2. Navigate upstream: identify the transform that produced this dataset.
3. Open that transform's code. Review the `readiness_pct` transformation logic.
4. Navigate further upstream to the raw dataset. Preview data to compare raw values vs. cleaned values.
5. If error is in raw data: document and escalate to the data owner of the source system.
6. If error is in transform logic: identify the specific bug, document it, then:
   a. Create a feature branch.
   b. Fix the transform.
   c. Build on the branch — verify output is correct.
   d. Check downstream consumers in lineage view — all must be notified before merge.
   e. Submit PR with the fix and impact assessment.

---

### TASK 10-B: MANAGE A FOUNDRY BRANCH FOR DEVELOPMENT

**CONDITIONS:** You are implementing a significant ontology change (new Interface + two Object Type modifications) that should not affect production until fully tested.

**STANDARDS:** All development occurs on a named branch. Production (`master`) is never directly modified. Branch is merged only after review and passing builds.

**PROCEDURE:**

1. In Compass, navigate to your project. Click **Branches** → **New Branch**.
2. Name the branch: `dev/interface-readiness-[date]`. Branch from `master`.
3. All work (transform edits, ontology changes, Workshop updates) is done on this branch.
4. Build your changes on the branch. Verify outputs in dataset preview and Object Explorer.
5. Open a PR: branch → `dev` (integration). Add reviewers. Describe scope of change.
6. After `dev` integration testing is complete and no regressions are found, open a second PR: `dev` → `master`.
7. Merge to `master` only after lead approval. Production updates take effect after the merge completes and builds run.

> **CAUTION: Never commit directly to `master`. Never skip the PR review process for production changes. Even trivial-looking changes (renaming a property display name) can break downstream Workshop applications that reference the API name. Every change requires review.**

---

### TASK 10-C: SET UP AUTOMATED CHECKS IN CI

**CONDITIONS:** Your transforms currently have no automated data quality checks. A bad build produced incorrect C-rating values and it was not caught until an analyst reported it three days later.

**STANDARDS:** Checks run automatically after every build. ERROR-severity check failures block the pipeline. WARNING-severity check failures log but do not block. Check results are visible in the build log.

**PROCEDURE:**

The check pattern is implemented in `data_skills/13_foundry_patterns/foundry_checks.py`. For production, define checks alongside your transform:

```python
from transforms.api import check, Check
from transforms.api import transform, Input, Output
from pyspark.sql import functions as F

@check(outputs=Output("/USAREUR-AF/operational/processed/unit_readiness_clean"))
def check_no_null_unit_ids(output):
    """ERROR: null unit_id values block downstream consumers."""
    df = output.dataframe()
    null_count = df.filter(F.col("unit_id").isNull()).count()
    assert null_count == 0, f"{null_count} null unit_id values in output"

@check(outputs=Output("/USAREUR-AF/operational/processed/unit_readiness_clean"))
def check_readiness_pct_in_range(output):
    """ERROR: readiness_pct must be 0.0–100.0."""
    df = output.dataframe()
    bad = df.filter((F.col("readiness_pct") < 0) | (F.col("readiness_pct") > 100)).count()
    assert bad == 0, f"{bad} rows with readiness_pct out of [0, 100]"

@check(outputs=Output("/USAREUR-AF/operational/processed/unit_readiness_clean"))
def check_valid_c_rating(output):
    """ERROR: only valid C-ratings accepted."""
    df = output.dataframe()
    invalid = df.filter(~F.col("c_rating").isin(["C1", "C2", "C3", "C4"])).count()
    assert invalid == 0, f"{invalid} invalid c_rating values"
```

In `pipeline-spec.yml`, configure checks to run as part of the build:

```yaml
checks:
  - type: python_unit_tests
    target: transforms-python
  - type: foundry_checks
    target: transforms-python
```

---

## 10-2. Change Management Workflow for Production Pipeline Modifications

Before modifying any shared production pipeline:

1. **Impact assessment:** Open the lineage graph. List every downstream dataset, Object Type, and application that will be affected.
2. **Coordination:** Notify downstream application owners and data stewards. Get written acknowledgment if the change is breaking.
3. **Feature branch:** All development on a named branch, never on `master`.
4. **Testing:** Build and validate on the branch. Verify check results. Test downstream applications on the branch.
5. **PR and review:** Submit PR with impact assessment. Require reviewer approval before merge.
6. **Merge window:** Merge to `master` during low-usage hours if change affects high-priority applications.
7. **Post-merge verification:** Verify builds complete successfully. Check that downstream Object Types and applications refresh correctly.
8. **Rollback plan:** Document how to revert the change if post-merge issues are detected.

See Appendix D for the complete TM-30 Change Management Checklist.

---

# APPENDIX A — ADVANCED PYSPARK REFERENCE

## A-1. Window Functions

```python
from pyspark.sql import functions as F
from pyspark.sql.window import Window

# Latest record per unit (most recent SITREP)
w_latest = Window.partitionBy("unit_id").orderBy(F.desc("report_dtg"))
df = df.withColumn("row_num", F.row_number().over(w_latest))
latest = df.filter(F.col("row_num") == 1).drop("row_num")

# Period-over-period readiness change
w_ordered = Window.partitionBy("unit_id").orderBy("report_dtg")
df = df.withColumn(
    "prev_readiness", F.lag("readiness_pct", 1).over(w_ordered)
)
df = df.withColumn(
    "readiness_delta", F.col("readiness_pct") - F.col("prev_readiness")
)

# Cumulative SITREP count per unit
w_cumulative = Window.partitionBy("unit_id").orderBy("report_dtg").rowsBetween(
    Window.unboundedPreceding, 0
)
df = df.withColumn("sitrep_count_cumulative", F.count("*").over(w_cumulative))

# Rank units by readiness within each AOR
w_rank = Window.partitionBy("aor").orderBy(F.desc("readiness_pct"))
df = df.withColumn("aor_readiness_rank", F.rank().over(w_rank))
```

## A-2. Complex Join Patterns

```python
# Broadcast join for small lookup tables (avoids shuffle)
mos_lookup = spark.read.parquet("/path/to/mos_codes")  # small table
df = df.join(F.broadcast(mos_lookup), on="mos_code", how="left")

# Self-join for unit hierarchy (unit → parent unit)
units = df.alias("child")
parents = df.select(
    F.col("unit_id").alias("parent_unit_id"),
    F.col("display_name").alias("parent_name")
).alias("parent")
hierarchy = units.join(
    parents,
    F.col("child.higher_hq_id") == F.col("parent.parent_unit_id"),
    how="left"
)

# Anti-join: units with NO sitrep this cycle
expected = all_units.select("unit_id")
submitted = sitreps.select("unit_id").distinct()
missing = expected.join(submitted, on="unit_id", how="left_anti")
```

## A-3. UDFs — Use With Caution

> **CAUTION: Python UDFs (User Defined Functions) execute row-by-row in a Python process, bypassing Spark's native JVM execution. This typically results in 10–100× slower execution compared to equivalent native Spark functions. Always check `pyspark.sql.functions` for a native equivalent before writing a UDF. If you must use a UDF, prefer Pandas UDFs (vectorized) over row-level UDFs.**

```python
# AVOID: Row-level UDF (slow)
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

@udf(returnType=StringType())
def pct_to_c_rating(pct):
    if pct is None: return None
    if pct >= 85: return "C1"
    if pct >= 65: return "C2"
    if pct >= 35: return "C3"
    return "C4"

# PREFER: Native Spark (fast)
df = df.withColumn("c_rating",
    F.when(F.col("readiness_pct") >= 85, "C1")
     .when(F.col("readiness_pct") >= 65, "C2")
     .when(F.col("readiness_pct") >= 35, "C3")
     .otherwise("C4")
)
```

## A-4. Time-Series Patterns

```python
# Parse military DTG string to timestamp
df = df.withColumn(
    "report_ts",
    F.to_timestamp(F.col("dtg_string"), "ddHHmm'Z' MMM yy")
)

# All timestamps stored as UTC
df = df.withColumn("report_ts_utc", F.to_utc_timestamp("report_ts", "UTC"))

# Extract fiscal year (Army FY: Oct 1 – Sep 30)
df = df.withColumn(
    "fiscal_year",
    F.when(F.month("report_ts") >= 10,
           F.year("report_ts") + 1)
    .otherwise(F.year("report_ts"))
)

# 30-day rolling average readiness (window function)
w_30d = Window.partitionBy("unit_id").orderBy(
    F.col("report_ts").cast("long")
).rangeBetween(-30 * 86400, 0)  # 30 days in seconds

df = df.withColumn(
    "readiness_30d_avg",
    F.avg("readiness_pct").over(w_30d)
)
```

---

# APPENDIX B — ONTOLOGY DESIGN PATTERNS

| Use Case | Recommended Pattern | Example | Anti-Pattern to Avoid |
|----------|--------------------|---------|-----------------------|
| Cross-type shared properties | Interface | `HasReadinessStatus` on Unit, Personnel, Equipment | Redefine the same property on each type independently |
| Value computed from multiple source columns | Function-backed derived property | `compositeReadinessScore` from personnel + equipment pcts | Store as a column in raw dataset |
| Relationship with metadata | Link type with link properties | `personnel_assignment` with `assignmentType`, `startDtg` | Two separate one-to-one link types |
| High-cardinality historical records | Object Type + incremental backing transform | `Sitrep` backed by incremental sitrep_normalized | Curated dataset rebuilt daily from full historical feed |
| Lookup / reference data | Separate small Object Type | `MosCode`, `AorBoundary` | Hard-code reference values in transform logic |
| Hierarchical relationships | Self-referential link type | `Unit.parentUnit` → `Unit` | Flatten hierarchy into columns |
| Multi-source entity reconciliation | Single Object Type backed by reconciled curated dataset | `Unit` backed by SAMS-E + MTOE join | One Object Type per source system |
| Time-series property tracking | Separate Object Type for events/readings | `ReadinessSnapshot` with timestamp | Overwrite current value on Unit each cycle |

---

# APPENDIX C — AIP AUTHORIZATION CHECKLIST

The following AIP capabilities require written command authorization before production deployment. "Production" means any deployment accessible to operational users or any deployment that writes to production Ontology data.

## C-1. AIP Logic Workflows

- [ ] Triggering condition is documented and reviewed
- [ ] All Actions in the Logic workflow are read-only OR human review gate is inserted before any write Action
- [ ] Logic has been tested on development branch with synthetic data
- [ ] Data steward has reviewed which Object Types are affected
- [ ] Command authorization obtained in writing (email or tracked ticket)
- [ ] Rollback plan documented (how to disable Logic if unexpected behavior occurs)

## C-2. AIP Agents

- [ ] System prompt reviewed by team lead
- [ ] Agent tools are limited to minimum required Object Types and Functions
- [ ] No write Actions assigned to agent without explicit command approval
- [ ] Agent has been tested with adversarial queries (attempts to get agent to reveal data outside its scope)
- [ ] Human review messaging is displayed in the Workshop widget adjacent to Agent output
- [ ] Command authorization obtained in writing
- [ ] Agent is not connected to external APIs or services outside the MSS boundary

## C-3. Code Workspace Model Deployment

- [ ] Model does not write operational conclusions directly to Ontology without human review
- [ ] Input datasets are curated tier only (no raw datasets)
- [ ] Model outputs are written to a designated output dataset, not to live Object Type properties
- [ ] Model validation metrics documented
- [ ] Command authorization obtained before output dataset is consumed by any production application

## C-4. General AIP Authorization Contact

Contact the USAREUR-AF Data Office for command authorization processing. Include:
- AIP capability type (Logic / Agent / Model)
- Object Types and Actions accessed
- User population who will interact with the AIP feature
- Impact assessment if AIP output is incorrect

---

# APPENDIX D — TM-30 CHANGE MANAGEMENT CHECKLIST

Complete before merging any production change to `master`.

## D-1. Pre-Development

- [ ] Impact assessment completed: all downstream datasets, Object Types, and applications identified
- [ ] Downstream application owners notified of upcoming change
- [ ] Data steward coordination completed for ontology changes
- [ ] Feature branch created from `master`: `feature/[description]-[date]`
- [ ] Authorization obtained for AIP or OSDK changes (Appendix C)

## D-2. Development and Testing

- [ ] All changes made on feature branch — no direct commits to `master` or `dev`
- [ ] Code builds cleanly on feature branch with no errors or warnings
- [ ] All automated checks pass (zero ERROR-severity failures)
- [ ] Schema enforcement validated: output schema matches expected `StructType`
- [ ] Incremental transforms tested for first-run (full snapshot) and subsequent incremental runs
- [ ] Actions tested with valid and invalid inputs on development branch
- [ ] FOO functions tested in development before publishing to Ontology
- [ ] AIP Logic or Agent tested with synthetic/historical data on dev branch
- [ ] Downstream applications tested on the feature branch

## D-3. Code Review

- [ ] PR opened against `dev` integration branch
- [ ] PR description includes: scope, affected resources, test results, rollback plan
- [ ] At least one peer reviewer has approved
- [ ] Data steward has approved ontology changes (in PR comments)
- [ ] Team lead has been notified of the PR

## D-4. Production Merge

- [ ] Feature branch merged to `dev`; integration tests completed on `dev`
- [ ] PR opened from `dev` to `master`
- [ ] Lead data engineer or team lead approval obtained
- [ ] Merge window selected (low-usage hours for high-impact changes)
- [ ] Post-merge: all builds complete successfully
- [ ] Post-merge: downstream Object Types and applications verified
- [ ] Post-merge: monitoring alerts active and checked within 24 hours of merge

## D-5. Rollback

- [ ] Rollback procedure documented before merge
- [ ] For breaking schema changes: previous schema documented; rollback transform available
- [ ] For ontology changes: previous ontology state captured on a snapshot branch
- [ ] For AIP changes: Logic/Agent can be disabled without code changes (kill switch configured)

---

# GLOSSARY

| Term | Definition |
|------|-----------|
| **@incremental** | Foundry decorator marking a transform to process only new data since last successful run |
| **@lightweight_transform** | Foundry decorator for non-Spark (pandas) transforms; use for small datasets |
| **Action** | A user or system-triggered data write operation on the Ontology |
| **AIP** | AI Platform — the AI/ML layer of MSS (Foundry); includes Logic, Agents, Code Workspaces |
| **AIP Agent** | A conversational AI assistant backed by Ontology tools and functions |
| **AIP Logic** | Event-driven automation that fires on Ontology object property changes |
| **Broadcast join** | Spark optimization: copies a small dataset to all executors to avoid a full shuffle |
| **C-rating** | Army readiness classification (C1=highest to C4=lowest) |
| **Check** | Automated data quality assertion that runs after a transform and can block pipeline progression |
| **Code Workspace** | Jupyter-based interactive development environment within the MSS boundary |
| **Column pruning** | Selecting only required columns before expensive Spark operations |
| **Contour** | MSS dataset-level analytics tool; supports multi-dataset joins and aggregations |
| **Derived property** | An Object Type property whose value is computed at query time, not stored |
| **FOO** | Functions on Objects — TypeScript functions that execute against the Ontology |
| **Function Repository** | Foundry Code Repository containing TypeScript Functions |
| **Interface** | An ontology construct defining a shared property contract across multiple Object Types |
| **Lineage graph** | Foundry visualization of data flow from source to application |
| **Object Storage V2** | Foundry's advanced object storage backend with indexing and property-level policies |
| **OPCON** | Operational Control — command relationship |
| **OSDK** | Ontology SDK — generated client library for external programmatic access to MSS Ontology |
| **Partitioning** | Distributing Spark data across executors for parallel processing |
| **Predicate pushdown** | Applying filter conditions as early as possible to reduce data scanned |
| **Quiver** | MSS object-based analytics tool; queries Object Types directly with Ontology permissions |
| **require_incremental** | @incremental parameter that fails the build if incremental mode is unavailable |
| **Schema enforcement** | Defining and applying a `StructType` to validate transform output types |
| **TACON** | Tactical Control — command relationship |
| **UDF** | User Defined Function — custom Python function used in Spark; use sparingly (performance penalty) |
| **Watermark** | A stored timestamp or transaction ID marking the last successfully processed state in a pipeline |
| **Window function** | Spark operation that computes across a partition of rows (rank, lag, rolling average) |

Cross-reference GLOSSARY_data_foundry.md for full platform terminology definitions.

---

*TM-30 — Maven Smart System (MSS) Advanced Builder Technical Manual*
*USAREUR-AF Operational Data Team*
*Wiesbaden, Germany | 2026*
*UNCLASSIFIED — Approved for public release; distribution is unlimited.*
*Prerequisite: TM-10, TM-20*
