"""
Tests for dtg.py — DTG parsing, formatting, and validation.
"""
import pytest
from dtg import now_dtg, parse_dtg, validate_dtg
from datetime import datetime, timezone


# ── now_dtg ───────────────────────────────────────────────────────────────────

def test_now_dtg_format():
    """now_dtg() must match DDHHMM Z MON YY pattern."""
    import re
    dtg = now_dtg()
    pattern = r"^\d{6}Z [A-Z]{3} \d{2}$"
    assert re.match(pattern, dtg), f"Unexpected DTG format: {dtg!r}"


def test_now_dtg_roundtrip():
    """now_dtg() output must survive a parse round-trip."""
    dtg = now_dtg()
    parsed = parse_dtg(dtg)
    assert parsed is not None
    assert parsed.tzinfo == timezone.utc


# ── parse_dtg ─────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("dtg_str, expected_day, expected_hour, expected_minute, expected_month, expected_year", [
    ("091435Z MAR 26", 9,  14, 35, 3,  2026),
    ("010000Z JAN 26", 1,  0,  0,  1,  2026),
    ("312359Z DEC 25", 31, 23, 59, 12, 2025),
    ("150600Z JUL 24", 15, 6,  0,  7,  2024),
])
def test_parse_dtg_valid(dtg_str, expected_day, expected_hour, expected_minute, expected_month, expected_year):
    result = parse_dtg(dtg_str)
    assert result is not None
    assert result.day    == expected_day
    assert result.hour   == expected_hour
    assert result.minute == expected_minute
    assert result.month  == expected_month
    assert result.year   == expected_year
    assert result.tzinfo == timezone.utc


@pytest.mark.parametrize("bad_dtg", [
    "",           # empty
    "NOTADTG",    # garbage
    "091435 MAR 26",   # missing Z
    "091435Z MARCH 26",  # full month name
    "091435Z MAR",      # missing year
    "9999Z MAR 26",    # wrong time format
    "091435Z ZZZ 26",  # invalid month
])
def test_parse_dtg_invalid_returns_none(bad_dtg):
    assert parse_dtg(bad_dtg) is None


# ── validate_dtg ──────────────────────────────────────────────────────────────

def test_validate_dtg_accepts_valid():
    assert validate_dtg("091435Z MAR 26") is True


def test_validate_dtg_rejects_invalid():
    assert validate_dtg("not a dtg") is False


def test_validate_dtg_empty():
    assert validate_dtg("") is False
