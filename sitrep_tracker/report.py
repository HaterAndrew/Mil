"""
SITREP report formatter — plain-text NATO-style output.
"""

from typing import Any


def format_sitrep(row: Any, events: list[Any] | None = None) -> str:
    """
    Render a SITREP record as a formatted plain-text report.
    Follows a simplified NATO SITREP structure.
    """
    sep = "=" * 60
    lines = [
        sep,
        f"SITUATION REPORT (SITREP) — ID: {row['id']}",
        sep,
        f"DTG:        {row['dtg']}",
        f"UNIT:       {row['unit']}",
        f"LOCATION:   {row['location']}",
        f"STATUS:     {row['status']}",
        "",
        "1. SITUATION",
        _block(row['situation']),
        "",
        "2. PERSONNEL STATUS",
        _block(row['personnel'] or "No PERSTATUS reported."),
        "",
        "3. EQUIPMENT STATUS",
        _block(row['equipment'] or "No EQPTSTATUS reported."),
        "",
        "4. SUSTAINMENT / LOGSTAT",
        _block(row['sustainment'] or "No LOGSTAT reported."),
        "",
        "5. ACTIONS TAKEN / IN PROGRESS",
        _block(row['actions'] or "None reported."),
        "",
        f"NEXT SITREP: {row['next_sitrep'] or 'TBD'}",
    ]

    if events:
        lines += ["", "EVENT LOG", "-" * 40]
        for ev in events:
            lines.append(f"  [{ev['dtg']}] ({ev['event_type']}) {ev['description']}")

    lines += [sep]
    return "\n".join(lines)


def _block(text: str, indent: int = 4) -> str:
    """Indent a block of text."""
    prefix = " " * indent
    return "\n".join(prefix + line for line in text.splitlines())
