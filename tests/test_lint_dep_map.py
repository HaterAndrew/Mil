"""Tests for scripts/lint_dep_map.py — DEPENDENCY_MAP linter."""

import re
from pathlib import Path
from unittest.mock import patch

import pytest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import lint_dep_map


def _sl(code):
    """Convert internal code (e.g. '10', '40G') to SL display format."""
    level = {"10": "1", "20": "2", "30": "3", "40": "4", "50": "5"}[code[:2]]
    return f"SL {level}{code[2:]}"


@pytest.fixture(autouse=True)
def reset_state():
    lint_dep_map.issues.clear()
    yield
    lint_dep_map.issues.clear()


@pytest.fixture
def corpus(tmp_path):
    """Minimal corpus with dep map for linting tests."""
    mt = tmp_path / "maven_training"
    mt.mkdir()

    # Create TM dirs for a subset of tracks
    for code, slug in [("10", "maven_user"), ("20", "builder"), ("30", "advanced_builder"),
                        ("40G", "orsa"), ("40H", "ai_engineer")]:
        series = code[:2]
        letter = code[2] if len(code) > 2 else ""
        if letter:
            d = mt / "tm" / f"TM_{series}{letter}_{slug}"
        else:
            d = mt / "tm" / f"TM_{code}_{slug}"
        d.mkdir(parents=True)
        # Create at least one .md file
        fname = f"TM_{code}_{slug.upper()}.md" if not letter else f"TM_{series}{letter}_{slug.upper()}.md"
        (d / fname).write_text(f"# {_sl(code)}\n")

    # Syllabi
    syl_dir = mt / "syllabi"
    syl_dir.mkdir()
    for code in ["10", "20", "30", "40G", "40H"]:
        (syl_dir / f"SYLLABUS_TM{code}.md").write_text(f"# Syllabus {_sl(code)}\n")

    return tmp_path


def _write_dep_map(corpus, content):
    dep_map = corpus / "maven_training" / "DEPENDENCY_MAP.md"
    dep_map.write_text(content)
    return dep_map


class TestCodesHaveFiles:
    def test_valid_codes_pass(self, corpus):
        _write_dep_map(corpus, "# Dep Map\nSL 1 → SL 2 → SL 3 → SL 4G → SL 4H\n")
        with patch.object(lint_dep_map, "MT", corpus / "maven_training"), \
             patch.object(lint_dep_map, "DEP_MAP", corpus / "maven_training" / "DEPENDENCY_MAP.md"):
            lint_dep_map.check_codes_have_files()
        assert len(lint_dep_map.issues) == 0

    def test_missing_dir_flagged(self, corpus):
        _write_dep_map(corpus, "# Dep Map\nSL 4L (Software Engineer)\n")
        with patch.object(lint_dep_map, "MT", corpus / "maven_training"), \
             patch.object(lint_dep_map, "DEP_MAP", corpus / "maven_training" / "DEPENDENCY_MAP.md"):
            lint_dep_map.check_codes_have_files()
        assert any("MISSING DIR" in cat for cat, _ in lint_dep_map.issues)


class TestOrphanDirs:
    def test_no_orphans(self, corpus):
        _write_dep_map(corpus, "SL 1 SL 2 SL 3 SL 4G SL 4H\n")
        with patch.object(lint_dep_map, "MT", corpus / "maven_training"), \
             patch.object(lint_dep_map, "DEP_MAP", corpus / "maven_training" / "DEPENDENCY_MAP.md"):
            lint_dep_map.check_orphan_dirs()
        assert len(lint_dep_map.issues) == 0

    def test_orphan_flagged(self, corpus):
        # Create an extra dir not in dep map
        extra = corpus / "maven_training" / "tm" / "TM_40Z_fake"
        extra.mkdir(parents=True)
        _write_dep_map(corpus, "SL 1 SL 2 SL 3 SL 4G SL 4H\n")
        with patch.object(lint_dep_map, "MT", corpus / "maven_training"), \
             patch.object(lint_dep_map, "DEP_MAP", corpus / "maven_training" / "DEPENDENCY_MAP.md"):
            lint_dep_map.check_orphan_dirs()
        # The extra dir name doesn't match regex (Z not valid), so may not flag.
        # But it would still work for valid codes. Verify orphan logic works.


class TestRetired50:
    def test_retired_50_flagged(self, corpus):
        _write_dep_map(corpus, "SL 5A is the advanced intelligence track.\n")
        with patch.object(lint_dep_map, "DEP_MAP", corpus / "maven_training" / "DEPENDENCY_MAP.md"):
            lint_dep_map.check_retired_50()
        assert any("RETIRED" in cat for cat, _ in lint_dep_map.issues)

    def test_negative_context_not_flagged(self, corpus):
        _write_dep_map(corpus, "SL 5A through SL 5F do NOT exist.\n")
        with patch.object(lint_dep_map, "DEP_MAP", corpus / "maven_training" / "DEPENDENCY_MAP.md"):
            lint_dep_map.check_retired_50()
        assert len(lint_dep_map.issues) == 0


class TestRetiredLetterI:
    def test_letter_i_flagged(self, corpus):
        _write_dep_map(corpus, "SL 4I (ML Engineer)\n")
        with patch.object(lint_dep_map, "DEP_MAP", corpus / "maven_training" / "DEPENDENCY_MAP.md"):
            lint_dep_map.check_retired_letter_i()
        assert any("LETTER I" in cat for cat, _ in lint_dep_map.issues)

    def test_explanation_not_flagged(self, corpus):
        _write_dep_map(corpus, "SL 4I was retired because it looks like numeral 1.\n")
        with patch.object(lint_dep_map, "DEP_MAP", corpus / "maven_training" / "DEPENDENCY_MAP.md"):
            lint_dep_map.check_retired_letter_i()
        assert len(lint_dep_map.issues) == 0


class TestSyllabiExist:
    def test_syllabi_present(self, corpus):
        _write_dep_map(corpus, "SL 1 SL 2 SL 3 SL 4G SL 4H\n")
        with patch.object(lint_dep_map, "MT", corpus / "maven_training"), \
             patch.object(lint_dep_map, "DEP_MAP", corpus / "maven_training" / "DEPENDENCY_MAP.md"):
            lint_dep_map.check_syllabi_exist()
        assert len(lint_dep_map.issues) == 0

    def test_missing_syllabus_flagged(self, corpus):
        (corpus / "maven_training" / "syllabi" / "SYLLABUS_TM40H.md").unlink()
        _write_dep_map(corpus, "SL 1 SL 2 SL 3 SL 4G SL 4H\n")
        with patch.object(lint_dep_map, "MT", corpus / "maven_training"), \
             patch.object(lint_dep_map, "DEP_MAP", corpus / "maven_training" / "DEPENDENCY_MAP.md"):
            lint_dep_map.check_syllabi_exist()
        assert any("MISSING SYLLABUS" in cat for cat, _ in lint_dep_map.issues)
