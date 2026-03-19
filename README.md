# Staff Duty Roster Solver

Quarterly staff duty roster generator for ASCC HQ. Uses Integer Linear Programming (ILP) to assign duty days to directorates proportionally to their eligible soldier count, with separate fairness enforcement on weekday vs. weekend/holiday days.

## What it produces

Two rosters per run (SDNCO and SD_Runner), output as:
- **Excel workbook** — Roster calendar tab, per-directorate summary, fairness analysis
- **HTML dashboard** — Color-coded monthly calendar + summary + Gini fairness metrics

## Fairness model

Each directorate receives duty days proportional to its eligible headcount:

```
target_days_d = (eligible_d / total_eligible) × total_quarter_days
```

The ILP enforces that each directorate's actual assignment stays within ±1 of target — for both total days and weekend/holiday ("hard") days independently.

Hard days = weekend days + holiday days (designated training holidays per AEA Pam 350-1).

## Holiday calendar

1. **AEA Pam 350-1** (default) — attempts to scrape the USAREUR-AF training holiday PDF from DoD media. Includes command-designated training holidays that create 4-day weekends.
2. **Federal holidays** (fallback) — US federal holidays via the `holidays` library.
3. **Bridge day heuristic** — when a federal holiday falls on Tuesday or Thursday, the adjacent Monday/Friday is added as a bridge (replicates USAREUR-AF 4-day weekend policy).
4. **Manual overrides** — pass additional dates with `--holiday YYYY-MM-DD`.

Use `--no-pdf-scrape` to skip the DoD fetch (e.g., in air-gapped environments).

## Usage

### From a JSON config (recommended — allows different eligible counts per role)

```bash
python3 -m staff_duty.main --config sample_config.json --output ./output/
```

JSON schema:
```json
{
  "start": "2026-07-01",
  "end":   "2026-09-30",
  "sdnco": [
    {"name": "G1", "eligible": 10},
    {"name": "G2", "eligible": 5}
  ],
  "sd_runner": [
    {"name": "G1", "eligible": 8},
    {"name": "G2", "eligible": 4}
  ]
}
```

Use `"directorates"` instead of `"sdnco"` + `"sd_runner"` to share the same list for both roles.

### Quick inline run (same headcounts for both roles)

```bash
python3 -m staff_duty.main \
  --start 2026-04-01 --end 2026-06-30 \
  --dir G1:10 --dir G2:5 --dir G3:5 --dir G4:6 --dir G6:8 --dir G8:4 --dir ACOS:3 \
  --output ./output/
```

### Add command-directed holidays not in the PDF

```bash
python3 -m staff_duty.main --config q3.json \
  --holiday 2026-08-03 --holiday 2026-08-07 \
  --output ./output/
```

### Skip PDF scrape (air-gapped / offline)

```bash
python3 -m staff_duty.main --config q3.json --no-pdf-scrape --output ./output/
```

## Dependencies

```
pulp         # ILP solver (CBC backend, no license required)
openpyxl     # Excel output
holidays     # US federal holiday calendar
pdfplumber   # AEA Pam 350-1 PDF parsing
click        # CLI
```

Install:
```bash
pip install pulp openpyxl holidays pdfplumber click
```

## Quarterly workflow

1. Update headcounts in JSON config (eligible soldiers per directorate may change each quarter)
2. Run solver: `python3 -m staff_duty.main --config qN_YYYY.json --output ./output/`
3. Share Excel with each directorate — they populate their assigned days with actual names
4. Share HTML dashboard with command for fairness review
