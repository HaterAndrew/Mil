"""
SITREP Tracker — CLI entry point.
Usage: python cli.py [COMMAND] [OPTIONS]
"""

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box

from db import init_db, insert_sitrep, get_sitrep, list_sitreps, update_sitrep_status, insert_event, get_events
from dtg import now_dtg, validate_dtg
from report import format_sitrep

console = Console()

STATUS_COLORS = {
    "OPEN":    "green",
    "PENDING": "yellow",
    "CLOSED":  "red",
}


@click.group()
def cli():
    """SITREP Tracker — USAREUR-AF Operational Data Tool"""
    init_db()


# ---------------------------------------------------------------------------
# NEW SITREP
# ---------------------------------------------------------------------------

@cli.command("new")
@click.option("--unit",        prompt="Reporting Unit",     help="Unit identifier (e.g. 2-34 AR)")
@click.option("--location",    prompt="Location / Grid",    help="Current location or MGRS grid")
@click.option("--situation",   prompt="Situation Summary",  help="Current situation narrative")
@click.option("--personnel",   default="", prompt="Personnel Status (PERSTATUS)", help="e.g. 4x WIA, 0x KIA")
@click.option("--equipment",   default="", prompt="Equipment Status",             help="Equipment readiness summary")
@click.option("--sustainment", default="", prompt="Sustainment / LOGSTAT",        help="Logistics / sustainment status")
@click.option("--actions",     default="", prompt="Actions Taken / In Progress",  help="Current and completed actions")
@click.option("--next",        default="", prompt="Next SITREP DTG (blank=TBD)",  help="DTG of next SITREP")
@click.option("--dtg",         default="", help="Override DTG (auto-generated if blank)")
def new_sitrep(unit, location, situation, personnel, equipment, sustainment, actions, next, dtg):
    """Submit a new SITREP."""
    dtg_val = dtg.strip() if dtg.strip() else now_dtg()
    if dtg.strip() and not validate_dtg(dtg.strip()):
        console.print("[red]Invalid DTG format. Use: DDHHMM Z MON YY (e.g. 091435Z MAR 26)[/red]")
        raise SystemExit(1)

    sitrep_id = insert_sitrep({
        "dtg":         dtg_val,
        "unit":        unit.strip().upper(),
        "location":    location.strip().upper(),
        "status":      "OPEN",
        "situation":   situation.strip(),
        "personnel":   personnel.strip() or None,
        "equipment":   equipment.strip() or None,
        "sustainment": sustainment.strip() or None,
        "actions":     actions.strip() or None,
        "next_sitrep": next.strip() or None,
    })

    console.print(Panel(
        f"[green]SITREP submitted.[/green]\nID: [bold]{sitrep_id}[/bold]  DTG: [bold]{dtg_val}[/bold]",
        title="[bold green]SITREP ACCEPTED[/bold green]",
        border_style="green"
    ))


# ---------------------------------------------------------------------------
# LIST SITREPS
# ---------------------------------------------------------------------------

@cli.command("list")
@click.option("--status", default=None, help="Filter by status: OPEN | PENDING | CLOSED")
@click.option("--unit",   default=None, help="Filter by unit name (partial match)")
@click.option("--limit",  default=25,   help="Max rows to return (default 25)")
def list_cmd(status, unit, limit):
    """List SITREPs in tabular format."""
    rows = list_sitreps(status_filter=status, unit_filter=unit, limit=limit)

    if not rows:
        console.print("[yellow]No SITREPs found.[/yellow]")
        return

    table = Table(title="SITREP LOG", box=box.SIMPLE_HEAVY, show_lines=False)
    table.add_column("ID",       style="dim",    width=5)
    table.add_column("DTG",      style="cyan",   width=18)
    table.add_column("UNIT",     style="bold",   width=14)
    table.add_column("LOCATION", width=16)
    table.add_column("STATUS",   width=9)
    table.add_column("SITUATION", max_width=40)

    for r in rows:
        color = STATUS_COLORS.get(r["status"], "white")
        status_text = Text(r["status"], style=color)
        situation_snippet = (r["situation"][:60] + "…") if len(r["situation"]) > 60 else r["situation"]
        table.add_row(
            str(r["id"]),
            r["dtg"],
            r["unit"],
            r["location"],
            status_text,
            situation_snippet,
        )

    console.print(table)
    console.print(f"[dim]{len(rows)} record(s) returned.[/dim]")


# ---------------------------------------------------------------------------
# VIEW SITREP
# ---------------------------------------------------------------------------

@cli.command("view")
@click.argument("sitrep_id", type=int)
@click.option("--events", is_flag=True, default=False, help="Include event log")
def view_cmd(sitrep_id, events):
    """Display a full SITREP report by ID."""
    row = get_sitrep(sitrep_id)
    if not row:
        console.print(f"[red]SITREP ID {sitrep_id} not found.[/red]")
        raise SystemExit(1)

    ev_rows = get_events(sitrep_id) if events else []
    report = format_sitrep(row, ev_rows if events else None)
    console.print(report)


# ---------------------------------------------------------------------------
# UPDATE STATUS
# ---------------------------------------------------------------------------

@cli.command("status")
@click.argument("sitrep_id", type=int)
@click.argument("new_status", type=click.Choice(["OPEN","PENDING","CLOSED"], case_sensitive=False))
def status_cmd(sitrep_id, new_status):
    """Update the status of an existing SITREP."""
    row = get_sitrep(sitrep_id)
    if not row:
        console.print(f"[red]SITREP ID {sitrep_id} not found.[/red]")
        raise SystemExit(1)

    update_sitrep_status(sitrep_id, new_status)
    color = STATUS_COLORS.get(new_status.upper(), "white")
    console.print(f"SITREP [bold]{sitrep_id}[/bold] status → [{color}]{new_status.upper()}[/{color}]")


# ---------------------------------------------------------------------------
# LOG EVENT
# ---------------------------------------------------------------------------

@cli.command("event")
@click.argument("sitrep_id", type=int)
@click.option("--type",   "event_type", prompt="Event Type (CONTACT/MOVEMENT/LOGSTAT/CASEVAC/OTHER)",
              type=click.Choice(["CONTACT","MOVEMENT","LOGSTAT","CASEVAC","OTHER"], case_sensitive=False))
@click.option("--desc",   prompt="Description", help="Event description")
@click.option("--dtg",    default="", help="DTG of event (auto-generated if blank)")
def event_cmd(sitrep_id, event_type, desc, dtg):
    """Log an event against an existing SITREP."""
    row = get_sitrep(sitrep_id)
    if not row:
        console.print(f"[red]SITREP ID {sitrep_id} not found.[/red]")
        raise SystemExit(1)

    dtg_val = dtg.strip() if dtg.strip() else now_dtg()
    if dtg.strip() and not validate_dtg(dtg.strip()):
        console.print("[red]Invalid DTG format.[/red]")
        raise SystemExit(1)

    ev_id = insert_event(sitrep_id, dtg_val, event_type, desc.strip())
    console.print(f"Event [bold]{ev_id}[/bold] logged against SITREP [bold]{sitrep_id}[/bold] [{event_type.upper()}]")


# ---------------------------------------------------------------------------
# EXPORT
# ---------------------------------------------------------------------------

@cli.command("export")
@click.argument("sitrep_id", type=int)
@click.argument("outfile", type=click.Path())
@click.option("--events", is_flag=True, default=False, help="Include event log")
def export_cmd(sitrep_id, outfile, events):
    """Export a SITREP report to a plain-text file."""
    row = get_sitrep(sitrep_id)
    if not row:
        console.print(f"[red]SITREP ID {sitrep_id} not found.[/red]")
        raise SystemExit(1)

    ev_rows = get_events(sitrep_id) if events else []
    report = format_sitrep(row, ev_rows if events else None)

    with open(outfile, "w") as f:
        f.write(report + "\n")

    console.print(f"[green]Exported SITREP {sitrep_id} → {outfile}[/green]")


# ---------------------------------------------------------------------------
# DTG HELPER
# ---------------------------------------------------------------------------

@cli.command("dtg")
def dtg_cmd():
    """Print the current UTC DTG."""
    console.print(f"[cyan]{now_dtg()}[/cyan]")


if __name__ == "__main__":
    cli()
