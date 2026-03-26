# MAVEN SMART SYSTEM — QUICK REFERENCE CARD
### USAREUR-AF Operational Data Team — Keep This Open While You Work

---

## WHERE TO GO FOR MORE

| Need | Publication |
|------|------------|
| Never used MSS before | [SL 1 — Maven User](../tm/TM_10_maven_user/TM_10_MAVEN_USER.md) |
| Building dashboards / basic pipelines | [SL 2 — Builder](../tm/TM_20_builder/TM_20_BUILDER.md) |
| Advanced transforms, ontology, AIP, OSDK | [SL 3 — Advanced Builder](../tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md) |
| Intelligence (INT) WFF staff | [SL 4A — Intelligence](../tm/TM_40A_intelligence/TM_40A_INTELLIGENCE.md) |
| Fires WFF staff | [SL 4B — Fires](../tm/TM_40B_fires/TM_40B_FIRES.md) |
| Movement & Maneuver (M2) WFF staff | [SL 4C — Movement & Maneuver](../tm/TM_40C_movement_maneuver/TM_40C_MOVEMENT_MANEUVER.md) |
| Sustainment WFF staff | [SL 4D — Sustainment](../tm/TM_40D_sustainment/TM_40D_SUSTAINMENT.md) |
| Protection WFF staff | [SL 4E — Protection](../tm/TM_40E_protection/TM_40E_PROTECTION.md) |
| Mission Command (MC) WFF staff | [SL 4F — Mission Command](../tm/TM_40F_mission_command/TM_40F_MISSION_COMMAND.md) |
| ORSA / quantitative analysis specialist | [SL 4G — ORSA](../tm/TM_40G_orsa/TM_40G_ORSA.md) |
| AI engineering / AIP Logic / Agents | [SL 4H — AI Engineer](../tm/TM_40H_ai_engineer/TM_40H_AI_ENGINEER.md) |
| ML model development and deployment | [SL 4M — ML Engineer](../tm/TM_40M_ml_engineer/TM_40M_ML_ENGINEER.md) |
| Technical program / project management | [SL 4J — Program Manager](../tm/TM_40J_program_manager/TM_40J_PROGRAM_MANAGER.md) |
| Knowledge management / AAR / lessons learned | [SL 4K — Knowledge Manager](../tm/TM_40K_knowledge_manager/TM_40K_KNOWLEDGE_MANAGER.md) |
| Software engineering / OSDK / external apps | [SL 4L — Software Engineer](../tm/TM_40L_software_engineer/TM_40L_SOFTWARE_ENGINEER.md) |
| Advanced specialist training (post-SL 4G–O) | [SL 5 Series Index](../README.md#tm-50go----advanced-technical-specialist-tracks) |
| Brief commanders / senior leaders | [Data Literacy for Senior Leaders](../doctrine/DATA_LITERACY_senior_leaders.md) |
| Comprehensive data concepts reference | [Data Literacy Technical Reference](../doctrine/DATA_LITERACY_technical_reference.md) |
| What does this term mean? | [Glossary — Data & Foundry](../doctrine/GLOSSARY_data_foundry.md) |

---

## THE STACK (READ BOTTOM TO TOP)

```
Workshop App / AIP Agent
        ↑
   Ontology (Objects, Links, Actions)
        ↑
   Curated Dataset
        ↑
   Staging Dataset
        ↑
   Raw Dataset (never touch)
```

---

## TRANSFORM SKELETON

```python
from transforms.api import transform_df, Input, Output
import pyspark.sql.functions as F

@transform_df(
    Output("/path/output"),
    source=Input("/path/input"),
)
def compute(source):
    return source.filter(F.col("field").isNotNull())
```

---

## COMMON PYSPARK

```python
# Filter          df.filter(F.col("x") == "Y")
# Add column      df.withColumn("new", F.upper(F.col("old")))
# Rename          df.withColumnRenamed("old", "new")
# Drop dupes      df.dropDuplicates(["id"])
# Join            df1.join(df2, "id", "left")
# Group/count     df.groupBy("unit").agg(F.count("*").alias("n"))
# Cast            df.withColumn("x", F.col("x").cast("integer"))
# Null fill       df.fillna({"col": "DEFAULT"})
# Timestamp now   F.current_timestamp()
# Date parse      F.to_timestamp(F.col("s"), "yyyy-MM-dd HH:mm:ss")
```

---

## DECORATOR QUICK PICK

| Data size | Needs history | Use |
|-----------|--------------|-----|
| Large | No | `@transform_df` |
| Large | Yes (append only) | `@incremental` |
| Small | No | `@lightweight_transform` |

---

## ONTOLOGY SETUP ORDER

1. Build curated dataset
2. Create Object Type → set primary key
3. Map properties
4. Create Link Types
5. Add Computed Properties (optional)
6. Test in Object Explorer

---

## WORKSHOP WIDGET PICK

| Need | Widget |
|------|--------|
| Show many objects | Object Table |
| Show one object | Object Detail |
| Filter input | Filter Panel / Dropdown |
| Chart | Bar / Line / Pie Chart |
| Map | Map Widget |
| Write data | Button + Action / Action Form |
| Big number | Metric Tile |

---

## NAMING QUICK RULES

- Datasets: `/Project/AOR/source/raw|staging|curated`
- Object Types: `PascalCase` (`UnitStatus`)
- Code Repos: `kebab-case` (`unit-status-transforms`)
- Functions/Transforms: `snake_case` (`raw_to_staging`)
- Properties: `camelCase` API name, "Title Case" display name

---

## PERMISSIONS I NEED (ask team lead)

- [ ] Editor on project folder
- [ ] Editor on ontology branch
- [ ] Developer on Code Repos
- [ ] Viewer on source datasets

---

## IF SOMETHING IS BROKEN

1. **Build fails** → read the full error, find "Caused by:"
2. **Empty output** → check your filters, add `.count()` to debug
3. **Schema mismatch** → delete output dataset, rebuild
4. **App not showing objects** → check ontology branch is correct
5. **Object not searchable** → check primary key is set and unique
6. **Action fails** → check validation rules and user permissions

---

## WHICH TM DO I NEED?

```
Viewing data and dashboards only?
  → SL 1: MAVEN USER (all staff)

Building dashboards, Workshop apps, or basic pipelines?
  → SL 2: BUILDER (all staff)

WFF functional staff (INT/FIRES/M2/SUST/PROT/MC)?
  → SL 4A through SL 4F (WFF tracks, after SL 3 — no coding required)
     Intelligence     → SL 4A
     Fires            → SL 4B
     Movement/Manvr   → SL 4C
     Sustainment      → SL 4D
     Protection       → SL 4E
     Mission Command  → SL 4F

17/25-series, S6, G6, G2, or operational data analyst?
  → SL 3: ADVANCED BUILDER (data-adjacent), then SL 4G–O

Technical specialist role? (after SL 3)
  → ORSA / quantitative analyst      → SL 4G / SL 5G
  → AI engineer / AIP Logic          → SL 4H / SL 5H
  → ML engineer / model development  → SL 4M / SL 5M
  → Program manager / pipeline PM    → SL 4J / SL 5J
  → Knowledge manager / IM officer   → SL 4K / SL 5K
  → Software engineer / OSDK/Python  → SL 4L / SL 5L

Completed SL 4G–O? → Take the corresponding SL 5G–O advanced track.
```

---

## PREREQUISITE CHAIN

```
SL 1 (no prereq) → SL 2 → SL 3 ─┬─ WFF Staff  → SL 4A through SL 4F
                                      │
                                      └─ Technical → SL 4G through SL 4O
                                                              ↓
                                                         SL 5G through SL 5O

All staff must complete SL 1 before any other TM.
WFF tracks (SL 4A–F): require SL 1 + SL 2 + SL 3. No coding required.
Technical tracks (SL 4G–O): require SL 3 (or demonstrated equivalent).
Advanced tracks (SL 5G–O): require corresponding SL 4G–O.
```

---

## COMMON TASK QUICK REFERENCE

| Task / Question | Go To |
|---|---|
| How do I log into Maven/MSS? | SL 1, Task 1-1 |
| How do I find and filter a dataset? | SL 1, Task 2-1 |
| How do I create a Workshop dashboard? | SL 2, Task 3-1 |
| How do I build a Pipeline Builder pipeline? | SL 2, Task 3-1 |
| How do I write a Python transform? | SL 3 / SL 4L |
| How do I create an Object Type in the Ontology? | SL 3 / SL 4L |
| How do I configure an Intelligence COP layer? | SL 4A |
| How do I display targeting and fires data on MSS? | SL 4B |
| How do I track unit positions and maneuver routes? | SL 4C |
| How do I view LOGSTAT and readiness data on MSS? | SL 4D |
| How do I configure force protection CCIRs? | SL 4E |
| How do I configure CCIRs and build a BUA product? | SL 4F |
| How do I build a statistical model for a commander product? | SL 4G |
| How do I deploy an AIP Logic workflow? | SL 4H |
| How do I train and validate an ML model in Foundry? | SL 4M |
| How do I track a data pipeline project in MSS? | SL 4J |
| How do I manage forms and lessons learned in MSS? | SL 4K |
| How do I use the OSDK in an external application? | SL 4L |
| How do I implement advanced Bayesian methods? | SL 5G |
| How do I build a multi-step AIP Agent? | SL 5H |
| How do I perform model validation for operational deployment? | SL 5M |
| How do I manage a portfolio of data products? | SL 5J |
| How do I build a federated knowledge taxonomy? | SL 5K |
| How do I architect a full OSDK application? | SL 5L |
