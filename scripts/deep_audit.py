#!/usr/bin/env python3
"""
deep_audit.py — Full-spectrum pre-publication audit for USAREUR-AF Maven Training corpus.

15 check groups (A–O):

  A  File completeness       — every expected TM/CG/SYL/EXAM/EX/training-mgmt file exists
  B  Stale text references   — retired specialist labels, TM-50A–F series, wrong prereq claims
  C  PDF inventory           — stale PDFs deleted; all current-scheme PDFs present
  D  Prereq label accuracy   — all TM-40 (WFF+Specialist)=TM-30, Advanced=TM-40x
  E  Syllabus structure      — required sections present (Prereqs, Objectives, Assessment, Schedule)
  F  Exam structure          — PRE/POST exams have minimum detectable item count
  G  TM document structure   — H1 title, BLUF, Army WARNING/CAUTION/NOTE style, min word count
  H  Broken internal links   — relative markdown [text](path) links resolve to real files
  I  Archive contamination   — active files don't link into _archive/ directories
  J  HTML correctness        — task_index.html and mss_info_app for stale track ids/prereq chips
  K  Duration consistency    — MTP table durations match SYLLABUS course-length fields
  L  CG ↔ TM bidirectional  — each TM references its CG; each CG references its TM
  M  Valid track code refs   — all "TM-XX" mentions in prose are valid track codes
  N  Training mgmt coverage  — TEO/POI/MTP/FDP cover every TM-40 track
  O  Terminology & format    — key proper nouns capitalized; consistent TM-XX hyphen format

Severity levels:
  ERROR  — must fix before publication
  WARN   — review; may be intentional
  INFO   — low priority / informational

Usage:
    python scripts/deep_audit.py              # all checks, errors + warnings
    python scripts/deep_audit.py --errors-only
    python scripts/deep_audit.py --verbose    # include INFO items
    python scripts/deep_audit.py --checks A,B,D   # run specific checks only

Exit codes:  0 = PASS  |  1 = WARNINGS only  |  2 = ERRORS found
"""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────────────
# CANONICAL STRUCTURE
# ─────────────────────────────────────────────────────────────────────────────

ROOT = Path(__file__).resolve().parent.parent
MT   = ROOT / "maven_training"

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
}
ADV_TRACKS = {
    "50G": "orsa_advanced",
    "50H": "ai_engineer_advanced",
    "50M": "ml_engineer_advanced",
    "50J": "program_manager_advanced",
    "50K": "knowledge_manager_advanced",
    "50L": "software_engineer_advanced",
}
BASE_TRACKS = {"10": "maven_user", "20": "builder", "30": "advanced_builder"}
ALL_TRACKS  = {**BASE_TRACKS, **WFF_TRACKS, **SPEC_TRACKS, **ADV_TRACKS}

# Canonical course durations in days (from authoritative MTP / DEPENDENCY_MAP)
CANONICAL_DAYS: dict[str, int] = {
    "20":  5, "30":  5,
    "40A": 3, "40B": 3, "40C": 3, "40D": 3, "40E": 3, "40F": 3,
    "40G": 5, "40H": 5, "40M": 5, "40J": 4, "40K": 4, "40L": 5,
    "50G": 5, "50H": 5, "50M": 5, "50J": 3, "50K": 3, "50L": 5,
}

# Archive directories — expected to contain stale refs; skip in most checks
ARCHIVE_DIRS = {"_archive", "_archive_pre_review", "pdf", "source_material",
                ".venv", "node_modules", "mss_widget"}

# Files that intentionally describe retired/stale identifiers
META_SKIP = {
    "DEPENDENCY_MAP.md", "audit.py", "deep_audit.py", "build_pdfs.py",
    "generate_dep_map.py",
}

# ─────────────────────────────────────────────────────────────────────────────
# ISSUE COLLECTION
# ─────────────────────────────────────────────────────────────────────────────

_issues: list[tuple[str, str, str]] = []  # (severity, category, message)


def _issue(severity: str, category: str, msg: str, path=None, line: int = None):
    loc = ""
    if path:
        try:
            rel = Path(path).relative_to(ROOT)
        except ValueError:
            rel = path
        loc = f"  [{rel}"
        if line:
            loc += f":{line}"
        loc += "]"
    _issues.append((severity, category, msg + loc))


def err(cat, msg, path=None, line=None):  _issue("ERROR", cat, msg, path, line)
def warn(cat, msg, path=None, line=None): _issue("WARN",  cat, msg, path, line)
def info(cat, msg, path=None, line=None): _issue("INFO",  cat, msg, path, line)


# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def is_archive(path: Path) -> bool:
    return any(d in path.parts for d in ARCHIVE_DIRS)


def scan_lines(path: Path, skip_archive: bool = True):
    """Yield (lineno, line) for a text file."""
    if skip_archive and is_archive(path):
        return
    if path.name in META_SKIP:
        return
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            for i, line in enumerate(fh, 1):
                yield i, line
    except Exception:
        pass


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""


def word_count(text: str) -> int:
    return len(text.split())


def all_md_files(skip_archive: bool = True) -> list[Path]:
    files = list(MT.rglob("*.md")) + [ROOT / "README.md"]
    if skip_archive:
        files = [f for f in files if not is_archive(f) and f.name not in META_SKIP]
    return files


def need(path, label: str):
    """Assert a file exists; log ERROR if missing."""
    if not Path(path).exists():
        err("A:MISSING", f"{label} not found", path)


# ─────────────────────────────────────────────────────────────────────────────
# CHECK A — File completeness
# ─────────────────────────────────────────────────────────────────────────────

def check_A():
    print("[A] File completeness...")

    # TM source + CONCEPTS_GUIDE for every 40/50-series track
    for code, slug in {**WFF_TRACKS, **SPEC_TRACKS, **ADV_TRACKS}.items():
        s, l   = code[:2], code[2]
        d      = MT / "tm" / f"TM_{s}{l}_{slug}"
        tm_f   = d / f"TM_{s}{l}_{slug.upper()}.md"
        cg_f   = d / f"CONCEPTS_GUIDE_TM{s}{l}_{slug.upper()}.md"
        need(tm_f, f"TM source TM-{code}")
        need(cg_f, f"Concepts Guide TM-{code}")

    # Base TMs (no CG for TM-10/20/30)
    for code, slug in BASE_TRACKS.items():
        need(MT / "tm" / f"TM_{code}_{slug}" / f"TM_{code}_{slug.upper()}.md",
             f"TM source TM-{code}")

    # Syllabi — all tracks
    for code in ALL_TRACKS:
        need(MT / "syllabi" / f"SYLLABUS_TM{code}.md", f"Syllabus TM-{code}")

    # Exams — PRE + POST for every track (TM-10 has no written POST; uses practical exercise)
    for code in ALL_TRACKS:
        need(MT / "exercises" / "exams" / f"EXAM_TM{code}_PRE.md",
             f"Exam PRE TM-{code}")
        if code != "10":
            need(MT / "exercises" / "exams" / f"EXAM_TM{code}_POST.md",
                 f"Exam POST TM-{code}")

    # Exercise dirs — TM-10/20/30 + all TM-40 (TM-50 has no exercise dirs)
    ex_tracks = {"10": "operator_basics", "20": "no_code_builder", "30": "advanced_builder",
                 **WFF_TRACKS, **SPEC_TRACKS}
    for code, slug in ex_tracks.items():
        ex = MT / "exercises" / f"EX_{code}_{slug}"
        need(ex / "EXERCISE.md",          f"EX_{code} EXERCISE.md")
        need(ex / "ENVIRONMENT_SETUP.md", f"EX_{code} ENVIRONMENT_SETUP.md")

    # Training management core files
    for f in ("MTP_MSS.md", "POI_MSS.md", "CAD_MSS.md", "TEO_MSS.md",
              "ENROLLMENT_SOP.md", "FACULTY_DEVELOPMENT_PLAN.md"):
        need(MT / "training_management" / f, f"Training mgmt: {f}")

    # Doctrine files
    for f in ("DATA_LITERACY_technical_reference.md", "GLOSSARY_data_foundry.md"):
        need(MT / "doctrine" / f, f"Doctrine: {f}")

    # HTML applications
    need(MT / "task_index.html",                 "HTML: task_index.html")
    need(MT / "mss_info_app" / "index.html",     "HTML: mss_info_app/index.html")


# ─────────────────────────────────────────────────────────────────────────────
# CHECK B — Stale text references
# ─────────────────────────────────────────────────────────────────────────────

# Pattern, severity, category, human description
_STALE = [
    # Retired TM-50A–F series
    (r"\bTM[-\s]?50[A-Fa-f]\b",
     "ERROR", "B:STALE-REF",
     "TM-50A–F series is retired; only TM-50G–M is valid"),
    # Old specialist label mappings (TM-40A=ORSA was the OLD scheme; now TM-40G=ORSA)
    (r"\bTM[-\s]?40A\s*[\(\[:]?\s*ORSA",
     "ERROR", "B:STALE-REF", "old label TM-40A=ORSA → correct label is TM-40G"),
    (r"\bTM[-\s]?40B\s*[\(\[:]?\s*AI\s*Eng(?:ineer)?",
     "ERROR", "B:STALE-REF", "old label TM-40B=AI Eng → correct label is TM-40H"),
    (r"\bTM[-\s]?40C\s*[\(\[:]?\s*ML\s*Eng(?:ineer)?",
     "ERROR", "B:STALE-REF", "old label TM-40C=ML Eng → correct label is TM-40M"),
    (r"\bTM[-\s]?40D\s*[\(\[:]?\s*Program\s*Manager",
     "ERROR", "B:STALE-REF", "old label TM-40D=PM → correct label is TM-40J"),
    (r"\bTM[-\s]?40E\s*[\(\[:]?\s*Knowledge\s*Manager",
     "ERROR", "B:STALE-REF", "old label TM-40E=KM → correct label is TM-40K"),
    (r"\bTM[-\s]?40F\s*[\(\[:]?\s*Software\s*Engineer",
     "ERROR", "B:STALE-REF", "old label TM-40F=SWE → correct label is TM-40L"),
    # Wrong prereq assertions — all TM-40 tracks (WFF + Specialist) require TM-30
    (r"TM[-\s]?40[A-Fa-f].*prerequisite[:\s]+TM[-\s]?20(?!.*TM[-\s]?30)",
     "ERROR", "B:PREREQ",
     "WFF track (A–F) claims TM-20-only prereq; correct prereq is TM-30"),
    (r"TM[-\s]?40[G-Mg-m].*prerequisite[:\s]+TM[-\s]?20(?!.*TM[-\s]?30)",
     "ERROR", "B:PREREQ",
     "specialist track (G–M) claims TM-20-only prereq; correct prereq is TM-30"),
]

_DISAMBIG_RX = re.compile(r'TM[-\s]?40[A-Fa-f].*TM[-\s]?40[G-Mg-m]', re.IGNORECASE)
# Lines that correctly state TM-50A–F do NOT exist (explanatory / negation)
_NEGATION_50_RX = re.compile(
    r'(?:no|not|none|there\s+(?:is|are)\s+no|do\s+not\s+exist|does\s+not\s+exist)'
    r'.*TM[-\s]?50[A-F]'
    r'|TM[-\s]?50[A-F].*(?:do\s+not|does\s+not|not\s+applicable|no\s+such)',
    re.IGNORECASE,
)


def check_B():
    print("[B] Stale text references...")

    compiled = [(re.compile(p, re.IGNORECASE), sev, cat, desc)
                for p, sev, cat, desc in _STALE]

    scan_targets = all_md_files() + list(MT.rglob("*.html"))
    for fpath in scan_targets:
        for lineno, line in scan_lines(fpath):
            # Disambiguation lines intentionally mention both families — skip
            if _DISAMBIG_RX.search(line):
                continue
            # Correct negation statements ("No TM-50A–F tracks exist") — skip
            if _NEGATION_50_RX.search(line):
                continue
            for rx, sev, cat, desc in compiled:
                if rx.search(line):
                    _issue(sev, cat, desc, fpath, lineno)


# ─────────────────────────────────────────────────────────────────────────────
# CHECK C — PDF inventory
# ─────────────────────────────────────────────────────────────────────────────

_STALE_PDF_RX = [
    # Old specialist CG naming: TM40A–F mapped to ORSA/AI/ML/PM/KM/SWE slugs
    re.compile(r"CONCEPTS_GUIDE_TM40[A-F]_(?!MISSION_COMMAND|INTELLIGENCE|FIRES|"
               r"MOVEMENT_MANEUVER|SUSTAINMENT|PROTECTION).+\.pdf$", re.IGNORECASE),
    re.compile(r"CONCEPTS_GUIDE_TM50[A-F]_.+\.pdf$", re.IGNORECASE),
    re.compile(r"EX_40[A-F]_(?!INTELLIGENCE|FIRES|MOVEMENT_MANEUVER|SUSTAINMENT|"
               r"PROTECTION|MISSION_COMMAND).+\.pdf$", re.IGNORECASE),
    re.compile(r"EXAM_TM50[A-F]_.+\.pdf$", re.IGNORECASE),
    re.compile(r"^TM_40[A-F]_(?!INTELLIGENCE|FIRES|MOVEMENT_MANEUVER|SUSTAINMENT|"
               r"PROTECTION|MISSION_COMMAND).+\.pdf$", re.IGNORECASE),
    re.compile(r"^TM_50[A-F]_.+\.pdf$", re.IGNORECASE),
]


def check_C():
    print("[C] PDF inventory...")

    pdf_dir = MT / "pdf"
    if not pdf_dir.exists():
        err("C:PDF", "maven_training/pdf/ directory is missing")
        return

    existing = {p.name for p in pdf_dir.glob("*.pdf")}

    # Flag stale PDFs
    for name in sorted(existing):
        for rx in _STALE_PDF_RX:
            if rx.search(name):
                err("C:STALE-PDF", f"stale PDF should be deleted: {name}")
                break

    # Assert expected PDFs exist
    def want(name: str):
        if name not in existing:
            warn("C:MISSING-PDF", f"expected PDF absent: {name}")

    for code, slug in {**WFF_TRACKS, **SPEC_TRACKS, **ADV_TRACKS}.items():
        s, l = code[:2], code[2]
        want(f"TM_{s}{l}_{slug.upper()}.pdf")
        want(f"CONCEPTS_GUIDE_TM{s}{l}_{slug.upper()}.pdf")

    for code, slug in BASE_TRACKS.items():
        want(f"TM_{code}_{slug.upper()}.pdf")

    # Syllabi PDFs — 10/20/30 + all TM-40 (TM-50 syllabi not yet published = OK)
    for code in list(BASE_TRACKS) + list(WFF_TRACKS) + list(SPEC_TRACKS):
        want(f"SYLLABUS_TM{code}.pdf")

    # Exam PDFs — TM-10/20/30 + TM-40 (TM-10 has no written POST exam)
    for code in list(BASE_TRACKS) + list(WFF_TRACKS) + list(SPEC_TRACKS):
        want(f"EXAM_TM{code}_PRE.pdf")
        if code != "10":
            want(f"EXAM_TM{code}_POST.pdf")

    # Exercise PDFs
    ex_labels = {
        "10": "OPERATOR_BASICS", "20": "NO_CODE_BUILDER", "30": "ADVANCED_BUILDER",
        "40A": "INTELLIGENCE",      "40B": "FIRES",          "40C": "MOVEMENT_MANEUVER",
        "40D": "SUSTAINMENT",       "40E": "PROTECTION",     "40F": "MISSION_COMMAND",
        "40G": "ORSA",              "40H": "AI_ENGINEER",    "40M": "ML_ENGINEER",
        "40J": "PROGRAM_MANAGER",   "40K": "KNOWLEDGE_MANAGER", "40L": "SOFTWARE_ENGINEER",
    }
    for code, label in ex_labels.items():
        want(f"EX_{code}_{label}.pdf")


# ─────────────────────────────────────────────────────────────────────────────
# CHECK D — Prereq label correctness
# ─────────────────────────────────────────────────────────────────────────────

def check_D():
    print("[D] Prereq label accuracy...")

    prereq_rx = re.compile(r"prereq|prerequisite", re.IGNORECASE)
    tm20_rx   = re.compile(r"TM[-\s]?20\b", re.IGNORECASE)
    tm30_rx   = re.compile(r"TM[-\s]?30\b", re.IGNORECASE)

    def check_file(fpath, code, expect_tm20=False, expect_tm30=False):
        """
        Scan for wrong prereq labels. Only flag lines that are about THIS
        document's own prereqs — i.e., lines that either mention this track's
        code or are in the document header (first 30 lines).
        Companion cross-reference tables mention other tracks' prereqs;
        those are correct by design and must not be flagged.
        """
        if not fpath.exists():
            return
        own_code_rx = re.compile(rf"TM[-\s]?{re.escape(code)}\b", re.IGNORECASE)
        for lineno, line in scan_lines(fpath):
            if not prereq_rx.search(line):
                continue
            if _DISAMBIG_RX.search(line):
                continue
            # Army TM prereq declarations appear in the document header (first 25 lines).
            # Lines beyond that are typically cross-reference tables about OTHER tracks.
            if lineno > 25:
                continue
            if expect_tm30 and tm20_rx.search(line) and not tm30_rx.search(line):
                err("D:PREREQ",
                    f"{fpath.name}: track shows TM-20-only prereq; should be TM-30",
                    fpath, lineno)

    # WFF A–F: prereq = TM-30 (same as specialist tracks — design decision 2026-03-13)
    for code, slug in WFF_TRACKS.items():
        s, l = code[:2], code[2]
        check_file(MT / "tm" / f"TM_{s}{l}_{slug}" / f"TM_{s}{l}_{slug.upper()}.md",
                   code, expect_tm30=True)
        check_file(MT / "syllabi" / f"SYLLABUS_TM{code}.md",
                   code, expect_tm30=True)

    # Specialist G–M: prereq = TM-30
    for code, slug in SPEC_TRACKS.items():
        s, l = code[:2], code[2]
        check_file(MT / "tm" / f"TM_{s}{l}_{slug}" / f"TM_{s}{l}_{slug.upper()}.md",
                   code, expect_tm30=True)
        check_file(MT / "syllabi" / f"SYLLABUS_TM{code}.md",
                   code, expect_tm30=True)

    # Advanced 50-series: each must mention its paired TM-40X
    for code, slug in ADV_TRACKS.items():
        s, l = code[:2], code[2]
        paired = f"40{l}"
        fpath  = MT / "tm" / f"TM_{s}{l}_{slug}" / f"TM_{s}{l}_{slug.upper()}.md"
        if not fpath.exists():
            continue
        text = read_text(fpath)
        if not re.search(rf"TM[-\s]?{paired}\b", text, re.IGNORECASE):
            warn("D:PREREQ",
                 f"TM-{code} (advanced) does not reference its paired prereq TM-{paired}",
                 fpath)


# ─────────────────────────────────────────────────────────────────────────────
# CHECK E — Syllabus structure
# ─────────────────────────────────────────────────────────────────────────────

_SYL_REQUIRED = [
    (re.compile(r"prereq|prerequisite",         re.IGNORECASE), "Prerequisites section"),
    (re.compile(r"learning\s+objective|terminal\s+learning|TLO", re.IGNORECASE), "Learning Objectives"),
    (re.compile(r"assessment|exam|evaluation",   re.IGNORECASE), "Assessment/Exam section"),
    (re.compile(r"schedule|lesson\s+outline|course\s+outline|day\s+\d", re.IGNORECASE), "Schedule/Outline"),
    (re.compile(r"audience|who\s+should|personnel", re.IGNORECASE), "Audience/Who Should Attend"),
]

_SYL_MIN_WORDS = 200


def check_E():
    print("[E] Syllabus structure...")

    for code in ALL_TRACKS:
        syl = MT / "syllabi" / f"SYLLABUS_TM{code}.md"
        if not syl.exists():
            continue
        text = read_text(syl)

        # H1 title
        if not re.search(r"^#\s+\S", text, re.MULTILINE):
            err("E:STRUCTURE", f"SYLLABUS_TM{code}: no H1 title line", syl)

        # Track code appears in first 10 lines
        header_block = "\n".join(text.splitlines()[:10])
        if f"TM-{code}" not in header_block and f"TM {code}" not in header_block:
            warn("E:HEADER",
                 f"SYLLABUS_TM{code}: track code not found in first 10 lines — check title",
                 syl)

        # Required sections
        for rx, label in _SYL_REQUIRED:
            if not rx.search(text):
                warn("E:STRUCTURE", f"SYLLABUS_TM{code}: no {label} found", syl)

        # Minimum depth
        wc = word_count(text)
        if wc < _SYL_MIN_WORDS:
            warn("E:STUB",
                 f"SYLLABUS_TM{code}: only {wc} words — may be a stub (min {_SYL_MIN_WORDS})",
                 syl)


# ─────────────────────────────────────────────────────────────────────────────
# CHECK F — Exam structure
# ─────────────────────────────────────────────────────────────────────────────

_QUESTION_RX = re.compile(
    r"(?:^\s*\d+[\.\)]\s+\S|^\s*\*\*\d+\.|^#{1,4}\s+\*?\*?\d+\.)",
    re.MULTILINE,
)
_MIN_Q = {"PRE": 8, "POST": 10}
_MIN_EXAM_WORDS = 150


def check_F():
    print("[F] Exam structure...")

    for code in ALL_TRACKS:
        for kind in ("PRE", "POST"):
            exam = MT / "exercises" / "exams" / f"EXAM_TM{code}_{kind}.md"
            if not exam.exists():
                continue
            text = read_text(exam)

            if not re.search(r"^#\s+\S", text, re.MULTILINE):
                warn("F:STRUCTURE", f"EXAM_TM{code}_{kind}: no H1 title", exam)

            # Detectable item count (numbered items, bold-numbered questions)
            q_count = len(_QUESTION_RX.findall(text))
            if q_count < _MIN_Q[kind]:
                warn("F:QUESTIONS",
                     f"EXAM_TM{code}_{kind}: ~{q_count} detectable items "
                     f"(expected ≥{_MIN_Q[kind]})", exam)

            wc = word_count(text)
            if wc < _MIN_EXAM_WORDS:
                warn("F:STUB",
                     f"EXAM_TM{code}_{kind}: only {wc} words — may be a stub", exam)


# ─────────────────────────────────────────────────────────────────────────────
# CHECK G — TM document structure
# ─────────────────────────────────────────────────────────────────────────────

_TM_MIN_WORDS = {"base": 1000, "wff": 1500, "spec": 2500, "adv": 2000}

_TM_REQUIRED_SECTIONS = [
    (re.compile(r"^#{1,3}\s+(?:purpose|scope|overview|introduction|chapter\s+1)",
                re.IGNORECASE | re.MULTILINE),
     "Chapter 1 / Introduction / Purpose section"),
    (re.compile(r"^#{1,3}\s+(?:chapter\s+[2-9]|\d+\.\s+\S)",
                re.IGNORECASE | re.MULTILINE),
     "Multiple chapters (at least Chapter 2)"),
    (re.compile(r"\bBLUF\b"),
     "BLUF statement"),
    (re.compile(r"\bWARNING\b|\bCAUTION\b|\bNOTE\b"),
     "WARNING / CAUTION / NOTE callout (Army TM style)"),
]


def _check_tm_file(fpath: Path, code: str, tier: str):
    if not fpath.exists():
        return
    text = read_text(fpath)

    # H1 title
    if not re.search(r"^#\s+\S", text, re.MULTILINE):
        err("G:STRUCTURE", f"TM-{code}: no H1 title", fpath)

    # Required structural elements
    for rx, label in _TM_REQUIRED_SECTIONS:
        if not rx.search(text):
            sev = "WARN" if label in ("BLUF statement",) else "WARN"
            _issue(sev, "G:STRUCTURE",
                   f"TM-{code}: '{label}' not found", fpath)

    # Minimum word count
    wc = word_count(text)
    min_w = _TM_MIN_WORDS[tier]
    if wc < min_w:
        warn("G:STUB",
             f"TM-{code}: {wc} words — below expected minimum of {min_w} for {tier} tier",
             fpath)

    # Appendix check for 40/50-series (substantive TMs should have appendices)
    if tier in ("spec", "adv") and not re.search(r"^#+\s*Appendix", text,
                                                   re.IGNORECASE | re.MULTILINE):
        warn("G:STRUCTURE", f"TM-{code}: no Appendix section found (specialist/advanced TMs expected to have appendices)", fpath)

    # TABLE OF CONTENTS check for longer TMs
    if wc > 2000 and not re.search(r"table\s+of\s+contents|TOC", text, re.IGNORECASE):
        warn("G:STRUCTURE", f"TM-{code}: no Table of Contents found (document is {wc} words)", fpath)


def check_G():
    print("[G] TM document structure...")

    for code, slug in BASE_TRACKS.items():
        _check_tm_file(MT / "tm" / f"TM_{code}_{slug}" / f"TM_{code}_{slug.upper()}.md",
                       code, "base")
    for code, slug in WFF_TRACKS.items():
        s, l = code[:2], code[2]
        _check_tm_file(MT / "tm" / f"TM_{s}{l}_{slug}" / f"TM_{s}{l}_{slug.upper()}.md",
                       code, "wff")
    for code, slug in SPEC_TRACKS.items():
        s, l = code[:2], code[2]
        _check_tm_file(MT / "tm" / f"TM_{s}{l}_{slug}" / f"TM_{s}{l}_{slug.upper()}.md",
                       code, "spec")
    for code, slug in ADV_TRACKS.items():
        s, l = code[:2], code[2]
        _check_tm_file(MT / "tm" / f"TM_{s}{l}_{slug}" / f"TM_{s}{l}_{slug.upper()}.md",
                       code, "adv")


# ─────────────────────────────────────────────────────────────────────────────
# CHECK H — Broken internal markdown links
# ─────────────────────────────────────────────────────────────────────────────

_MDLINK_RX = re.compile(r'\[([^\]]*)\]\(([^)#\s][^)]*)\)')


def check_H():
    print("[H] Broken internal markdown links...")

    for fpath in all_md_files():
        for lineno, line in scan_lines(fpath):
            for m in _MDLINK_RX.finditer(line):
                href = m.group(2).strip()

                # Skip external links
                if href.startswith(("http://", "https://", "mailto:")):
                    continue

                # Strip inline anchor
                if "#" in href:
                    href = href.split("#", 1)[0]
                if not href:
                    continue

                target = (fpath.parent / href).resolve()
                if not target.exists():
                    warn("H:BROKEN-LINK",
                         f"broken link '{m.group(2)}'",
                         fpath, lineno)


# ─────────────────────────────────────────────────────────────────────────────
# CHECK I — Archive contamination
# ─────────────────────────────────────────────────────────────────────────────

_ARCHIVE_LINK_RX = re.compile(r'\]\([^)]*_archive[^)]*\)', re.IGNORECASE)


def check_I():
    print("[I] Archive contamination...")

    for fpath in all_md_files():
        for lineno, line in scan_lines(fpath):
            if _ARCHIVE_LINK_RX.search(line):
                warn("I:ARCHIVE-LINK",
                     "active file links into _archive/ directory",
                     fpath, lineno)


# ─────────────────────────────────────────────────────────────────────────────
# CHECK J — HTML correctness
# ─────────────────────────────────────────────────────────────────────────────

_HTML_PATTERNS = [
    # Old specialist slug: id/href uses tm-40a-orsa style (A–F mapped to ORSA/AI/etc.)
    (re.compile(r'(?:id|href|data-[a-z]+)=["\'][^"\']*?tm-?40[a-f]-'
                r'(?:orsa|ai-engineer|ml-engineer|program-manager|knowledge-manager|software-engineer)',
                re.IGNORECASE),
     "ERROR", "J:STALE-SLUG",
     "old specialist HTML slug (TM-40A–F mapped to role names); should be TM-40G–M"),
    # Retired TM-50A–F in any context
    (re.compile(r"\btm-?50[a-f]\b", re.IGNORECASE),
     "ERROR", "J:STALE-REF",
     "TM-50A–F retired; only TM-50G–M valid"),
]


def check_J():
    print("[J] HTML correctness...")

    html_files = [
        MT / "task_index.html",
        MT / "mss_info_app" / "index.html",
        MT / "mss_info_app" / "training_schedule.html",
    ]

    for fpath in html_files:
        if not fpath.exists():
            warn("J:MISSING", f"{fpath.name} not found")
            continue
        for lineno, line in scan_lines(fpath, skip_archive=False):
            for rx, sev, cat, desc in _HTML_PATTERNS:
                if rx.search(line):
                    _issue(sev, cat, desc, fpath, lineno)

    # mss_info_app/index.html: verify card counts are correct
    idx = MT / "mss_info_app" / "index.html"
    if idx.exists():
        text = read_text(idx)
        wff_refs  = len(set(re.findall(r'tm-40[a-f]', text, re.IGNORECASE)))
        spec_refs = len(set(re.findall(r'tm-40[g-m]', text, re.IGNORECASE)))
        adv_refs  = len(set(re.findall(r'tm-50[g-m]', text, re.IGNORECASE)))
        if wff_refs < 6:
            warn("J:CARD-COUNT",
                 f"mss_info_app/index.html: only {wff_refs}/6 WFF track codes (TM-40A–F) found")
        if spec_refs < 6:
            warn("J:CARD-COUNT",
                 f"mss_info_app/index.html: only {spec_refs}/6 specialist track codes (TM-40G–M) found")
        if adv_refs < 6:
            warn("J:CARD-COUNT",
                 f"mss_info_app/index.html: only {adv_refs}/6 advanced track codes (TM-50G–M) found")

        # All TM-40 tracks (WFF + Specialist) require TM-30
        # Flag any WFF card that shows TM-20 prereq without TM-30
        for lineno, line in scan_lines(idx, skip_archive=False):
            if re.search(r'tm-40[a-f]', line, re.IGNORECASE):
                if re.search(r'\bTM-20\b', line, re.IGNORECASE) and \
                   not re.search(r'\bTM-30\b', line, re.IGNORECASE):
                    warn("J:PREREQ-CHIP",
                         "WFF track card (TM-40A–F) shows TM-20 chip — should be TM-30",
                         idx, lineno)


# ─────────────────────────────────────────────────────────────────────────────
# CHECK K — Course duration consistency (MTP vs Syllabi)
# ─────────────────────────────────────────────────────────────────────────────

# MTP table row format: | TM-40A | ... | 3 | TM-20 (Required) |
# Column 4 (0-indexed col 3) is days.
_MTP_ROW_RX = re.compile(
    r'\|\s*TM[-\s]?(\d+[A-Ma-m]?)\s*\|[^|]*\|[^|]*\|\s*(\d+)\s*\|',
    re.IGNORECASE,
)

# Syllabus field: | **Duration** | 5 days (40 hours) |
_SYL_DUR_RX = re.compile(r'\|\s*\*{0,2}[Dd]uration\*{0,2}\s*\|\s*(\d+)\s*day', re.IGNORECASE)


def check_K():
    print("[K] Duration consistency...")

    mtp = MT / "training_management" / "MTP_MSS.md"
    mtp_days: dict[str, int] = {}
    if mtp.exists():
        for _, line in scan_lines(mtp, skip_archive=False):
            m = _MTP_ROW_RX.search(line)
            if m:
                code = m.group(1).upper()
                days = int(m.group(2))
                mtp_days[code] = days

    for code, canonical in CANONICAL_DAYS.items():
        # Check MTP
        if code in mtp_days:
            if mtp_days[code] != canonical:
                err("K:DURATION",
                    f"MTP_MSS: TM-{code} = {mtp_days[code]} days; "
                    f"canonical is {canonical} days",
                    mtp)
        else:
            # Only warn if TM-40/50 series (TM-10 duration is informal)
            if code not in ("10",):
                warn("K:DURATION",
                     f"MTP_MSS: TM-{code} not found in duration table")

        # Check syllabus
        syl = MT / "syllabi" / f"SYLLABUS_TM{code}.md"
        if not syl.exists():
            continue
        text = read_text(syl)
        m = _SYL_DUR_RX.search(text)
        if m:
            syl_days = int(m.group(1))
            if syl_days != canonical:
                err("K:DURATION",
                    f"SYLLABUS_TM{code}: {syl_days} days; canonical is {canonical} days",
                    syl)
        else:
            warn("K:DURATION",
                 f"SYLLABUS_TM{code}: no parseable duration field (looking for '| Duration | N days')",
                 syl)


# ─────────────────────────────────────────────────────────────────────────────
# CHECK L — CONCEPTS_GUIDE ↔ TM bidirectional reference
# ─────────────────────────────────────────────────────────────────────────────

def check_L():
    print("[L] CG↔TM bidirectional references...")

    for code, slug in {**WFF_TRACKS, **SPEC_TRACKS, **ADV_TRACKS}.items():
        s, l     = code[:2], code[2]
        base_dir = MT / "tm" / f"TM_{s}{l}_{slug}"
        tm_file  = base_dir / f"TM_{s}{l}_{slug.upper()}.md"
        cg_file  = base_dir / f"CONCEPTS_GUIDE_TM{s}{l}_{slug.upper()}.md"

        if not tm_file.exists() or not cg_file.exists():
            continue  # already caught by check A

        tm_text = read_text(tm_file)
        cg_text = read_text(cg_file)

        # TM should reference its CG (by stem or "Concepts Guide")
        cg_stem = f"CONCEPTS_GUIDE_TM{s}{l}"
        if cg_stem not in tm_text and "concepts guide" not in tm_text.lower():
            warn("L:TM-MISSING-CG-REF",
                 f"TM-{code} source does not reference its Concepts Guide",
                 tm_file)

        # CG should reference its TM (by track code or TM file stem)
        tm_stem = f"TM_{s}{l}_{slug.upper()}"
        if tm_stem not in cg_text and f"TM-{code}" not in cg_text:
            warn("L:CG-MISSING-TM-REF",
                 f"Concepts Guide for TM-{code} does not reference its TM",
                 cg_file)


# ─────────────────────────────────────────────────────────────────────────────
# CHECK M — Valid track code references in prose
# ─────────────────────────────────────────────────────────────────────────────

# Matches any TM-XX reference that is definitively NOT a valid track code
_INVALID_TRACK_RX = re.compile(
    r"\bTM[-\s]?("
    r"40[N-Zn-z]"        # TM-40 beyond M
    r"|50[A-Fa-f]"       # TM-50A–F (retired)
    r"|50[N-Zn-z]"       # TM-50 beyond M
    r"|[6-9]\d[A-Z]?"    # TM-60+ (hypothetical future)
    r")\b",
    re.IGNORECASE,
)


def check_M():
    print("[M] Valid track code references...")

    for fpath in all_md_files() + list(MT.rglob("*.html")):
        for lineno, line in scan_lines(fpath):
            # Skip negation statements that correctly explain retired codes
            if _NEGATION_50_RX.search(line):
                continue
            # Skip range notation in NOTES/disambiguation lines ("TM-50A–F do not exist")
            if re.search(r'TM[-\s]?50[A-F][–—-]', line, re.IGNORECASE):
                continue
            # Skip placeholder notation (TM-40X, TM-50X = "any track in series")
            if re.search(r'TM[-\s]?[45]0X\b', line, re.IGNORECASE):
                continue
            m = _INVALID_TRACK_RX.search(line)
            if m:
                err("M:INVALID-TRACK",
                    f"invalid/retired track code: '{m.group().strip()}'",
                    fpath, lineno)


# ─────────────────────────────────────────────────────────────────────────────
# CHECK N — Training management document coverage
# ─────────────────────────────────────────────────────────────────────────────

_TM_MGMT_FILES = {
    "TEO_MSS.md":                "N:TEO-COVERAGE",
    "POI_MSS.md":                "N:POI-COVERAGE",
    "MTP_MSS.md":                "N:MTP-COVERAGE",
    "FACULTY_DEVELOPMENT_PLAN.md": "N:FDP-COVERAGE",
    "CAD_MSS.md":                "N:CAD-COVERAGE",
}


def check_N():
    print("[N] Training management coverage...")

    for fname, cat in _TM_MGMT_FILES.items():
        fpath = MT / "training_management" / fname
        if not fpath.exists():
            continue
        text = read_text(fpath)
        for code in {**WFF_TRACKS, **SPEC_TRACKS}:
            # Accept "TM-40G", "TM 40G", or bare "40G" in a table
            if (f"TM-{code}" not in text and
                    f"TM {code}" not in text and
                    f"TM-{code[:-1]}{code[-1]}" not in text):
                warn(cat, f"{fname}: no reference to TM-{code}", fpath)


# ─────────────────────────────────────────────────────────────────────────────
# CHECK O — Terminology and formatting consistency
# ─────────────────────────────────────────────────────────────────────────────

def check_O():
    print("[O] Terminology & format consistency...")

    for fpath in all_md_files():
        text = read_text(fpath)
        if not text:
            continue

        # ── "TM XX" vs "TM-XX" mixed usage within the same file ──────────────
        # Army document identification numbers (e.g. "TM 20-MSS-BLD") use space format
        # by regulation — exclude those (pattern: TM NN-word or TM NN-NN).
        has_hyphen  = bool(re.search(r'\bTM-\d', text))
        # Space format as a TRACK REFERENCE (TM 40G, TM 20, etc.), not a doc number
        # Doc numbers: "TM 11-5820-890-10" style (digits-digits) — skip those
        has_space_ref = bool(re.search(r'\bTM\s+\d+[A-M]?\b(?!\s*-)', text))
        if has_hyphen and has_space_ref:
            warn("O:FORMAT",
                 "mixed 'TM-XX' and 'TM XX' formatting — standardize on 'TM-XX'",
                 fpath)

        # ── "pre-requisite" / "Pre-Requisite" should be "prerequisite" ────────
        if re.search(r'\bpre-requisite\b', text, re.IGNORECASE):
            warn("O:SPELLING",
                 "use 'prerequisite' not 'pre-requisite'",
                 fpath)

        # ── Foundry product-name capitalization ───────────────────────────────
        # "palantir foundry" (all lowercase) is a flag; "Palantir Foundry" is correct
        if re.search(r'\bpalantir foundry\b', text) and \
           not re.search(r'\bPalantir Foundry\b', text):
            warn("O:CAPITALIZATION",
                 "inconsistent capitalization of 'Palantir Foundry' (found lowercase instance)",
                 fpath)

        # ── "Maven Smart System" vs "maven smart system" ─────────────────────
        if re.search(r'\bmaven smart system\b', text) and \
           not re.search(r'\bMaven Smart System\b', text):
            warn("O:CAPITALIZATION",
                 "inconsistent capitalization of 'Maven Smart System'",
                 fpath)

        # ── MSS acronym consistency: first use should expand it ──────────────
        # (Check only if MSS is used but "Maven Smart System" never appears)
        if re.search(r'\bMSS\b', text) and \
           not re.search(r'Maven Smart System', text, re.IGNORECASE):
            info("O:ACRONYM",
                 "file uses 'MSS' but never expands to 'Maven Smart System'",
                 fpath)

        # ── Stale distribution label ──────────────────────────────────────────
        # If file says DRAFT in its header, flag for review before publication
        header = "\n".join(text.splitlines()[:20])
        if re.search(r'\bDRAFT\b', header):
            warn("O:DRAFT-LABEL",
                 "document header contains DRAFT label — confirm publication-ready status",
                 fpath)

        # ── Date currency: flag any year < 2024 in VERSION/DATE HEADER lines ───
        # Only scan first 15 lines — document metadata headers are always at the top.
        # This avoids false positives from changelog prose referencing historical years.
        for lineno, line in scan_lines(fpath):
            if lineno > 15:
                break
            if re.search(r"(?:version|date|published|updated|issued).*\b(20(?:1[0-9]|2[0-3]))\b",
                         line, re.IGNORECASE):
                warn("O:STALE-DATE",
                     f"possible stale date (year < 2024) in version/date line",
                     fpath, lineno)
                break  # one warning per file is enough


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

_CHECK_MAP = {
    "A": ("File completeness",          check_A),
    "B": ("Stale text references",      check_B),
    "C": ("PDF inventory",              check_C),
    "D": ("Prereq label accuracy",      check_D),
    "E": ("Syllabus structure",         check_E),
    "F": ("Exam structure",             check_F),
    "G": ("TM document structure",      check_G),
    "H": ("Broken internal links",      check_H),
    "I": ("Archive contamination",      check_I),
    "J": ("HTML correctness",           check_J),
    "K": ("Duration consistency",       check_K),
    "L": ("CG↔TM bidirectional refs",  check_L),
    "M": ("Valid track code refs",      check_M),
    "N": ("Training mgmt coverage",     check_N),
    "O": ("Terminology & format",       check_O),
}

_SEV_ORDER = {"ERROR": 0, "WARN": 1, "INFO": 2}
_SEV_ICON  = {"ERROR": "✗", "WARN": "⚠", "INFO": "·"}


def main():
    parser = argparse.ArgumentParser(
        description="Maven Training corpus deep audit",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Checks: " + ", ".join(f"{k}={v[0]}" for k, v in _CHECK_MAP.items()),
    )
    parser.add_argument("--errors-only", action="store_true",
                        help="Only display ERROR-level issues")
    parser.add_argument("--verbose", action="store_true",
                        help="Also display INFO-level items")
    parser.add_argument("--checks", metavar="A,B,C",
                        help="Comma-separated subset of checks to run (default: all)")
    args = parser.parse_args()

    enabled = (set(args.checks.upper().split(",")) if args.checks
               else set(_CHECK_MAP.keys()))

    print("=" * 72)
    print("  MAVEN TRAINING DEEP AUDIT — USAREUR-AF C2DAO Training Branch")
    print("=" * 72)
    print()

    for letter, (label, fn) in _CHECK_MAP.items():
        if letter in enabled:
            fn()

    print()
    print("=" * 72)

    if not _issues:
        print("✓  AUDIT PASSED — corpus is publication-ready.")
        return 0

    # ── Filter by requested severity ─────────────────────────────────────────
    if args.errors_only:
        filtered = [(s, c, m) for s, c, m in _issues if s == "ERROR"]
    elif not args.verbose:
        filtered = [(s, c, m) for s, c, m in _issues if s != "INFO"]
    else:
        filtered = list(_issues)

    if not filtered:
        print("✓  No issues at selected severity level.")
        return 0

    error_n = sum(1 for s, _, _ in filtered if s == "ERROR")
    warn_n  = sum(1 for s, _, _ in filtered if s == "WARN")
    info_n  = sum(1 for s, _, _ in filtered if s == "INFO")

    print(f"  {error_n} ERROR(S)   {warn_n} WARNING(S)   {info_n} INFO")
    print()

    # ── Group by severity then category ──────────────────────────────────────
    by_sev_cat: dict[tuple[str, str], list[str]] = defaultdict(list)
    for sev, cat, msg in filtered:
        by_sev_cat[(sev, cat)].append(msg)

    for (sev, cat), msgs in sorted(by_sev_cat.items(),
                                   key=lambda x: (_SEV_ORDER.get(x[0][0], 9), x[0])):
        icon = _SEV_ICON.get(sev, "?")
        print(f"  {icon} [{sev}] {cat}  ({len(msgs)} issue{'s' if len(msgs) > 1 else ''})")
        for m in msgs:
            print(f"        {m}")
        print()

    # ── Summary table ─────────────────────────────────────────────────────────
    print("-" * 72)
    print("  SUMMARY BY CHECK:")
    print()
    any_check_reported = False
    for letter, (label, _) in _CHECK_MAP.items():
        if letter not in enabled:
            continue
        check_issues = [(s, c, m) for s, c, m in filtered if c.startswith(f"{letter}:")]
        if not check_issues:
            continue
        any_check_reported = True
        has_error = any(s == "ERROR" for s, _, _ in check_issues)
        status_label = "FAIL" if has_error else "WARN"
        icon = "✗" if has_error else "⚠"
        print(f"  {icon}  {letter}: {label:<32} {len(check_issues):3d} issue(s)  [{status_label}]")

    if not any_check_reported:
        print("  (no issues to report)")

    print()
    if error_n > 0:
        print("✗  NOT PUBLICATION-READY — resolve all ERROR items before release.")
        return 2
    else:
        print("⚠  Review warnings before final publication release.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
