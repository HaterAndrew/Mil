# MAVEN SMART SYSTEM — QUICK REFERENCE CARD
### USAREUR-AF Operational Data Team — Keep This Open While You Work

---

## WHERE TO GO FOR MORE

| Need | Publication |
|------|------------|
| Never used MSS before | [TM-10 — Maven User](../tm/TM_10_maven_user/TM_10_MAVEN_USER.md) |
| Building dashboards / basic pipelines | [TM-20 — Builder](../tm/TM_20_builder/TM_20_BUILDER.md) |
| Advanced transforms, ontology, AIP, OSDK | [TM-30 — Advanced Builder](../tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md) |
| Intelligence (INT) WFF staff | [TM-40A — Intelligence](../tm/TM_40A_intelligence/TM_40A_INTELLIGENCE.md) |
| Fires WFF staff | [TM-40B — Fires](../tm/TM_40B_fires/TM_40B_FIRES.md) |
| Movement & Maneuver (M2) WFF staff | [TM-40C — Movement & Maneuver](../tm/TM_40C_movement_maneuver/TM_40C_MOVEMENT_MANEUVER.md) |
| Sustainment WFF staff | [TM-40D — Sustainment](../tm/TM_40D_sustainment/TM_40D_SUSTAINMENT.md) |
| Protection WFF staff | [TM-40E — Protection](../tm/TM_40E_protection/TM_40E_PROTECTION.md) |
| Mission Command (MC) WFF staff | [TM-40F — Mission Command](../tm/TM_40F_mission_command/TM_40F_MISSION_COMMAND.md) |
| ORSA / quantitative analysis specialist | [TM-40G — ORSA](../tm/TM_40G_orsa/TM_40G_ORSA.md) |
| AI engineering / AIP Logic / Agents | [TM-40H — AI Engineer](../tm/TM_40H_ai_engineer/TM_40H_AI_ENGINEER.md) |
| ML model development and deployment | [TM-40I — ML Engineer](../tm/TM_40I_ml_engineer/TM_40I_ML_ENGINEER.md) |
| Technical program / project management | [TM-40J — Program Manager](../tm/TM_40J_program_manager/TM_40J_PROGRAM_MANAGER.md) |
| Knowledge management / AAR / lessons learned | [TM-40K — Knowledge Manager](../tm/TM_40K_knowledge_manager/TM_40K_KNOWLEDGE_MANAGER.md) |
| Software engineering / OSDK / external apps | [TM-40L — Software Engineer](../tm/TM_40L_software_engineer/TM_40L_SOFTWARE_ENGINEER.md) |
| Advanced specialist training (post-TM-40G–L) | [TM-50 Series Index](../README.md#tm-50gl----advanced-technical-specialist-tracks) |
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
  → TM-10: MAVEN USER (all staff)

Building dashboards, Workshop apps, or basic pipelines?
  → TM-20: BUILDER (all staff)

WFF functional staff (INT/FIRES/M2/SUST/PROT/MC)?
  → TM-40A through TM-40F (WFF tracks, after TM-30 — no coding required)
     Intelligence     → TM-40A
     Fires            → TM-40B
     Movement/Manvr   → TM-40C
     Sustainment      → TM-40D
     Protection       → TM-40E
     Mission Command  → TM-40F

17/25-series, S6, G6, G2, or operational data analyst?
  → TM-30: ADVANCED BUILDER (data-adjacent), then TM-40G–L

Technical specialist role? (after TM-30)
  → ORSA / quantitative analyst      → TM-40G / TM-50G
  → AI engineer / AIP Logic          → TM-40H / TM-50H
  → ML engineer / model development  → TM-40I / TM-50I
  → Program manager / pipeline PM    → TM-40J / TM-50J
  → Knowledge manager / IM officer   → TM-40K / TM-50K
  → Software engineer / OSDK/Python  → TM-40L / TM-50L

Completed TM-40G–L? → Take the corresponding TM-50G–L advanced track.
```

---

## PREREQUISITE CHAIN

```
TM-10 (no prereq) → TM-20 → TM-30 ─┬─ WFF Staff  → TM-40A through TM-40F
                                      │
                                      └─ Technical → TM-40G through TM-40L
                                                              ↓
                                                         TM-50G through TM-50L

All staff must complete TM-10 before any other TM.
WFF tracks (TM-40A–F): require TM-10 + TM-20 + TM-30. No coding required.
Technical tracks (TM-40G–L): require TM-30 (or demonstrated equivalent).
Advanced tracks (TM-50G–L): require corresponding TM-40G–L.
```

---

## COMMON TASK QUICK REFERENCE

| Task / Question | Go To |
|---|---|
| How do I log into Maven/MSS? | TM-10, Task 1-1 |
| How do I find and filter a dataset? | TM-10, Task 2-1 |
| How do I create a Workshop dashboard? | TM-20, Task 3-1 |
| How do I build a Pipeline Builder pipeline? | TM-20, Task 3-1 |
| How do I write a Python transform? | TM-30 / TM-40L |
| How do I create an Object Type in the Ontology? | TM-30 / TM-40L |
| How do I configure an Intelligence COP layer? | TM-40A |
| How do I display targeting and fires data on MSS? | TM-40B |
| How do I track unit positions and maneuver routes? | TM-40C |
| How do I view LOGSTAT and readiness data on MSS? | TM-40D |
| How do I configure force protection CCIRs? | TM-40E |
| How do I configure CCIRs and build a BUA product? | TM-40F |
| How do I build a statistical model for a commander product? | TM-40G |
| How do I deploy an AIP Logic workflow? | TM-40H |
| How do I train and validate an ML model in Foundry? | TM-40I |
| How do I track a data pipeline project in MSS? | TM-40J |
| How do I manage forms and lessons learned in MSS? | TM-40K |
| How do I use the OSDK in an external application? | TM-40L |
| How do I implement advanced Bayesian methods? | TM-50G |
| How do I build a multi-step AIP Agent? | TM-50H |
| How do I perform model validation for operational deployment? | TM-50I |
| How do I manage a portfolio of data products? | TM-50J |
| How do I build a federated knowledge taxonomy? | TM-50K |
| How do I architect a full OSDK application? | TM-50L |
