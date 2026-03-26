# CLAUDE.md — Maven Training Corpus & Apps

USAREUR-AF training content management system: course materials (MD → HTML/PDF/PPT), Streamlit micro-apps, and build/audit tooling.

## Commands

| Command | Description |
|---------|-------------|
| `python3 scripts/audit.py` | Run corpus audit against DEPENDENCY_MAP |
| `python3 scripts/deep_audit.py` | Extended audit with cross-reference checks |
| `python3 scripts/build_pdfs.py` | Rebuild all PDFs from source |
| `python3 scripts/generate_dep_map.py` | Regenerate dependency map (MD + HTML + PDF) |
| `python3 scripts/build_new_decks.py` | Build slide decks from templates |
| `streamlit run apps/portal.py` | Launch the Streamlit portal |

## Architecture

```
maven_training/          # Training content corpus
  mss_info_app/          #   MSS Training Hub (static HTML)
  mss_widget/            #   MSS Training Hub (React/TSX widget)
  pdf/                   #   Generated PDFs + manifest
  DEPENDENCY_MAP.md      #   Authoritative prereq cross-reference
apps/                    # Streamlit micro-apps
  portal.py              #   Main portal entry point
  curriculum_tracker/    #   Sub-app: curriculum tracking
  enrollment_manager/    #   Sub-app: enrollment management
  ...                    #   (each sub-app has models, api, dashboard, db, seed)
scripts/                 # Build, audit, and generation scripts
tests/                   # Test suite
skills/                  # Claude Code skills/plugins
sitrep_tracker/          # SITREP tracking tool
```

## Key Files

- `maven_training/DEPENDENCY_MAP.md` — authoritative prereq cross-reference (open first during audits)
- `apps/portal.py` — main Streamlit portal entry point
- `scripts/build_pdfs.py` — PDF generation pipeline
- `maven_training/pdf/.manifest.json` — PDF build manifest
- `maven_training/mss_info_app/index.html` — MSS Training Hub (HTML source of truth)
- `maven_training/mss_info_app/index_sharepoint.html` — SharePoint-targeted variant

## Code Style

- Python for all scripts and apps; parameterized SQL for queries
- Army Writing Style, BLUF framing for documentation
- Doctrine references use TCS framework (Training Circular System)
- Course codes follow pattern: `TM-{level}{track}` (e.g., TM-40M, TM-50G)

## Gotchas

- **Track letter I → M**: Letter I was retired because it looks like numeral 1. ML Engineer tracks are TM-40M/TM-50M, not TM-40I/TM-50I. Valid track letters: G–H, J–O.
- **"File X" = published output**: When user references a file by name, default to the rendered version (HTML/PDF/PPT/DOC). Only use markdown source if they explicitly say "markdown."
- **HTML-first update order**: Always update HTML first, then port to React/SharePoint. Never derive HTML from React. Do not mention React/SharePoint unless the user brings it up.
- **Dual maintenance**: Content changes to MSS Training Hub must go to BOTH `mss_info_app/index.html` (HTML) AND `mss_widget/src/panels/*.tsx` (React). Never update one without the other.
- **TM-30 is a hard prereq**: TM-30 is required before ALL TM-40 tracks. FBC is a parallel track, not a prereq.
- **PDF manifest**: After rebuilding PDFs, the manifest (`pdf/.manifest.json`) and SHA file (`pdf/pdf_manifest.sha256`) must also be updated.

## Environment

- Branch: `master` (PR target: `main`)
- CI: dual pipeline (`.github/` + `.gitlab-ci.yml`)
- Deployment: Cloudflare Pages (auto from git), Foundry (mss.data.mil), Google Cloud Run/NIPR (`http://34.38.132.172`)
- NIPR deploy: `deploy/` dir in `maven_training/` → Cloud Run `mss-training-hub` in `europe-west1` on `heimdall-prototype-odt`

## Workflow

- Open `DEPENDENCY_MAP.md` at the start of any audit or cross-reference task
- Save intermediate state during long tasks; keep only the latest checkpoint
- When building slide decks, use `scripts/build_new_decks.py` (not manual HTML)
- Doctrine vs. best-practice: doctrine references go in course materials; strategy/journal references go in supplementary reading only

## Testing

- `python3 -m pytest tests/` — run full test suite
- Sub-apps each have their own `seed.py` for populating test data
