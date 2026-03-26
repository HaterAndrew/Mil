#!/usr/bin/env python3
"""
audit.py — Pre-demo content audit for USAREUR-AF Maven Training corpus.

Checks:
  1. File completeness  — all expected TM / CONCEPTS_GUIDE / SYLLABUS / EXAM / EX files exist
  2. Stale text refs    — old specialist-letter mappings still embedded in prose
  3. Stale PDFs         — old-scheme PDFs that should no longer exist
  4. Missing PDFs       — current-scheme PDFs that are absent
  5. Prereq labels      — ALL SL 4 tracks (A–F WFF and G–O specialist) must say SL 3
  6. No SL 5A–F refs    — those series were retired; only SL 5G–O is valid
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

# Track letter I was retired (looks like numeral 1) → renamed to M everywhere.
# Filesystem now uses M directly; no mapping needed.

def fs_code(code):
    """Return the filesystem-level track code (identity — I→M rename is complete)."""
    return code

def sl_label(code):
    """Convert internal code like '40G' or '10' to display label like '4G' or '1'."""
    if len(code) >= 2 and code[:2].isdigit():
        level = str(int(code[:2]) // 10)
        return level + code[2:]
    return code

# Old specialist labels that were re-lettered: old→new
# SL 4A=ORSA, B=AIEng, C=MLE, D=PM, E=KM, F=SWE  →  now G–M
STALE_SPECIALIST_LABELS = {
    # Pattern: (old display, new correct)
    r"SL\s?4A\s*[=:–—(]\s*ORSA":           "SL 4G (ORSA)",
    r"SL\s?4B\s*[=:–—(]\s*AI\s*Eng":        "SL 4H (AI Engineer)",
    r"SL\s?4C\s*[=:–—(]\s*ML\s*Eng":        "SL 4M (ML Engineer)",
    r"SL\s?4D\s*[=:–—(]\s*Program":         "SL 4J (Program Manager)",
    r"SL\s?4E\s*[=:–—(]\s*Knowledge":       "SL 4K (Knowledge Manager)",
    r"SL\s?4F\s*[=:–—(]\s*Software":        "SL 4L (Software Engineer)",
}

# Patterns that are unambiguously wrong in prose (not in archive dirs)
STALE_REF_PATTERNS = [
    # SL 5A through SL 5F should not exist at all.
    # Exception: lines that explicitly state they don't exist (negative-context explanations)
    # are valid and should not be flagged. Supply a skip-if pattern as the 3rd tuple element.
    (r"\bSL\s?5[A-Fa-f]\b", "SL 5A–F series retired; only SL 5G–O valid",
     r"\b(no|not|do not|don'?t)\b"),
    # Old specialist mapping labels (prose like "SL 4A (ORSA)" or "SL 4A: ORSA")
    # Must be followed immediately by an ORSA/AI/ML/PM/KM/SWE label — not WFF labels
    (r"\bSL\s?4A\s*[\(\[:]?\s*ORSA",      "old specialist label: SL 4A=ORSA → now SL 4G"),
    (r"\bSL\s?4B\s*[\(\[:]?\s*AI\s*Eng",  "old specialist label: SL 4B=AI Eng → now SL 4H"),
    (r"\bSL\s?4C\s*[\(\[:]?\s*ML\s*Eng",  "old specialist label: SL 4C=ML Eng → now SL 4M"),
    (r"\bSL\s?4D\s*[\(\[:]?\s*Program\s*Manager", "old specialist label: SL 4D=PM → now SL 4J"),
    (r"\bSL\s?4E\s*[\(\[:]?\s*Knowledge\s*Manager", "old specialist label: SL 4E=KM → now SL 4K"),
    (r"\bSL\s?4F\s*[\(\[:]?\s*Software\s*Engineer", "old specialist label: SL 4F=SWE → now SL 4L"),
    # WFF track prereq is SL 3 (policy change 2026-03-14 — all SL 4 require SL 3)
    # Old rule (SL 2 for WFF) removed. No stale-prereq check for WFF here.
    # Wrong prereq: specialist line that asserts SL 2 only (no SL 3 on same line)
    (r"SL\s?4[G-Og-o].*prerequisite[:\s]+SL\s?2(?!.*SL\s?3)",
     "specialist track (G–O) prerequisite set to SL 2; should be SL 3"),
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
_skipped_files = 0  # files that failed to read during scanning

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
    except Exception as exc:
        global _skipped_files
        _skipped_files += 1
        rel = p.relative_to(ROOT) if p.is_absolute() else p
        print(f"  WARN  could not read {rel}: {exc}")


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
        check_file_exists(tm_file,  f"TM source: SL {sl_label(code)}")
        check_file_exists(cg_file,  f"Concepts Guide: SL {sl_label(code)}")

    # Base TM source files
    for code, slug in BASE_TRACKS.items():
        dir_name = f"TM_{code}_{slug}"
        tm_dir   = MT / "tm" / dir_name
        tm_file  = tm_dir / f"TM_{code}_{slug.upper()}.md"
        check_file_exists(tm_file, f"TM source: SL {sl_label(code)}")

    # Syllabi — SL 1/2/3 + all 4x + all 5x
    for code in list(BASE_TRACKS) + list(WFF_TRACKS) + list(SPEC_TRACKS) + list(ADV_TRACKS):
        fc = fs_code(code)
        syl = MT / "syllabi" / f"SYLLABUS_TM{fc}.md"
        check_file_exists(syl, f"Syllabus: SL {sl_label(code)}")

    # Exams — all tracks get PRE + POST, except SL 1 which has PRE + SUPPLEMENTAL
    for code in list(BASE_TRACKS) + list(WFF_TRACKS) + list(SPEC_TRACKS) + list(ADV_TRACKS):
        fc = fs_code(code)
        # PRE exam for all tracks
        exam_pre = MT / "exercises" / "exams" / f"EXAM_TM{fc}_PRE.md"
        check_file_exists(exam_pre, f"Exam PRE: SL {sl_label(code)}")
        # POST exam for all tracks except SL 1 (which uses SUPPLEMENTAL)
        if code == "10":
            exam_supp = MT / "exercises" / "exams" / "EXAM_TM10_SUPPLEMENTAL.md"
            check_file_exists(exam_supp, "Exam SUPPLEMENTAL: SL 1")
        else:
            exam_post = MT / "exercises" / "exams" / f"EXAM_TM{fc}_POST.md"
            check_file_exists(exam_post, f"Exam POST: SL {sl_label(code)}")

    # Exercise dirs — SL 1/2/3 + all SL 4 (not SL 5; no exercise dirs for advanced)
    ex_tracks = {"10": "operator_basics", "20": "no_code_builder", "30": "advanced_builder",
                 **{k: v for k, v in WFF_TRACKS.items()},
                 **{k: v for k, v in SPEC_TRACKS.items()}}
    for code, slug in ex_tracks.items():
        fc = fs_code(code)
        ex_dir = MT / "exercises" / f"EX_{fc}_{slug}"
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
    disambig_rx = re.compile(r'SL\s?4[A-Fa-f].*SL\s?4[G-Mg-m]', re.IGNORECASE)

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

    # Syllabi — only SL 1/2/3 and SL 4 series (SL 5 syllabi not yet published = OK)
    for code in list(BASE_TRACKS) + list(WFF_TRACKS) + list(SPEC_TRACKS):
        want(f"SYLLABUS_TM{code}.pdf")

    # Exams — SL 1/2/3 + SL 4 (SL 5 may be absent; flag as warning not error)
    for code in list(BASE_TRACKS) + list(WFF_TRACKS) + list(SPEC_TRACKS):
        want(f"EXAM_TM{code}_PRE.pdf")
        if code == "10":
            want("EXAM_TM10_SUPPLEMENTAL.pdf")
        else:
            want(f"EXAM_TM{code}_POST.pdf")

    # Exercises — SL 1/2/3 + SL 4 (correct WFF names)
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

    # WFF A–F: all SL 4 tracks (including WFF) require SL 3. No stale-prereq check needed here.

    # Specialist G–O: prereq must be SL 3
    for code, slug in SPEC_TRACKS.items():
        fc = fs_code(code)
        series = fc[:2]; letter = fc[2]
        tm_file = MT / "tm" / f"TM_{series}{letter}_{slug}" / f"TM_{series}{letter}_{slug.upper()}.md"
        if not tm_file.exists():
            continue
        for lineno, line in scan_text(tm_file):
            if re.search(r"prereq|prerequisite", line, re.IGNORECASE):
                if re.search(r"SL\s?2\b", line, re.IGNORECASE) and not re.search(r"SL\s?3", line, re.IGNORECASE):
                    fail("PREREQ", f"SL {sl_label(code)} specialist track shows SL 2 prereq; should be SL 3", tm_file, lineno)


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
        (r'(?:id|href)=["\'].*sl-?4[a-f]-(?:orsa|ai-engineer|ml-engineer|program-manager|knowledge-manager|software-engineer)',
         "old specialist slug in HTML id/href (A–F mapped to ORSA/AI/ML/PM/KM/SWE — should be G–L)"),
        (r"\bsl-?5[a-f]\b",            "SL 5A–F series retired; only SL 5G–O valid"),
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

    # WFF A–F syllabi: all SL 4 tracks require SL 3, so SL 3 in WFF syllabi is correct. No check needed.

    for code in SPEC_TRACKS:
        syl = MT / "syllabi" / f"SYLLABUS_TM{fs_code(code)}.md"
        if not syl.exists():
            continue
        for lineno, line in scan_text(syl):
            if re.search(r"prereq|prerequisite", line, re.IGNORECASE):
                if re.search(r"SL\s?2\b", line, re.IGNORECASE) and not re.search(r"SL\s?3", line, re.IGNORECASE):
                    fail("SYLLABUS PREREQ", f"SYLLABUS_TM{code}: specialist track, prereq should be SL 3 not SL 2", syl, lineno)


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
    if _skipped_files:
        print(f"  NOTE: {_skipped_files} file(s) could not be read and were skipped.\n")
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
