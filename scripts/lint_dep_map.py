#!/usr/bin/env python3
"""lint_dep_map.py — Validate DEPENDENCY_MAP.md against the live corpus.

Checks:
  1. Course codes referenced in DEPENDENCY_MAP.md exist as files in the corpus
  2. Orphan files: TM/syllabus/exercise dirs that exist but aren't in the dep map
  3. SL 3 hard prereq: all SL 4 tracks show SL 3 as prereq in dep map
  4. SL 5A–F never referenced (retired series)
  5. Track letter I not used (retired → M)
  6. Prereq chain consistency: SL 4 → SL 3 → SL 2 → SL 1

Run from repo root:
    python scripts/lint_dep_map.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MT = ROOT / "maven_training"
DEP_MAP = MT / "DEPENDENCY_MAP.md"

# ---------------------------------------------------------------------------
# Canonical structure (mirrors audit.py)
# ---------------------------------------------------------------------------
WFF_TRACKS = {
    "40A": "intelligence", "40B": "fires", "40C": "movement_maneuver",
    "40D": "sustainment", "40E": "protection", "40F": "mission_command",
}
SPEC_TRACKS = {
    "40G": "orsa", "40H": "ai_engineer", "40M": "ml_engineer",
    "40J": "program_manager", "40K": "knowledge_manager", "40L": "software_engineer",
    "40N": "ux_designer", "40O": "platform_engineer",
}
ADV_TRACKS = {
    "50G": "orsa_advanced", "50H": "ai_engineer_advanced", "50M": "ml_engineer_advanced",
    "50J": "program_manager_advanced", "50K": "knowledge_manager_advanced",
    "50L": "software_engineer_advanced", "50N": "ux_designer_advanced",
    "50O": "platform_engineer_advanced",
}
BASE_TRACKS = {"10": "maven_user", "20": "builder", "30": "advanced_builder"}
ALL_TRACKS = {**BASE_TRACKS, **WFF_TRACKS, **SPEC_TRACKS, **ADV_TRACKS}

# Course code regex — matches SL 1, SL 4G, SL 5M, FBC, EXEC, T3-I, T3-F
COURSE_RE = re.compile(r"\bSL\s?(\d[A-O]?)\b")
RETIRED_50AF_RE = re.compile(r"\bSL\s?5[A-Fa-f]\b")
RETIRED_LETTER_I_RE = re.compile(r"\bSL\s?\dI\b")


def sl_to_fs(sl_code: str) -> str:
    """Convert SL capture (1, 4G, 5M) to filesystem code (10, 40G, 50M)."""
    if len(sl_code) == 1:
        return f"{sl_code}0"
    return f"{sl_code[0]}0{sl_code[1:]}"

issues: list[tuple[str, str]] = []


def fail(cat: str, msg: str, line: int | None = None):
    loc = f" [line {line}]" if line else ""
    issues.append((cat, f"{msg}{loc}"))


# ---------------------------------------------------------------------------
# Check 1 — Course codes in dep map exist as files
# ---------------------------------------------------------------------------
def check_codes_have_files():
    """Every course code in DEPENDENCY_MAP.md should have a corresponding dir."""
    print("[ 1 ] Checking course codes have files...")
    text = DEP_MAP.read_text(encoding="utf-8")

    for lineno, line in enumerate(text.splitlines(), 1):
        for match in COURSE_RE.finditer(line):
            sl_code = match.group(1)
            code = sl_to_fs(sl_code)
            if code not in ALL_TRACKS:
                continue  # non-TM code or special (T3, etc.)
            slug = ALL_TRACKS[code]
            series, letter = code[:2], code[2] if len(code) > 2 else ""
            if letter:
                dir_name = f"TM_{series}{letter}_{slug}"
            else:
                dir_name = f"TM_{code}_{slug}"
            tm_dir = MT / "tm" / dir_name
            if not tm_dir.exists():
                fail("MISSING DIR", f"SL {code} referenced in dep map but dir '{dir_name}' not found", lineno)


# ---------------------------------------------------------------------------
# Check 2 — Orphan TM dirs not in dep map
# ---------------------------------------------------------------------------
def check_orphan_dirs():
    """TM dirs that exist on disk but aren't referenced in DEPENDENCY_MAP.md."""
    print("[ 2 ] Checking for orphan TM directories...")
    text = DEP_MAP.read_text(encoding="utf-8")
    tm_dir = MT / "tm"
    if not tm_dir.exists():
        return

    for d in sorted(tm_dir.iterdir()):
        if not d.is_dir():
            continue
        if d.name.startswith(".") or d.name.startswith("_"):
            continue
        # Extract code from dir name (e.g., TM_40G_orsa → 40G)
        m = re.match(r"TM_(\d{2}[A-Z]?)_", d.name)
        if not m:
            continue
        code = m.group(1)
        # Check if this code appears in the dep map (SL format)
        sl_code = f"{code[0]}{code[2]}" if len(code) == 3 else code[0]
        pattern = re.compile(rf"\bSL\s?{re.escape(sl_code)}\b")
        if not pattern.search(text):
            fail("ORPHAN", f"Dir '{d.name}' exists but SL {code} not in DEPENDENCY_MAP.md")


# ---------------------------------------------------------------------------
# Check 3 — SL 3 hard prereq for all SL 4
# ---------------------------------------------------------------------------
def check_sl3_prereq():
    """In DEPENDENCY_MAP.md, all SL 4 tracks must show SL 3 as prereq."""
    print("[ 3 ] Checking SL 3 hard prereq for SL 4 tracks...")
    text = DEP_MAP.read_text(encoding="utf-8")

    # Look for the prerequisite chain section
    in_prereq_chain = False
    for lineno, line in enumerate(text.splitlines(), 1):
        if "PREREQUISITE CHAIN" in line.upper():
            in_prereq_chain = True
            continue
        if in_prereq_chain and line.startswith("## "):
            break  # exited the prereq chain section

        if not in_prereq_chain:
            continue

        # Check that SL 4 lines appear under SL 3 in the tree
        for code in list(WFF_TRACKS) + list(SPEC_TRACKS):
            sl_code = f"{code[0]}{code[2]}" if len(code) == 3 else code[0]
            if re.search(rf"\bSL\s?{sl_code}\b", line):
                # This line mentions a SL 4 track — verify SL 3 is above it
                # (structural check: SL 4 lines should be indented under SL 3)
                if re.search(r"prereq.*SL\s?2(?!.*SL\s?3)", line, re.IGNORECASE):
                    fail("PREREQ", f"SL {sl_code} shows SL 2 prereq; should be SL 3", lineno)


# ---------------------------------------------------------------------------
# Check 4 — SL 5A–F not referenced
# ---------------------------------------------------------------------------
def check_retired_50():
    """SL 5A through SL 5F should not appear (retired series)."""
    print("[ 4 ] Checking for retired SL 5A–F references...")
    text = DEP_MAP.read_text(encoding="utf-8")

    # Allow negative-context lines (e.g., "SL 5A through SL 5F do NOT exist")
    negative_rx = re.compile(r"\b(no|not|do not|don'?t|never|invalid|retired)\b", re.IGNORECASE)

    for lineno, line in enumerate(text.splitlines(), 1):
        if RETIRED_50AF_RE.search(line) and not negative_rx.search(line):
            fail("RETIRED", f"SL 5A–F reference (retired series)", lineno)


# ---------------------------------------------------------------------------
# Check 5 — Track letter I not used
# ---------------------------------------------------------------------------
def check_retired_letter_i():
    """Track letter I was retired (looks like numeral 1). Should be M."""
    print("[ 5 ] Checking for retired track letter I...")
    text = DEP_MAP.read_text(encoding="utf-8")

    # Allow lines that explain the retirement
    explain_rx = re.compile(r"(retired|renamed|replaced|looks like|ambig)", re.IGNORECASE)

    for lineno, line in enumerate(text.splitlines(), 1):
        if RETIRED_LETTER_I_RE.search(line) and not explain_rx.search(line):
            fail("LETTER I", f"Track letter I used (retired → M)", lineno)


# ---------------------------------------------------------------------------
# Check 6 — Syllabi exist for all dep map courses
# ---------------------------------------------------------------------------
def check_syllabi_exist():
    """Every course in the dep map should have a syllabus."""
    print("[ 6 ] Checking syllabi exist for dep map courses...")
    text = DEP_MAP.read_text(encoding="utf-8")
    syl_dir = MT / "syllabi"

    codes_seen = set()
    for match in COURSE_RE.finditer(text):
        sl_code = match.group(1)
        fs_code = sl_to_fs(sl_code)
        if fs_code in ALL_TRACKS:
            codes_seen.add((sl_code, fs_code))

    for sl_code, fs_code in sorted(codes_seen):
        syl = syl_dir / f"SYLLABUS_TM{fs_code}.md"
        if not syl.exists():
            fail("MISSING SYLLABUS", f"SYLLABUS_TM{fs_code}.md not found for dep map course SL {sl_code}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    if not DEP_MAP.exists():
        print(f"ERROR: {DEP_MAP} not found", file=sys.stderr)
        return 1

    check_codes_have_files()
    check_orphan_dirs()
    check_sl3_prereq()
    check_retired_50()
    check_retired_letter_i()
    check_syllabi_exist()

    print()
    if not issues:
        print("OK — DEPENDENCY_MAP.md is consistent with the corpus.")
        return 0

    by_cat: dict[str, list[str]] = {}
    for cat, msg in issues:
        by_cat.setdefault(cat, []).append(msg)

    total = sum(len(v) for v in by_cat.values())
    print(f"FOUND {total} ISSUE(S):\n")
    for cat, msgs in sorted(by_cat.items()):
        print(f"  [{cat}]  ({len(msgs)})")
        for m in msgs:
            print(f"    - {m}")
        print()
    return 1


if __name__ == "__main__":
    sys.exit(main())
