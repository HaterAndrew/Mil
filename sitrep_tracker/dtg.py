"""
DTG (Date-Time Group) utilities.
Military format: DDHHMM Z MON YY  e.g. 091435Z MAR 26
"""

from datetime import datetime, timezone

MONTHS = ["JAN","FEB","MAR","APR","MAY","JUN",
          "JUL","AUG","SEP","OCT","NOV","DEC"]


def now_dtg() -> str:
    """Return current UTC time as a DTG string."""
    utc = datetime.now(timezone.utc)
    return f"{utc.day:02d}{utc.hour:02d}{utc.minute:02d}Z {MONTHS[utc.month-1]} {str(utc.year)[2:]}"


def parse_dtg(dtg: str) -> datetime | None:
    """Parse a DTG string back to a datetime (UTC). Returns None on failure."""
    try:
        parts = dtg.strip().split()
        # parts: ['091435Z', 'MAR', '26']
        raw = parts[0].rstrip("Z")
        day = int(raw[0:2])
        hour = int(raw[2:4])
        minute = int(raw[4:6])
        month = MONTHS.index(parts[1].upper()) + 1
        year = 2000 + int(parts[2])
        return datetime(year, month, day, hour, minute, tzinfo=timezone.utc)
    except Exception:
        return None


def validate_dtg(dtg: str) -> bool:
    return parse_dtg(dtg) is not None
