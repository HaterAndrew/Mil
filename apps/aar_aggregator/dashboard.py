"""AAR Aggregator — Streamlit dashboard.

Professional AAR analysis with priority matrix, keyword trends,
GO/NO_GO tracking, category co-occurrence, and issue resolution.
"""

from __future__ import annotations

import json
import os
import sys
from datetime import date, timedelta
from pathlib import Path

_app_dir = Path(__file__).resolve().parent
if str(_app_dir.parent) not in sys.path:
    sys.path.insert(0, str(_app_dir.parent))

import pandas as pd
import requests
import streamlit as st

try:
    import plotly.express as px
    import plotly.graph_objects as go
    HAS_PLOTLY = True
except ImportError:
    HAS_PLOTLY = False

from aar_aggregator.db import (
    AAR,
    SessionLocal,
    aar_summary_stats,
    category_cooccurrence,
    find_recurring_issues,
    go_nogo_trend,
    init_db,
    keyword_frequency,
    priority_matrix,
    trend_by_category,
    trend_over_time,
)

from theme import inject_branding, apply_plotly_theme, NAVY, NAVY_DARK, NAVY_LIGHT, NAVY_MID, GOLD, GOLD_DARK, GOLD_LIGHT, RAG_GREEN, RAG_AMBER, RAG_RED, GRAY_400, GRAY_700, WARNING_RED, CAUTION_AMBER, GREEN_OK, NOTE_TEAL

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
API_BASE = os.environ.get("AAR_AGGREGATOR_API_URL", "http://localhost:8003")

st.set_page_config(
    page_title="MSS AAR Aggregator",
    page_icon="\U0001F4CB",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_branding("MSS AAR Aggregator")

WFF_CATEGORIES = [
    "INTELLIGENCE", "FIRES", "MOVEMENT_MANEUVER",
    "SUSTAINMENT", "PROTECTION", "MISSION_COMMAND",
]

WFF_COLORS = {
    "INTELLIGENCE": NAVY_MID,
    "FIRES": WARNING_RED,
    "MOVEMENT_MANEUVER": GREEN_OK,
    "SUSTAINMENT": GOLD,
    "PROTECTION": "#6A1B9A",
    "MISSION_COMMAND": NOTE_TEAL,
    "UNCATEGORIZED": GRAY_400,
}


# ---------------------------------------------------------------------------
# Direct DB access
# ---------------------------------------------------------------------------
@st.cache_data(ttl=30)
def load_summary_stats():
    init_db()
    db = SessionLocal()
    try:
        return aar_summary_stats(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_priority_matrix():
    db = SessionLocal()
    try:
        return priority_matrix(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_keywords(top_n=25):
    db = SessionLocal()
    try:
        return keyword_frequency(db, top_n)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_go_nogo():
    db = SessionLocal()
    try:
        return go_nogo_trend(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_cooccurrence():
    db = SessionLocal()
    try:
        return category_cooccurrence(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_category_trend(date_from=None, date_to=None):
    db = SessionLocal()
    try:
        return trend_by_category(db, date_from, date_to)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_time_trend(date_from=None, date_to=None):
    db = SessionLocal()
    try:
        return trend_over_time(db, date_from, date_to)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_recurring(min_count=2, date_from=None, date_to=None):
    db = SessionLocal()
    try:
        return find_recurring_issues(db, min_count, date_from, date_to)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_aars():
    db = SessionLocal()
    try:
        aars = db.query(AAR).order_by(AAR.date.desc()).all()
        result = []
        for a in aars:
            result.append({
                "id": a.id,
                "date": a.date.isoformat(),
                "tm_levels": a.tm_levels,
                "location": a.location,
                "student_count": a.student_count,
                "instructor_names": a.instructor_names,
                "planned_objectives": a.planned_objectives,
                "actual_execution": a.actual_execution,
                "instructor_recommendations": a.instructor_recommendations,
                "submitted_by": a.submitted_by,
                "n_sustains": len(a.sustains),
                "n_improves": len(a.improves),
                "n_evals": len(a.evaluations),
                "n_discs": len(a.discrepancies),
                "sustains": [s.item_text for s in a.sustains],
                "improves": [{
                    "problem": i.problem, "proposed_fix": i.proposed_fix,
                    "priority": i.priority, "category": i.category, "owner": i.owner,
                } for i in a.improves],
                "evaluations": [{
                    "trainee_name": e.trainee_name, "tm_level": e.tm_level,
                    "result": e.result, "notes": e.notes,
                } for e in a.evaluations],
                "discrepancies": [{
                    "document": d.document, "section_page": d.section_page,
                    "issue_description": d.issue_description, "severity": d.severity,
                } for d in a.discrepancies],
            })
        return result
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Foundation / All course filter
# ---------------------------------------------------------------------------
FOUNDATION_COURSES = {"SL 1", "SL 2", "SL 3"}

TRACK_OPTIONS = {
    "Foundation (SL 1/2/3)": FOUNDATION_COURSES,
    "All Courses": None,  # None = no filter
}


def track_selector(key: str = "track_view") -> set[str] | None:
    """Render track view selector. Returns course set or None for all."""
    selected = st.radio(
        "Track View",
        list(TRACK_OPTIONS.keys()),
        index=0,
        horizontal=True,
        key=key,
    )
    return TRACK_OPTIONS[selected]


def filter_aars_by_track(aars: list[dict], track_courses: set[str] | None) -> list[dict]:
    """Filter AARs to those with at least one TM level in the active track."""
    if track_courses is None:
        return aars
    return [a for a in aars if any(tm in track_courses for tm in a["tm_levels"])]


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
st.sidebar.title("MSS AAR Aggregator")
st.sidebar.caption("USAREUR-AF Operational Data Team")
st.sidebar.markdown("---")

tab_names = [
    "Command Overview",
    "Priority Matrix",
    "Keyword Analysis",
    "GO/NO_GO Tracking",
    "Recurring Issues",
    "Category Analysis",
    "Browse AARs",
    "AAR Entry",
]
active_tab = st.sidebar.radio("Navigate", tab_names)

# Date filter (shared)
st.sidebar.markdown("---")
st.sidebar.subheader("Date Filter")
default_from = date.today() - timedelta(days=365)
date_from = st.sidebar.date_input("From", value=default_from, key="date_from")
date_to = st.sidebar.date_input("To", value=date.today(), key="date_to")


# =============================================================================
# TAB: Command Overview
# =============================================================================
if active_tab == "Command Overview":
    st.title("AAR Command Overview")

    active_track = track_selector(key="cmd_track")

    with st.spinner("Loading data..."):
        stats = load_summary_stats()
    if stats.get("total_aars", 0) == 0:
        st.info("No AARs in database. Seed data or enter AARs to get started.")
        st.stop()

    # KPI row
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    c1.metric("Total AARs", stats["total_aars"])
    c2.metric("Students Trained", stats["total_students_trained"])
    c3.metric("Overall GO Rate", f"{stats['overall_go_rate']}%")
    c4.metric("Improve Items", stats["total_improves"])
    c5.metric("Discrepancies", stats["total_discrepancies"])
    c6.metric("Sustain Items", stats["total_sustains"])

    st.markdown("---")

    col_l, col_r = st.columns(2)

    with col_l:
        # TM level breakdown — filtered to active track
        st.subheader("Training Events by TM Level")
        tm_counts = stats.get("tm_level_counts", {})
        if active_track is not None:
            tm_counts = {k: v for k, v in tm_counts.items() if k in active_track}
        if tm_counts and HAS_PLOTLY:
            df_tm = pd.DataFrame(list(tm_counts.items()), columns=["TM Level", "Count"])
            df_tm = df_tm.sort_values("TM Level")
            fig = px.bar(df_tm, x="TM Level", y="Count",
                         color="Count", color_continuous_scale="Blues")
            fig.update_layout(height=300, showlegend=False)
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

    with col_r:
        # Category breakdown
        st.subheader("Issues by WFF Category")
        cat_data = load_category_trend(date_from, date_to)
        if cat_data and HAS_PLOTLY:
            df_cat = pd.DataFrame(list(cat_data.items()), columns=["Category", "Count"])
            colors = [WFF_COLORS.get(c, "#999") for c in df_cat["Category"]]
            fig = go.Figure(data=[go.Bar(
                x=df_cat["Category"], y=df_cat["Count"],
                marker_color=colors,
                text=df_cat["Count"], textposition="auto",
            )])
            fig.update_layout(height=300, xaxis_tickangle=-30)
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # GO/NO_GO trend
    go_data = load_go_nogo()
    if go_data and HAS_PLOTLY:
        st.subheader("GO/NO_GO Rate Over Time")
        df_go = pd.DataFrame(go_data)
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df_go["date"], y=df_go["go_rate"],
            mode="lines+markers",
            name="GO Rate",
            marker_color=GREEN_OK,
            text=[f"{r['tm_level']}: {r['go_rate']}%" for _, r in df_go.iterrows()],
            hoverinfo="text+x",
        ))
        fig.add_hline(y=80, line_dash="dash", line_color=CAUTION_AMBER,
                      annotation_text="80% target")
        fig.update_layout(height=300, yaxis_range=[0, 105],
                          yaxis_title="GO Rate (%)", xaxis_title="")
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # Monthly improve trend
    time_data = load_time_trend(date_from, date_to)
    if time_data and HAS_PLOTLY:
        st.subheader("Monthly Improve Item Volume")
        df_time = pd.DataFrame(time_data)
        fig = px.area(df_time, x="month", y="improve_count",
                      color_discrete_sequence=[WARNING_RED])
        fig.update_layout(height=250, yaxis_title="Improve Items", xaxis_title="")
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)


# =============================================================================
# TAB: Priority Matrix
# =============================================================================
elif active_tab == "Priority Matrix":
    st.title("Issue Priority Matrix")
    st.caption("Frequency x Severity — top-right quadrant needs immediate action.")

    matrix = load_priority_matrix()
    if not matrix:
        st.info("No improve items to analyze.")
        st.stop()

    df = pd.DataFrame(matrix)

    if HAS_PLOTLY:
        # Scatter: frequency vs severity
        fig = px.scatter(
            df, x="frequency", y="severity_score",
            size="frequency",
            color="priority",
            color_discrete_map={"H": WARNING_RED, "M": CAUTION_AMBER, "L": GREEN_OK},
            hover_data=["problem", "category"],
            title="Issue Priority Matrix (Frequency x Severity)",
        )
        # Quadrant lines
        fig.add_hline(y=2, line_dash="dot", line_color="gray")
        fig.add_vline(x=2, line_dash="dot", line_color="gray")

        # Quadrant labels
        fig.add_annotation(x=max(df["frequency"]), y=3, text="ACT NOW",
                           showarrow=False, font=dict(color="red", size=14))
        fig.add_annotation(x=0.5, y=3, text="MONITOR",
                           showarrow=False, font=dict(color="orange", size=12))
        fig.add_annotation(x=max(df["frequency"]), y=1, text="WATCH",
                           showarrow=False, font=dict(color="orange", size=12))
        fig.add_annotation(x=0.5, y=1, text="LOW RISK",
                           showarrow=False, font=dict(color="green", size=12))

        fig.update_layout(
            height=500,
            xaxis_title="Frequency (# of AARs)",
            yaxis_title="Severity (H=3, M=2, L=1)",
            yaxis=dict(tickvals=[1, 2, 3], ticktext=["Low", "Medium", "High"]),
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # Action items table
    st.subheader("Priority-Ranked Issues")
    for item in matrix[:10]:
        severity_icon = {"H": "\U0001F534", "M": "\U0001F7E1", "L": "\U0001F7E2"}.get(item["priority"], "\u26AA")
        cat = item["category"] or "Uncategorized"
        st.markdown(
            f"{severity_icon} **{item['problem']}** — "
            f"Frequency: {item['frequency']} | Priority: {item['priority']} | "
            f"Category: {cat} | AARs: {item['aar_ids']}"
        )


# =============================================================================
# TAB: Keyword Analysis
# =============================================================================
elif active_tab == "Keyword Analysis":
    st.title("Issue Keyword Analysis")
    st.caption("Most frequent terms in improve item descriptions — identifies systemic themes.")

    top_n = st.slider("Top N keywords", 10, 40, 25)
    keywords = load_keywords(top_n)

    if not keywords:
        st.info("No improve items to analyze.")
        st.stop()

    if HAS_PLOTLY:
        df_kw = pd.DataFrame(keywords)
        fig = px.bar(
            df_kw, x="count", y="word",
            orientation="h",
            title=f"Top {top_n} Keywords in Improve Items",
            color="count",
            color_continuous_scale="Reds",
        )
        fig.update_layout(
            height=max(400, top_n * 25),
            yaxis=dict(categoryorder="total ascending"),
            xaxis_title="Frequency", yaxis_title="",
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # Category co-occurrence
    cooccur = load_cooccurrence()
    if cooccur and HAS_PLOTLY:
        st.subheader("WFF Category Co-occurrence")
        st.caption("Which WFF problem areas tend to appear together in the same AARs.")
        df_co = pd.DataFrame(cooccur)
        if not df_co.empty:
            fig = px.scatter(
                df_co, x="category_a", y="category_b",
                size="co_occurrences",
                color="co_occurrences",
                color_continuous_scale="YlOrRd",
                title="Category Co-occurrence Matrix",
            )
            fig.update_layout(height=400)
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

            st.dataframe(df_co.rename(columns={
                "category_a": "Category A", "category_b": "Category B",
                "co_occurrences": "Co-occurrences",
            }), use_container_width=True, hide_index=True)


# =============================================================================
# TAB: GO/NO_GO Tracking
# =============================================================================
elif active_tab == "GO/NO_GO Tracking":
    st.title("Student Evaluation Tracking")

    active_track = track_selector(key="gonogo_track")

    go_data = load_go_nogo()
    if not go_data:
        st.info("No evaluation data.")
        st.stop()

    # Filter to active track
    if active_track is not None:
        go_data = [g for g in go_data if g["tm_level"] in active_track]
    if not go_data:
        st.info("No evaluation data for selected track.")
        st.stop()

    df = pd.DataFrame(go_data)

    # Overall stats
    total_go = df["go_count"].sum()
    total_nogo = df["nogo_count"].sum()
    total_eval = total_go + total_nogo
    overall_rate = round(total_go / total_eval * 100, 1) if total_eval else 0

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Evaluated", total_eval)
    c2.metric("GO", total_go)
    c3.metric("NO_GO", total_nogo)
    c4.metric("Overall GO Rate", f"{overall_rate}%")

    st.markdown("---")

    if HAS_PLOTLY:
        col_l, col_r = st.columns(2)

        with col_l:
            # GO rate over time with color coding
            colors = [GREEN_OK if r >= 85 else CAUTION_AMBER if r >= 70 else WARNING_RED
                      for r in df["go_rate"]]
            fig = go.Figure(data=[go.Bar(
                x=df["date"],
                y=df["go_rate"],
                marker_color=colors,
                text=[f"{r['tm_level']}<br>{r['go_rate']}%" for _, r in df.iterrows()],
                textposition="auto",
            )])
            fig.update_layout(
                title="GO Rate by Training Event",
                height=400, yaxis_range=[0, 105],
                yaxis_title="GO Rate (%)", xaxis_title="",
            )
            fig.add_hline(y=80, line_dash="dash", line_color="gray",
                          annotation_text="80% target")
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

        with col_r:
            # GO rate by TM level
            df_by_tm = df.groupby("tm_level").agg(
                total_go=("go_count", "sum"),
                total_nogo=("nogo_count", "sum"),
            ).reset_index()
            df_by_tm["go_rate"] = round(
                df_by_tm["total_go"] / (df_by_tm["total_go"] + df_by_tm["total_nogo"]) * 100, 1
            )
            df_by_tm = df_by_tm.sort_values("tm_level")

            fig = go.Figure()
            fig.add_trace(go.Bar(name="GO", x=df_by_tm["tm_level"],
                                 y=df_by_tm["total_go"], marker_color=GREEN_OK))
            fig.add_trace(go.Bar(name="NO_GO", x=df_by_tm["tm_level"],
                                 y=df_by_tm["total_nogo"], marker_color=WARNING_RED))
            fig.update_layout(
                title="GO/NO_GO by TM Level",
                barmode="stack", height=400,
                xaxis_title="", yaxis_title="Students",
            )
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

    # Detail table
    st.subheader("Evaluation Detail by Event")
    st.dataframe(
        df.rename(columns={
            "date": "Date", "tm_level": "TM Level",
            "total_evaluated": "Evaluated", "go_count": "GO",
            "nogo_count": "NO_GO", "go_rate": "GO Rate %",
        }),
        use_container_width=True, hide_index=True,
    )


# =============================================================================
# TAB: Recurring Issues
# =============================================================================
elif active_tab == "Recurring Issues":
    st.title("Recurring Issues")
    st.caption("Problems appearing in 2+ AARs -- signals systemic issues requiring action.")

    recurring = load_recurring(2, date_from, date_to)

    if not recurring:
        st.info("No recurring issues found in the selected date range.")
        st.stop()

    # Summary
    st.metric("Systemic Issues Identified", len(recurring))
    st.markdown("---")

    for item in recurring:
        severity_icon = {"H": "\U0001F534", "M": "\U0001F7E1", "L": "\U0001F7E2"}.get(
            item.get("priority", "M"), "\u26AA")

        with st.container():
            cols = st.columns([4, 1, 1, 1])
            cols[0].markdown(f"{severity_icon} **{item['problem']}**")
            cols[1].metric("Occurrences", item["count"])
            cols[2].write(f"Priority: **{item.get('priority', 'N/A')}**")
            cols[3].write(f"Category: {item.get('category', 'N/A')}")
            st.caption(f"AAR IDs: {item['aar_ids']} | Dates: {', '.join(d for d in item['dates'] if d)}")
            st.markdown("---")


# =============================================================================
# TAB: Category Analysis
# =============================================================================
elif active_tab == "Category Analysis":
    st.title("WFF Category Analysis")

    cat_data = load_category_trend(date_from, date_to)
    time_data = load_time_trend(date_from, date_to)

    if not cat_data:
        st.info("No data in selected date range.")
        st.stop()

    if HAS_PLOTLY:
        col_l, col_r = st.columns(2)

        with col_l:
            st.subheader("Issues by WFF Category")
            df_cat = pd.DataFrame(list(cat_data.items()), columns=["Category", "Count"])
            colors = [WFF_COLORS.get(c, "#999") for c in df_cat["Category"]]
            fig = go.Figure(data=[go.Pie(
                labels=df_cat["Category"], values=df_cat["Count"],
                marker=dict(colors=colors),
                textinfo="label+percent",
                hole=0.4,
            )])
            fig.update_layout(height=400, title="WFF Distribution")
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

        with col_r:
            if time_data:
                st.subheader("Monthly Improve Item Trend")
                df_time = pd.DataFrame(time_data)
                fig = px.line(df_time, x="month", y="improve_count",
                              markers=True, title="Issues Over Time")
                fig.update_layout(height=400, yaxis_title="Count", xaxis_title="")
                apply_plotly_theme(fig)
                st.plotly_chart(fig, use_container_width=True)

    # Co-occurrence
    cooccur = load_cooccurrence()
    if cooccur:
        st.subheader("WFF Category Co-occurrence")
        df_co = pd.DataFrame(cooccur)
        st.dataframe(df_co.rename(columns={
            "category_a": "Category A", "category_b": "Category B",
            "co_occurrences": "Times Co-occurring",
        }), use_container_width=True, hide_index=True)


# =============================================================================
# TAB: Browse AARs
# =============================================================================
elif active_tab == "Browse AARs":
    st.title("Browse AARs")

    active_track = track_selector(key="browse_track")

    aars = load_aars()
    if not aars:
        st.info("No AARs found.")
        st.stop()

    # Apply track filter first
    aars = filter_aars_by_track(aars, active_track)

    # Additional TM level filter within the track
    tm_filter = st.multiselect("Filter by TM Level",
                                sorted(set(tm for a in aars for tm in a["tm_levels"])))

    filtered = aars
    if tm_filter:
        filtered = [a for a in aars if any(tm in a["tm_levels"] for tm in tm_filter)]

    st.caption(f"Showing {len(filtered)} of {len(aars)} AARs")

    for aar in filtered:
        tm_str = ", ".join(aar["tm_levels"])
        with st.expander(
            f"AAR #{aar['id']} -- {aar['date']} | {tm_str} | "
            f"{aar['student_count']} students | "
            f"{aar['n_improves']} improves, {aar['n_discs']} discrepancies"
        ):
            col_l, col_r = st.columns(2)
            with col_l:
                st.markdown(f"**Submitted by:** {aar['submitted_by']}")
                st.markdown(f"**Location:** {aar['location']}")
                st.markdown(f"**Students:** {aar['student_count']}")
            with col_r:
                st.markdown(f"**Instructors:** {', '.join(aar['instructor_names'])}")
                st.markdown(f"**Sustains:** {aar['n_sustains']} | **Improves:** {aar['n_improves']}")
                st.markdown(f"**Evaluations:** {aar['n_evals']} | **Discrepancies:** {aar['n_discs']}")

            st.markdown("---")

            st.markdown("**Planned Objectives:**")
            st.text(aar["planned_objectives"])
            st.markdown("**What Actually Happened:**")
            st.text(aar["actual_execution"])

            if aar["sustains"]:
                st.markdown("**Sustains:**")
                for s in aar["sustains"]:
                    st.markdown(f"- {s}")

            if aar["improves"]:
                st.markdown("**Improve Items:**")
                df_imp = pd.DataFrame(aar["improves"])
                st.dataframe(df_imp.rename(columns={
                    "problem": "Problem", "proposed_fix": "Fix",
                    "priority": "Pri", "category": "Category", "owner": "Owner",
                }), use_container_width=True, hide_index=True)

            if aar["evaluations"]:
                st.markdown("**Student Evaluations:**")
                df_ev = pd.DataFrame(aar["evaluations"])
                st.dataframe(df_ev.rename(columns={
                    "trainee_name": "Trainee", "tm_level": "TM",
                    "result": "Result", "notes": "Notes",
                }), use_container_width=True, hide_index=True)

            if aar["discrepancies"]:
                st.markdown("**Curriculum Discrepancies:**")
                df_disc = pd.DataFrame(aar["discrepancies"])
                st.dataframe(df_disc.rename(columns={
                    "document": "Document", "section_page": "Section",
                    "issue_description": "Issue", "severity": "Sev",
                }), use_container_width=True, hide_index=True)

            if aar.get("instructor_recommendations"):
                st.markdown("**Instructor Recommendations:**")
                st.text(aar["instructor_recommendations"])


# =============================================================================
# TAB: AAR Entry
# =============================================================================
elif active_tab == "AAR Entry":
    st.title("New AAR Entry")

    def api_post(endpoint, json_data=None, files=None):
        try:
            if files:
                resp = requests.post(f"{API_BASE}{endpoint}", files=files, timeout=30)
            else:
                resp = requests.post(f"{API_BASE}{endpoint}", json=json_data, timeout=30)
            return resp
        except requests.ConnectionError:
            st.error(f"Cannot reach API at {API_BASE}.")
            return None

    with st.form("aar_form"):
        st.subheader("Section 1 -- Event Details")
        col1, col2 = st.columns(2)
        with col1:
            aar_date = st.date_input("Date of Training")
            location = st.text_input("Location / Environment", placeholder="MSS sandbox")
            student_count = st.number_input("Number of Students", min_value=1, value=8)
        with col2:
            tm_input = st.text_input("TM Levels (comma-separated)", placeholder="SL 1, SL 2")
            ex_input = st.text_input("Exercises (comma-separated)", placeholder="EX_10")
            instr_input = st.text_input("Instructor Names (comma-separated)", placeholder="MAJ SMITH, SGT KELLY")

        st.subheader("Section 2 -- What Was Planned")
        planned = st.text_area("Training Objectives", height=100)

        st.subheader("Section 3 -- What Actually Happened")
        actual = st.text_area("Execution Description", height=100)

        st.subheader("Section 4 -- Sustain (2-5 items)")
        sustains = []
        for i in range(5):
            s = st.text_input(f"Sustain {i+1}", key=f"sustain_{i}",
                              placeholder="What worked well?" if i < 2 else "(optional)")
            if s.strip():
                sustains.append(s.strip())

        st.subheader("Section 5 -- Improve")
        improves = []
        for i in range(5):
            cols = st.columns([3, 2, 1, 1])
            problem = cols[0].text_input(f"Problem {i+1}", key=f"imp_prob_{i}")
            fix = cols[1].text_input(f"Fix {i+1}", key=f"imp_fix_{i}")
            priority = cols[2].selectbox("Priority", ["H", "M", "L"], key=f"imp_pri_{i}", index=1)
            category = cols[3].selectbox("Category", [""] + WFF_CATEGORIES, key=f"imp_cat_{i}")
            if problem.strip():
                improves.append({
                    "problem": problem.strip(),
                    "proposed_fix": fix.strip() or None,
                    "owner": None,
                    "priority": priority,
                    "category": category if category else None,
                })

        st.subheader("Section 9 -- Instructor Recommendations")
        recommendations = st.text_area("Recommendations", height=80)

        submitted_by = st.text_input("Submitted By", placeholder="MAJ SMITH")

        submitted = st.form_submit_button("Submit AAR")

    if submitted:
        if not planned or not actual or not sustains or not submitted_by:
            st.warning("Fill in required fields: objectives, execution, at least 1 sustain, submitted by.")
        else:
            tm_levels = [t.strip().upper() for t in tm_input.split(",") if t.strip()]
            exercises = [e.strip().upper() for e in ex_input.split(",") if e.strip()]
            instructors = [n.strip() for n in instr_input.split(",") if n.strip()]

            payload = {
                "date": aar_date.isoformat(),
                "tm_levels": tm_levels or ["SL 1"],
                "exercises": exercises,
                "location": location or "Unknown",
                "student_count": student_count,
                "instructor_names": instructors or ["Unknown"],
                "planned_objectives": planned,
                "actual_execution": actual,
                "sustains": sustains,
                "improves": improves,
                "evaluations": [],
                "discrepancies": [],
                "env_issues": [],
                "instructor_recommendations": recommendations or None,
                "submitted_by": submitted_by,
            }

            resp = api_post("/aars", json_data=payload)
            if resp and resp.status_code == 201:
                st.success(f"AAR created: ID {resp.json()['id']}")
                st.cache_data.clear()
            elif resp:
                st.error(f"Failed: {resp.text}")

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="app-footer">USAREUR-AF OPERATIONAL DATA TEAM — MSS AAR AGGREGATOR</div>',
    unsafe_allow_html=True,
)
