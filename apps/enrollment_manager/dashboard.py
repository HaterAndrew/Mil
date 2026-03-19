"""Enrollment Manager — Streamlit dashboard.

Manage class enrollment, seat allocation, waitlists, and rosters for
scheduled MSS training events across USAREUR-AF.
"""

from __future__ import annotations

import os
import sys
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

from enrollment_manager.db import (
    COURSE_CATALOG,
    Enrollment,
    SessionLocal,
    TrainingClass,
    WaitlistEntry,
    get_class_availability,
    get_class_roster,
    get_enrollment_stats,
    get_student_enrollments,
    init_db,
)

from theme import inject_branding, apply_plotly_theme, NAVY, NAVY_DARK, NAVY_LIGHT, NAVY_MID, GOLD, GOLD_DARK, GOLD_LIGHT, RAG_GREEN, RAG_AMBER, RAG_RED, GRAY_400, GRAY_700

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
API_BASE = os.environ.get("ENROLLMENT_MANAGER_API_URL", "http://localhost:8012")

st.set_page_config(
    page_title="MSS Enrollment Manager",
    page_icon="\U0001F4CB",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_branding("MSS Enrollment Manager")

# ---------------------------------------------------------------------------
# Direct DB access for dashboard (avoids API round-trips for analytics)
# ---------------------------------------------------------------------------
init_db()  # Ensure tables exist before any query


@st.cache_data(ttl=30)
def load_stats():
    db = SessionLocal()
    try:
        return get_enrollment_stats(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_classes():
    """Load all training classes with enrollment counts."""
    db = SessionLocal()
    try:
        classes = db.query(TrainingClass).order_by(TrainingClass.start_date).all()
        result = []
        for tc in classes:
            enrolled = (
                db.query(Enrollment)
                .filter(Enrollment.class_id == tc.class_id, Enrollment.status == "ENROLLED")
                .count()
            )
            waitlisted = (
                db.query(WaitlistEntry)
                .filter(WaitlistEntry.class_id == tc.class_id, WaitlistEntry.status == "WAITING")
                .count()
            )
            fill_pct = round(enrolled / tc.max_seats * 100, 1) if tc.max_seats else 0.0
            result.append({
                "class_id": tc.class_id,
                "course_id": tc.course_id,
                "class_name": tc.class_name,
                "start_date": tc.start_date.isoformat() if tc.start_date else "",
                "end_date": tc.end_date.isoformat() if tc.end_date else "",
                "location": tc.location,
                "max_seats": tc.max_seats,
                "enrolled": enrolled,
                "waitlisted": waitlisted,
                "fill_pct": fill_pct,
                "instructor": tc.instructor_name or "",
                "status": tc.status,
            })
        return result
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_class_roster(class_id: int):
    db = SessionLocal()
    try:
        roster = get_class_roster(class_id, db)
        return [
            {
                "seat": e.seat_number,
                "rank": e.rank,
                "last_name": e.last_name,
                "first_name": e.first_name,
                "dodid": e.dodid,
                "unit": e.unit,
                "status": e.status,
                "enrollment_date": e.enrollment_date.isoformat() if e.enrollment_date else "",
            }
            for e in roster
        ]
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_class_waitlist(class_id: int):
    db = SessionLocal()
    try:
        entries = (
            db.query(WaitlistEntry)
            .filter(WaitlistEntry.class_id == class_id, WaitlistEntry.status == "WAITING")
            .order_by(WaitlistEntry.priority.desc(), WaitlistEntry.request_date.asc())
            .all()
        )
        return [
            {
                "priority": e.priority,
                "rank": e.rank,
                "last_name": e.last_name,
                "first_name": e.first_name,
                "dodid": e.dodid,
                "unit": e.unit,
                "request_date": e.request_date.isoformat() if e.request_date else "",
            }
            for e in entries
        ]
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_all_enrollments():
    """Load all enrollments for student search."""
    db = SessionLocal()
    try:
        enrollments = db.query(Enrollment).all()
        seen = {}
        for e in enrollments:
            if e.dodid not in seen:
                seen[e.dodid] = {
                    "dodid": e.dodid,
                    "rank": e.rank,
                    "last_name": e.last_name,
                    "first_name": e.first_name,
                    "unit": e.unit,
                }
        return list(seen.values())
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_student_detail(dodid: str):
    db = SessionLocal()
    try:
        return get_student_enrollments(dodid, db)
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
st.sidebar.title("MSS Enrollment Manager")
st.sidebar.caption("USAREUR-AF Operational Data Team")
st.sidebar.markdown("---")

tab_names = [
    "Enrollment Overview",
    "Class Manager",
    "Seat Allocation",
    "Student Lookup",
    "Waitlist Management",
]
active_tab = st.sidebar.radio("Navigate", tab_names)


# =============================================================================
# TAB: Enrollment Overview
# =============================================================================
if active_tab == "Enrollment Overview":
    st.title("Enrollment Overview")

    with st.spinner("Loading data..."):
        stats = load_stats()
        classes = load_classes()

    if not classes:
        st.info("No training classes found. Seed the database to get started.")
        st.stop()

    # --- KPI Row ---
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Classes", stats["total_classes"])
    c2.metric("Total Enrolled", stats["total_enrolled"])
    c3.metric("Avg Fill Rate", f"{stats['avg_fill_rate']:.0f}%")
    c4.metric("Waitlisted", stats["total_waitlisted"])

    st.markdown("---")

    upcoming = [c for c in classes if c["status"] in ("SCHEDULED", "IN_PROGRESS")]

    # --- Fill Rate Overview Chart ---
    if upcoming and HAS_PLOTLY:
        st.subheader("Fill Rate by Class")
        df_fill = pd.DataFrame(upcoming)
        fill_colors = []
        for _, row in df_fill.iterrows():
            fill = row["fill_pct"]
            if fill >= 100:
                fill_colors.append(RAG_RED)
            elif fill >= 80:
                fill_colors.append(RAG_AMBER)
            elif fill > 50:
                fill_colors.append(RAG_GREEN)
            else:
                fill_colors.append(NAVY_MID)

        fig = go.Figure(data=[go.Bar(
            x=df_fill["class_name"],
            y=df_fill["fill_pct"],
            marker_color=fill_colors,
            text=[f"{p:.0f}%" for p in df_fill["fill_pct"]],
            textposition="auto",
        )])
        fig.add_hline(y=100, line_dash="dash", line_color=RAG_RED, opacity=0.5,
                       annotation_text="Capacity")
        fig.update_layout(
            height=350, xaxis_tickangle=-45,
            xaxis_title="", yaxis_title="Fill Rate (%)",
            yaxis_range=[0, 120], showlegend=False,
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

    # --- Upcoming classes table ---
    st.subheader("Upcoming & Active Classes")

    if upcoming:
        df = pd.DataFrame(upcoming)
        display_cols = [
            "class_name", "course_id", "start_date", "end_date", "location",
            "enrolled", "max_seats", "fill_pct", "waitlisted", "status",
        ]
        df_display = df[display_cols].rename(columns={
            "class_name": "Class", "course_id": "Course", "start_date": "Start",
            "end_date": "End", "location": "Location", "enrolled": "Enrolled",
            "max_seats": "Max", "fill_pct": "Fill %", "waitlisted": "Waitlisted",
            "status": "Status",
        })
        st.dataframe(df_display, use_container_width=True, hide_index=True)
    else:
        st.info("No upcoming classes scheduled.")

    # --- Fill rate overview chart ---
    if upcoming and HAS_PLOTLY:
        st.subheader("Class Fill Rates")
        df_chart = pd.DataFrame(upcoming)
        colors = []
        for _, row in df_chart.iterrows():
            fill = row["fill_pct"]
            if fill >= 100:
                colors.append(RAG_RED)
            elif fill >= 80:
                colors.append(RAG_AMBER)
            elif fill > 50:
                colors.append(RAG_GREEN)
            else:
                colors.append(NAVY_MID)
        fig = go.Figure(data=[go.Bar(
            x=df_chart["class_name"],
            y=df_chart["fill_pct"],
            marker_color=colors,
            text=[f"{p:.0f}%" for p in df_chart["fill_pct"]],
            textposition="auto",
        )])
        fig.add_hline(y=100, line_dash="dash", line_color=RAG_RED, opacity=0.5,
                       annotation_text="Capacity")
        fig.update_layout(
            height=350, xaxis_tickangle=-45, xaxis_title="",
            yaxis_title="Fill Rate (%)", yaxis_range=[0, 120],
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # --- Completed/Cancelled summary ---
    other = [c for c in classes if c["status"] in ("COMPLETED", "CANCELLED")]
    if other:
        with st.expander(f"Completed/Cancelled Classes ({len(other)})"):
            df_other = pd.DataFrame(other)
            st.dataframe(
                df_other[["class_name", "status", "location", "start_date"]].rename(columns={
                    "class_name": "Class", "status": "Status", "location": "Location",
                    "start_date": "Date",
                }),
                use_container_width=True, hide_index=True,
            )


# =============================================================================
# TAB: Class Manager
# =============================================================================
elif active_tab == "Class Manager":
    st.title("Class Manager")

    classes = load_classes()
    if not classes:
        st.info("No classes found.")
        st.stop()

    # Class selector
    class_options = {f"{c['class_name']} (ID: {c['class_id']})": c["class_id"] for c in classes}
    selected_label = st.selectbox("Select Class", list(class_options.keys()))
    selected_id = class_options[selected_label]

    # Find the selected class info
    class_info = next((c for c in classes if c["class_id"] == selected_id), None)

    if class_info:
        # --- Class details + RAG status ---
        fill = class_info["fill_pct"]
        if fill >= 100:
            rag_color = RAG_RED
            rag_label = "FULL"
        elif fill >= 80:
            rag_color = RAG_AMBER
            rag_label = "NEAR FULL"
        elif fill > 50:
            rag_color = RAG_GREEN
            rag_label = "OPEN"
        else:
            rag_color = NAVY_MID
            rag_label = "OPEN"

        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("Course", class_info["course_id"])
        c2.metric("Location", class_info["location"])
        c3.metric("Enrolled", f"{class_info['enrolled']}/{class_info['max_seats']}")
        c4.metric("Fill Rate", f"{fill:.0f}%")
        c5.metric("Waitlisted", class_info["waitlisted"])

        # RAG status indicator
        st.markdown(
            f'<div style="display:inline-block; padding:4px 12px; '
            f'background:{rag_color}; color:white; font-weight:bold; '
            f'font-size:12px; border-radius:3px; letter-spacing:1px;">'
            f'{rag_label} &mdash; {class_info["status"]}</div>',
            unsafe_allow_html=True,
        )

        st.markdown("---")

        # --- Roster ---
        st.subheader("Class Roster")
        roster = load_class_roster(selected_id)
        if roster:
            df_r = pd.DataFrame(roster)
            st.dataframe(
                df_r.rename(columns={
                    "seat": "Seat", "rank": "Rank", "last_name": "Last",
                    "first_name": "First", "dodid": "DODID", "unit": "Unit",
                    "status": "Status", "enrollment_date": "Enrolled",
                }),
                use_container_width=True, hide_index=True,
            )
        else:
            st.info("No students enrolled in this class.")

        # --- Waitlist for this class ---
        waitlist = load_class_waitlist(selected_id)
        if waitlist:
            st.subheader(f"Waitlist ({len(waitlist)} waiting)")
            df_w = pd.DataFrame(waitlist)
            st.dataframe(
                df_w.rename(columns={
                    "priority": "Priority", "rank": "Rank", "last_name": "Last",
                    "first_name": "First", "dodid": "DODID", "unit": "Unit",
                    "request_date": "Requested",
                }),
                use_container_width=True, hide_index=True,
            )

        # --- Availability summary ---
        st.subheader("Availability")
        seats_remaining = class_info["max_seats"] - class_info["enrolled"]
        if seats_remaining > 0:
            st.success(f"{seats_remaining} seats remaining out of {class_info['max_seats']}")
        elif class_info["waitlisted"] > 0:
            st.error(f"Class is full. {class_info['waitlisted']} on waitlist.")
        else:
            st.warning("Class is full. No waitlist entries.")


# =============================================================================
# TAB: Seat Allocation
# =============================================================================
elif active_tab == "Seat Allocation":
    st.title("Seat Allocation")
    st.caption("Fill rate per upcoming class. GREEN (>50%) | AMBER (>80%) | RED (full/waitlisted)")

    classes = load_classes()
    upcoming = [c for c in classes if c["status"] in ("SCHEDULED", "IN_PROGRESS")]

    if not upcoming:
        st.info("No upcoming classes.")
        st.stop()

    if HAS_PLOTLY:
        df = pd.DataFrame(upcoming)

        # Color-code bars by fill rate
        colors = []
        for _, row in df.iterrows():
            fill = row["fill_pct"]
            if fill >= 100:
                colors.append(RAG_RED)
            elif fill >= 80:
                colors.append(RAG_AMBER)
            elif fill > 50:
                colors.append(RAG_GREEN)
            else:
                colors.append(NAVY_MID)

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df["class_name"],
            y=df["fill_pct"],
            marker_color=colors,
            text=[f"{p:.0f}%" for p in df["fill_pct"]],
            textposition="auto",
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Fill: %{y:.1f}%<br>"
                "<extra></extra>"
            ),
        ))

        # Add 100% threshold line
        fig.add_hline(y=100, line_dash="dash", line_color=RAG_RED, opacity=0.5,
                       annotation_text="Capacity", annotation_position="top right")
        fig.add_hline(y=80, line_dash="dot", line_color=RAG_AMBER, opacity=0.4)

        fig.update_layout(
            height=500,
            xaxis_tickangle=-45,
            xaxis_title="",
            yaxis_title="Fill Rate (%)",
            yaxis_range=[0, 120],
            showlegend=False,
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # Summary table
    st.subheader("Summary")
    full_classes = [c for c in upcoming if c["fill_pct"] >= 100]
    near_full = [c for c in upcoming if 80 <= c["fill_pct"] < 100]
    open_classes = [c for c in upcoming if c["fill_pct"] < 80]

    s1, s2, s3 = st.columns(3)
    s1.metric("Full / Waitlisted", len(full_classes))
    s2.metric("Near Full (>80%)", len(near_full))
    s3.metric("Open (<80%)", len(open_classes))


# =============================================================================
# TAB: Student Lookup
# =============================================================================
elif active_tab == "Student Lookup":
    st.title("Student Lookup")

    all_students = load_all_enrollments()

    search = st.text_input("Search by name or DODID", placeholder="KELLY or 1000000000")

    if search:
        search_upper = search.strip().upper()
        matches = [
            s for s in all_students
            if search_upper in s["last_name"] or search_upper in s["first_name"]
            or search_upper in s["dodid"]
        ]

        dodid = None
        if not matches:
            st.warning("No matches found.")
        elif len(matches) > 1:
            options = [
                f"{s['rank']} {s['last_name']}, {s['first_name']} ({s['dodid']})"
                for s in matches
            ]
            selected = st.selectbox("Multiple matches -- select:", options)
            idx = options.index(selected)
            dodid = matches[idx]["dodid"]
        else:
            dodid = matches[0]["dodid"]

        if dodid is not None:
            student = next((s for s in all_students if s["dodid"] == dodid), None)
            if student:
                st.subheader(f"{student['rank']} {student['last_name']}, {student['first_name']}")
                st.caption(f"Unit: {student['unit']} | DODID: {student['dodid']}")

            enrollments = load_student_detail(dodid)
            if enrollments:
                st.subheader("Enrollments")
                df_e = pd.DataFrame(enrollments)
                st.dataframe(
                    df_e[["class_name", "course_id", "start_date", "end_date",
                          "location", "enrollment_status", "seat_number"]].rename(columns={
                        "class_name": "Class", "course_id": "Course",
                        "start_date": "Start", "end_date": "End",
                        "location": "Location", "enrollment_status": "Status",
                        "seat_number": "Seat",
                    }),
                    use_container_width=True, hide_index=True,
                )
            else:
                st.info("No enrollments found for this student.")


# =============================================================================
# TAB: Waitlist Management
# =============================================================================
elif active_tab == "Waitlist Management":
    st.title("Waitlist Management")

    classes = load_classes()
    # Filter to classes that have waitlisted students
    classes_with_waitlist = [c for c in classes if c["waitlisted"] > 0]

    if not classes_with_waitlist:
        st.info("No classes currently have waitlisted students.")
        st.stop()

    st.subheader(f"Classes with Waitlists ({len(classes_with_waitlist)})")

    for cls in classes_with_waitlist:
        with st.expander(
            f"{cls['class_name']} -- {cls['waitlisted']} waiting "
            f"({cls['enrolled']}/{cls['max_seats']} enrolled)"
        ):
            # Class info
            c1, c2, c3 = st.columns(3)
            c1.metric("Enrolled", f"{cls['enrolled']}/{cls['max_seats']}")
            c2.metric("Fill Rate", f"{cls['fill_pct']:.0f}%")
            c3.metric("Waitlisted", cls["waitlisted"])

            # Waitlist table
            waitlist = load_class_waitlist(cls["class_id"])
            if waitlist:
                df_w = pd.DataFrame(waitlist)
                st.dataframe(
                    df_w.rename(columns={
                        "priority": "Priority", "rank": "Rank", "last_name": "Last",
                        "first_name": "First", "dodid": "DODID", "unit": "Unit",
                        "request_date": "Requested",
                    }),
                    use_container_width=True, hide_index=True,
                )

    # Overall waitlist summary
    st.markdown("---")
    st.subheader("Waitlist Summary")
    total_waiting = sum(c["waitlisted"] for c in classes_with_waitlist)
    st.metric("Total Across All Classes", total_waiting)

    if HAS_PLOTLY:
        df_wl = pd.DataFrame(classes_with_waitlist)
        fig = go.Figure(data=[go.Bar(
            x=df_wl["class_name"],
            y=df_wl["waitlisted"],
            marker_color=RAG_AMBER,
            text=df_wl["waitlisted"],
            textposition="auto",
        )])
        fig.update_layout(
            height=350,
            xaxis_tickangle=-45,
            xaxis_title="",
            yaxis_title="Waitlisted Students",
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="app-footer">USAREUR-AF OPERATIONAL DATA TEAM — MSS ENROLLMENT MANAGER</div>',
    unsafe_allow_html=True,
)
