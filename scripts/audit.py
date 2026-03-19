#!/usr/bin/env python3
"""
audit.py — Pre-demo content audit for USAREUR-AF Maven Training corpus.

Checks:
  1. File completeness  — all expected TM / CONCEPTS_GUIDE / SYLLABUS / EXAM / EX files exist
  2. Stale text refs    — old specialist-letter mappings still embedded in prose
  3. Stale PDFs         — old-scheme PDFs that should no longer exist
  4. Missing PDFs       — current-scheme PDFs that are absent
  5. Prereq labels      — ALL TM-40 tracks (A–F WFF and G–O specialist) must say TM-30
  6. No TM-50A–F refs   — those series were retired; only TM-50G–O is valid
  7. HTML/JS ids        — task_index.html and mss_info_app/index.html checked for stale ids

Run from repo root:
    python scripts/audit.py
"""

import os
import re
import sys
from pathlib import Path

# ── repo root ──────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
MT   = ROOT / "maven_training"

# ── canonical structure ────────────────────────────────────────────────────
WFF_TRACKS = {
    "40A": "intelligence",
    "40B": "fires",
    "40C": "movement_maneuver",
    "40D": "sustainment",
    "40E": "protection",
    "40F": "mission_command",
}
SPEC_TRACKS = {
    "40G": "orsa",
    "40H": "ai_engineer",
    "40M": "ml_engineer",
    "40J": "program_manager",
    "40K": "knowledge_manager",
    "40L": "software_engineer",
    "40N": "ux_designer",
    "40O": "platform_engineer",
}
ADV_TRACKS = {
    "50G": "orsa_advanced",
    "50H": "ai_engineer_advanced",
    "50M": "ml_engineer_advanced",
    "50J": "program_manager_advanced",
    "50K": "knowledge_manager_advanced",
    "50L": "software_engineer_advanced",
    "50N": "ux_designer_advanced",
    "50O": "platform_engineer_advanced",
}
BASE_TRACKS = {"10": "maven_user", "20": "builder", "30": "advanced_builder"}

ALL_TRACKS = {**BASE_TRACKS, **WFF_TRACKS, **SPEC_TRACKS, **ADV_TRACKS}

# Track letter I was retired (looks like numeral 1) → renamed to M in display.
# Filesystem paths still use "I". Map canonical code → filesystem letter.
FS_LETTER = {"40M": "40I", "50M": "50I"}

def fs_code(code):
    """Return the filesystem-level track code (handles I→M rename)."""
    return FS_LETTER.get(code, code)

# Old specialist labels that were re-lettered: old→new
# TM-40A=ORSA, B=AIEng, C=MLE, D=PM, E=KM, F=SWE  →  now G–M
STALE_SPECIALIST_LABELS = {
    # Pattern: (old display, new correct)
    r"TM[-\s]?40A\s*[=:–—(]\s*ORSA":           "TM-40G (ORSA)",
    r"TM[-\s]?40B\s*[=:–—(]\s*AI\s*Eng":        "TM-40H (AI Engineer)",
    r"TM[-\s]?40C\s*[=:–—(]\s*ML\s*Eng":        "TM-40M (ML Engineer)",
    r"TM[-\s]?40D\s*[=:–—(]\s*Program":         "TM-40J (Program Manager)",
    r"TM[-\s]?40E\s*[=:–—(]\s*Knowledge":       "TM-40K (Knowledge Manager)",
    r"TM[-\s]?40F\s*[=:–—(]\s*Software":        "TM-40L (Software Engineer)",
}

# Patterns that are unambiguously wrong in prose (not in archive dirs)
STALE_REF_PATTERNS = [
    # TM-50A through TM-50F should not exist at all.
    # Exception: lines that explicitly state they don't exist (negative-context explanations)
    # are valid and should not be flagged. Supply a skip-if pattern as the 3rd tuple element.
    (r"\bTM[-\s]?50[A-Fa-f]\b", "TM-50A–F series retired; only TM-50G–O valid",
     r"\b(no|not|do not|don'?t)\b"),
    # Old specialist mapping labels (prose like "TM-40A (ORSA)" or "TM-40A: ORSA")
    # Must be followed immediately by an ORSA/AI/ML/PM/KM/SWE label — not WFF labels
    (r"\bTM[-\s]?40A\s*[\(\[:]?\s*ORSA",      "old specialist label: TM-40A=ORSA → now TM-40G"),
    (r"\bTM[-\s]?40B\s*[\(\[:]?\s*AI\s*Eng",  "old specialist label: TM-40B=AI Eng → now TM-40H"),
    (r"\bTM[-\s]?40C\s*[\(\[:]?\s*ML\s*Eng",  "old specialist label: TM-40C=ML Eng → now TM-40M"),
    (r"\bTM[-\s]?40D\s*[\(\[:]?\s*Program\s*Manager", "old specialist label: TM-40D=PM → now TM-40J"),
    (r"\bTM[-\s]?40E\s*[\(\[:]?\s*Knowledge\s*Manager", "old specialist label: TM-40E=KM → now TM-40K"),
    (r"\bTM[-\s]?40F\s*[\(\[:]?\s*Software\s*Engineer", "old specialist label: TM-40F=SWE → now TM-40L"),
    # WFF track prereq is TM-30 (policy change 2026-03-14 — all TM-40 require TM-30)
    # Old rule (TM-20 for WFF) removed. No stale-prereq check for WFF here.
    # Wrong prereq: specialist line that asserts TM-20 only (no TM-30 on same line)
    (r"TM[-\s]?40[G-Og-o].*prerequisite[:\s]+TM[-\s]?20(?!.*TM[-\s]?30)",
     "specialist track (G–O) prerequisite set to TM-20; should be TM-30"),
]

# PDFs that should NOT exist (stale naming scheme)
STALE_PDF_PATTERNS = [
    r"CONCEPTS_GUIDE_TM40[A-F]_(?!MISSION_COMMAND|INTELLIGENCE|FIRES|MOVEMENT_MANEUVER|SUSTAINMENT|PROTECTION).+\.pdf$",
    r"CONCEPTS_GUIDE_TM50[A-F]_.+\.pdf$",
    r"EX_40[A-F]_(?!INTELLIGENCE|FIRES|MOVEMENT_MANEUVER|SUSTAINMENT|PROTECTION|MISSION_COMMAND).+\.pdf$",
    r"EXAM_TM50[A-F]_.+\.pdf$",
    r"TM_40[A-F]_(?!INTELLIGENCE|FIRES|MOVEMENT_MANEUVER|SUSTAINMENT|PROTECTION|MISSION_COMMAND)\.pdf$",
    r"TM_50[A-F]_.+\.pdf$",
]

# ── helpers ────────────────────────────────────────────────────────────────
issues = []

def fail(category, msg, path=None, line=None):
    loc = ""
    if path:
        rel = Path(path).relative_to(ROOT) if Path(path).is_absolute() else path
        loc = f"  [{rel}"
        if line:
            loc += f":{line}"
        loc += "]"
    issues.append((category, msg + loc))

def check_file_exists(path, label):
    if not Path(path).exists():
        fail("MISSING FILE", f"{label} not found", path)

def scan_text(path, skip_dirs=("_archive", "_archive_pre_review", "pdf")):
    """Yield (lineno, line) for every line in a text file, skipping archive dirs."""
    p = Path(path)
    for skip in skip_dirs:
        if skip in p.parts:
            return
    try:
        with open(p, encoding="utf-8", errors="replace") as fh:
            for i, line in enumerate(fh, 1):
                yield i, line
    except Exception:
        pass


# ══════════════════════════════════════════════════════════════════════════
# CHECK 1 — File completeness
# ══════════════════════════════════════════════════════════════════════════
def check_completeness():
    print("[ 1 ] Checking file completeness...")

    # TM source files
    for code, slug in {**WFF_TRACKS, **SPEC_TRACKS, **ADV_TRACKS}.items():
        fc = fs_code(code)
        series = fc[:2]          # "40" or "50"
        letter = fc[2]           # filesystem letter
        dir_name = f"TM_{series}{letter}_{slug}"
        tm_dir   = MT / "tm" / dir_name
        tm_file  = tm_dir / f"TM_{series}{letter}_{slug.upper()}.md"
        cg_file  = tm_dir / f"CONCEPTS_GUIDE_TM{series}{letter}_{slug.upper()}.md"
        check_file_exists(tm_file,  f"TM source: TM-{code}")
        check_file_exists(cg_file,  f"Concepts Guide: TM-{code}")

    # Base TM source files
    for code, slug in BASE_TRACKS.items():
        dir_name = f"TM_{code}_{slug}"
        tm_dir   = MT / "tm" / dir_name
        tm_file  = tm_dir / f"TM_{code}_{slug.upper()}.md"
        check_file_exists(tm_file, f"TM source: TM-{code}")

    # Syllabi — TM10/20/30 + all 40 + all 50
    for code in list(BASE_TRACKS) + list(WFF_TRACKS) + list(SPEC_TRACKS) + list(ADV_TRACKS):
        fc = fs_code(code)
        syl = MT / "syllabi" / f"SYLLABUS_TM{fc}.md"
        check_file_exists(syl, f"Syllabus: TM-{code}")

    # Exams — all tracks get PRE + POST, except TM-10 which has PRE + SUPPLEMENTAL
    for code in list(BASE_TRACKS) + list(WFF_TRACKS) + list(SPEC_TRACKS) + list(ADV_TRACKS):
        fc = fs_code(code)
        # PRE exam for all tracks
        exam_pre = MT / "exercises" / "exams" / f"EXAM_TM{fc}_PRE.md"
        check_file_exists(exam_pre, f"Exam PRE: TM-{code}")
        # POST exam for all tracks except TM-10 (which uses SUPPLEMENTAL)
        if code == "10":
            exam_supp = MT / "exercises" / "exams" / "EXAM_TM10_SUPPLEMENTAL.md"
            check_file_exists(exam_supp, "Exam SUPPLEMENTAL: TM-10")
        else:
            exam_post = MT / "exercises" / "exams" / f"EXAM_TM{fc}_POST.md"
            check_file_exists(exam_post, f"Exam POST: TM-{code}")

    # Exercise dirs — TM10/20/30 + all TM-40 (not TM-50; no exercise dirs for advanced)
    ex_tracks = {"10": "operator_basics", "20": "no_code_builder", "30": "advanced_builder",
                 **{k: v for k, v in WFF_TRACKS.items()},
                 **{k: v for k, v in SPEC_TRACKS.items()}}
    for code, slug in ex_tracks.items():
        fc = fs_code(code)
        ex_dir = MT / "exercises" / f"EX-{fc}_{slug}"
        for fname in ("EXERCISE.md", "ENVIRONMENT_SETUP.md"):
            check_file_exists(ex_dir / fname, f"Exercise {fname}: EX_{code}")


# ══════════════════════════════════════════════════════════════════════════
# CHECK 2 — Stale text references
# ══════════════════════════════════════════════════════════════════════════
def check_stale_refs():
    print("[ 2 ] Scanning for stale text references...")

    text_files = []
    for ext in ("*.md", "*.html"):
        text_files.extend(MT.rglob(ext))
    # Also root-level README
    text_files.append(ROOT / "README.md")

    # Compile patterns; support optional 3rd element = "skip if this also matches"
    compiled = []
    for item in STALE_REF_PATTERNS:
        pat, desc = item[0], item[1]
        skip_rx = re.compile(item[2], re.IGNORECASE) if len(item) > 2 else None
        compiled.append((re.compile(pat, re.IGNORECASE), desc, skip_rx))

    # Detects lines that compare/contrast WFF (A–F) vs specialist (G–M) tracks.
    # These are disambiguation lines; prereq mentions on them are intentional.
    disambig_rx = re.compile(r'TM[-\s]?40[A-Fa-f].*TM[-\s]?40[G-Mg-m]', re.IGNORECASE)

    # Meta-documents that intentionally describe retired/stale identifiers
    META_DOCS = {"DEPENDENCY_MAP.md"}

    for fpath in text_files:
        # Skip archive directories and meta-documents
        parts = fpath.parts
        if "_archive" in parts or "_archive_pre_review" in parts:
            continue
        if fpath.name in META_DOCS:
            continue
        for lineno, line in scan_text(fpath):
            # Skip lines that discuss both track families — these are correct by design
            if disambig_rx.search(line):
                continue
            for rx, desc, skip_rx in compiled:
                if rx.search(line):
                    # Skip if the line matches the negative-context exception pattern
                    if skip_rx and skip_rx.search(line):
                        continue
                    fail("STALE REF", desc, fpath, lineno)


# ══════════════════════════════════════════════════════════════════════════
# CHECK 3 — Stale PDFs
# ══════════════════════════════════════════════════════════════════════════
def check_stale_pdfs():
    print("[ 3 ] Checking for stale PDFs...")
    pdf_dir = MT / "pdf"
    if not pdf_dir.exists():
        fail("PDF", "pdf/ directory not found")
        return

    stale_rx = [re.compile(pat, re.IGNORECASE) for pat in STALE_PDF_PATTERNS]
    for pdf in sorted(pdf_dir.glob("*.pdf")):
        for rx in stale_rx:
            if rx.search(pdf.name):
                fail("STALE PDF", f"stale PDF should be deleted: {pdf.name}")
                break


# ══════════════════════════════════════════════════════════════════════════
# CHECK 4 — Missing PDFs (current naming scheme)
# ══════════════════════════════════════════════════════════════════════════
def check_missing_pdfs():
    print("[ 4 ] Checking for missing PDFs...")
    pdf_dir = MT / "pdf"
    existing = {p.name for p in pdf_dir.glob("*.pdf")} if pdf_dir.exists() else set()

    def want(name):
        if name not in existing:
            fail("MISSING PDF", f"expected PDF absent: {name}")

    # TM source PDFs (PDFs use canonical track code, not filesystem alias)
    for code, slug in {**WFF_TRACKS, **SPEC_TRACKS, **ADV_TRACKS}.items():
        series = code[:2]; letter = code[2]
        want(f"TM_{series}{letter}_{slug.upper()}.pdf")
        want(f"CONCEPTS_GUIDE_TM{series}{letter}_{slug.upper()}.pdf")

    # Base TMs
    for code, slug in BASE_TRACKS.items():
        want(f"TM_{code}_{slug.upper()}.pdf")

    # Syllabi — only TM10/20/30 and TM-40 series (50 series syllabi not yet published = OK)
    for code in list(BASE_TRACKS) + list(WFF_TRACKS) + list(SPEC_TRACKS):
        want(f"SYLLABUS_TM{code}.pdf")

    # Exams — TM10/20/30 + TM-40 (50-series may be absent; flag as warning not error)
    for code in list(BASE_TRACKS) + list(WFF_TRACKS) + list(SPEC_TRACKS):
        want(f"EXAM_TM{code}_PRE.pdf")
        if code == "10":
            want("EXAM_TM10_SUPPLEMENTAL.pdf")
        else:
            want(f"EXAM_TM{code}_POST.pdf")

    # Exercises — TM10/20/30 + TM-40 (correct WFF names)
    wff_ex_names = {
        "40A": "INTELLIGENCE", "40B": "FIRES", "40C": "MOVEMENT_MANEUVER",
        "40D": "SUSTAINMENT",  "40E": "PROTECTION", "40F": "MISSION_COMMAND",
    }
    spec_ex_names = {
        "40G": "ORSA", "40H": "AI_ENGINEER", "40M": "ML_ENGINEER",
        "40J": "PROGRAM_MANAGER", "40K": "KNOWLEDGE_MANAGER", "40L": "SOFTWARE_ENGINEER",
        "40N": "UX_DESIGNER", "40O": "PLATFORM_ENGINEER",
    }
    base_ex_names = {"10": "OPERATOR_BASICS", "20": "NO_CODE_BUILDER", "30": "ADVANCED_BUILDER"}
    for code, label in {**base_ex_names, **wff_ex_names, **spec_ex_names}.items():
        want(f"EX_{code}_{label}.pdf")


# ══════════════════════════════════════════════════════════════════════════
# CHECK 5 — Prereq labels in TM source files
# ══════════════════════════════════════════════════════════════════════════
def check_prereqs():
    print("[ 5 ] Checking prereq labels in TM source files...")

    # WFF A–F: all TM-40 tracks (including WFF) require TM-30. No stale-prereq check needed here.

    # Specialist G–O: prereq must be TM-30
    for code, slug in SPEC_TRACKS.items():
        fc = fs_code(code)
        series = fc[:2]; letter = fc[2]
        tm_file = MT / "tm" / f"TM_{series}{letter}_{slug}" / f"TM_{series}{letter}_{slug.upper()}.md"
        if not tm_file.exists():
            continue
        for lineno, line in scan_text(tm_file):
            if re.search(r"prereq|prerequisite", line, re.IGNORECASE):
                if re.search(r"TM[-\s]?20\b", line, re.IGNORECASE) and not re.search(r"TM[-\s]?30", line, re.IGNORECASE):
                    fail("PREREQ", f"TM-{code} specialist track shows TM-20 prereq; should be TM-30", tm_file, lineno)


# ══════════════════════════════════════════════════════════════════════════
# CHECK 6 — HTML files: stale track ids / labels
# ══════════════════════════════════════════════════════════════════════════
def check_html():
    print("[ 6 ] Checking HTML files for stale track references...")

    html_files = [
        MT / "task_index.html",
        MT / "mss_info_app" / "index.html",
        MT / "mss_info_app" / "training_schedule.html",
    ]

    # Patterns that are wrong in HTML context
    html_patterns = [
        # Stale anchor/id slugs mapping old letters to specialist roles
        (r'(?:id|href)=["\'].*tm-?40[a-f]-(?:orsa|ai-engineer|ml-engineer|program-manager|knowledge-manager|software-engineer)',
         "old specialist slug in HTML id/href (A–F mapped to ORSA/AI/ML/PM/KM/SWE — should be G–L)"),
        (r"\btm-?50[a-f]\b",            "TM-50A–F series retired; only TM-50G–O valid"),
    ]
    compiled = [(re.compile(pat, re.IGNORECASE), desc) for pat, desc in html_patterns]

    for fpath in html_files:
        if not fpath.exists():
            continue
        for lineno, line in scan_text(fpath, skip_dirs=()):
            for rx, desc in compiled:
                if rx.search(line):
                    fail("HTML STALE", desc, fpath, lineno)


# ══════════════════════════════════════════════════════════════════════════
# CHECK 7 — Syllabus prereq consistency
# ══════════════════════════════════════════════════════════════════════════
def check_syllabus_prereqs():
    print("[ 7 ] Checking syllabus prereq consistency...")

    # WFF A–F syllabi: all TM-40 tracks require TM-30, so TM-30 in WFF syllabi is correct. No check needed.

    for code in SPEC_TRACKS:
        syl = MT / "syllabi" / f"SYLLABUS_TM{fs_code(code)}.md"
        if not syl.exists():
            continue
        for lineno, line in scan_text(syl):
            if re.search(r"prereq|prerequisite", line, re.IGNORECASE):
                if re.search(r"TM[-\s]?20\b", line, re.IGNORECASE) and not re.search(r"TM[-\s]?30", line, re.IGNORECASE):
                    fail("SYLLABUS PREREQ", f"SYLLABUS_TM{code}: specialist track, prereq should be TM-30 not TM-20", syl, lineno)


# ══════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════
def main():
    check_completeness()
    check_stale_refs()
    check_stale_pdfs()
    check_missing_pdfs()
    check_prereqs()
    check_html()
    check_syllabus_prereqs()

    print()
    if not issues:
        print("✓  AUDIT PASSED — no issues found.")
        return 0

    # Group by category
    by_cat: dict[str, list[str]] = {}
    for cat, msg in issues:
        by_cat.setdefault(cat, []).append(msg)

    total = sum(len(v) for v in by_cat.values())
    print(f"✗  AUDIT FOUND {total} ISSUE(S) ACROSS {len(by_cat)} CATEGOR{'Y' if len(by_cat)==1 else 'IES'}:\n")
    for cat, msgs in sorted(by_cat.items()):
        print(f"  [{cat}]  ({len(msgs)} issue{'s' if len(msgs)>1 else ''})")
        for m in msgs:
            print(f"    • {m}")
        print()

    return 1


if __name__ == "__main__":
    sys.exit(main())
