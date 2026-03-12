> **DEPRECATED — March 2026**
> This document has been superseded by the Maven Training Curriculum TM series.
> Content distributed to: TM-10, TM-20, TM-30, TM-40A through TM-40F.
> Do not use for new training. Reference `maven_training/README.md` for current publications.

---

# MAVEN FIELD MANUAL
## Foundry Developer Reference — USAREUR-AF Operational Data Team
### Version 1.0 | Classification: UNCLASSIFIED

---

> **Purpose:** Take you from Foundry *user* to Foundry *developer*. Read this, then build something.
> **How to use it:** Read Chapter 1 first. Then go to whatever you need.

---

## TABLE OF CONTENTS

1. [Chapter 1 — What Foundry Actually Is](#chapter-1--what-foundry-actually-is)
2. [Chapter 2 — The Mental Model](#chapter-2--the-mental-model)
3. [Chapter 3 — Your First Week](#chapter-3--your-first-week)
4. [Chapter 4 — Data In: Datasets & Ingestion](#chapter-4--data-in-datasets--ingestion)
5. [Chapter 5 — Transforms: Making Data Useful](#chapter-5--transforms-making-data-useful)
6. [Chapter 6 — The Ontology](#chapter-6--the-ontology)
7. [Chapter 7 — Workshop: Building UIs](#chapter-7--workshop-building-uis)
8. [Chapter 8 — Actions & Write-Back](#chapter-8--actions--write-back)
9. [Chapter 9 — Functions & Computed Properties](#chapter-9--functions--computed-properties)
10. [Chapter 10 — AIP & AI Integration](#chapter-10--aip--ai-integration)
11. [Chapter 11 — Permissions & Markings](#chapter-11--permissions--markings)
12. [Chapter 12 — Build System & CI](#chapter-12--build-system--ci)
13. [Chapter 13 — Maven-Specific Patterns](#chapter-13--maven-specific-patterns)
14. [Quick Reference Glossary](#quick-reference-glossary)

---

## CHAPTER 1 — WHAT FOUNDRY ACTUALLY IS

### The One-Sentence Version
Foundry is a platform where you bring raw data in, clean and connect it, model it as real-world objects, and build applications on top — all in one place.

### The Three Layers (Memorize This)

```
┌─────────────────────────────────────┐
│  LAYER 3: APPLICATIONS              │  ← What users see (Workshop, Quiver, AIP)
├─────────────────────────────────────┤
│  LAYER 2: ONTOLOGY                  │  ← The "what it means" layer (objects, links)
├─────────────────────────────────────┤
│  LAYER 1: DATA (Datasets)           │  ← Raw → clean → aggregated tables
└─────────────────────────────────────┘
```

**You must build bottom-up.** No ontology without clean data. No apps without ontology.

### What Foundry Is NOT
- Not a database you query with SQL (though SQL runs inside it)
- Not a traditional BI tool (though it does dashboards)
- Not a standalone coding environment (though it has one)

### Maven Smart System Context
Maven is the Army's AI/ML enterprise program. It runs **on** Foundry. When someone says "Maven," they mean Foundry + Army data + Army-approved AI models. Your work lives inside Maven's Foundry environment. The platform is the same — the data and access controls are Army-specific.

---

## CHAPTER 2 — THE MENTAL MODEL

### Core Concepts in Plain Language

| Term | Plain English |
|------|---------------|
| **Dataset** | A table. Like a CSV, but managed by Foundry. |
| **Transform** | Code that turns one dataset into another. |
| **Ontology** | The shared definition of what things *are* (a Soldier, a Vehicle, a Unit). |
| **Object Type** | The blueprint for a thing (like a class in Python). |
| **Object** | One instance of that thing (one Soldier, one Vehicle). |
| **Link Type** | How two object types connect (Soldier → assigned to → Unit). |
| **Object Set** | A filtered group of objects (all Soldiers in 21st TSC). |
| **Action** | A button in an app that changes data back. |
| **Workshop** | Foundry's drag-and-drop app builder. |
| **Function** | Code that runs against the ontology (TypeScript). |
| **AIP** | The AI layer — LLMs, agents, logic on top of your ontology. |

### The Data Flow

```
External Source
      │
      ▼
[Raw Dataset]  ←── ingested as-is, never modify this
      │
      ▼
[Staging Dataset]  ←── cleaned, standardized, validated
      │
      ▼
[Curated Dataset]  ←── business-ready, ontology-backing
      │
      ▼
[Object Type]  ←── Ontology layer, the semantic model
      │
      ▼
[Workshop App / AIP Agent]  ←── what the user touches
```

**Rule:** Never skip a layer. Never let an app read from a raw dataset.

---

## CHAPTER 3 — YOUR FIRST WEEK

### Day 1: Orient Yourself

1. Log into Foundry. Find the **Home** screen.
2. Navigate to **Compass** — this is the file explorer. Everything lives here.
3. Find your team's project folder. Don't touch anything yet — just look.
4. Open **Data Lineage** on any dataset. See how data flows.
5. Find **Code Repositories**. This is where transforms live.

### Day 2: Read Before You Write

1. Find an existing transform in your team's repo. Read it.
2. Find the dataset it produces. Preview it.
3. Find the object type that dataset backs. Open Ontology Manager.
4. Find a Workshop app that uses that object type. Use it like a regular user.

**You now understand the full stack. Don't write a single line of code until you do this.**

### Day 3: Your First Transform

1. Create a new **Code Repository** (type: Transforms).
2. Write a transform that reads an existing dataset and produces a new one.
3. Build it. Fix errors. Build again.
4. Preview the output dataset.

### Day 4: Your First Object Type

1. Open **Ontology Manager**.
2. Create a new Object Type in the sandbox/dev ontology.
3. Attach your transform output as the backing dataset.
4. Add 3 properties. Map them to columns.
5. Search for your object in **Object Explorer**.

### Day 5: Your First Workshop Widget

1. Create a new Workshop app.
2. Add an Object Table widget.
3. Point it at your object type.
4. Filter it. Sort it. Done.

---

## CHAPTER 4 — DATA IN: DATASETS & INGESTION

### What a Dataset Is

A Foundry dataset is a versioned, managed table. It has:
- A **schema** (column names and types)
- **Transactions** (every write creates a new version)
- A **branch** (usually `master`)
- A **location** in Compass

### Dataset Branches

Foundry datasets support branching, like Git:
- `master` = production
- `dev` / feature branches = for development
- Always develop on a branch, promote to master when ready

### How Data Gets In

**Method 1: Magritte (Connectors)**
- Scheduled pulls from databases, S3, REST APIs, etc.
- Configured by admin/data engineer
- You consume the output — usually a raw dataset

**Method 2: Direct Upload**
- Compass → New → Dataset → Upload File
- Use for one-off reference data (lookup tables, shapefiles, etc.)
- Not for operational data feeds

**Method 3: Foundry Data Connection**
- Real-time or batch sync from approved external systems
- Requires admin configuration

**Method 4: API (Datasets API)**
- POST data programmatically via Foundry REST API
- Used for custom ingestion scripts
- Requires API token and dataset RID

### Dataset RID
Every dataset has a **Resource Identifier (RID)** — a permanent unique ID.
Format: `ri.foundry.main.dataset.xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`

You'll use RIDs constantly. Copy them from Compass → dataset → three-dot menu → Copy RID.

### Schema Best Practices

- Use `snake_case` for column names
- Use consistent types — don't mix strings and numbers in the same column
- Add a `_ingested_at` timestamp column to every raw dataset
- Null handling: decide upfront what nulls mean in your domain

---

## CHAPTER 5 — TRANSFORMS: MAKING DATA USEFUL

### What a Transform Is

A transform is code that reads one or more datasets and writes a new one. Foundry runs it on Spark (distributed compute), but you write it in Python (or SQL, or Java).

### Code Repository Structure

```
my-transforms/
├── transforms-python/
│   └── src/
│       └── myproject/
│           ├── __init__.py
│           ├── raw_to_staging.py
│           └── staging_to_curated.py
├── pipeline-spec.yml          ← build/schedule config
└── README.md
```

### Python Transform — Minimum Working Example

```python
from transforms.api import transform, Input, Output
import pyspark.sql.functions as F

@transform(
    output=Output("/path/to/output/dataset"),
    source=Input("/path/to/input/dataset"),
)
def compute(source, output):
    df = source.dataframe()
    df_clean = df.filter(F.col("status").isNotNull())
    output.write_dataframe(df_clean)
```

**That's it. That's a transform.**

### Key Decorators

| Decorator | Use |
|-----------|-----|
| `@transform` | Standard batch transform |
| `@transform_df` | Shorthand — receives/returns DataFrames directly |
| `@lightweight` | Runs on small compute (pandas, not Spark) — use for small data |
| `@incremental` | Only processes new/changed rows — use for large, growing datasets |

### `@transform_df` — Simpler Syntax

```python
from transforms.api import transform_df, Input, Output

@transform_df(
    Output("/output/dataset"),
    source=Input("/input/dataset"),
)
def compute(source):
    return source.filter(source["unit"].isNotNull())
```

### Incremental Transforms — Critical for Operational Data

Use when:
- Dataset grows daily (logs, events, SITREPs)
- Full recompute is too slow
- You only need to process new rows

```python
from transforms.api import transform, Input, Output
from transforms.api.incremental import IncrementalTransform

@transform(
    output=Output("/output/dataset"),
    source=Input("/input/dataset"),
)
def compute(source, output):
    # Only processes rows added since last run
    with IncrementalTransform(source, output) as incr:
        new_df = incr.get_input()
        processed = new_df.withColumn("processed_at", F.current_timestamp())
        incr.write_output(processed)
```

### Lightweight Transforms (Pandas)

For small reference tables or complex Python logic that doesn't need Spark:

```python
from transforms.api import lightweight, transform_df, Input, Output

@lightweight
@transform_df(
    Output("/output/small_table"),
    source=Input("/input/reference_data"),
)
def compute(source):
    import pandas as pd
    df = source.toPandas()          # convert from Spark
    df["full_name"] = df["first"] + " " + df["last"]
    return df
```

### Common PySpark Operations

```python
import pyspark.sql.functions as F
from pyspark.sql.types import StringType, IntegerType, TimestampType

# Filter
df.filter(F.col("status") == "ACTIVE")

# Add column
df.withColumn("upper_name", F.upper(F.col("name")))

# Rename
df.withColumnRenamed("old_name", "new_name")

# Join
df1.join(df2, df1["unit_id"] == df2["id"], "left")

# Aggregate
df.groupBy("unit").agg(F.count("*").alias("total"), F.max("dtg").alias("last_report"))

# Cast type
df.withColumn("count", F.col("count").cast(IntegerType()))

# Handle nulls
df.fillna({"status": "UNKNOWN", "count": 0})
df.dropna(subset=["required_field"])

# Window functions
from pyspark.sql.window import Window
w = Window.partitionBy("unit_id").orderBy(F.desc("dtg"))
df.withColumn("rank", F.row_number().over(w))
```

### Scheduling Transforms

In `pipeline-spec.yml`:

```yaml
schedules:
  - cron: "0 6 * * *"    # every day at 0600 UTC
    target: my_transform
```

Or configure in the UI: Code Repository → Builds → Schedule.

### Debugging Tips

1. **Build fails immediately** → syntax error. Check the error message first line.
2. **Build fails mid-run** → Spark error. Look for the `Caused by:` line in the logs.
3. **Output is empty** → your filter removed everything. Add `.show()` in test, check counts.
4. **Schema mismatch** → output schema changed. Delete the output dataset and rebuild.
5. **Memory error** → data too big for lightweight. Switch to `@transform` (Spark).

---

## CHAPTER 6 — THE ONTOLOGY

### Why the Ontology Matters

The Ontology is Foundry's semantic layer. It answers: *"What does this data represent?"*

Without the ontology:
- Data is tables with columns
- Every app re-implements the same logic
- No cross-app sharing of logic

With the ontology:
- Data is **Soldiers**, **Vehicles**, **Missions**
- Logic lives in one place (computed properties, functions)
- Every app speaks the same language

### Object Type — The Blueprint

An Object Type defines a class of real-world things. It has:
- **Primary key** — one column that uniquely identifies each object
- **Properties** — columns mapped from the backing dataset
- **Title property** — what shows in search results
- **Backing dataset** — the curated dataset it reads from

### Creating an Object Type (Step by Step)

1. Ontology Manager → Object Types → New Object Type
2. Name it (singular noun, PascalCase: `SoldierReport`, `UnitStatus`)
3. Set the backing dataset (your curated dataset)
4. Set the primary key column
5. Set the title property (the display name)
6. Add properties — map each column you want exposed
7. Publish to the ontology

### Properties

Each property has:
- **API name** — `camelCase`, used in code (`reportDate`, `unitId`)
- **Display name** — human readable ("Report Date", "Unit ID")
- **Type** — String, Integer, Long, Double, Boolean, Timestamp, GeoPoint, Attachment

**Do not** expose raw/internal columns as properties. Only expose what an app or analyst needs.

### Link Types — Connecting Objects

Link types define relationships between object types.

Example: A `Soldier` is assigned to a `Unit`

1. Ontology Manager → Link Types → New Link Type
2. Name the relationship ("assigned to")
3. Set Object Type A: `Soldier`
4. Set Object Type B: `Unit`
5. Set cardinality: Many-to-One (many Soldiers, one Unit)
6. Map the foreign key column

Link types are bidirectional — you get both directions automatically.

### Object Sets

An Object Set is a saved, filtered group of objects.

- Created in **Object Explorer** or **Workshop**
- Can be static (pinned objects) or dynamic (filter rule)
- Used as inputs to Workshop widgets, functions, AIP agents

### Computed Properties

A property whose value is **calculated**, not stored.

Use when:
- The value depends on multiple columns
- The value changes based on time
- You need to call an external Function

Example: `daysSinceLastReport` = `TODAY - lastReportDate`

Configured in Ontology Manager → Object Type → Properties → Add Computed Property.

### Ontology Branching

Like datasets, the ontology supports branches.

- **Production ontology** = what live apps use
- **Staging/dev ontology** = where you build and test
- **Always develop on a branch.** Merge to production through a PR.

**Mistakes on the production ontology break live apps.**

---

## CHAPTER 7 — WORKSHOP: BUILDING UIs

### What Workshop Is

Workshop is Foundry's drag-and-drop app builder. You arrange widgets on a canvas, connect them to the ontology, and configure interactions. No frontend coding required for basic apps.

### Workshop Concepts

| Term | Meaning |
|------|---------|
| **Module** | One page/screen of your app |
| **Widget** | A UI component (table, chart, map, button) |
| **Variable** | A stored value that widgets share (like a selected filter) |
| **Event** | An action triggered by user interaction |
| **Object Set** | The data source for most widgets |

### Basic App Structure

```
App
├── Module: Overview
│   ├── Filter Panel (input widget)
│   ├── Object Table (data widget)
│   └── Summary Card (display widget)
├── Module: Detail View
│   └── Object Detail (shows one object's properties)
└── Module: Map View
    └── Map Widget (GeoPoint objects)
```

### Step-by-Step: Build a Basic App

1. Workshop → New Application
2. Name it, choose your ontology
3. New Module → name it
4. Drag in an **Object Table** widget
5. Set its Object Type
6. Add columns (properties to display)
7. Add a **Search Box** widget — link it to the table
8. Add a **Filter Panel** — select filterable properties
9. Publish

### Common Widgets

| Widget | Use |
|--------|-----|
| Object Table | Display multiple objects in rows |
| Object Detail | Show all properties of one selected object |
| Chart (Bar/Line/Pie) | Aggregate stats |
| Map | GeoPoint objects on a map |
| Metric Tile | Big number display |
| Dropdown/Search | Filter inputs |
| Button | Trigger an Action |
| Markdown | Static text, instructions |
| Conditional Formatting | Color rows/cells by value |

### Variables — The Key to Interactivity

Variables make widgets talk to each other.

Example: User clicks a row in a table → detail panel updates.

1. Create a variable: `selectedSoldier` (type: Object — `Soldier`)
2. Table widget → Events → On Row Click → Set Variable `selectedSoldier` = clicked object
3. Detail widget → Data Source = `selectedSoldier`

Now clicking a row updates the detail panel.

### Linking Modules

Button widget → Events → On Click → Navigate to Module → pass selected object as parameter.

---

## CHAPTER 8 — ACTIONS & WRITE-BACK

### What Actions Are

Actions let users **change data** from inside a Workshop app. A user fills out a form, clicks Submit, and data writes back to the ontology.

### Action Types

Defined in Ontology Manager → Action Types.

Three kinds:
- **Create Object** — creates a new object instance
- **Modify Object** — edits an existing object's properties
- **Delete Object** — removes an object

### Creating an Action Type (Step by Step)

1. Ontology Manager → Action Types → New
2. Choose: Create / Modify / Delete
3. Select the Object Type it acts on
4. Define **Parameters** — the form fields the user fills in
5. Define **Logic** — which parameters map to which properties
6. Set **Validation Rules** — optional, but recommended
7. Set **Permissions** — who can run this action
8. Publish

### Using Actions in Workshop

1. Add a **Button** widget
2. Button → Configure → Action → select your Action Type
3. Map parameters to variables or fixed values
4. The button now triggers the action when clicked

### Form-Based Actions

For more complex input, use an **Action Form** widget instead of a button.
- Auto-generates form fields from Action Type parameters
- Built-in validation display
- Submit button included

### Validation Rules

Always add validation. Example rules:
- Required field: `reportDate` must not be null
- Range check: `confidence` must be between 0 and 100
- Conditional: if `status == "COMPLETE"`, then `completedBy` is required

---

## CHAPTER 9 — FUNCTIONS & COMPUTED PROPERTIES

### What Functions Are

Functions are TypeScript code that runs against the ontology. They enable:
- Complex computed properties
- Custom aggregations
- Logic that PySpark can't do at the ontology layer

### When to Use Functions vs Transforms

| Use Transform | Use Function |
|---------------|--------------|
| Data cleaning/ETL | Per-object calculations |
| Large-scale aggregation | Logic needing related objects |
| Schedule-based processing | Real-time computed values |
| Schema changes | Action-side effects |

### Function Repository Structure

```
my-functions/
├── src/
│   └── index.ts       ← your functions go here
├── package.json
└── tsconfig.json
```

### Basic Function Example

```typescript
import { Function, Integer, ObjectSet } from "@foundry/functions-api";
import { Objects, SoldierReport } from "@foundry/ontology-api";

export class MyFunctions {
  @Function()
  async countActiveReports(reports: ObjectSet<SoldierReport>): Promise<Integer> {
    const active = reports.filter(r => r.status === "ACTIVE");
    return (await active.all()).length;
  }
}
```

### Attaching a Function to an Object Type

1. Ontology Manager → Object Type → Properties → Add Property
2. Type: Function-Backed Property
3. Select your function repository and function
4. Map parameters
5. The property now appears as a computed value on every object

---

## CHAPTER 10 — AIP & AI INTEGRATION

### What AIP Is

AIP (AI Platform) is Foundry's AI layer. It connects LLMs (including approved DoD models) to your ontology data. Users can query objects in natural language. Developers can build AI-powered workflows.

### AIP Components

| Component | What It Does |
|-----------|-------------|
| **AIP Logic** | Define rules/automations on object events |
| **AIP Agent Studio** | Build conversational AI agents |
| **AIP Assist** | In-app AI copilot for users |
| **Palantir AI** | Underlying LLM access (GPT-4, approved models) |

### AIP Logic — Event-Driven Automation

Trigger: object property changes
Action: run a function, update a property, notify a user

Example: When `SoldierReport.status` changes to `"CRITICAL"` → automatically create a `NotificationObject` and set `priority = HIGH`.

### AIP Agent Studio — Building Agents

An AIP Agent:
1. Has access to **tools** (ontology queries, functions, actions)
2. Receives natural language input from a user
3. Reasons about which tools to call
4. Returns a response

Building an agent:
1. AIP Agent Studio → New Agent
2. Write a **system prompt** — tell the agent what it does and what it can access
3. Add **tools** — attach ontology object types, functions, action types
4. Test in the playground
5. Embed in Workshop with the Agent Widget

### System Prompt Best Practices

```
You are a SITREP assistant for USAREUR-AF. You help analysts query
and summarize unit status reports.

You have access to:
- UnitStatus objects: current operational status of units
- SoldierReport objects: individual soldier readiness reports
- UpdateStatus action: to update a unit's status

Always respond concisely. Use military time format.
Never speculate about data you cannot query.
```

### Security Note on AIP

- Only approved models run inside the Maven boundary
- Data never leaves the enclave when using approved models
- Do not connect AIP agents to external APIs without authorization
- Check with your data owner before giving an agent write (action) access

---

## CHAPTER 11 — PERMISSIONS & MARKINGS

### How Access Control Works in Foundry

Foundry has two layers of access control:

**1. Role-Based (Compass/Resource level)**
- Who can see/edit a dataset, repo, or app
- Set on each resource in Compass
- Roles: Viewer, Editor, Owner

**2. Markings (Data-level)**
- Row-level and column-level security on ontology objects
- Objects with a marking are invisible to users without that marking
- Applied to Object Types, not datasets

### Roles

| Role | Can Do |
|------|--------|
| Viewer | Read data, use apps |
| Editor | Modify code, transforms, configs |
| Owner | Grant permissions, delete resources |
| Developer | Specific to Code Repositories |

### Markings — Critical for Operational Data

A Marking is a label that restricts who sees what.

Common patterns in Army/Maven:
- Classification markings (UNCLASS, CUI, etc.)
- AOR-based markings (only EUCOM users see EUCOM data)
- Role-based markings (only S2 sees intel objects)

**You do not set markings — data owners do.** Your job as a developer:
- Ensure your transforms preserve markings from source datasets
- Do not denormalize or join data across marking boundaries without authorization
- If your output dataset needs a marking, request it from the data steward

### Developer Permissions Needed

To develop in Foundry, you typically need:
- Editor on your team's project folder
- Editor on the ontology branch you're working on
- Developer on Code Repositories
- Viewer on source datasets

Request through your team lead or Foundry admin.

---

## CHAPTER 12 — BUILD SYSTEM & CI

### How Builds Work

When you push code to a Code Repository, Foundry:
1. Detects the change
2. Triggers configured **Checks** (tests, linting)
3. If checks pass → triggers **Builds** (runs transforms)
4. Output datasets are updated

### Checks

Checks run before a build succeeds. Configure in `pipeline-spec.yml`:

```yaml
checks:
  - type: python_unit_tests
    target: transforms-python
```

Write tests alongside your transforms:

```python
# tests/test_my_transform.py
import pytest
from pyspark.sql import SparkSession

def test_filter_removes_nulls(spark):
    data = [("A", None), ("B", "ACTIVE"), ("C", "ACTIVE")]
    df = spark.createDataFrame(data, ["id", "status"])
    result = filter_nulls(df)
    assert result.count() == 2
```

### Build Orchestration

Transforms have dependencies. Foundry builds the graph automatically:

```
raw_dataset → staging_transform → staging_dataset → curated_transform → curated_dataset
```

If `staging_transform` changes, only it and downstream transforms rebuild.

### Branch Strategy (Recommended)

```
master (production)
  └── dev (integration)
        └── feature/your-feature (your work)
```

1. Branch off `dev`
2. Make changes, build, test
3. PR → `dev`, team review
4. When `dev` is stable → PR → `master`
5. `master` builds trigger production updates

### Never break master.

---

## CHAPTER 13 — MAVEN-SPECIFIC PATTERNS

### Naming Conventions

Follow these or you'll confuse your team.

**Datasets:**
```
/Project/AOR/source_name/raw          ← raw ingest
/Project/AOR/source_name/staging      ← cleaned
/Project/AOR/source_name/curated      ← ontology-ready
```

**Object Types:** PascalCase singular noun — `UnitStatus`, `SoldierReadiness`

**Code Repos:** `kebab-case` — `unit-status-transforms`, `sitrep-functions`

**Transforms:** `snake_case` function names — `raw_to_staging`, `compute_readiness_score`

### DTG (Date-Time Group) Handling

Always store DTGs as `TimestampType` in Spark, not strings.

```python
from pyspark.sql import functions as F

# Parse DTG string to timestamp
df.withColumn(
    "dtg_ts",
    F.to_timestamp(F.col("dtg_string"), "ddHHmm'Z' MMM yy")
)
```

Always store in UTC. Display conversion happens at the app layer.

### SITREP Pipeline Pattern

```
[Source SITREP Feed]
        ↓
[Raw Dataset]           ← store exactly what came in, no changes
        ↓
[Staging Dataset]       ← standardize fields, parse DTG, validate required fields
        ↓
[Curated Dataset]       ← one row per latest SITREP per unit
        ↓
[UnitStatus Object]     ← ontology object
        ↓
[Workshop SITREP App]   ← analysts use this
```

### Idempotent Ingestion

If your pipeline runs twice on the same data, the output should be identical.

```python
# Use a unique key + INSERT OR IGNORE pattern
# In Spark: deduplicate on write

df_deduped = df.dropDuplicates(["report_id"])
output.write_dataframe(df_deduped)
```

### Handling Late Arrivals

Operational data arrives late. Design for it:
- Use `received_at` (when Foundry got it) AND `report_dtg` (when the event happened)
- Design aggregations on `report_dtg`, not `received_at`
- Use incremental transforms with event-time watermarking for streaming

### Common Mistakes (Don't Do These)

| Mistake | Why It's Bad | Fix |
|---------|-------------|-----|
| Reading from raw dataset in Workshop | Raw data is dirty/unstable | Always go through staging → curated |
| Hardcoding file paths | Breaks on environment change | Use Input/Output decorators |
| F-string SQL queries | SQL injection risk | Use PySpark API or parameterized queries |
| Modifying production ontology directly | Breaks live apps | Always use a branch |
| Storing credentials in code | Security violation | Use environment variables |
| Giant single transform | Impossible to debug | Break into stages |
| No schema on output dataset | Downstream breaks silently | Enforce schema with `StructType` |

---

## QUICK REFERENCE GLOSSARY

| Term | Definition |
|------|-----------|
| **AIP** | AI Platform — Foundry's LLM/agent layer |
| **Action** | User-triggered data write-back |
| **Action Type** | The template defining an action |
| **Backing Dataset** | The dataset an Object Type reads from |
| **Branch** | A versioned copy of a dataset or ontology |
| **Build** | Foundry running a transform to produce output |
| **Check** | Automated test that runs before a build completes |
| **Compass** | Foundry's file/resource explorer |
| **Computed Property** | An Object property calculated by code, not stored |
| **Curated Dataset** | Clean, ontology-ready dataset |
| **Dataset** | A managed table in Foundry |
| **DTG** | Date-Time Group — military timestamp format |
| **Function** | TypeScript code that runs against the ontology |
| **Function Repository** | Code repo containing TypeScript functions |
| **Incremental Transform** | Transform that only processes new/changed data |
| **Lightweight Transform** | Small-compute transform (pandas, not Spark) |
| **Link Type** | Defined relationship between two Object Types |
| **Marking** | Data-level access control label |
| **Module** | One screen/page in a Workshop app |
| **Object** | One instance of an Object Type |
| **Object Set** | A filtered group of objects |
| **Object Type** | The blueprint for a real-world thing in the ontology |
| **Ontology** | Foundry's semantic model — what data *means* |
| **Ontology Manager** | UI for defining Object Types, Links, Actions |
| **Pipeline Builder** | Visual ETL tool (no-code alternative to transforms) |
| **Primary Key** | The column that uniquely identifies each object |
| **Property** | An attribute of an Object Type |
| **RID** | Resource Identifier — unique permanent ID for any Foundry resource |
| **Raw Dataset** | Unmodified data exactly as ingested |
| **Schema** | Column names and types for a dataset |
| **Spark** | Distributed compute engine that runs transforms |
| **Staging Dataset** | Cleaned and validated data, not yet ontology-ready |
| **Transaction** | A versioned write to a dataset |
| **Transform** | Code that reads datasets and produces new datasets |
| **Variable** | Shared value between Workshop widgets |
| **Workshop** | Foundry's drag-and-drop app builder |

---

## APPENDIX A — TRANSFORM TEMPLATE (COPY-PASTE READY)

```python
"""
Transform: raw_to_staging
Purpose: Clean and standardize [SOURCE] data for ontology ingestion
Input:  /Project/AOR/source/raw
Output: /Project/AOR/source/staging
"""

from transforms.api import transform_df, Input, Output
import pyspark.sql.functions as F
from pyspark.sql.types import TimestampType, StringType


@transform_df(
    Output("/Project/AOR/source/staging"),
    source=Input("/Project/AOR/source/raw"),
)
def compute(source):
    df = source

    # 1. Drop duplicates on primary key
    df = df.dropDuplicates(["primary_key_column"])

    # 2. Filter required fields
    df = df.filter(
        F.col("required_field_1").isNotNull() &
        F.col("required_field_2").isNotNull()
    )

    # 3. Standardize types
    df = df.withColumn("dtg", F.col("dtg_raw").cast(TimestampType()))
    df = df.withColumn("status", F.upper(F.trim(F.col("status"))))

    # 4. Add metadata
    df = df.withColumn("_processed_at", F.current_timestamp())

    return df
```

---

## APPENDIX B — CHECKLIST: READY FOR PRODUCTION?

Before you merge to master and push to production:

- [ ] Transform builds cleanly with no warnings
- [ ] Unit tests written and passing
- [ ] Output dataset schema is documented
- [ ] No hardcoded paths, credentials, or magic numbers
- [ ] Incremental transform used where data grows over time
- [ ] Source datasets are curated tier (not raw)
- [ ] Object Type backed by curated dataset only
- [ ] Markings preserved from source to output
- [ ] Actions have validation rules
- [ ] App tested by at least one non-developer user
- [ ] Naming conventions followed
- [ ] README updated in the code repo
- [ ] Branch merged via PR with reviewer approval
- [ ] Data owner notified of schema changes

---

*Maven Field Manual v1.0 — USAREUR-AF Operational Data Team*
*UNCLASSIFIED — For internal training use*
