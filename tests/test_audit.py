"""Tests for scripts/audit.py — corpus audit checks.

Tests the audit logic using temp directory structures rather than
the live corpus, so tests are isolated and self-contained.
"""

import re
import textwrap
from pathlib import Path
from unittest.mock import patch

import pytest

# Import audit module — scripts/ is on sys.path via conftest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import audit


def _sl(code):
    """Convert internal code (e.g. '10', '40G') to SL display format (e.g. 'SL 1', 'SL 4G')."""
    num = code[:2]          # '10', '20', '30', '40', '50'
    letter = code[2:]       # '', 'G', 'H', etc.
    level = {"10": "1", "20": "2", "30": "3", "40": "4", "50": "5"}[num]
    return f"SL {level}{letter}"


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------
@pytest.fixture(autouse=True)
def reset_audit_state():
    """Clear issues list and skipped files counter between tests."""
    audit.issues.clear()
    audit._skipped_files = 0
    yield
    audit.issues.clear()
    audit._skipped_files = 0


@pytest.fixture
def corpus(tmp_path):
    """Build a minimal valid corpus structure under tmp_path."""
    mt = tmp_path / "maven_training"
    mt.mkdir()

    # Base TM dirs and files
    for code, slug in audit.BASE_TRACKS.items():
        d = mt / "tm" / f"TM_{code}_{slug}"
        d.mkdir(parents=True)
        (d / f"TM_{code}_{slug.upper()}.md").write_text(f"# {_sl(code)}\nPrerequisite: SL 1\n")

    # WFF + Spec + Adv TM dirs and files
    for code, slug in {**audit.WFF_TRACKS, **audit.SPEC_TRACKS, **audit.ADV_TRACKS}.items():
        fc = audit.fs_code(code)
        series, letter = fc[:2], fc[2]
        d = mt / "tm" / f"TM_{series}{letter}_{slug}"
        d.mkdir(parents=True)
        prereq = "SL 3" if code.startswith("4") or code.startswith("5") else "SL 1"
        (d / f"TM_{series}{letter}_{slug.upper()}.md").write_text(
            f"# {_sl(code)}\nPrerequisite: {prereq}\n"
        )
        (d / f"CONCEPTS_GUIDE_TM{series}{letter}_{slug.upper()}.md").write_text(f"# CG {_sl(code)}\n")

    # Syllabi
    syl_dir = mt / "syllabi"
    syl_dir.mkdir()
    for code in list(audit.BASE_TRACKS) + list(audit.WFF_TRACKS) + list(audit.SPEC_TRACKS) + list(audit.ADV_TRACKS):
        (syl_dir / f"SYLLABUS_TM{audit.fs_code(code)}.md").write_text(
            f"# Syllabus {_sl(code)}\nPrerequisite: SL 3\n"
        )

    # Exams
    exam_dir = mt / "exercises" / "exams"
    exam_dir.mkdir(parents=True)
    for code in list(audit.BASE_TRACKS) + list(audit.WFF_TRACKS) + list(audit.SPEC_TRACKS) + list(audit.ADV_TRACKS):
        fc = audit.fs_code(code)
        (exam_dir / f"EXAM_TM{fc}_PRE.md").write_text(f"# Exam PRE {_sl(code)}\n")
        if code == "10":
            (exam_dir / "EXAM_TM10_SUPPLEMENTAL.md").write_text("# Supplemental\n")
        else:
            (exam_dir / f"EXAM_TM{fc}_POST.md").write_text(f"# Exam POST {_sl(code)}\n")

    # Exercise dirs (base + WFF + spec, not advanced)
    ex_tracks = {
        "10": "operator_basics", "20": "no_code_builder", "30": "advanced_builder",
        **audit.WFF_TRACKS, **audit.SPEC_TRACKS,
    }
    for code, slug in ex_tracks.items():
        fc = audit.fs_code(code)
        ex_dir = mt / "exercises" / f"EX_{fc}_{slug}"
        ex_dir.mkdir(parents=True)
        (ex_dir / "EXERCISE.md").write_text(f"# Exercise {code}\n")
        (ex_dir / "ENVIRONMENT_SETUP.md").write_text(f"# Env setup {code}\n")

    # PDF dir (empty but present)
    (mt / "pdf").mkdir()

    # HTML files
    (mt / "mss_info_app").mkdir(parents=True)
    (mt / "mss_info_app" / "index.html").write_text("<html></html>")

    # README
    (tmp_path / "README.md").write_text("# Maven Training\n")

    return tmp_path


# ---------------------------------------------------------------------------
# Check 1 — File completeness
# ---------------------------------------------------------------------------
class TestCompleteness:
    def test_complete_corpus_passes(self, corpus):
        with patch.object(audit, "ROOT", corpus), patch.object(audit, "MT", corpus / "maven_training"):
            audit.check_completeness()
        assert len(audit.issues) == 0

    def test_missing_tm_file_flagged(self, corpus):
        # Remove one TM file
        target = corpus / "maven_training" / "tm" / "TM_40G_orsa" / "TM_40G_ORSA.md"
        target.unlink()
        with patch.object(audit, "ROOT", corpus), patch.object(audit, "MT", corpus / "maven_training"):
            audit.check_completeness()
        assert any("TM source: SL 4G" in msg for _, msg in audit.issues)

    def test_missing_syllabus_flagged(self, corpus):
        (corpus / "maven_training" / "syllabi" / "SYLLABUS_TM40H.md").unlink()
        with patch.object(audit, "ROOT", corpus), patch.object(audit, "MT", corpus / "maven_training"):
            audit.check_completeness()
        assert any("Syllabus: SL 4H" in msg for _, msg in audit.issues)

    def test_missing_exam_flagged(self, corpus):
        (corpus / "maven_training" / "exercises" / "exams" / "EXAM_TM30_POST.md").unlink()
        with patch.object(audit, "ROOT", corpus), patch.object(audit, "MT", corpus / "maven_training"):
            audit.check_completeness()
        assert any("Exam POST: SL 3" in msg for _, msg in audit.issues)

    def test_missing_exercise_flagged(self, corpus):
        (corpus / "maven_training" / "exercises" / "EX_20_no_code_builder" / "EXERCISE.md").unlink()
        with patch.object(audit, "ROOT", corpus), patch.object(audit, "MT", corpus / "maven_training"):
            audit.check_completeness()
        assert any("Exercise EXERCISE.md: EX_20" in msg for _, msg in audit.issues)


# ---------------------------------------------------------------------------
# Check 2 — Stale text references
# ---------------------------------------------------------------------------
class TestStaleRefs:
    def test_retired_50_series_flagged(self, corpus):
        stale_file = corpus / "maven_training" / "tm" / "TM_10_maven_user" / "TM_10_MAVEN_USER.md"
        stale_file.write_text("# SL 1\nStudents should complete SL 5A before this.\n")
        with patch.object(audit, "ROOT", corpus), patch.object(audit, "MT", corpus / "maven_training"):
            audit.check_stale_refs()
        assert any("SL 5A" in msg for _, msg in audit.issues)

    def test_negative_context_not_flagged(self, corpus):
        ok_file = corpus / "maven_training" / "tm" / "TM_10_maven_user" / "TM_10_MAVEN_USER.md"
        ok_file.write_text("# SL 1\nNote: SL 5A does not exist.\n")
        with patch.object(audit, "ROOT", corpus), patch.object(audit, "MT", corpus / "maven_training"):
            audit.check_stale_refs()
        # Should NOT be flagged because "not" is on the same line
        stale_issues = [msg for cat, msg in audit.issues if "SL 5A" in msg]
        assert len(stale_issues) == 0

    def test_archive_dir_skipped(self, corpus):
        arch = corpus / "maven_training" / "_archive" / "old.md"
        arch.parent.mkdir(parents=True)
        arch.write_text("SL 5B is great\n")
        with patch.object(audit, "ROOT", corpus), patch.object(audit, "MT", corpus / "maven_training"):
            audit.check_stale_refs()
        assert not any("SL 5B" in msg for _, msg in audit.issues)


# ---------------------------------------------------------------------------
# Check 5 — Prereq labels
# ---------------------------------------------------------------------------
class TestPrereqs:
    def test_wrong_specialist_prereq_flagged(self, corpus):
        tm_file = corpus / "maven_training" / "tm" / "TM_40G_orsa" / "TM_40G_ORSA.md"
        tm_file.write_text("# SL 4G ORSA\nPrerequisite: SL 2\n")
        with patch.object(audit, "ROOT", corpus), patch.object(audit, "MT", corpus / "maven_training"):
            audit.check_prereqs()
        assert any("SL 4G" in msg and "PREREQ" in cat for cat, msg in audit.issues)

    def test_correct_prereq_not_flagged(self, corpus):
        tm_file = corpus / "maven_training" / "tm" / "TM_40G_orsa" / "TM_40G_ORSA.md"
        tm_file.write_text("# SL 4G ORSA\nPrerequisite: SL 3\n")
        with patch.object(audit, "ROOT", corpus), patch.object(audit, "MT", corpus / "maven_training"):
            audit.check_prereqs()
        prereq_issues = [msg for cat, msg in audit.issues if cat == "PREREQ"]
        assert len(prereq_issues) == 0


# ---------------------------------------------------------------------------
# Check 7 — Syllabus prereq consistency
# ---------------------------------------------------------------------------
class TestSyllabusPrereqs:
    def test_wrong_syllabus_prereq_flagged(self, corpus):
        syl = corpus / "maven_training" / "syllabi" / "SYLLABUS_TM40G.md"
        syl.write_text("# Syllabus SL 4G\nPrerequisite: SL 2\n")
        with patch.object(audit, "ROOT", corpus), patch.object(audit, "MT", corpus / "maven_training"):
            audit.check_syllabus_prereqs()
        assert any("SYLLABUS PREREQ" in cat for cat, _ in audit.issues)

    def test_correct_syllabus_prereq_passes(self, corpus):
        syl = corpus / "maven_training" / "syllabi" / "SYLLABUS_TM40G.md"
        syl.write_text("# Syllabus SL 4G\nPrerequisite: SL 3\n")
        with patch.object(audit, "ROOT", corpus), patch.object(audit, "MT", corpus / "maven_training"):
            audit.check_syllabus_prereqs()
        syl_issues = [msg for cat, msg in audit.issues if cat == "SYLLABUS PREREQ"]
        assert len(syl_issues) == 0
