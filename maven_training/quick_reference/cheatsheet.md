# MAVEN SMART SYSTEM — QUICK REFERENCE CARD
### USAREUR-AF Operational Data Team — Keep This Open While You Work

---

## WHERE TO GO FOR MORE

| Need | Publication |
|------|------------|
| Never used MSS before | [TM-10 — Maven User](../tm/TM_10_maven_user/TM_10_MAVEN_USER.md) |
| Building dashboards / basic pipelines | [TM-20 — Builder](../tm/TM_20_builder/TM_20_BUILDER.md) |
| Advanced transforms, ontology, AIP, OSDK | [TM-30 — Advanced Builder](../tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md) |
| Brief commanders / senior leaders | [ADP 1 — Senior Leaders](../doctrine/ADP_1_data_literacy_senior.md) |
| Comprehensive data concepts reference | [ADRP 1 — Data Literacy](../doctrine/ADRP_1_data_literacy.md) |
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
