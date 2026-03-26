"""Core packaging logic for the Offline Package Builder.

Scans the maven_training corpus, resolves prerequisite dependencies,
and builds self-contained ZIP archives for disconnected/DDIL environments.
"""

from __future__ import annotations

import io
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Ensure sibling packages (readiness_tracker, etc.) are importable
_apps_dir = str(Path(__file__).resolve().parent.parent)
if _apps_dir not in sys.path:
    sys.path.insert(0, _apps_dir)

# ---------------------------------------------------------------------------
# Prereq chain — imported from readiness_tracker (single source of truth)
# ---------------------------------------------------------------------------
from readiness_tracker.db import PREREQ_CHAIN, ALL_COURSES  # noqa: E402

# Map TM identifiers to their directory names under tm/
_TM_DIR_MAP: dict[str, str] = {
    "SL 1": "TM_10_maven_user",
    "SL 2": "TM_20_builder",
    "SL 3": "TM_30_advanced_builder",
    "SL 4A": "TM_40A_intelligence",
    "SL 4B": "TM_40B_fires",
    "SL 4C": "TM_40C_movement_maneuver",
    "SL 4D": "TM_40D_sustainment",
    "SL 4E": "TM_40E_protection",
    "SL 4F": "TM_40F_mission_command",
    "SL 4G": "TM_40G_orsa",
    "SL 4H": "TM_40H_ai_engineer",
    "SL 4M": "TM_40M_ml_engineer",
    "SL 4J": "TM_40J_program_manager",
    "SL 4K": "TM_40K_knowledge_manager",
    "SL 4L": "TM_40L_software_engineer",
    "SL 4N": "TM_40N_ui_ux_designer",
    "SL 4O": "TM_40O_platform_engineer",
    "SL 5G": "TM_50G_orsa_advanced",
    "SL 5H": "TM_50H_ai_engineer_advanced",
    "SL 5M": "TM_50M_ml_engineer_advanced",
    "SL 5J": "TM_50J_program_manager_advanced",
    "SL 5K": "TM_50K_knowledge_manager_advanced",
    "SL 5L": "TM_50L_software_engineer_advanced",
    "SL 5N": "TM_50N_ui_ux_designer_advanced",
    "SL 5O": "TM_50O_platform_engineer_advanced",
}

# Map exercise identifiers to their directory names under exercises/
_EX_DIR_MAP: dict[str, str] = {
    "EX_10": "EX_10_operator_basics",
    "EX_20": "EX_20_no_code_builder",
    "EX_30": "EX_30_advanced_builder",
    "EX_40A": "EX_40A_intelligence",
    "EX_40B": "EX_40B_fires",
    "EX_40C": "EX_40C_movement_maneuver",
    "EX_40D": "EX_40D_sustainment",
    "EX_40E": "EX_40E_protection",
    "EX_40F": "EX_40F_mission_command",
    "EX_40G": "EX_40G_orsa",
    "EX_40H": "EX_40H_ai_engineer",
    "EX_40M": "EX_40M_ml_engineer",
    "EX_40J": "EX_40J_program_manager",
    "EX_40K": "EX_40K_knowledge_manager",
    "EX_40L": "EX_40L_software_engineer",
    "EX_50G": "EX_50G_orsa",
    "EX_50H": "EX_50H_ai_engineer",
    "EX_50M": "EX_50M_ml_engineer",
    "EX_50J": "EX_50J_program_manager",
    "EX_50K": "EX_50K_knowledge_manager",
    "EX_50L": "EX_50L_software_engineer",
}


def _dir_size_kb(path: Path) -> int:
    """Sum file sizes within a directory (non-recursive into sub-sub-dirs)."""
    total = 0
    if path.is_dir():
        for f in path.rglob("*"):
            if f.is_file():
                total += f.stat().st_size
    return total // 1024


def _file_size_kb(path: Path) -> int:
    """File size in KB."""
    if path.is_file():
        return path.stat().st_size // 1024
    return 0


def _list_files(path: Path) -> list[str]:
    """List relative file paths within a directory."""
    if not path.is_dir():
        return []
    return sorted(
        str(f.relative_to(path))
        for f in path.rglob("*")
        if f.is_file() and not f.name.startswith(".")
    )


# ---------------------------------------------------------------------------
# Content discovery
# ---------------------------------------------------------------------------

def discover_content(root_path: str | Path) -> dict[str, dict[str, Any]]:
    """Scan maven_training/ and return a structured inventory by category.

    Returns a dict keyed by category (tm, syllabi, exercises, exams, doctrine,
    pdf, quick_reference) where each value is a dict of item_name -> metadata.
    """
    root = Path(root_path)
    inventory: dict[str, dict[str, Any]] = {
        "tm": {},
        "syllabi": {},
        "exercises": {},
        "exams": {},
        "doctrine": {},
        "pdf": {},
        "quick_reference": {},
    }

    # --- TMs ---
    tm_dir = root / "tm"
    if tm_dir.is_dir():
        for tm_id, dir_name in sorted(_TM_DIR_MAP.items()):
            tm_path = tm_dir / dir_name
            if tm_path.is_dir():
                inventory["tm"][tm_id] = {
                    "path": f"tm/{dir_name}/",
                    "files": _list_files(tm_path),
                    "size_kb": _dir_size_kb(tm_path),
                }

    # --- Syllabi ---
    syllabi_dir = root / "syllabi"
    if syllabi_dir.is_dir():
        for f in sorted(syllabi_dir.glob("SYLLABUS_*.md")):
            name = f.stem  # e.g. SYLLABUS_TM10
            inventory["syllabi"][name] = {
                "path": f"syllabi/{f.name}",
                "size_kb": _file_size_kb(f),
            }

    # --- Exercises ---
    ex_dir = root / "exercises"
    if ex_dir.is_dir():
        for ex_id, dir_name in sorted(_EX_DIR_MAP.items()):
            ex_path = ex_dir / dir_name
            if ex_path.is_dir():
                inventory["exercises"][ex_id] = {
                    "path": f"exercises/{dir_name}/",
                    "files": _list_files(ex_path),
                    "size_kb": _dir_size_kb(ex_path),
                }

    # --- Exams ---
    exams_dir = root / "exercises" / "exams"
    if exams_dir.is_dir():
        for f in sorted(exams_dir.glob("EXAM_*.md")):
            name = f.stem  # e.g. EXAM_TM10_PRE
            inventory["exams"][name] = {
                "path": f"exercises/exams/{f.name}",
                "size_kb": _file_size_kb(f),
            }

    # --- Doctrine ---
    doctrine_dir = root / "doctrine"
    if doctrine_dir.is_dir():
        for f in sorted(doctrine_dir.glob("*.md")):
            name = f.stem
            inventory["doctrine"][name] = {
                "path": f"doctrine/{f.name}",
                "size_kb": _file_size_kb(f),
            }

    # --- PDFs ---
    pdf_dir = root / "pdf"
    if pdf_dir.is_dir():
        for f in sorted(pdf_dir.glob("*.pdf")):
            name = f.name
            inventory["pdf"][name] = {
                "path": f"pdf/{f.name}",
                "size_kb": _file_size_kb(f),
            }

    # --- Quick Reference ---
    qr_dir = root / "quick_reference"
    if qr_dir.is_dir():
        for f in sorted(qr_dir.glob("*.md")):
            name = f.name
            inventory["quick_reference"][name] = {
                "path": f"quick_reference/{f.name}",
                "size_kb": _file_size_kb(f),
            }
        # Include cda_reference/ subdirectory if present
        cda_ref = qr_dir / "cda_reference"
        if cda_ref.is_dir():
            for f in sorted(cda_ref.glob("*.md")):
                name = f"cda_reference/{f.name}"
                inventory["quick_reference"][name] = {
                    "path": f"quick_reference/cda_reference/{f.name}",
                    "size_kb": _file_size_kb(f),
                }

    return inventory


# ---------------------------------------------------------------------------
# Dependency resolution
# ---------------------------------------------------------------------------

def resolve_dependencies(selected_tms: list[str]) -> dict[str, list[str]]:
    """Given selected TM identifiers, return a dict mapping each TM to its
    auto-included prerequisites (transitive).

    Returns only *added* prerequisites — items already in the selection are
    not listed as auto-included.
    """
    all_needed: set[str] = set()

    def _resolve(tm: str) -> None:
        if tm in all_needed:
            return
        all_needed.add(tm)
        for prereq in PREREQ_CHAIN.get(tm, []):
            _resolve(prereq)

    for tm in selected_tms:
        _resolve(tm)

    # Build explanation: which TMs were added and why
    original = set(selected_tms)
    added: dict[str, list[str]] = {}
    for tm in sorted(all_needed - original):
        # Find which selected item required this prereq
        dependents = [
            sel for sel in selected_tms
            if tm in _get_all_prereqs(sel)
        ]
        added[tm] = dependents

    return added


def _get_all_prereqs(tm: str) -> set[str]:
    """Return all transitive prerequisites for a TM."""
    result: set[str] = set()

    def _walk(t: str) -> None:
        for prereq in PREREQ_CHAIN.get(t, []):
            if prereq not in result:
                result.add(prereq)
                _walk(prereq)

    _walk(tm)
    return result


def get_all_tms_with_prereqs(selected_tms: list[str]) -> list[str]:
    """Return sorted list of all TMs including resolved prerequisites."""
    all_tms: set[str] = set()

    def _resolve(tm: str) -> None:
        if tm in all_tms:
            return
        all_tms.add(tm)
        for prereq in PREREQ_CHAIN.get(tm, []):
            _resolve(prereq)

    for tm in selected_tms:
        _resolve(tm)

    # Sort by TM number for clean ordering
    return sorted(all_tms)


# ---------------------------------------------------------------------------
# Size estimation
# ---------------------------------------------------------------------------

def estimate_size(
    inventory: dict[str, dict[str, Any]],
    selected: dict[str, list[str]],
    include_pdfs: bool = True,
) -> int:
    """Estimate total package size in KB based on selected content."""
    total_kb = 0
    for category, items in selected.items():
        if category == "pdf" and not include_pdfs:
            continue
        cat_inv = inventory.get(category, {})
        for item in items:
            meta = cat_inv.get(item, {})
            total_kb += meta.get("size_kb", 0)
    # Add ~5 KB overhead for MANIFEST.md and README_OFFLINE.md
    total_kb += 5
    return total_kb


# ---------------------------------------------------------------------------
# Package builder
# ---------------------------------------------------------------------------

def _generate_manifest(
    selected: dict[str, list[str]],
    inventory: dict[str, dict[str, Any]],
    auto_included: dict[str, list[str]],
) -> str:
    """Generate MANIFEST.md content listing all included files."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Offline Package Manifest",
        "",
        f"**Generated:** {now}",
        "",
        "---",
        "",
    ]

    # Note auto-included prereqs
    if auto_included:
        lines.append("## Auto-Included Prerequisites")
        lines.append("")
        for tm, dependents in sorted(auto_included.items()):
            dep_str = ", ".join(dependents)
            lines.append(f"- **{tm}** (required by {dep_str})")
        lines.append("")
        lines.append("---")
        lines.append("")

    category_labels = {
        "tm": "Technical Manuals",
        "syllabi": "Syllabi",
        "exercises": "Exercises",
        "exams": "Exams",
        "doctrine": "Doctrine",
        "pdf": "PDFs",
        "quick_reference": "Quick Reference",
    }

    total_files = 0
    total_kb = 0

    for category, items in selected.items():
        if not items:
            continue
        label = category_labels.get(category, category.title())
        lines.append(f"## {label}")
        lines.append("")
        for item in sorted(items):
            meta = inventory.get(category, {}).get(item, {})
            path = meta.get("path", item)
            size = meta.get("size_kb", 0)
            file_count = len(meta.get("files", []))
            total_kb += size
            if file_count:
                lines.append(f"- `{path}` ({file_count} files, ~{size} KB)")
                total_files += file_count
            else:
                lines.append(f"- `{path}` (~{size} KB)")
                total_files += 1
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"**Total:** ~{total_files} files, ~{total_kb} KB")
    lines.append("")

    return "\n".join(lines)


def _generate_readme_offline() -> str:
    """Generate README_OFFLINE.md with usage instructions."""
    return """# MSS Training — Offline Package

## Purpose
This package contains selected content from the MSS Training corpus,
bundled for use in disconnected, denied, intermittent, or limited-bandwidth
(DDIL) environments.

## Contents
See `MANIFEST.md` for a full listing of included files.

## Directory Structure
```
offline_package/
├── MANIFEST.md          This file listing
├── README_OFFLINE.md    Usage instructions (this file)
├── tm/                  Technical Manuals
├── syllabi/             Course syllabi
├── exercises/           Hands-on exercises
│   └── exams/           Pre/post exams
├── doctrine/            Doctrine publications
├── pdf/                 PDF versions of publications
└── quick_reference/     Quick reference guides
```

## Usage
1. Extract the ZIP to a local directory.
2. Open markdown files with any text editor or markdown viewer.
3. PDF versions are included for print or offline reading.
4. Follow the TM progression: SL 1 → SL 2 → SL 3 → SL 4 → SL 5.

## Prereq Chain
- **SL 1** (Operator) — no prerequisites
- **SL 2** (Builder) — requires SL 1
- **SL 3** (Advanced Builder) — requires SL 2
- **SL 4A–F** (WFF tracks) — requires SL 3
- **SL 4G–M** (Specialist tracks) — requires SL 3
- **SL 5G–M** (Advanced specialist) — requires corresponding SL 4

## Notes
- This is a point-in-time snapshot. Check the MSS Training Hub for updates.
- Content is CUI. Handle and store accordingly.
"""


def build_package(
    selected: dict[str, list[str]],
    inventory: dict[str, dict[str, Any]],
    auto_included: dict[str, list[str]],
    include_pdfs: bool = True,
    root_path: str | Path = "",
) -> bytes:
    """Create a ZIP archive in memory with selected content.

    Args:
        selected: Dict of category -> list of selected item keys.
        inventory: Full content inventory from discover_content().
        auto_included: Auto-included prereqs from resolve_dependencies().
        include_pdfs: Whether to include PDF files.
        root_path: Path to the maven_training directory.

    Returns:
        ZIP file contents as bytes.
    """
    root = Path(root_path)
    buf = io.BytesIO()

    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        # Add generated docs
        manifest = _generate_manifest(selected, inventory, auto_included)
        zf.writestr("offline_package/MANIFEST.md", manifest)
        zf.writestr("offline_package/README_OFFLINE.md", _generate_readme_offline())

        for category, items in selected.items():
            if category == "pdf" and not include_pdfs:
                continue

            cat_inv = inventory.get(category, {})
            for item in items:
                meta = cat_inv.get(item, {})
                rel_path = meta.get("path", "")
                if not rel_path:
                    continue

                src = root / rel_path

                if src.is_file():
                    # Single file (syllabi, exams, doctrine docs, PDFs)
                    arc_path = f"offline_package/{rel_path}"
                    zf.write(src, arc_path)

                elif src.is_dir():
                    # Directory (TMs, exercises) — include all files
                    for f in src.rglob("*"):
                        if f.is_file() and not f.name.startswith("."):
                            f_rel = f.relative_to(root)
                            arc_path = f"offline_package/{f_rel}"
                            zf.write(f, arc_path)

    buf.seek(0)
    return buf.getvalue()
