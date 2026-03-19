"""
Database layer for SITREP Tracker.
Uses SQLite for local persistence — no external dependencies.
"""

import sqlite3
import os
from pathlib import Path

DB_PATH = Path(os.environ.get("SITREP_DB", Path.home() / ".sitrep_tracker.db"))


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    with get_conn() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS sitreps (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                dtg         TEXT NOT NULL,          -- Date-Time Group (DDHHMM Z MON YY)
                unit        TEXT NOT NULL,          -- Reporting unit
                location    TEXT NOT NULL,          -- Current location / grid
                status      TEXT NOT NULL DEFAULT 'OPEN' CHECK(status IN ('OPEN','PENDING','CLOSED')),
                situation   TEXT NOT NULL,          -- Situation summary
                personnel   TEXT,                   -- PERSTATUS (e.g. 4x WIA, 0x KIA)
                equipment   TEXT,                   -- Equipment status
                sustainment TEXT,                   -- Sustainment / logistics
                actions     TEXT,                   -- Actions taken / in progress
                next_sitrep TEXT,                   -- DTG of next planned SITREP
                created_at  TEXT DEFAULT (datetime('now')),
                updated_at  TEXT DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS events (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                sitrep_id   INTEGER NOT NULL REFERENCES sitreps(id),
                dtg         TEXT NOT NULL,
                event_type  TEXT NOT NULL,   -- CONTACT | MOVEMENT | LOGSTAT | CASEVAC | OTHER
                description TEXT NOT NULL,
                created_at  TEXT DEFAULT (datetime('now'))
            );

            CREATE TRIGGER IF NOT EXISTS sitreps_updated_at
            AFTER UPDATE ON sitreps
            BEGIN
                UPDATE sitreps SET updated_at = datetime('now') WHERE id = NEW.id;
            END;
        """)


def insert_sitrep(data: dict) -> int:
    with get_conn() as conn:
        cur = conn.execute("""
            INSERT INTO sitreps (dtg, unit, location, status, situation,
                                 personnel, equipment, sustainment, actions, next_sitrep)
            VALUES (:dtg, :unit, :location, :status, :situation,
                    :personnel, :equipment, :sustainment, :actions, :next_sitrep)
        """, data)
        return cur.lastrowid


def get_sitrep(sitrep_id: int) -> sqlite3.Row | None:
    with get_conn() as conn:
        return conn.execute("SELECT * FROM sitreps WHERE id = ?", (sitrep_id,)).fetchone()


def list_sitreps(status_filter: str | None = None, unit_filter: str | None = None,
                 limit: int = 50) -> list[sqlite3.Row]:
    query = "SELECT * FROM sitreps WHERE 1=1"
    params: list = []
    if status_filter:
        query += " AND status = ?"
        params.append(status_filter.upper())
    if unit_filter:
        query += " AND unit LIKE ?"
        params.append(f"%{unit_filter}%")
    query += " ORDER BY created_at DESC LIMIT ?"
    params.append(limit)
    with get_conn() as conn:
        return conn.execute(query, params).fetchall()


def update_sitrep_status(sitrep_id: int, status: str):
    with get_conn() as conn:
        conn.execute("UPDATE sitreps SET status = ? WHERE id = ?",
                     (status.upper(), sitrep_id))


def insert_event(sitrep_id: int, dtg: str, event_type: str, description: str) -> int:
    with get_conn() as conn:
        cur = conn.execute("""
            INSERT INTO events (sitrep_id, dtg, event_type, description)
            VALUES (?, ?, ?, ?)
        """, (sitrep_id, dtg, event_type.upper(), description))
        return cur.lastrowid


def get_events(sitrep_id: int) -> list[sqlite3.Row]:
    with get_conn() as conn:
        return conn.execute(
            "SELECT * FROM events WHERE sitrep_id = ? ORDER BY dtg ASC",
            (sitrep_id,)
        ).fetchall()
