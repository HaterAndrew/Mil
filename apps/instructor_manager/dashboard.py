"""Instructor Certification Manager — Streamlit dashboard.

Tracks instructor certifications, course coverage gaps, expiration alerts,
individual instructor detail, and teaching workload analysis.
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

from instructor_manager.db import (
    ALL_COURSES,
    COURSE_CATALOG,
    Certification,
    Instructor,
    SessionLocal,
    TeachingHistory,
    get_coverage_matrix,
    get_expiring_certifications,
    get_instructor_certifications,
    get_instructor_load,
    init_db,
)

from theme import (
    inject_branding,
    apply_plotly_theme,
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
    RAG_COLORSCALE,
    GRAY_400,
    GRAY_700,
    WARNING_RED,
    CAUTION_AMBER,
)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
API_BASE = os.environ.get("INSTRUCTOR_MANAGER_API_URL", "http://localhost:8011")

st.set_page_config(
    page_title="MSS Instructor Manager",
    page_icon="\U0001F393",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_branding("MSS Instructor Manager")

# Military-style RAG color mapping
COLORS = {
    "GREEN": RAG_GREEN,
    "AMBER": RAG_AMBER,
    "RED": RAG_RED,
}


# ---------------------------------------------------------------------------
# Direct DB access (avoids API round-trips for dashboard analytics)
# ---------------------------------------------------------------------------
init_db()  # Ensure tables exist before any query


@st.cache_data(ttl=30)
def load_instructors():
    """Load all instructors with summary cert info."""
    db = SessionLocal()
    try:
        instructors = db.query(Instructor).order_by(Instructor.last_name).all()
        result = []
        for inst in instructors:
            current_certs = [
                c for c in inst.certifications if c.status == "CURRENT"
            ]
            result.append({
                "instructor_id": inst.instructor_id,
                "rank": inst.rank,
                "last_name": inst.last_name,
                "first_name": inst.first_name,
                "unit": inst.unit,
                "mos": inst.mos,
                "status": inst.status,
                "current_certs": len(current_certs),
                "cert_courses": sorted([c.course_id for c in current_certs]),
            })
        return result
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_coverage():
    """Load course coverage matrix from DB."""
    db = SessionLocal()
    try:
        return get_coverage_matrix(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_expiring(days: int):
    """Load certs expiring within N days."""
    db = SessionLocal()
    try:
        return get_expiring_certifications(days, db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_workload():
    """Load teaching workload (last 90 days)."""
    db = SessionLocal()
    try:
        return get_instructor_load(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_instructor_detail(instructor_id: str):
    """Load full detail for one instructor: certs + teaching history."""
    db = SessionLocal()
    try:
        inst = db.query(Instructor).filter(
            Instructor.instructor_id == instructor_id
        ).first()
        if not inst:
            return None

        certs = []
        for c in inst.certifications:
            days_left = (c.expiration_date - date.today()).days if c.status == "CURRENT" else None
            certs.append({
                "course_id": c.course_id,
                "course_name": COURSE_CATALOG.get(c.course_id, (c.course_id, 0))[0],
                "certified_date": c.certified_date.isoformat(),
                "expiration_date": c.expiration_date.isoformat(),
                "status": c.status,
                "certifying_authority": c.certifying_authority or "",
                "days_remaining": days_left,
            })

        history = []
        for h in sorted(inst.teaching_history, key=lambda x: x.event_date, reverse=True):
            history.append({
                "course_id": h.course_id,
                "course_name": COURSE_CATALOG.get(h.course_id, (h.course_id, 0))[0],
                "event_date": h.event_date.isoformat(),
                "location": h.location or "",
                "students_count": h.students_count,
                "rating": h.rating or "",
            })

        # Teaching events in last 90 days
        cutoff_90 = date.today() - timedelta(days=90)
        recent_count = len([h for h in inst.teaching_history if h.event_date >= cutoff_90])

        return {
            "instructor_id": inst.instructor_id,
            "rank": inst.rank,
            "last_name": inst.last_name,
            "first_name": inst.first_name,
            "unit": inst.unit,
            "mos": inst.mos,
            "status": inst.status,
            "certifications": certs,
            "teaching_history": history,
            "recent_event_count": recent_count,
        }
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
st.sidebar.title("MSS Instructor Manager")
st.sidebar.caption("USAREUR-AF Operational Data Team")
st.sidebar.markdown("---")

tab_names = [
    "Instructor Overview",
    "Course Coverage Matrix",
    "Expiration Tracker",
    "Instructor Detail",
    "Teaching Workload",
]
active_tab = st.sidebar.radio("Navigate", tab_names)


# =============================================================================
# TAB: Instructor Overview
# =============================================================================
if active_tab == "Instructor Overview":
    st.title("Instructor Overview")

    with st.spinner("Loading data..."):
        instructors = load_instructors()
        coverage = load_coverage()
        expiring_30 = load_expiring(30)

    if not instructors:
        st.info("No instructors loaded. Seed the database first.")
        st.stop()

    # --- KPI Row ---
    total = len(instructors)
    active = sum(1 for i in instructors if i["status"] == "ACTIVE")
    expiring_count = len(expiring_30)
    # Courses with zero certified instructors
    no_instructor = sum(1 for c in coverage if c["certified_count"] == 0)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Instructors", total)
    c2.metric("Active", active, delta=f"{active/total*100:.0f}%" if total else "0%")
    c3.metric("Certs Expiring <30d", expiring_count,
              delta_color="inverse",
              delta="action required" if expiring_count > 0 else "none")
    c4.metric("Courses w/ No Instructor", no_instructor,
              delta_color="inverse",
              delta="gap" if no_instructor > 0 else "covered")

    st.markdown("---")

    # --- Instructor roster table ---
    st.subheader("Instructor Roster")
    df = pd.DataFrame(instructors)
    # Format cert_courses as comma-separated string for display
    df["courses"] = df["cert_courses"].apply(lambda x: ", ".join(x) if x else "None")
    display_cols = ["instructor_id", "rank", "last_name", "first_name", "unit",
                    "mos", "status", "current_certs", "courses"]
    st.dataframe(
        df[display_cols].rename(columns={
            "instructor_id": "ID", "rank": "Rank", "last_name": "Last",
            "first_name": "First", "unit": "Unit", "mos": "MOS",
            "status": "Status", "current_certs": "Active Certs",
            "courses": "Certified Courses",
        }),
        use_container_width=True,
        hide_index=True,
    )


# =============================================================================
# TAB: Course Coverage Matrix
# =============================================================================
elif active_tab == "Course Coverage Matrix":
    st.title("Course Coverage Matrix")
    st.caption(
        "GREEN >= 3 certified instructors | AMBER >= 1 | RED = 0 (gap)"
    )

    coverage = load_coverage()
    if not coverage:
        st.info("No coverage data available.")
        st.stop()

    df_cov = pd.DataFrame(coverage)

    if HAS_PLOTLY:
        # Heatmap: single row showing certified count per course, colored by RAG
        colors = [COLORS.get(r, "#999") for r in df_cov["rag"]]

        fig = go.Figure(data=[go.Bar(
            x=df_cov["course_id"],
            y=df_cov["certified_count"],
            marker_color=colors,
            text=df_cov["certified_count"],
            textposition="auto",
            hovertext=[
                f"{row['course_id']}: {row['course_name']}<br>"
                f"{row['certified_count']} certified instructors<br>"
                f"Status: {row['rag']}"
                for _, row in df_cov.iterrows()
            ],
            hoverinfo="text",
        )])
        fig.update_layout(
            height=400,
            xaxis_tickangle=-45,
            xaxis_title="",
            yaxis_title="Certified Instructors",
            # Reference lines for RAG thresholds
            shapes=[
                dict(type="line", y0=3, y1=3, x0=-0.5, x1=len(df_cov) - 0.5,
                     line=dict(color=RAG_GREEN, width=2, dash="dash")),
                dict(type="line", y0=1, y1=1, x0=-0.5, x1=len(df_cov) - 0.5,
                     line=dict(color=RAG_AMBER, width=2, dash="dash")),
            ],
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # Summary counts
    st.subheader("Coverage Summary")
    cols = st.columns(3)
    green_count = sum(1 for c in coverage if c["rag"] == "GREEN")
    amber_count = sum(1 for c in coverage if c["rag"] == "AMBER")
    red_count = sum(1 for c in coverage if c["rag"] == "RED")
    cols[0].metric("GREEN (>= 3)", green_count)
    cols[1].metric("AMBER (1-2)", amber_count)
    cols[2].metric("RED (0 - GAP)", red_count)

    # List RED courses explicitly as warnings
    red_courses = [c for c in coverage if c["rag"] == "RED"]
    if red_courses:
        st.markdown("---")
        st.subheader("Critical Gaps — No Certified Instructors")
        for c in red_courses:
            st.error(f"**{c['course_id']}** ({c['course_name']}) — "
                     f"No certified instructors available. {c['hours']}hr course.")


# =============================================================================
# TAB: Expiration Tracker
# =============================================================================
elif active_tab == "Expiration Tracker":
    st.title("Certification Expiration Tracker")

    # Load all three windows
    exp_30 = load_expiring(30)
    exp_60 = load_expiring(60)
    exp_90 = load_expiring(90)

    # KPIs
    c1, c2, c3 = st.columns(3)
    c1.metric("Expiring <30 Days", len(exp_30))
    c2.metric("Expiring <60 Days", len(exp_60))
    c3.metric("Expiring <90 Days", len(exp_90))

    st.markdown("---")

    if not exp_90:
        st.success("No certifications expiring in the next 90 days.")
        st.stop()

    # Display with RAG color coding
    df_exp = pd.DataFrame(exp_90)

    # Color-coded display
    for _, row in df_exp.iterrows():
        rag = row["rag"]
        if rag == "RED":
            st.error(
                f"**{row['rank']} {row['last_name']}, {row['first_name']}** "
                f"({row['unit']}) — {row['course_id']} ({row['course_name']}) "
                f"expires {row['expiration_date']} "
                f"(**{row['days_remaining']}d remaining**)"
            )
        elif rag == "AMBER":
            st.warning(
                f"**{row['rank']} {row['last_name']}, {row['first_name']}** "
                f"({row['unit']}) — {row['course_id']} ({row['course_name']}) "
                f"expires {row['expiration_date']} "
                f"({row['days_remaining']}d remaining)"
            )
        else:
            st.info(
                f"**{row['rank']} {row['last_name']}, {row['first_name']}** "
                f"({row['unit']}) — {row['course_id']} ({row['course_name']}) "
                f"expires {row['expiration_date']} "
                f"({row['days_remaining']}d remaining)"
            )


# =============================================================================
# TAB: Instructor Detail
# =============================================================================
elif active_tab == "Instructor Detail":
    st.title("Instructor Detail Lookup")

    instructors = load_instructors()
    if not instructors:
        st.info("No instructors loaded.")
        st.stop()

    # Search by name or ID
    search = st.text_input("Search by name or ID", placeholder="MORRISON or INST-001")

    if search:
        search_upper = search.strip().upper()
        matches = [
            i for i in instructors
            if search_upper in i["last_name"]
            or search_upper in i["first_name"]
            or search_upper in i["instructor_id"]
        ]

        inst_id = None
        if not matches:
            st.warning("No matches found.")
        elif len(matches) > 1:
            options = [
                f"{m['rank']} {m['last_name']}, {m['first_name']} ({m['instructor_id']})"
                for m in matches
            ]
            selected = st.selectbox("Multiple matches — select:", options)
            idx = options.index(selected)
            inst_id = matches[idx]["instructor_id"]
        else:
            inst_id = matches[0]["instructor_id"]

        if inst_id is not None:
            detail = load_instructor_detail(inst_id)
            if detail:
                st.subheader(
                    f"{detail['rank']} {detail['last_name']}, {detail['first_name']}"
                )
                st.caption(
                    f"Unit: {detail['unit']} | MOS: {detail['mos']} | "
                    f"ID: {detail['instructor_id']} | Status: {detail['status']}"
                )

                # Workload indicator
                recent = detail["recent_event_count"]
                overloaded = recent > 5
                if overloaded:
                    st.warning(
                        f"Teaching load (90d): **{recent} events** — OVERLOADED"
                    )
                else:
                    st.info(f"Teaching load (90d): **{recent} events**")

                # Certifications table
                st.subheader("Certifications")
                if detail["certifications"]:
                    df_certs = pd.DataFrame(detail["certifications"])
                    st.dataframe(
                        df_certs.rename(columns={
                            "course_id": "Course", "course_name": "Name",
                            "certified_date": "Certified", "expiration_date": "Expires",
                            "status": "Status", "certifying_authority": "Authority",
                            "days_remaining": "Days Left",
                        }),
                        use_container_width=True,
                        hide_index=True,
                    )
                else:
                    st.info("No certifications on record.")

                # Teaching history table
                st.subheader("Teaching History")
                if detail["teaching_history"]:
                    df_hist = pd.DataFrame(detail["teaching_history"])
                    st.dataframe(
                        df_hist.rename(columns={
                            "course_id": "Course", "course_name": "Name",
                            "event_date": "Date", "location": "Location",
                            "students_count": "Students", "rating": "Rating",
                        }),
                        use_container_width=True,
                        hide_index=True,
                    )
                else:
                    st.info("No teaching history on record.")


# =============================================================================
# TAB: Teaching Workload
# =============================================================================
elif active_tab == "Teaching Workload":
    st.title("Teaching Workload (Last 90 Days)")
    st.caption(
        "Instructors with > 5 events in 90 days are flagged as overloaded."
    )

    workload = load_workload()
    if not workload:
        st.info("No active instructors found.")
        st.stop()

    df_wl = pd.DataFrame(workload)

    # KPIs
    total_events = df_wl["event_count"].sum()
    overloaded_count = df_wl["overloaded"].sum()
    avg_events = df_wl["event_count"].mean()

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Teaching Events (90d)", int(total_events))
    c2.metric("Overloaded Instructors", int(overloaded_count),
              delta_color="inverse",
              delta="rebalance" if overloaded_count > 0 else "balanced")
    c3.metric("Avg Events/Instructor", f"{avg_events:.1f}")

    st.markdown("---")

    if HAS_PLOTLY:
        # Bar chart: events per instructor, colored by overloaded status
        labels = [
            f"{r['rank']} {r['last_name']}" for _, r in df_wl.iterrows()
        ]
        colors = [
            WARNING_RED if r["overloaded"] else NAVY
            for _, r in df_wl.iterrows()
        ]

        fig = go.Figure(data=[go.Bar(
            x=labels,
            y=df_wl["event_count"],
            marker_color=colors,
            text=df_wl["event_count"],
            textposition="auto",
        )])

        # Overload threshold line
        fig.add_hline(
            y=5, line_dash="dash", line_color=RAG_AMBER,
            annotation_text="Overload threshold (5)",
            annotation_position="top right",
        )

        fig.update_layout(
            height=450,
            xaxis_tickangle=-45,
            xaxis_title="",
            yaxis_title="Teaching Events",
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # Overloaded instructors callout
    overloaded = [w for w in workload if w["overloaded"]]
    if overloaded:
        st.subheader("Overloaded Instructors")
        for w in overloaded:
            st.warning(
                f"**{w['rank']} {w['last_name']}, {w['first_name']}** "
                f"({w['unit']}) — {w['event_count']} events in 90 days"
            )

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="app-footer">USAREUR-AF OPERATIONAL DATA TEAM — MSS INSTRUCTOR MANAGER</div>',
    unsafe_allow_html=True,
)
