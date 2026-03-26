"""MTT Scheduler — Streamlit dashboard.

Theater-wide Mobile Training Team scheduling tool for managing MSS training
events, instructor assignments, venue/resource allocation, and enrollment
across the USAREUR-AF AOR.
"""

from __future__ import annotations

import os
import sys
from datetime import date, timedelta
from pathlib import Path

# Ensure parent package is importable when Streamlit runs this file directly
_app_dir = Path(__file__).resolve().parent
if str(_app_dir.parent) not in sys.path:
    sys.path.insert(0, str(_app_dir.parent))

import pandas as pd
import streamlit as st

try:
    import plotly.express as px
    import plotly.graph_objects as go
    HAS_PLOTLY = True
except ImportError:
    HAS_PLOTLY = False

from mtt_scheduler.db import (
    Enrollment,
    Event,
    Instructor,
    SessionLocal,
    Venue,
    check_instructor_conflicts,
    get_calendar_data,
    get_capacity_utilization,
    get_location_summary,
    init_db,
)

from theme import (
    apply_plotly_theme,
    inject_branding,
    NAVY,
    NAVY_DARK,
    NAVY_LIGHT,
    NAVY_MID,
    GOLD,
    GOLD_DARK,
    GOLD_LIGHT,
    RAG_GREEN,
    RAG_AMBER,
    RAG_RED,
    GRAY_400,
    GRAY_700,
    WARNING_RED,
    CAUTION_AMBER,
    WHITE,
)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
API_BASE = os.environ.get("MTT_SCHEDULER_API_URL", "http://localhost:8005")

st.set_page_config(
    page_title="MTT Scheduler",
    page_icon="\U0001F4C5",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_branding("MTT Scheduler")

# Status color map
STATUS_COLORS = {
    "PLANNED": NAVY_MID,
    "ACTIVE": RAG_GREEN,
    "COMPLETE": GOLD,
    "CANCELLED": RAG_RED,
}

# ---------------------------------------------------------------------------
# Direct DB access for dashboard (avoids API round-trips for analytics)
# ---------------------------------------------------------------------------
init_db()


@st.cache_data(ttl=30)
def load_calendar_data():
    db = SessionLocal()
    try:
        return get_calendar_data(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_conflicts():
    db = SessionLocal()
    try:
        return check_instructor_conflicts(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_utilization():
    db = SessionLocal()
    try:
        return get_capacity_utilization(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_location_summary():
    db = SessionLocal()
    try:
        return get_location_summary(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_events():
    db = SessionLocal()
    try:
        events = db.query(Event).order_by(Event.start_date).all()
        results = []
        for ev in events:
            enrolled = len([e for e in ev.enrollments if e.status != "DROPPED"])
            instructor_names = [f"{i.rank} {i.name}" for i in ev.instructors]
            venue_name = ev.venue.name if ev.venue else "TBD"
            results.append({
                "id": ev.id,
                "name": ev.name,
                "course_id": ev.course_id,
                "location": ev.location,
                "venue": venue_name,
                "start_date": ev.start_date,
                "end_date": ev.end_date,
                "status": ev.status,
                "max_capacity": ev.max_capacity,
                "enrolled": enrolled,
                "fill_pct": round(enrolled / ev.max_capacity * 100, 1) if ev.max_capacity else 0,
                "instructors": ", ".join(instructor_names) if instructor_names else "Unassigned",
                "notes": ev.notes or "",
            })
        return results
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_instructors():
    db = SessionLocal()
    try:
        instructors = db.query(Instructor).order_by(Instructor.name).all()
        results = []
        for inst in instructors:
            results.append({
                "id": inst.id,
                "name": inst.name,
                "rank": inst.rank,
                "unit": inst.unit,
                "qualifications": ", ".join(inst.get_qualifications()),
                "available_from": inst.available_from,
                "available_to": inst.available_to,
                "assigned_events": len(inst.events),
                "event_names": ", ".join(e.name for e in inst.events) if inst.events else "None",
            })
        return results
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_venues():
    db = SessionLocal()
    try:
        venues = db.query(Venue).order_by(Venue.name).all()
        results = []
        for v in venues:
            event_count = len(v.events)
            results.append({
                "id": v.id,
                "name": v.name,
                "location": v.location,
                "capacity": v.capacity,
                "has_network": v.has_network,
                "has_sipr": v.has_sipr,
                "notes": v.notes or "",
                "event_count": event_count,
            })
        return results
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_enrollments(event_id: int):
    db = SessionLocal()
    try:
        enrollments = (
            db.query(Enrollment)
            .filter(Enrollment.event_id == event_id)
            .order_by(Enrollment.soldier_name)
            .all()
        )
        return [
            {
                "id": e.id,
                "dodid": e.dodid,
                "soldier_name": e.soldier_name,
                "soldier_rank": e.soldier_rank,
                "soldier_unit": e.soldier_unit,
                "status": e.status,
            }
            for e in enrollments
        ]
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
st.sidebar.title("MTT Scheduler")
st.sidebar.caption("USAREUR-AF OPERATIONAL DATA TEAM")
st.sidebar.markdown("---")

tab_names = [
    "Event Calendar",
    "Event Manager",
    "Instructor Pool",
    "Enrollment",
    "Venue Manager",
    "Capacity Dashboard",
]
active_tab = st.sidebar.radio("Navigate", tab_names)


# =============================================================================
# TAB: Event Calendar
# =============================================================================
if active_tab == "Event Calendar":
    st.title("MTT Event Calendar")
    st.caption("Timeline view of all scheduled MSS training events across the AOR")

    with st.spinner("Loading data..."):
        events = load_events()

    if not events:
        st.info("No events scheduled. Use Event Manager to create events.")
        st.stop()

    # --- KPI row ---
    total = len(events)
    planned = len([e for e in events if e["status"] == "PLANNED"])
    active = len([e for e in events if e["status"] == "ACTIVE"])
    complete = len([e for e in events if e["status"] == "COMPLETE"])
    total_enrolled = sum(e["enrolled"] for e in events)

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Total Events", total)
    c2.metric("Planned", planned)
    c3.metric("Active", active)
    c4.metric("Complete", complete)
    c5.metric("Total Enrolled", total_enrolled)

    st.markdown("---")

    # --- Gantt chart ---
    if HAS_PLOTLY:
        df = pd.DataFrame(events)

        # Build Gantt-style timeline
        fig = go.Figure()

        for status_val, color in STATUS_COLORS.items():
            mask = df[df["status"] == status_val]
            if mask.empty:
                continue

            for _, row in mask.iterrows():
                fig.add_trace(go.Bar(
                    x=[(row["end_date"] - row["start_date"]).days + 1],
                    y=[row["name"]],
                    base=row["start_date"],
                    orientation="h",
                    marker=dict(color=color),
                    name=status_val,
                    showlegend=False,
                    hovertemplate=(
                        f"<b>{row['name']}</b><br>"
                        f"Course: {row['course_id']}<br>"
                        f"Location: {row['location']}<br>"
                        f"{row['start_date']} to {row['end_date']}<br>"
                        f"Enrolled: {row['enrolled']}/{row['max_capacity']}<br>"
                        f"Status: {row['status']}"
                        "<extra></extra>"
                    ),
                ))

        # Add legend entries
        for status_val, color in STATUS_COLORS.items():
            fig.add_trace(go.Bar(
                x=[0], y=[""], base=[date.today()],
                orientation="h",
                marker=dict(color=color),
                name=status_val,
                showlegend=True,
                visible="legendonly" if status_val == "CANCELLED" else True,
            ))

        fig.update_layout(
            barmode="overlay",
            height=max(400, len(events) * 45 + 100),
            xaxis=dict(
                type="date",
                title="",
                gridcolor="#E0E4EF",
            ),
            yaxis=dict(title="", autorange="reversed"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02),
            margin=dict(l=10, r=10, t=40, b=10),
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # --- Status filter table ---
    st.subheader("Event Details")
    status_filter = st.multiselect(
        "Filter by status",
        ["PLANNED", "ACTIVE", "COMPLETE", "CANCELLED"],
        default=["PLANNED", "ACTIVE", "COMPLETE"],
    )
    filtered = [e for e in events if e["status"] in status_filter]
    if filtered:
        df_display = pd.DataFrame(filtered)
        cols = ["course_id", "name", "location", "start_date", "end_date",
                "status", "enrolled", "max_capacity", "fill_pct", "instructors"]
        st.dataframe(
            df_display[cols].rename(columns={
                "course_id": "Course", "name": "Event", "location": "Location",
                "start_date": "Start", "end_date": "End", "status": "Status",
                "enrolled": "Enrolled", "max_capacity": "Capacity",
                "fill_pct": "Fill %", "instructors": "Instructors",
            }),
            use_container_width=True,
            hide_index=True,
        )


# =============================================================================
# TAB: Event Manager
# =============================================================================
elif active_tab == "Event Manager":
    st.title("Event Manager")
    st.caption("Create and manage MTT training events")

    events = load_events()
    venues = load_venues()
    instructors = load_instructors()

    # --- Create new event ---
    with st.expander("Create New Event", expanded=False):
        with st.form("create_event"):
            col1, col2 = st.columns(2)
            with col1:
                ev_name = st.text_input("Event Name", placeholder="SL 1 Maven User — Location")
                ev_course = st.selectbox(
                    "Course",
                    ["SL 1", "SL 2", "SL 3",
                     "SL 4A", "SL 4B", "SL 4C", "SL 4D", "SL 4E", "SL 4F",
                     "SL 4G", "SL 4H", "SL 4M", "SL 4J", "SL 4K", "SL 4L"],
                )
                ev_location = st.text_input("Location", placeholder="Grafenwoehr, Germany")
                ev_venue = st.selectbox(
                    "Venue",
                    ["None"] + [f"{v['name']} ({v['location']})" for v in venues],
                )

            with col2:
                ev_start = st.date_input("Start Date", value=date.today() + timedelta(days=14))
                ev_end = st.date_input("End Date", value=date.today() + timedelta(days=15))
                ev_capacity = st.number_input("Max Capacity", min_value=1, max_value=200, value=20)
                ev_notes = st.text_area("Notes", placeholder="Special requirements, prereqs, etc.")

            submitted = st.form_submit_button("Create Event")
            if submitted:
                if not ev_name or not ev_location:
                    st.error("Name and Location are required.")
                elif ev_end < ev_start:
                    st.error("End date must be on or after start date.")
                else:
                    db = SessionLocal()
                    try:
                        venue_id = None
                        if ev_venue != "None":
                            venue_idx = [f"{v['name']} ({v['location']})" for v in venues].index(ev_venue)
                            venue_id = venues[venue_idx]["id"]

                        new_event = Event(
                            name=ev_name,
                            course_id=ev_course,
                            location=ev_location,
                            venue_id=venue_id,
                            start_date=ev_start,
                            end_date=ev_end,
                            max_capacity=ev_capacity,
                            status="PLANNED",
                            notes=ev_notes if ev_notes else None,
                        )
                        db.add(new_event)
                        db.commit()
                        st.success(f"Event '{ev_name}' created.")
                        st.cache_data.clear()
                    finally:
                        db.close()

    # --- Event table with status updates ---
    st.subheader("All Events")
    if events:
        df_ev = pd.DataFrame(events)
        cols = ["id", "course_id", "name", "location", "start_date", "end_date",
                "status", "enrolled", "max_capacity", "instructors"]
        st.dataframe(
            df_ev[cols].rename(columns={
                "id": "ID", "course_id": "Course", "name": "Event",
                "location": "Location", "start_date": "Start", "end_date": "End",
                "status": "Status", "enrolled": "Enrolled",
                "max_capacity": "Capacity", "instructors": "Instructors",
            }),
            use_container_width=True,
            hide_index=True,
        )

        # Status update
        st.subheader("Update Event Status")
        col_s1, col_s2, col_s3 = st.columns(3)
        with col_s1:
            event_options = [f"[{e['id']}] {e['name']}" for e in events]
            selected_event = st.selectbox("Select Event", event_options, key="status_event")
        with col_s2:
            new_status = st.selectbox("New Status", ["PLANNED", "ACTIVE", "COMPLETE", "CANCELLED"])
        with col_s3:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Update Status"):
                event_id = int(selected_event.split("]")[0].replace("[", ""))
                db = SessionLocal()
                try:
                    ev = db.query(Event).filter(Event.id == event_id).first()
                    if ev:
                        ev.status = new_status
                        db.commit()
                        st.success(f"Event status updated to {new_status}.")
                        st.cache_data.clear()
                finally:
                    db.close()

        # Instructor assignment
        st.subheader("Assign Instructor to Event")
        col_a1, col_a2, col_a3 = st.columns(3)
        with col_a1:
            assign_event = st.selectbox("Event", event_options, key="assign_event")
        with col_a2:
            inst_options = [f"[{i['id']}] {i['rank']} {i['name']}" for i in instructors]
            assign_inst = st.selectbox("Instructor", inst_options, key="assign_inst")
        with col_a3:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Assign"):
                event_id = int(assign_event.split("]")[0].replace("[", ""))
                inst_id = int(assign_inst.split("]")[0].replace("[", ""))
                db = SessionLocal()
                try:
                    ev = db.query(Event).filter(Event.id == event_id).first()
                    inst = db.query(Instructor).filter(Instructor.id == inst_id).first()
                    if ev and inst:
                        if inst in ev.instructors:
                            st.warning("Instructor already assigned to this event.")
                        else:
                            ev.instructors.append(inst)
                            db.commit()
                            st.success(f"{inst.rank} {inst.name} assigned to {ev.name}.")
                            st.cache_data.clear()
                finally:
                    db.close()
    else:
        st.info("No events created yet.")


# =============================================================================
# TAB: Instructor Pool
# =============================================================================
elif active_tab == "Instructor Pool":
    st.title("Instructor Pool")
    st.caption("Manage instructor qualifications, availability, and assignments")

    instructors = load_instructors()
    conflicts = load_conflicts()

    # --- Conflict warnings ---
    if conflicts:
        st.error(f"**{len(conflicts)} scheduling conflict(s) detected**")
        for c in conflicts:
            st.warning(
                f"**{c['instructor_name']}** is double-booked: "
                f"'{c['event1']}' and '{c['event2']}' overlap "
                f"({c['overlap_dates']})"
            )
        st.markdown("---")

    # --- KPI row ---
    if instructors:
        total_inst = len(instructors)
        assigned = len([i for i in instructors if i["assigned_events"] > 0])
        unassigned = total_inst - assigned
        max_load = max(i["assigned_events"] for i in instructors) if instructors else 0

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Instructors", total_inst)
        c2.metric("Assigned", assigned)
        c3.metric("Available", unassigned)
        c4.metric("Max Event Load", max_load)

    # --- Create new instructor ---
    with st.expander("Add New Instructor", expanded=False):
        with st.form("create_instructor"):
            col1, col2 = st.columns(2)
            with col1:
                inst_name = st.text_input("Name (Last)", placeholder="SMITH")
                inst_rank = st.text_input("Rank", placeholder="CW2")
                inst_unit = st.text_input("Unit", placeholder="USAREUR-AF ODT")
            with col2:
                inst_quals = st.multiselect(
                    "Qualifications",
                    ["SL 1", "SL 2", "SL 3",
                     "SL 4A", "SL 4B", "SL 4C", "SL 4D", "SL 4E", "SL 4F",
                     "SL 4G", "SL 4H", "SL 4M", "SL 4J", "SL 4K", "SL 4L"],
                )
                inst_avail_from = st.date_input("Available From", value=date.today())
                inst_avail_to = st.date_input("Available To", value=date.today() + timedelta(days=120))

            submitted = st.form_submit_button("Add Instructor")
            if submitted:
                if not inst_name or not inst_rank or not inst_unit:
                    st.error("Name, Rank, and Unit are required.")
                else:
                    db = SessionLocal()
                    try:
                        new_inst = Instructor(
                            name=inst_name.strip().upper(),
                            rank=inst_rank.strip().upper(),
                            unit=inst_unit.strip().upper(),
                            available_from=inst_avail_from,
                            available_to=inst_avail_to,
                        )
                        new_inst.set_qualifications(inst_quals)
                        db.add(new_inst)
                        db.commit()
                        st.success(f"Instructor {inst_rank} {inst_name} added.")
                        st.cache_data.clear()
                    finally:
                        db.close()

    # --- Instructor table ---
    st.subheader("Instructor Roster")
    if instructors:
        df_inst = pd.DataFrame(instructors)
        cols = ["rank", "name", "unit", "qualifications",
                "available_from", "available_to", "assigned_events", "event_names"]
        st.dataframe(
            df_inst[cols].rename(columns={
                "rank": "Rank", "name": "Name", "unit": "Unit",
                "qualifications": "Qualifications",
                "available_from": "Avail From", "available_to": "Avail To",
                "assigned_events": "Events", "event_names": "Assigned To",
            }),
            use_container_width=True,
            hide_index=True,
        )

        # --- Availability timeline ---
        if HAS_PLOTLY:
            st.subheader("Instructor Availability Timeline")
            fig = go.Figure()
            for inst in instructors:
                label = f"{inst['rank']} {inst['name']}"
                duration = (inst["available_to"] - inst["available_from"]).days + 1
                fig.add_trace(go.Bar(
                    x=[duration],
                    y=[label],
                    base=inst["available_from"],
                    orientation="h",
                    marker=dict(
                        color=RAG_GREEN if inst["assigned_events"] > 0 else NAVY_MID,
                    ),
                    hovertemplate=(
                        f"<b>{label}</b><br>"
                        f"Available: {inst['available_from']} to {inst['available_to']}<br>"
                        f"Events: {inst['assigned_events']}<br>"
                        f"Quals: {inst['qualifications']}"
                        "<extra></extra>"
                    ),
                    showlegend=False,
                ))

            fig.update_layout(
                height=max(300, len(instructors) * 40 + 80),
                xaxis=dict(type="date", title=""),
                yaxis=dict(title="", autorange="reversed"),
                margin=dict(l=10, r=10, t=10, b=10),
            )
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No instructors in the pool.")


# =============================================================================
# TAB: Enrollment
# =============================================================================
elif active_tab == "Enrollment":
    st.title("Enrollment Management")
    st.caption("Manage student enrollment for MTT events")

    events = load_events()

    if not events:
        st.info("No events available. Create events first.")
        st.stop()

    # --- Event selector ---
    event_options = [f"[{e['id']}] {e['course_id']} — {e['name']}" for e in events]
    selected = st.selectbox("Select Event", event_options)
    event_id = int(selected.split("]")[0].replace("[", ""))
    event_data = next(e for e in events if e["id"] == event_id)

    # --- Event info + capacity gauge ---
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Course", event_data["course_id"])
    col2.metric("Location", event_data["location"])
    col3.metric("Status", event_data["status"])
    col4.metric(
        "Capacity",
        f"{event_data['enrolled']}/{event_data['max_capacity']}",
        delta=f"{event_data['fill_pct']}% full",
    )

    # Capacity gauge
    if HAS_PLOTLY:
        fill = event_data["fill_pct"]
        gauge_color = RAG_GREEN if fill < 80 else (RAG_AMBER if fill < 95 else RAG_RED)

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=fill,
            number=dict(suffix="%"),
            title=dict(text="Capacity Utilization"),
            gauge=dict(
                axis=dict(range=[0, 100]),
                bar=dict(color=gauge_color),
                steps=[
                    dict(range=[0, 50], color="#EEF2FA"),
                    dict(range=[50, 80], color="#FDF5DC"),
                    dict(range=[80, 100], color="#fdf0f0"),
                ],
                threshold=dict(
                    line=dict(color=RAG_RED, width=2),
                    thickness=0.75,
                    value=100,
                ),
            ),
        ))
        fig.update_layout(height=250, margin=dict(l=20, r=20, t=40, b=20))
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # --- Enrollment table ---
    enrollments = load_enrollments(event_id)
    st.subheader(f"Enrolled Students ({len(enrollments)})")

    if enrollments:
        df_enroll = pd.DataFrame(enrollments)
        st.dataframe(
            df_enroll[["soldier_rank", "soldier_name", "soldier_unit", "dodid", "status"]].rename(
                columns={
                    "soldier_rank": "Rank", "soldier_name": "Name",
                    "soldier_unit": "Unit", "dodid": "DODID", "status": "Status",
                }
            ),
            use_container_width=True,
            hide_index=True,
        )

        # Status breakdown
        status_counts = {}
        for e in enrollments:
            status_counts[e["status"]] = status_counts.get(e["status"], 0) + 1
        cols = st.columns(len(status_counts))
        for i, (s, cnt) in enumerate(sorted(status_counts.items())):
            cols[i].metric(s, cnt)

    # --- Add enrollment ---
    with st.expander("Enroll New Student", expanded=False):
        with st.form("enroll_student"):
            col1, col2 = st.columns(2)
            with col1:
                s_name = st.text_input("Soldier Name (LAST, FIRST)", placeholder="KELLY, JAMES")
                s_rank = st.text_input("Rank", placeholder="SGT")
            with col2:
                s_unit = st.text_input("Unit", placeholder="1-1 IN BN")
                s_dodid = st.text_input("DODID (10 digits)", placeholder="1000000000")

            submitted = st.form_submit_button("Enroll")
            if submitted:
                if not s_name or not s_rank or not s_unit or not s_dodid:
                    st.error("All fields are required.")
                elif len(s_dodid) != 10 or not s_dodid.isdigit():
                    st.error("DODID must be exactly 10 digits.")
                elif event_data["enrolled"] >= event_data["max_capacity"]:
                    st.error("Event is at max capacity.")
                else:
                    db = SessionLocal()
                    try:
                        # Check for duplicate
                        existing = (
                            db.query(Enrollment)
                            .filter(
                                Enrollment.event_id == event_id,
                                Enrollment.dodid == s_dodid,
                                Enrollment.status != "DROPPED",
                            )
                            .first()
                        )
                        if existing:
                            st.warning("Soldier already enrolled in this event.")
                        else:
                            enrollment = Enrollment(
                                event_id=event_id,
                                dodid=s_dodid,
                                soldier_name=s_name.strip().upper(),
                                soldier_rank=s_rank.strip().upper(),
                                soldier_unit=s_unit.strip().upper(),
                                status="ENROLLED",
                            )
                            db.add(enrollment)
                            db.commit()
                            st.success(f"{s_rank} {s_name} enrolled.")
                            st.cache_data.clear()
                    finally:
                        db.close()

    # --- Update enrollment status ---
    if enrollments:
        st.subheader("Update Enrollment Status")
        col_u1, col_u2, col_u3 = st.columns(3)
        with col_u1:
            enroll_options = [
                f"[{e['id']}] {e['soldier_rank']} {e['soldier_name']}"
                for e in enrollments
            ]
            sel_enrollment = st.selectbox("Select Student", enroll_options)
        with col_u2:
            new_enroll_status = st.selectbox(
                "New Status",
                ["ENROLLED", "COMPLETE", "NO_SHOW", "DROPPED"],
            )
        with col_u3:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Update"):
                enroll_id = int(sel_enrollment.split("]")[0].replace("[", ""))
                db = SessionLocal()
                try:
                    enr = db.query(Enrollment).filter(Enrollment.id == enroll_id).first()
                    if enr:
                        enr.status = new_enroll_status
                        db.commit()
                        st.success(f"Status updated to {new_enroll_status}.")
                        st.cache_data.clear()
                finally:
                    db.close()


# =============================================================================
# TAB: Venue Manager
# =============================================================================
elif active_tab == "Venue Manager":
    st.title("Venue Manager")
    st.caption("Manage training venues across the AOR")

    venues = load_venues()
    events = load_events()

    # --- Venue table ---
    if venues:
        df_v = pd.DataFrame(venues)
        st.dataframe(
            df_v[["name", "location", "capacity", "has_network", "has_sipr",
                   "event_count", "notes"]].rename(columns={
                "name": "Venue", "location": "Location", "capacity": "Capacity",
                "has_network": "NIPR", "has_sipr": "SIPR",
                "event_count": "Events", "notes": "Notes",
            }),
            use_container_width=True,
            hide_index=True,
        )

    # --- Create new venue ---
    with st.expander("Add New Venue", expanded=False):
        with st.form("create_venue"):
            col1, col2 = st.columns(2)
            with col1:
                v_name = st.text_input("Venue Name", placeholder="Building 123 Training Room")
                v_location = st.text_input("Location", placeholder="Grafenwoehr, Germany")
                v_capacity = st.number_input("Capacity", min_value=1, max_value=500, value=20)
            with col2:
                v_network = st.checkbox("NIPR Network Available", value=True)
                v_sipr = st.checkbox("SIPR Network Available", value=False)
                v_notes = st.text_area("Notes", placeholder="Special access requirements, etc.")

            submitted = st.form_submit_button("Add Venue")
            if submitted:
                if not v_name or not v_location:
                    st.error("Name and Location are required.")
                else:
                    db = SessionLocal()
                    try:
                        venue = Venue(
                            name=v_name.strip(),
                            location=v_location.strip(),
                            capacity=v_capacity,
                            has_network=v_network,
                            has_sipr=v_sipr,
                            notes=v_notes if v_notes else None,
                        )
                        db.add(venue)
                        db.commit()
                        st.success(f"Venue '{v_name}' added.")
                        st.cache_data.clear()
                    finally:
                        db.close()

    # --- Venue availability calendar ---
    if venues and events and HAS_PLOTLY:
        st.subheader("Venue Utilization Calendar")

        venue_events: dict[str, list[dict]] = {v["name"]: [] for v in venues}
        for ev in events:
            if ev["venue"] in venue_events and ev["status"] != "CANCELLED":
                venue_events[ev["venue"]].append(ev)

        fig = go.Figure()
        for venue_name, v_events in venue_events.items():
            for ev in v_events:
                duration = (ev["end_date"] - ev["start_date"]).days + 1
                fig.add_trace(go.Bar(
                    x=[duration],
                    y=[venue_name],
                    base=ev["start_date"],
                    orientation="h",
                    marker=dict(color=STATUS_COLORS.get(ev["status"], GRAY_400)),
                    hovertemplate=(
                        f"<b>{ev['name']}</b><br>"
                        f"{ev['start_date']} to {ev['end_date']}<br>"
                        f"Status: {ev['status']}"
                        "<extra></extra>"
                    ),
                    showlegend=False,
                ))

        fig.update_layout(
            barmode="overlay",
            height=max(250, len(venues) * 50 + 80),
            xaxis=dict(type="date", title=""),
            yaxis=dict(title="", autorange="reversed"),
            margin=dict(l=10, r=10, t=10, b=10),
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)


# =============================================================================
# TAB: Capacity Dashboard
# =============================================================================
elif active_tab == "Capacity Dashboard":
    st.title("Capacity Dashboard")
    st.caption("Utilization metrics, fill rates, and location analysis")

    utilization = load_utilization()
    loc_summary = load_location_summary()
    events = load_events()

    if not utilization:
        st.info("No events to analyze.")
        st.stop()

    # --- KPI row ---
    total_capacity = sum(u["max_capacity"] for u in utilization)
    total_enrolled = sum(u["enrolled"] for u in utilization)
    avg_fill = round(total_enrolled / total_capacity * 100, 1) if total_capacity else 0
    at_risk = len([u for u in utilization if u["fill_pct"] < 50 and u["status"] == "PLANNED"])

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Capacity", total_capacity)
    c2.metric("Total Enrolled", total_enrolled)
    c3.metric("Avg Fill Rate", f"{avg_fill}%")
    c4.metric("Under-Filled (PLANNED)", at_risk, delta_color="inverse")

    st.markdown("---")

    # --- Fill rate chart ---
    col_left, col_right = st.columns([3, 2])

    with col_left:
        st.subheader("Event Fill Rates")
        if HAS_PLOTLY:
            df_u = pd.DataFrame(utilization)
            # Color based on fill rate
            colors = []
            for _, row in df_u.iterrows():
                if row["fill_pct"] >= 80:
                    colors.append(RAG_GREEN)
                elif row["fill_pct"] >= 50:
                    colors.append(RAG_AMBER)
                else:
                    colors.append(RAG_RED)

            fig = go.Figure(data=[go.Bar(
                x=df_u["name"],
                y=df_u["fill_pct"],
                marker_color=colors,
                text=[f"{p:.0f}%" for p in df_u["fill_pct"]],
                textposition="auto",
                hovertemplate=(
                    "<b>%{x}</b><br>"
                    "Fill: %{y:.1f}%<br>"
                    "<extra></extra>"
                ),
            )])
            fig.update_layout(
                height=400,
                xaxis_tickangle=-45,
                yaxis=dict(title="Fill %", range=[0, 105]),
                xaxis_title="",
            )
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

    with col_right:
        st.subheader("Location Summary")
        if loc_summary:
            df_loc = pd.DataFrame(loc_summary)
            st.dataframe(
                df_loc[["location", "total_events", "planned", "active",
                         "complete", "total_enrolled"]].rename(columns={
                    "location": "Location", "total_events": "Events",
                    "planned": "Planned", "active": "Active",
                    "complete": "Complete", "total_enrolled": "Enrolled",
                }),
                use_container_width=True,
                hide_index=True,
            )

    st.markdown("---")

    # --- Location heatmap ---
    if loc_summary and HAS_PLOTLY:
        st.subheader("Events by Location")
        df_loc = pd.DataFrame(loc_summary)

        fig = go.Figure(data=[go.Bar(
            x=df_loc["location"],
            y=df_loc["total_events"],
            marker_color=NAVY_MID,
            text=df_loc["total_events"],
            textposition="auto",
        )])
        fig.update_layout(
            height=350,
            xaxis_title="",
            yaxis_title="Number of Events",
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # --- Utilization details table ---
    st.subheader("Detailed Utilization")
    if utilization:
        df_detail = pd.DataFrame(utilization)
        cols = ["name", "course_id", "location", "status",
                "enrolled", "max_capacity", "available", "fill_pct"]
        st.dataframe(
            df_detail[cols].rename(columns={
                "name": "Event", "course_id": "Course", "location": "Location",
                "status": "Status", "enrolled": "Enrolled",
                "max_capacity": "Capacity", "available": "Available",
                "fill_pct": "Fill %",
            }),
            use_container_width=True,
            hide_index=True,
        )

    # --- Course distribution pie chart ---
    if events and HAS_PLOTLY:
        st.subheader("Events by Course Type")
        course_counts: dict[str, int] = {}
        for ev in events:
            cid = ev["course_id"]
            course_counts[cid] = course_counts.get(cid, 0) + 1

        fig = go.Figure(data=[go.Pie(
            labels=list(course_counts.keys()),
            values=list(course_counts.values()),
            marker=dict(colors=[NAVY_DARK, NAVY, NAVY_MID, NAVY_LIGHT, GOLD, GOLD_DARK]),
            textinfo="label+value",
            hole=0.4,
        )])
        fig.update_layout(
            height=350,
            margin=dict(l=10, r=10, t=10, b=10),
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="app-footer">USAREUR-AF OPERATIONAL DATA TEAM — MSS MTT SCHEDULER</div>',
    unsafe_allow_html=True,
)
