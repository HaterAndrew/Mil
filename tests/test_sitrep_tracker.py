"""
Tests for sitrep_tracker — SITREP and event CRUD, FK enforcement,
status constraints, and filtering.
"""
import pytest
import sqlite3
import db


# ── Helpers ───────────────────────────────────────────────────────────────────

def make_sitrep(**overrides) -> dict:
    """Return a minimal valid SITREP payload, with optional field overrides."""
    base = {
        "dtg":         "091435Z MAR 26",
        "unit":        "2-34 AR",
        "location":    "YU 4512 8834",
        "status":      "OPEN",
        "situation":   "Screen ops along PL IRON.",
        "personnel":   None,
        "equipment":   None,
        "sustainment": None,
        "actions":     None,
        "next_sitrep": None,
    }
    base.update(overrides)
    return base


# ── Insert / retrieve ─────────────────────────────────────────────────────────

def test_insert_and_retrieve_sitrep():
    sid = db.insert_sitrep(make_sitrep())
    assert sid is not None and sid > 0

    row = db.get_sitrep(sid)
    assert row is not None
    assert row["unit"] == "2-34 AR"
    assert row["status"] == "OPEN"
    assert row["dtg"] == "091435Z MAR 26"


def test_get_sitrep_missing_returns_none():
    assert db.get_sitrep(99999) is None


def test_insert_multiple_sitreps_unique_ids():
    id1 = db.insert_sitrep(make_sitrep(unit="1-36 IN"))
    id2 = db.insert_sitrep(make_sitrep(unit="2-34 AR"))
    assert id1 != id2


# ── Status update ─────────────────────────────────────────────────────────────

@pytest.mark.parametrize("new_status", ["OPEN", "PENDING", "CLOSED"])
def test_update_sitrep_status_valid(new_status):
    sid = db.insert_sitrep(make_sitrep())
    db.update_sitrep_status(sid, new_status)
    assert db.get_sitrep(sid)["status"] == new_status


def test_status_check_constraint_rejects_invalid():
    """DB-level CHECK constraint must reject values outside OPEN/PENDING/CLOSED."""
    sid = db.insert_sitrep(make_sitrep())
    with pytest.raises(sqlite3.IntegrityError):
        with db.get_conn() as conn:
            conn.execute("UPDATE sitreps SET status = ? WHERE id = ?", ("BOGUS", sid))


# ── List / filtering ──────────────────────────────────────────────────────────

def test_list_sitreps_returns_all():
    db.insert_sitrep(make_sitrep(unit="UNIT-1"))
    db.insert_sitrep(make_sitrep(unit="UNIT-2"))
    rows = db.list_sitreps()
    assert len(rows) == 2


def test_list_sitreps_status_filter():
    db.insert_sitrep(make_sitrep(unit="A", status="OPEN"))
    db.insert_sitrep(make_sitrep(unit="B", status="CLOSED"))
    open_rows = db.list_sitreps(status_filter="OPEN")
    assert len(open_rows) == 1
    assert open_rows[0]["unit"] == "A"


def test_list_sitreps_unit_filter_partial_match():
    db.insert_sitrep(make_sitrep(unit="2-34 AR"))
    db.insert_sitrep(make_sitrep(unit="1-36 IN"))
    rows = db.list_sitreps(unit_filter="AR")
    assert len(rows) == 1
    assert rows[0]["unit"] == "2-34 AR"


def test_list_sitreps_limit():
    for i in range(10):
        db.insert_sitrep(make_sitrep(unit=f"UNIT-{i}"))
    rows = db.list_sitreps(limit=3)
    assert len(rows) == 3


# ── Events ────────────────────────────────────────────────────────────────────

def test_insert_and_retrieve_event():
    sid = db.insert_sitrep(make_sitrep())
    eid = db.insert_event(sid, "091435Z MAR 26", "CONTACT", "Possible UAS observed.")
    assert eid > 0

    events = db.get_events(sid)
    assert len(events) == 1
    assert events[0]["event_type"] == "CONTACT"
    assert events[0]["sitrep_id"] == sid


def test_get_events_empty_for_new_sitrep():
    sid = db.insert_sitrep(make_sitrep())
    assert db.get_events(sid) == []


def test_events_ordered_by_dtg():
    sid = db.insert_sitrep(make_sitrep())
    db.insert_event(sid, "091800Z MAR 26", "MOVEMENT", "Second event.")
    db.insert_event(sid, "091200Z MAR 26", "LOGSTAT", "First event.")
    events = db.get_events(sid)
    assert events[0]["dtg"] == "091200Z MAR 26"
    assert events[1]["dtg"] == "091800Z MAR 26"


# ── Foreign key enforcement ───────────────────────────────────────────────────

def test_fk_enforcement_rejects_orphaned_event():
    """FK PRAGMA must prevent inserting an event for a non-existent SITREP."""
    with pytest.raises(sqlite3.IntegrityError):
        db.insert_event(99999, "091435Z MAR 26", "OTHER", "Orphaned event.")


# ── Timestamps ────────────────────────────────────────────────────────────────

def test_created_at_populated_on_insert():
    sid = db.insert_sitrep(make_sitrep())
    row = db.get_sitrep(sid)
    assert row["created_at"] is not None


def test_updated_at_changes_on_status_update():
    import time
    sid = db.insert_sitrep(make_sitrep())
    before = db.get_sitrep(sid)["updated_at"]
    time.sleep(1.1)  # SQLite datetime() resolution is 1 second
    db.update_sitrep_status(sid, "CLOSED")
    after = db.get_sitrep(sid)["updated_at"]
    assert after > before
