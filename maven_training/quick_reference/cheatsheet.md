# MAVEN SMART SYSTEM — QUICK REFERENCE CARD
### USAREUR-AF Operational Data Team — Keep This Open While You Work

---

## WHERE TO GO FOR MORE

| Need | Publication |
|------|------------|
| Never used MSS before | [TM-10 — Maven User](../tm/TM_10_maven_user/TM_10_MAVEN_USER.md) |
| Building dashboards / basic pipelines | [TM-20 — Builder](../tm/TM_20_builder/TM_20_BUILDER.md) |
| Advanced transforms, ontology, AIP, OSDK | [TM-30 — Advanced Builder](../tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md) |
| ORSA / quantitative analysis specialist | [TM-40A — ORSA](../tm/TM_40A_orsa/TM_40A_ORSA.md) |
| AI engineering / AIP Logic / Agents | [TM-40B — AI Engineer](../tm/TM_40B_ai_engineer/TM_40B_AI_ENGINEER.md) |
| ML model development and deployment | [TM-40C — ML Engineer](../tm/TM_40C_ml_engineer/TM_40C_ML_ENGINEER.md) |
| Technical program / project management | [TM-40D — Program Manager](../tm/TM_40D_program_manager/TM_40D_PROGRAM_MANAGER.md) |
| Knowledge management / AAR / lessons learned | [TM-40E — Knowledge Manager](../tm/TM_40E_knowledge_manager/TM_40E_KNOWLEDGE_MANAGER.md) |
| Software engineering / OSDK / external apps | [TM-40F — Software Engineer](../tm/TM_40F_software_engineer/TM_40F_SOFTWARE_ENGINEER.md) |
| Advanced specialist training (post-TM-40) | [TM-50 Series Index](../README.md#tm-50-series----advanced-specialist-tracks) |
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
Am I using Maven to view data and dashboards only?
  → TM-10: MAVEN USER (all staff)

Am I building dashboards, Workshop apps, or basic pipelines?
  → TM-20: BUILDER (all staff)

Am I from 17/25-series, S6, G6, G2, G9, or an operational data analyst?
  → TM-30: ADVANCED BUILDER (data-adjacent)

What is my specialist role?
  → ORSA / quantitative analyst      → TM-40A / TM-50A (ORSA)
  → AI engineer / AIP Logic          → TM-40B / TM-50B (AI Engineer)
  → ML engineer / model development  → TM-40C / TM-50C (ML Engineer)
  → Program manager / pipeline PM    → TM-40D / TM-50D (Program Manager)
  → Knowledge manager / IM officer   → TM-40E / TM-50E (Knowledge Manager)
  → Software engineer / OSDK/Python  → TM-40F / TM-50F (Software Engineer)

Already completed TM-40? → Take the corresponding TM-50 advanced track.
```

---

## PREREQUISITE CHAIN

```
TM-10 (no prereq) → TM-20 → TM-30 → TM-40[A-F] → TM-50[A-F]

All staff must complete TM-10 before any other TM.
TM-40/50 require TM-30 (or demonstrated equivalent).
TM-50 requires TM-40 in the same specialist track.
```

---

## COMMON TASK QUICK REFERENCE

| Task / Question | Go To |
|---|---|
| How do I log into Maven/MSS? | TM-10, Task 1-1 |
| How do I find and filter a dataset? | TM-10, Task 2-1 |
| How do I create a Workshop dashboard? | TM-20, Task 3-1 |
| How do I build a Pipeline Builder pipeline? | TM-20, Task 3-1 |
| How do I write a Python transform? | TM-30 / TM-40F |
| How do I create an Object Type in the Ontology? | TM-30 / TM-40F |
| How do I build a statistical model for a commander product? | TM-40A |
| How do I deploy an AIP Logic workflow? | TM-40B |
| How do I train and validate an ML model in Foundry? | TM-40C |
| How do I track a data pipeline project in MSS? | TM-40D |
| How do I manage forms and lessons learned in MSS? | TM-40E |
| How do I use the OSDK in an external application? | TM-40F |
| How do I implement advanced Bayesian methods? | TM-50A |
| How do I build a multi-step AIP Agent? | TM-50B |
| How do I perform model validation for operational deployment? | TM-50C |
| How do I manage a portfolio of data products? | TM-50D |
| How do I build a federated knowledge taxonomy? | TM-50E |
| How do I architect a full OSDK application? | TM-50F |
