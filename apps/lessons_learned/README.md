# Lessons Learned Pipeline

Structured lessons-learned pipeline with full tagging taxonomy aligned to the TM-40K Knowledge Manager syllabus. Goes beyond WFF-level roll-up to implement cross-cutting analysis by TTP category, echelon, classification level, and doctrine reference.

## Quick Start

```bash
# From repo root

# 1. Seed demo data (~40 lessons, ~25 action items, ~30 comments)
python -m apps.lessons_learned.seed

# 2. Start API (port 8014)
uvicorn apps.lessons_learned.api:app --reload --port 8014

# 3. Start dashboard (port 8514) — in a separate terminal
streamlit run apps/lessons_learned/dashboard.py --server.port 8514
```

## API Docs

With the API running: http://localhost:8014/docs

## Dashboard Tabs

1. **Pipeline Overview** — KPIs, status funnel, priority and source type breakdowns
2. **Tag Analysis** — frequency charts per tag type with drill-down to associated lessons
3. **Cross-Reference Matrix** — co-occurrence heatmap between any two tag types
4. **Action Tracker** — open action items with due dates and RAG overdue indicators
5. **Lesson Browser** — searchable, filterable table with detail view
6. **Trend Analysis** — monthly submissions stacked by source type

## Tag Taxonomy

| Tag Type | Examples |
|---|---|
| TTP_CATEGORY | Data Collection, Visualization, Analysis, Quality Control |
| ECHELON | Squad, Battalion, Brigade, Division, Theater |
| WFF | Intelligence, Fires, Movement & Maneuver, Sustainment |
| DOCTRINE_REF | ADP 6-0, ADP 2-0, ATP 2-01.3 |
| COURSE_ID | TM-40G, TM-40H, TM-40K |
| KEYWORD | Free-text keywords |

## Notes

- The `.db` file is gitignored and never committed
- Tagging taxonomy follows TM-40K Knowledge Manager syllabus structure
- Cross-reference analysis enables identification of systemic patterns across WFF and TTP boundaries
