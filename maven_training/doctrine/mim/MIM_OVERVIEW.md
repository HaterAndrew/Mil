<!-- MAVEN TRAINING CORPUS — CDA REFERENCE MATERIAL
     Source: odt_workspace/docs/architecture/mim/overview.md
     Supports: TM-40H (AI Engineer), TM-40M (ML Engineer), TM-40K (Knowledge Manager), TM-40L (Software Engineer), TM-50H/I/K/L (Advanced)
     Type: Architecture Reference — MIM Toolchain Overview
-->

# MIM — MIP Information Model Toolchain

A Python monorepo that parses, models, and generates code from NATO's MIP Information Model (MIM) 5.3 specification.

---

## Data Sources

Two parsers, each suited to different use cases:

| Source | Classes | Enumerations | Literals |
|--------|---------|--------------|----------|
| HTML Export | 1,208 | 522 | 6,717 |
| XSD Schemas | 1,127 | 499 | 5,235 |

### HTML Export Parser (recommended)

Parses the Enterprise Architect HTML export. Preserves the full EA metamodel including association roles, primitive types, and original stereotypes.

```python
import mim.portal as portal

files = portal.get_files("5.3")          # download / cache the 5.3 release
model = portal.parse.parse_html(files)   # returns a MIMModel
```

### XSD Schema Parser

Parses the XSD schema files. Use for exchange-schema compliance where inheritance is flattened and attribute names are class-prefixed.

```python
from mim.portal.parse.xsd import parse_xsd_directory

model = parse_xsd_directory("data/model_version_5_3/xsd")
```

### Key Differences

| Aspect | HTML Parser | XSD Parser |
|--------|-------------|------------|
| Inheritance | Preserved hierarchy | Flattened (includes inherited attrs) |
| Stereotypes | EA stereotypes (`cls`, `dataType`) | Schema annotations (`Abstract`) |
| Attribute naming | Short names (`bearingAngle`) | Prefixed (`ActionBearingAngle`) |
| Use case | Complete model fidelity | Exchange schema compliance |

---

## Repository Structure

`uv` workspace monorepo. Active packages are **bold**.

| Directory | Description | Status |
|-----------|-------------|--------|
| **`mim-ir/`** | Canonical IR types — `MIMModel`, `MIMClass`, `MIMEnumeration`, etc. | **89 tests passing** |
| **`mim-portal/`** | HTML & XSD parsers, MIM portal client, model download | **106 tests passing** |
| **`mim-backends/mim-backend-foundry/`** | Palantir Foundry ontology code generation | **Active** |
| `mim-backends/mim-backend-sql/` | SQL DDL generation from MIM IR | Active |
| `mim-backends/mim-backend-*` | Future backends (OpenAPI, JSON Schema, Python, TS) | Planned |
| **`shared/mim-kernel/`** | Shared primitives: IDs, errors, time utilities | **42 tests passing** |
| `shared/mim-provenance/` | Provenance & lineage tracking | Planned |
| `shared/mim-testing/` | Shared test fixtures and helpers | Active |
| `mim-adapters/` | Data-pipeline adapters (Foundry, S3, Kafka, REST, …) | Planned |
| `apps/mim-viewer/` | React model browser (Vite + JSX) | Active |
| `apps/mim-admin/` | FastAPI admin server + Vite client | Active |
| `data/model_version_5_3/` | MIM 5.3 source data (HTML export, XSD, XMI) — Git LFS | Committed |

### Dependency Graph

```
shared/mim-kernel  (IDs, errors, time)
       ↑
     mim-ir        (Pydantic IR types)
       ↑
   mim-portal      (parsers, client)     →  notebooks, apps
       ↑
   mim-backends/*  (Foundry, SQL, …)
```

---

## Package Quick Reference

### `mim.ir` — Intermediate Representation

```python
from mim.ir import MIMModel, MIMClass, MIMEnumeration, MIMAttribute
from mim.ir import load_model, save_model, model_to_json

model = load_model("snapshot.json")
for cls in model.classes:
    print(cls.name, len(cls.attributes))
```

### `mim.portal` — Portal Client & Parsers

```python
import mim.portal as portal

versions = portal.get_versions()
files    = portal.get_files("5.3")

from mim.portal.parse.html import parse_html_export
model = parse_html_export("data/model_version_5_3/MIM 5.3 - HTML Export")
```

Environment variables (set in `.env`):

| Variable | Purpose |
|----------|---------|
| `MIM_PORTAL_USERNAME` | Portal login |
| `MIM_PORTAL_PASSWORD` | Portal password |
| `MIM_DEFAULT_VERSION` | Default version (e.g. `5.3`) |
| `MIM_CACHE_DIR` | Cache directory (default `~/.mim/cache`) |

### `mim.backend.foundry` — Foundry Code Generation

```python
from mim.ir import MIMModel
from mim.backend.foundry import MIMToFoundryConverter, MappingConfig

model: MIMModel = ...  # loaded via mim.portal
converter = MIMToFoundryConverter(MappingConfig())
result = converter.convert(model)
converter.write_output(Path("output/"))
```

### `mim.kernel` — Shared Primitives

```python
from mim.kernel import SemanticId, generate_stable_id, MIMError, ParseError
from mim.kernel import parse_ea_datetime, format_iso_datetime, utc_now
```

---

## Related Documents

- [MIM_STANDARD.md](./MIM_STANDARD.md) — MIM semantic model, namespaces, roles, code types, design principles
- [MIM_STATE.md](./MIM_STATE.md) — Project status snapshot (2026-02-28), maturity by area
- [MIM_ACADEMICS.md](./MIM_ACADEMICS.md) — Dr. Gerz, NATO interoperability, MIM→Foundry alignment analysis
- [MIM_DECISION_RECORDS.md](./MIM_DECISION_RECORDS.md) — ADR: repository ADR structure
- [MIM_FUTURE_CLASSES.md](./MIM_FUTURE_CLASSES.md) — Planned components: adapters, backends, studio, SDK
- [MIM_ONTOLOGY_DOCS.md](./MIM_ONTOLOGY_DOCS.md) — OSDK Maker Package TypeScript API reference
