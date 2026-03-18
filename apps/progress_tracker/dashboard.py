"""Progress Tracker — Streamlit dashboard.

Individual soldier training timeline visualization, stalled/overdue
flagging, printable training records, and goal tracking.
"""

from __future__ import annotations

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

from progress_tracker.db import (
    COURSE_CATALOG,
    SessionLocal,
    flag_overdue,
    generate_training_record,
    get_all_overdue,
    get_soldier_goals,
    get_soldier_timeline,
    get_stalled_soldiers,
    init_db,
)
from readiness_tracker.db import (
    SessionLocal as RTSessionLocal,
    Trainee,
    init_db as rt_init_db,
)

from theme import (
    apply_plotly_theme,
    inject_branding,
    GOLD,
    GOLD_DARK,
    GOLD_LIGHT,
    GRAY_100,
    GRAY_400,
    GRAY_700,
    NAVY,
    NAVY_DARK,
    NAVY_LIGHT,
    NAVY_MID,
    RAG_AMBER,
    RAG_GREEN,
    RAG_RED,
    WARNING_RED,
    CAUTION_AMBER,
)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
API_BASE = "http://localhost:8004"

st.set_page_config(
    page_title="MSS Progress Tracker",
    page_icon="\U0001F4C8",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_branding("MSS Progress Tracker")

# Status color mapping
STATUS_COLORS = {
    "COMPLETE": RAG_GREEN,
    "ON_TRACK": NAVY_MID,
    "AT_RISK": RAG_AMBER,
    "OVERDUE": RAG_RED,
}

# ---------------------------------------------------------------------------
# Initialize DBs
# ---------------------------------------------------------------------------
rt_init_db()
init_db()


# ---------------------------------------------------------------------------
# Cached data loaders
# ---------------------------------------------------------------------------
@st.cache_data(ttl=30)
def load_trainees() -> list[dict]:
    """Load all trainees from readiness_tracker DB."""
    db = RTSessionLocal()
    try:
        trainees = db.query(Trainee).order_by(Trainee.last_name).all()
        return [
            {
                "dodid": t.dodid,
                "name": f"{t.last_name}, {t.first_name}",
                "rank": t.rank,
                "unit": t.unit,
                "mos": t.mos or "",
            }
            for t in trainees
        ]
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_stalled(days: int) -> list[dict]:
    db = SessionLocal()
    try:
        return get_stalled_soldiers(db, days=days)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_overdue() -> list[dict]:
    db = SessionLocal()
    try:
        return get_all_overdue(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_timeline(dodid: str) -> list[dict]:
    db = SessionLocal()
    try:
        return get_soldier_timeline(dodid, db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_record(dodid: str) -> dict | None:
    db = SessionLocal()
    try:
        return generate_training_record(dodid, db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_goals(dodid: str) -> list[dict]:
    db = SessionLocal()
    try:
        return get_soldier_goals(dodid, db)
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Helper: soldier selector
# ---------------------------------------------------------------------------
def soldier_selector(key: str = "soldier_sel") -> str | None:
    """Render a soldier search/select widget. Returns DODID or None."""
    trainees = load_trainees()
    if not trainees:
        st.info("No trainees loaded. Seed both readiness_tracker and progress_tracker.")
        return None

    search = st.text_input(
        "Search by name or DODID",
        placeholder="KELLY or 1000000000",
        key=f"search_{key}",
    )

    if search:
        search_upper = search.strip().upper()
        matches = [
            t for t in trainees
            if search_upper in t["name"].upper() or search_upper in t["dodid"]
        ]
        if not matches:
            st.warning("No matches found.")
            return None
        elif len(matches) > 1:
            options = [f"{t['rank']} {t['name']} ({t['dodid']})" for t in matches]
            selected = st.selectbox("Multiple matches:", options, key=f"select_{key}")
            idx = options.index(selected)
            return matches[idx]["dodid"]
        else:
            return matches[0]["dodid"]
    return None


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
st.sidebar.title("MSS Progress Tracker")
st.sidebar.caption("USAREUR-AF Operational Data Team")
st.sidebar.markdown("---")

tab_names = [
    "Timeline View",
    "Stalled Soldiers",
    "Overdue Milestones",
    "Training Record",
    "Goal Tracker",
]
active_tab = st.sidebar.radio("Navigate", tab_names)


# =============================================================================
# TAB: Timeline View
# =============================================================================
if active_tab == "Timeline View":
    st.title("Individual Training Timeline")
    st.caption("Select a soldier to view their training milestones as a Gantt-style chart.")

    dodid = soldier_selector(key="timeline")

    if dodid:
        timeline = load_timeline(dodid)
        record = load_record(dodid)

        if record:
            # Soldier header
            st.subheader(f"{record['rank']} {record['name']}")
            st.caption(f"Unit: {record['unit']} | DODID: {dodid}")

            c1, c2, c3 = st.columns(3)
            c1.metric("Milestones", len(timeline))
            c2.metric("% Complete", f"{record['pct_complete']:.0f}%")
            status_label = record["overall_status"]
            c3.metric("Overall Status", status_label)

            st.markdown("---")

        if not timeline:
            st.info("No milestones set for this soldier. Add milestones via the API or seed data.")
        elif HAS_PLOTLY:
            # Build Gantt-like horizontal bar chart
            # Each milestone is a bar from created_at (or 30 days before target) to target_date
            gantt_data = []
            for m in timeline:
                # Use created_at as start, or 30 days before target if no created_at
                start = m["target_date"] - timedelta(days=30)
                gantt_data.append({
                    "Course": f"{m['course_id']} - {m['course_name']}",
                    "Start": start,
                    "End": m["target_date"],
                    "Status": m["status"],
                    "Days Remaining": m["days_remaining"],
                })

            df_gantt = pd.DataFrame(gantt_data)

            fig = px.timeline(
                df_gantt,
                x_start="Start",
                x_end="End",
                y="Course",
                color="Status",
                color_discrete_map=STATUS_COLORS,
                hover_data=["Days Remaining"],
            )
            fig.update_layout(
                height=max(250, len(timeline) * 50 + 100),
                xaxis_title="",
                yaxis_title="",
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=1.02),
            )
            # Add today line
            fig.add_vline(
                x=date.today().isoformat(),
                line_dash="dash",
                line_color=GOLD,
                line_width=2,
                annotation_text="TODAY",
                annotation_font_color=GOLD,
            )
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

            # Detail table below
            st.subheader("Milestone Details")
            df_detail = pd.DataFrame(timeline)
            display_cols = ["course_id", "course_name", "target_date", "status", "days_remaining", "notes"]
            available_cols = [c for c in display_cols if c in df_detail.columns]
            st.dataframe(
                df_detail[available_cols].rename(columns={
                    "course_id": "Course",
                    "course_name": "Name",
                    "target_date": "Target Date",
                    "status": "Status",
                    "days_remaining": "Days Remaining",
                    "notes": "Notes",
                }),
                use_container_width=True,
                hide_index=True,
            )


# =============================================================================
# TAB: Stalled Soldiers
# =============================================================================
elif active_tab == "Stalled Soldiers":
    st.title("Stalled Training Progression")
    st.caption("Soldiers with no new course completions within the configurable threshold.")

    days_threshold = st.slider(
        "Days without activity",
        min_value=7,
        max_value=180,
        value=30,
        step=7,
        key="stalled_days",
    )

    stalled = load_stalled(days_threshold)

    if not stalled:
        st.success(f"No soldiers stalled beyond {days_threshold} days.")
    else:
        st.warning(f"**{len(stalled)} soldiers** with no progress in {days_threshold}+ days.")

        # KPI row
        units_affected = len(set(s["unit"] for s in stalled))
        avg_days = sum(s["days_since_activity"] for s in stalled) / len(stalled)
        c1, c2, c3 = st.columns(3)
        c1.metric("Stalled Soldiers", len(stalled))
        c2.metric("Units Affected", units_affected)
        c3.metric("Avg Days Stalled", f"{avg_days:.0f}")

        st.markdown("---")

        # Stalled by unit bar chart
        if HAS_PLOTLY:
            df_stalled = pd.DataFrame(stalled)
            unit_counts = df_stalled.groupby("unit").size().reset_index(name="count")
            fig = go.Figure(data=[go.Bar(
                x=unit_counts["unit"],
                y=unit_counts["count"],
                marker_color=WARNING_RED,
                text=unit_counts["count"],
                textposition="auto",
            )])
            fig.update_layout(
                height=300,
                xaxis_title="",
                yaxis_title="Stalled Soldiers",
                title="Stalled Soldiers by Unit",
            )
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

        # Detail table
        st.subheader("Stalled Personnel List")
        df_s = pd.DataFrame(stalled)
        display_cols = ["rank", "name", "unit", "furthest_course", "last_completion_date", "days_since_activity"]
        available_cols = [c for c in display_cols if c in df_s.columns]
        st.dataframe(
            df_s[available_cols].rename(columns={
                "rank": "Rank",
                "name": "Name",
                "unit": "Unit",
                "furthest_course": "Furthest Course",
                "last_completion_date": "Last Completion",
                "days_since_activity": "Days Stalled",
            }),
            use_container_width=True,
            hide_index=True,
        )


# =============================================================================
# TAB: Overdue Milestones
# =============================================================================
elif active_tab == "Overdue Milestones":
    st.title("Overdue Training Milestones")
    st.caption("All milestones past their target date, grouped by unit.")

    overdue = load_overdue()

    if not overdue:
        st.success("No overdue milestones.")
    else:
        st.error(f"**{len(overdue)} overdue milestones** across the formation.")

        # KPI row
        units_with_overdue = len(set(o["unit"] for o in overdue))
        max_overdue = max(o["days_overdue"] for o in overdue) if overdue else 0
        c1, c2, c3 = st.columns(3)
        c1.metric("Overdue Items", len(overdue))
        c2.metric("Units Affected", units_with_overdue)
        c3.metric("Worst Overdue (days)", max_overdue)

        st.markdown("---")

        # Overdue by unit bar chart
        if HAS_PLOTLY:
            df_od = pd.DataFrame(overdue)
            unit_counts = df_od.groupby("unit").size().reset_index(name="count")
            fig = go.Figure(data=[go.Bar(
                x=unit_counts["unit"],
                y=unit_counts["count"],
                marker_color=RAG_RED,
                text=unit_counts["count"],
                textposition="auto",
            )])
            fig.update_layout(
                height=300,
                xaxis_title="",
                yaxis_title="Overdue Milestones",
                title="Overdue Milestones by Unit",
            )
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

            # Overdue by course
            st.subheader("Overdue by Course")
            course_counts = df_od.groupby("course_id").size().reset_index(name="count")
            course_counts = course_counts.sort_values("count", ascending=False)
            fig2 = go.Figure(data=[go.Bar(
                x=course_counts["course_id"],
                y=course_counts["count"],
                marker_color=CAUTION_AMBER,
                text=course_counts["count"],
                textposition="auto",
            )])
            fig2.update_layout(
                height=300,
                xaxis_title="",
                yaxis_title="Count",
                title="Overdue Milestones by Course",
            )
            apply_plotly_theme(fig2)
            st.plotly_chart(fig2, use_container_width=True)

        # Detail table
        st.subheader("Overdue Details")
        df_detail = pd.DataFrame(overdue)
        display_cols = ["rank", "name", "unit", "course_id", "course_name", "target_date", "days_overdue"]
        available_cols = [c for c in display_cols if c in df_detail.columns]
        st.dataframe(
            df_detail[available_cols].rename(columns={
                "rank": "Rank",
                "name": "Name",
                "unit": "Unit",
                "course_id": "Course",
                "course_name": "Course Name",
                "target_date": "Target Date",
                "days_overdue": "Days Overdue",
            }),
            use_container_width=True,
            hide_index=True,
        )


# =============================================================================
# TAB: Training Record
# =============================================================================
elif active_tab == "Training Record":
    st.title("Individual Training Record")
    st.caption("Select a soldier to view their full training record (printable format).")

    dodid = soldier_selector(key="record")

    if dodid:
        record = load_record(dodid)
        if not record:
            st.error("Trainee not found.")
        else:
            # Printable header block
            st.markdown(f"""
            <div style="border: 2px solid {NAVY}; border-radius: 4px; padding: 16px; margin-bottom: 16px;
                        background: linear-gradient(to right, {NAVY} 0%, {NAVY} 4px, white 4px);">
                <div style="padding-left: 12px;">
                    <h2 style="margin: 0; color: {NAVY};">INDIVIDUAL TRAINING RECORD</h2>
                    <table style="width: 100%; margin-top: 12px; font-size: 14px;">
                        <tr>
                            <td><strong>Name:</strong> {record['name']}</td>
                            <td><strong>Rank:</strong> {record['rank']}</td>
                            <td><strong>DODID:</strong> {record['dodid']}</td>
                        </tr>
                        <tr>
                            <td><strong>Unit:</strong> {record['unit']}</td>
                            <td><strong>MOS:</strong> {record.get('mos', '')}</td>
                            <td><strong>Date:</strong> {date.today().isoformat()}</td>
                        </tr>
                    </table>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Status summary
            status_color = STATUS_COLORS.get(record["overall_status"], GRAY_400)
            c1, c2, c3 = st.columns(3)
            c1.metric("Overall Status", record["overall_status"])
            c2.metric("% Complete", f"{record['pct_complete']:.0f}%")
            c3.metric("Total Milestones", len(record["milestones"]))

            st.progress(record["pct_complete"] / 100, text=f"{record['pct_complete']:.0f}% milestones complete")

            # Milestones table
            if record["milestones"]:
                st.subheader("Training Milestones")
                df_m = pd.DataFrame(record["milestones"])
                display_cols = ["course_id", "course_name", "target_date", "status", "days_remaining", "notes"]
                available_cols = [c for c in display_cols if c in df_m.columns]
                st.dataframe(
                    df_m[available_cols].rename(columns={
                        "course_id": "Course",
                        "course_name": "Name",
                        "target_date": "Target",
                        "status": "Status",
                        "days_remaining": "Days Rem",
                        "notes": "Notes",
                    }),
                    use_container_width=True,
                    hide_index=True,
                )

            # Completion history
            if record.get("completions"):
                st.subheader("Completion History")
                df_c = pd.DataFrame(record["completions"])
                display_cols = ["course_id", "course_name", "result", "evaluation_date", "evaluator_name"]
                available_cols = [c for c in display_cols if c in df_c.columns]
                st.dataframe(
                    df_c[available_cols].rename(columns={
                        "course_id": "Course",
                        "course_name": "Name",
                        "result": "Result",
                        "evaluation_date": "Eval Date",
                        "evaluator_name": "Evaluator",
                    }),
                    use_container_width=True,
                    hide_index=True,
                )

            # Print hint
            st.markdown("---")
            st.caption("Use browser print (Ctrl+P / Cmd+P) to generate a printable PDF of this record.")


# =============================================================================
# TAB: Goal Tracker
# =============================================================================
elif active_tab == "Goal Tracker":
    st.title("Individual Goal Tracker")
    st.caption("Set and track training goals with prereq eligibility indicators.")

    dodid = soldier_selector(key="goals")

    if dodid:
        goals = load_goals(dodid)
        record = load_record(dodid)

        if record:
            st.subheader(f"{record['rank']} {record['name']}")
            st.caption(f"Unit: {record['unit']} | DODID: {dodid}")
            st.markdown("---")

        if not goals:
            st.info("No goals set for this soldier.")
        else:
            st.subheader("Active Goals")
            for g in goals:
                # Determine visual indicator
                if g["achieved"]:
                    icon = "\u2705"
                    border_color = RAG_GREEN
                    status_text = "ACHIEVED"
                    bg = f"rgba(26,92,40,0.06)"
                elif not g["eligible"]:
                    icon = "\U0001F512"
                    border_color = GRAY_400
                    status_text = f"LOCKED — Missing: {', '.join(g['missing_prereqs'])}"
                    bg = f"rgba(122,136,168,0.06)"
                else:
                    # Eligible, check if overdue
                    days_left = (g["target_date"] - date.today()).days
                    if days_left < 0:
                        icon = "\u26A0\uFE0F"
                        border_color = RAG_RED
                        status_text = f"OVERDUE by {abs(days_left)} days"
                        bg = f"rgba(138,26,26,0.06)"
                    elif days_left <= 14:
                        icon = "\U0001F7E1"
                        border_color = RAG_AMBER
                        status_text = f"AT RISK — {days_left} days remaining"
                        bg = f"rgba(184,104,16,0.06)"
                    else:
                        icon = "\U0001F7E2"
                        border_color = NAVY_MID
                        status_text = f"ON TRACK — {days_left} days remaining"
                        bg = f"rgba(30,74,136,0.06)"

                course_name = g.get("course_name", g["target_course"])
                st.markdown(f"""
                <div style="border: 2px solid {border_color}; border-radius: 6px; padding: 12px;
                            margin-bottom: 8px; background: {bg};">
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="font-size: 24px;">{icon}</span>
                        <div>
                            <div style="font-weight: bold; color: {NAVY};">
                                {g['target_course']} — {course_name}
                            </div>
                            <div style="font-size: 12px; color: {GRAY_700};">
                                Target: {g['target_date']} | {status_text}
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        # Goal progress chart
        if goals and HAS_PLOTLY:
            achieved_count = sum(1 for g in goals if g["achieved"])
            remaining = len(goals) - achieved_count
            fig = go.Figure(data=[go.Pie(
                labels=["Achieved", "In Progress"],
                values=[achieved_count, remaining],
                marker=dict(colors=[RAG_GREEN, NAVY_MID]),
                hole=0.5,
                textinfo="label+value",
            )])
            fig.update_layout(
                height=250,
                title="Goal Completion",
                showlegend=False,
            )
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="app-footer">USAREUR-AF OPERATIONAL DATA TEAM — MSS PROGRESS TRACKER</div>',
    unsafe_allow_html=True,
)
