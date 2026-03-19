# PDF Build Workflow — USAREUR-AF Maven Training

## Overview

All training publications are maintained as Markdown source files and compiled to PDF using `scripts/build_pdfs.py`. PDFs are committed to the repository alongside source — no external build step required for distribution.

## Output Location

```
maven_training/pdf/          ← 69 PDFs, one per publication
scripts/build_pdfs.py        ← build script
```

## Prerequisites

```bash
pip install markdown
# Chrome must be installed and available as 'google-chrome'
```

## Running the Build

From the repo root:

```bash
python scripts/build_pdfs.py
```

Output: `[OK]` or `[FAIL]` per file, summary count at the end.

## When to Regenerate

**Regenerate PDFs after any of the following:**

| Trigger | Affected PDFs |
|---------|--------------|
| Any TM content change | That TM's PDF |
| GLOSSARY update | `GLOSSARY_data_foundry.pdf` |
| Syllabus update | That syllabus PDF |
| MTP update | `MTP_MSS.pdf` |
| Doctrine change | `DATA_LITERACY_senior_leaders.pdf`, `DATA_LITERACY_technical_reference.pdf` |
| Standards or cheatsheet update | `NAMING_AND_GOVERNANCE_STANDARDS.pdf`, `CHEATSHEET.pdf` |
| README update | `00_README.pdf` |
| mss_info_app/index.html update | `MSS_TRAINING_HUB.pdf` |

**Rule: regenerate and commit PDFs on every push that modifies any source document.**

## Publication List (33 PDFs)

| PDF | Source |
|-----|--------|
| `00_README.pdf` | `maven_training/README.md` |
| `DATA_LITERACY_senior_leaders.pdf` | `doctrine/DATA_LITERACY_senior_leaders.md` |
| `DATA_LITERACY_technical_reference.pdf` | `doctrine/DATA_LITERACY_technical_reference.md` |
| `GLOSSARY_data_foundry.pdf` | `doctrine/GLOSSARY_data_foundry.md` |
| `NAMING_AND_GOVERNANCE_STANDARDS.pdf` | `standards/NAMING_AND_GOVERNANCE_STANDARDS.md` |
| `CHEATSHEET.pdf` | `quick_reference/cheatsheet.md` |
| `MTP_MSS.pdf` | `training_management/MTP_MSS.md` |
| `MSS_TRAINING_HUB.pdf` | `mss_info_app/index.html` |
| `SYLLABUS_TM10.pdf` through `SYLLABUS_TM40F.pdf` | `syllabi/` |
| `TM_10_MAVEN_USER.pdf` through `TM_50F_SOFTWARE_ENGINEER_ADVANCED.pdf` | `tm/` |

## Build Script Notes

- Uses Python `markdown` library for MD→HTML conversion
- Uses Chrome headless (`--headless=new`) for HTML→PDF
- CSS theme: USAREUR-AF navy/gold, Arial, 10.5pt body, gold `<hr>` separators
- Page footer: "USAREUR-AF Operational Data Team | [page] of [total]"
- `_archive/` files are excluded from build targets

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `FAIL` on a file | Check Chrome is installed: `google-chrome --version` |
| Missing `markdown` module | `pip install markdown` |
| PDF has broken formatting | Open the temp HTML file (add `print(tmp_path)` before unlink) and inspect in browser |
| File not found error | Verify the source path in `TARGETS` list matches actual file location |

## Adding a New Publication

1. Create the markdown file in the appropriate `maven_training/` subdirectory
2. Add an entry to the `TARGETS` list in `scripts/build_pdfs.py`:
   ```python
   ("maven_training/path/to/file.md", "OUTPUT_STEM"),
   ```
3. Run the build and verify the PDF
4. Commit both the source file and the generated PDF
