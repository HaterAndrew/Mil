# Glossary Search

Full-text search across all glossary terms, doctrine documents, and training
material definitions in the USAREUR-AF maven_training corpus.

## Ports

| Service   | Port |
|-----------|------|
| Dashboard | 8507 |
| API       | 8007 |

## Quick Start

```bash
# From repo root

# 1. Seed the database (indexes markdown files or loads sample terms)
python -m apps.glossary_search.seed

# 2. Start the API
uvicorn apps.glossary_search.api:app --port 8007 --reload

# 3. Start the dashboard (separate terminal)
streamlit run apps/glossary_search/dashboard.py --server.port 8507
```

## Source Documents

The indexer parses these markdown files from `maven_training/`:

- `doctrine/GLOSSARY_data_foundry.md` — primary glossary (200+ terms)
- `doctrine/DATA_LITERACY_technical_reference.md` — technical data concepts
- `doctrine/DATA_LITERACY_senior_leaders.md` — senior leader orientation terms
- `doctrine/CDA_CONSTRAINTS_AND_DIRECTIVES.md` — architectural constraints
- `doctrine/CG_GUIDANCE.md` — CG directives and themes
- `doctrine/ONTOLOGY_DESIGN_PRINCIPLES.md` — ontology design terms
- `quick_reference/cheatsheet.md` — quick reference definitions
- Additional `.md` files in `doctrine/` and `quick_reference/` subdirectories

## API Endpoints

| Method | Path           | Description                     |
|--------|----------------|---------------------------------|
| GET    | /health        | Health check                    |
| GET    | /search        | Full-text search (q, category, limit) |
| GET    | /terms         | List all terms (paginated)      |
| GET    | /terms/{id}    | Single term by ID               |
| GET    | /categories    | List categories with counts     |
| POST   | /reindex       | Rebuild index from source files |
| GET    | /stats         | Index statistics                |

## Term Categories

- **GLOSSARY** — Data/platform terms from the primary glossary
- **DOCTRINE** — Terms from doctrinal and architectural guidance
- **ACRONYM** — Military and technical acronyms
- **CONCEPT** — General data science and engineering concepts

## Architecture

- **models.py** — Pydantic V2 request/response models
- **db.py** — SQLAlchemy ORM + markdown parser + search logic
- **api.py** — FastAPI REST endpoints
- **dashboard.py** — Streamlit UI with search, browse, stats, reindex
- **seed.py** — Initial database population (corpus or fallback samples)
