"""Training Readiness Tracker — Streamlit dashboard.

Professional commander-facing dashboard with RAG heatmap, bottleneck
analysis, training funnel, velocity tracking, and individual lookup.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure parent package is importable when Streamlit runs this file directly
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

from readiness_tracker.db import (
    ALL_COURSES,
    COURSE_CATALOG,
    COURSE_TIERS,
    PREREQ_CHAIN,
    SessionLocal,
    get_bottleneck_analysis,
    get_funnel_data,
    get_rag_heatmap_data,
    get_training_velocity,
    get_unit_rollup,
    get_unit_summary,
    init_db,
    Trainee,
    Completion,
)

from theme import inject_branding, apply_plotly_theme, NAVY, NAVY_DARK, NAVY_LIGHT, NAVY_MID, GOLD, GOLD_DARK, GOLD_LIGHT, RAG_GREEN, RAG_AMBER, RAG_RED, RAG_COLORSCALE, GRAY_400, GRAY_700, WARNING_RED, CAUTION_AMBER

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
API_BASE = "http://localhost:8001"

st.set_page_config(
    page_title="MSS Training Readiness",
    page_icon="\U0001F3AF",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_branding("MSS Training Readiness")

# Military-style color scheme (mapped to USAREUR-AF brand)
COLORS = {
    "GREEN": RAG_GREEN,
    "AMBER": RAG_AMBER,
    "RED": RAG_RED,
    "DARK_BG": NAVY_DARK,
    "HEADER": NAVY,
    "ACCENT": NAVY_MID,
}


# ---------------------------------------------------------------------------
# Direct DB access for dashboard (avoids API round-trips for analytics)
# ---------------------------------------------------------------------------
init_db()  # Ensure tables exist before any query


@st.cache_data(ttl=30)
def load_rag_data():
    db = SessionLocal()
    try:
        return get_rag_heatmap_data(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_bottleneck():
    db = SessionLocal()
    try:
        return get_bottleneck_analysis(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_velocity():
    db = SessionLocal()
    try:
        return get_training_velocity(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_funnel():
    db = SessionLocal()
    try:
        return get_funnel_data(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_unit_summary():
    db = SessionLocal()
    try:
        return get_unit_summary(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_rollups():
    db = SessionLocal()
    try:
        return get_unit_rollup(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_trainees():
    db = SessionLocal()
    try:
        trainees = db.query(Trainee).order_by(Trainee.last_name).all()
        result = []
        for t in trainees:
            go_count = len([c for c in t.completions if c.result == "GO"])
            nogo_count = len([c for c in t.completions if c.result == "NO_GO"])
            go_courses = sorted([c.course_id for c in t.completions if c.result == "GO"])
            # Determine furthest course
            furthest = go_courses[-1] if go_courses else "None"
            result.append({
                "dodid": t.dodid,
                "rank": t.rank,
                "last_name": t.last_name,
                "first_name": t.first_name,
                "unit": t.unit,
                "mos": t.mos or "",
                "go_count": go_count,
                "nogo_count": nogo_count,
                "furthest": furthest,
                "courses": go_courses,
            })
        return result
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_trainee_detail(dodid: str):
    db = SessionLocal()
    try:
        t = db.query(Trainee).filter(Trainee.dodid == dodid).first()
        if not t:
            return None
        completions = []
        for c in t.completions:
            completions.append({
                "course_id": c.course_id,
                "course_name": COURSE_CATALOG.get(c.course_id, ("", 0))[0],
                "result": c.result,
                "evaluation_date": c.evaluation_date.isoformat() if c.evaluation_date else "",
                "evaluator_name": c.evaluator_name or "",
            })
        # Eligible courses
        go_set = {c.course_id for c in t.completions if c.result == "GO"}
        eligible = []
        for course_id, prereqs in PREREQ_CHAIN.items():
            if course_id not in go_set and all(p in go_set for p in prereqs):
                eligible.append(course_id)

        return {
            "dodid": t.dodid,
            "rank": t.rank,
            "last_name": t.last_name,
            "first_name": t.first_name,
            "unit": t.unit,
            "mos": t.mos or "",
            "completions": completions,
            "eligible": eligible,
            "go_courses": sorted(go_set),
        }
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Display order for courses (excludes BSP for heatmap)
# ---------------------------------------------------------------------------
DISPLAY_ORDER = [
    "TM-10", "TM-20", "TM-30",
    "TM-40A", "TM-40B", "TM-40C", "TM-40D", "TM-40E", "TM-40F",
    "TM-40G", "TM-40H", "TM-40M", "TM-40J", "TM-40K", "TM-40L",
    "TM-50G", "TM-50H", "TM-50M", "TM-50J", "TM-50K", "TM-50L",
]

FOUNDATION_COURSES = ["TM-10", "TM-20", "TM-30"]

# Track view options — Foundation is always the default
TRACK_OPTIONS = {
    "Foundation (TM-10/20/30)": FOUNDATION_COURSES,
    "All Courses": DISPLAY_ORDER,
}


def track_selector(key: str = "track_view") -> list[str]:
    """Render a track view selector and return the filtered course list."""
    selected = st.radio(
        "Track View",
        list(TRACK_OPTIONS.keys()),
        index=0,
        horizontal=True,
        key=key,
    )
    return TRACK_OPTIONS[selected]


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
st.sidebar.title("MSS Training Readiness")
st.sidebar.caption("USAREUR-AF Operational Data Team")
st.sidebar.markdown("---")

tab_names = [
    "Commander's Dashboard",
    "RAG Heatmap",
    "Bottleneck Analysis",
    "Unit Drill-Down",
    "Individual Trainee",
    "CSV Upload",
    "Export",
]
active_tab = st.sidebar.radio("Navigate", tab_names)


# =============================================================================
# TAB: Commander's Dashboard
# =============================================================================
if active_tab == "Commander's Dashboard":
    st.title("Commander's Training Readiness Dashboard")

    # Track view selector — Foundation by default
    active_courses = track_selector(key="cmd_track")

    # --- KPI Row ---
    trainees = load_trainees()
    unit_summary = load_unit_summary()
    funnel = load_funnel()
    velocity = load_velocity()

    if not trainees:
        st.info("No trainees loaded. Seed the database or upload a roster.")
        st.stop()

    total = len(trainees)
    units = len(unit_summary)
    # Count only courses within the active view
    avg_courses = sum(
        sum(1 for c in t["courses"] if c in active_courses)
        for t in trainees
    ) / total if total else 0
    # Highest foundation milestone
    tm10_count = sum(1 for t in trainees if "TM-10" in t["courses"])
    tm20_count = sum(1 for t in trainees if "TM-20" in t["courses"])
    tm30_count = sum(1 for t in trainees if "TM-30" in t["courses"])

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Total Trainees", total)
    c2.metric("Units", units)
    c3.metric("TM-10 Complete", tm10_count, delta=f"{tm10_count/total*100:.0f}%")
    c4.metric("TM-20 Complete", tm20_count, delta=f"{tm20_count/total*100:.0f}%")
    c5.metric("TM-30 Complete", tm30_count, delta=f"{tm30_count/total*100:.0f}%")

    st.markdown("---")

    # --- Training Funnel ---
    col_left, col_right = st.columns([3, 2])

    with col_left:
        st.subheader("Training Progression Funnel")
        if funnel and HAS_PLOTLY:
            # Filter funnel stages to active courses
            df_f = pd.DataFrame(funnel)
            funnel_colors = [NAVY_DARK, NAVY, NAVY_MID, NAVY_LIGHT, GOLD]
            fig = go.Figure(go.Funnel(
                y=df_f["stage"],
                x=df_f["count"],
                textinfo="value+percent initial",
                marker=dict(color=funnel_colors[:len(df_f)]),
            ))
            fig.update_layout(height=350, margin=dict(l=10, r=10, t=10, b=10))
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

    with col_right:
        st.subheader("Unit Readiness Summary")
        if unit_summary:
            df_u = pd.DataFrame(unit_summary)
            df_u.columns = ["Unit", "Trainees", "Avg Courses", "Max Courses", "Zero Progress"]
            st.dataframe(df_u, use_container_width=True, hide_index=True)

    st.markdown("---")

    # --- Velocity + Completion Distribution ---
    col_v, col_d = st.columns(2)

    with col_v:
        st.subheader("Training Velocity (Completions/Month)")
        if velocity and HAS_PLOTLY:
            df_vel = pd.DataFrame(velocity)
            fig = px.bar(
                df_vel, x="month", y="completions",
                color="completions",
                color_continuous_scale="Blues",
            )
            fig.update_layout(height=300, showlegend=False,
                              xaxis_title="", yaxis_title="GO Completions")
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

    with col_d:
        st.subheader("Course Completion Distribution")
        rollups = load_rollups()
        if rollups and HAS_PLOTLY:
            all_counts: dict[str, int] = {}
            for r in rollups:
                for cid, cnt in r.get("course_counts", {}).items():
                    all_counts[cid] = all_counts.get(cid, 0) + cnt

            # Only show courses in active view
            ordered = [(c, all_counts.get(c, 0)) for c in active_courses]
            df = pd.DataFrame(ordered, columns=["Course", "GO Count"])

            # Color by tier
            tier_colors = []
            for c in active_courses:
                if c.startswith("TM-1") or c.startswith("TM-2") or c.startswith("TM-3"):
                    tier_colors.append(NAVY_MID)
                elif c.startswith("TM-40") and c[-1] in "ABCDEF":
                    tier_colors.append(RAG_GREEN)
                elif c.startswith("TM-40"):
                    tier_colors.append(RAG_AMBER)
                else:
                    tier_colors.append(WARNING_RED)

            fig = go.Figure(data=[go.Bar(
                x=df["Course"], y=df["GO Count"],
                marker_color=tier_colors,
                text=df["GO Count"], textposition="auto",
            )])
            fig.update_layout(
                height=300, xaxis_tickangle=-45,
                xaxis_title="", yaxis_title="GO Count",
            )
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)


# =============================================================================
# TAB: RAG Heatmap
# =============================================================================
elif active_tab == "RAG Heatmap":
    st.title("Unit Readiness Heatmap (RAG)")
    st.caption("GREEN >= 80% | AMBER >= 50% | RED < 50% of unit with GO result")

    rag_data = load_rag_data()
    if not rag_data:
        st.info("No data available.")
        st.stop()

    # Track view selector — Foundation by default
    filtered_courses = track_selector(key="rag_track")

    # Pivot data for heatmap
    df_rag = pd.DataFrame(rag_data)
    df_rag = df_rag[df_rag["course_id"].isin(filtered_courses)]

    if df_rag.empty:
        st.info("No data for selected tiers.")
        st.stop()

    if HAS_PLOTLY:
        pivot = df_rag.pivot(index="unit", columns="course_id", values="pct")
        # Reorder columns
        ordered_cols = [c for c in filtered_courses if c in pivot.columns]
        pivot = pivot[ordered_cols]

        # Build hover text
        hover_pivot = df_rag.pivot(index="unit", columns="course_id", values="go_count")
        hover_pivot = hover_pivot[ordered_cols]
        total_pivot = df_rag.pivot(index="unit", columns="course_id", values="total")
        total_pivot = total_pivot[ordered_cols]

        hover_text = []
        for i in range(len(pivot)):
            row = []
            for j in range(len(ordered_cols)):
                go_cnt = int(hover_pivot.iloc[i, j])
                tot = int(total_pivot.iloc[i, j])
                pct = pivot.iloc[i, j]
                row.append(f"{ordered_cols[j]}<br>{go_cnt}/{tot} ({pct:.0f}%)")
            hover_text.append(row)

        # Custom colorscale: RED -> AMBER -> GREEN
        colorscale = [
            [0.0, RAG_RED],
            [0.5, RAG_AMBER],
            [0.8, RAG_GREEN],
            [1.0, "#145020"],
        ]

        fig = go.Figure(data=go.Heatmap(
            z=pivot.values,
            x=ordered_cols,
            y=pivot.index.tolist(),
            text=hover_text,
            hoverinfo="text",
            colorscale=colorscale,
            zmin=0, zmax=100,
            colorbar=dict(title="% Complete"),
        ))

        # Add text annotations
        for i in range(len(pivot)):
            for j in range(len(ordered_cols)):
                val = pivot.iloc[i, j]
                fig.add_annotation(
                    x=ordered_cols[j], y=pivot.index[i],
                    text=f"{val:.0f}%",
                    showarrow=False,
                    font=dict(color="white" if val < 60 else "black", size=11),
                )

        fig.update_layout(
            height=max(300, len(pivot) * 60 + 100),
            xaxis_tickangle=-45,
            margin=dict(l=10, r=10, t=10, b=10),
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # Summary table below
    st.subheader("RAG Summary")
    rag_summary = df_rag.groupby("rag").size().reset_index(name="cells")
    cols = st.columns(3)
    for i, rag_val in enumerate(["GREEN", "AMBER", "RED"]):
        cnt = rag_summary[rag_summary["rag"] == rag_val]["cells"].sum() if rag_val in rag_summary["rag"].values else 0
        cols[i].metric(f"{rag_val}", cnt)


# =============================================================================
# TAB: Bottleneck Analysis
# =============================================================================
elif active_tab == "Bottleneck Analysis":
    st.title("Training Pipeline Bottleneck Analysis")
    st.caption("Soldiers who have completed prereqs but haven't completed the next course.")

    # Track view selector — Foundation by default
    active_courses = track_selector(key="bn_track")

    bottleneck = load_bottleneck()
    if not bottleneck:
        st.info("No data available.")
        st.stop()

    # Filter to active track view
    bottleneck = [b for b in bottleneck if b["course_id"] in active_courses]
    df_bn = pd.DataFrame(bottleneck)

    if HAS_PLOTLY:
        # Stacked bar: completed vs eligible-not-done
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name="Completed (GO)",
            x=df_bn["course_id"],
            y=df_bn["completed"],
            marker_color=RAG_GREEN,
            text=df_bn["completed"], textposition="auto",
        ))
        fig.add_trace(go.Bar(
            name="Eligible but Not Done",
            x=df_bn["course_id"],
            y=df_bn["eligible_not_done"],
            marker_color=RAG_AMBER,
            text=df_bn["eligible_not_done"], textposition="auto",
        ))
        fig.update_layout(
            barmode="stack",
            height=450,
            xaxis_tickangle=-45,
            legend=dict(orientation="h", yanchor="bottom", y=1.02),
            xaxis_title="", yaxis_title="Soldiers",
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # Top bottlenecks callout
    st.subheader("Top Bottlenecks")
    top_bn = sorted(bottleneck, key=lambda x: x["eligible_not_done"], reverse=True)[:5]
    for item in top_bn:
        if item["eligible_not_done"] > 0:
            name = COURSE_CATALOG.get(item["course_id"], (item["course_id"], 0))[0]
            st.warning(
                f"**{item['course_id']} ({name})**: "
                f"{item['eligible_not_done']} soldiers eligible but haven't started. "
                f"{item['completed']} completed."
            )


# =============================================================================
# TAB: Unit Drill-Down
# =============================================================================
elif active_tab == "Unit Drill-Down":
    st.title("Unit Drill-Down")

    # Track view selector — Foundation by default
    active_courses = track_selector(key="unit_track")

    unit_summary = load_unit_summary()
    trainees = load_trainees()
    if not unit_summary:
        st.info("No data.")
        st.stop()

    unit_names = [u["unit"] for u in unit_summary]
    selected_unit = st.selectbox("Select Unit", unit_names)

    unit_trainees = [t for t in trainees if t["unit"] == selected_unit]
    unit_info = next((u for u in unit_summary if u["unit"] == selected_unit), None)

    if unit_info:
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Trainees", unit_info["total_trainees"])
        c2.metric("Avg Courses", unit_info["avg_courses"])
        c3.metric("Max Courses", unit_info["max_courses"])
        c4.metric("Zero Progress", unit_info["zero_courses"],
                  delta_color="inverse",
                  delta=f"{unit_info['zero_courses']/unit_info['total_trainees']*100:.0f}%")

    st.markdown("---")

    # RAG for this unit — filtered to active track view
    rag_data = load_rag_data()
    unit_rag = [r for r in rag_data if r["unit"] == selected_unit and r["course_id"] in active_courses]

    if unit_rag and HAS_PLOTLY:
        st.subheader(f"{selected_unit} — Course Readiness")
        df_ur = pd.DataFrame(unit_rag)
        colors = [COLORS.get(r, "#999") for r in df_ur["rag"]]

        fig = go.Figure(data=[go.Bar(
            x=df_ur["course_id"],
            y=df_ur["pct"],
            marker_color=colors,
            text=[f"{p:.0f}%" for p in df_ur["pct"]],
            textposition="auto",
        )])
        fig.update_layout(
            height=350, xaxis_tickangle=-45,
            yaxis_range=[0, 105], yaxis_title="% Complete",
            xaxis_title="",
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # Trainee roster for this unit
    st.subheader(f"{selected_unit} — Personnel")
    if unit_trainees:
        df_t = pd.DataFrame(unit_trainees)
        display_cols = ["rank", "last_name", "first_name", "mos", "go_count", "furthest"]
        st.dataframe(
            df_t[display_cols].rename(columns={
                "rank": "Rank", "last_name": "Last", "first_name": "First",
                "mos": "MOS", "go_count": "GO Count", "furthest": "Furthest Course",
            }),
            use_container_width=True, hide_index=True,
        )


# =============================================================================
# TAB: Individual Trainee
# =============================================================================
elif active_tab == "Individual Trainee":
    st.title("Individual Trainee Lookup")

    # Track view selector — Foundation by default
    active_courses = track_selector(key="indiv_track")

    trainees = load_trainees()

    # Search by name or DODID
    search = st.text_input("Search by name or DODID", placeholder="KELLY or 1000000000")

    if search:
        search_upper = search.strip().upper()
        matches = [
            t for t in trainees
            if search_upper in t["last_name"] or search_upper in t["first_name"]
            or search_upper in t["dodid"]
        ]

        dodid = None
        if not matches:
            st.warning("No matches found.")
        elif len(matches) > 1:
            options = [f"{t['rank']} {t['last_name']}, {t['first_name']} ({t['dodid']})" for t in matches]
            selected = st.selectbox("Multiple matches — select:", options)
            idx = options.index(selected)
            dodid = matches[idx]["dodid"]
        else:
            dodid = matches[0]["dodid"]

        if dodid is not None:
            detail = load_trainee_detail(dodid)
            if detail:
                st.subheader(f"{detail['rank']} {detail['last_name']}, {detail['first_name']}")
                st.caption(f"Unit: {detail['unit']} | MOS: {detail['mos']} | DODID: {detail['dodid']}")

                go_courses = set(detail["go_courses"])

                # Progress bar scoped to active view
                active_go = [c for c in active_courses if c in go_courses]
                progress = len(active_go) / len(active_courses) if active_courses else 0
                st.progress(progress, text=f"{len(active_go)}/{len(active_courses)} courses completed")

                # Visual checkmark grid — separate status for each course
                st.subheader("Training Progress")

                # Render each course as an individual status indicator
                cols_per_row = min(len(active_courses), 6)
                for row_start in range(0, len(active_courses), cols_per_row):
                    row_courses = active_courses[row_start:row_start + cols_per_row]
                    cols = st.columns(cols_per_row)
                    for idx, cid in enumerate(row_courses):
                        with cols[idx]:
                            name = COURSE_CATALOG.get(cid, (cid, 0))[0]
                            if cid in go_courses:
                                # Complete — green checkmark
                                st.markdown(f"""
                                <div style="text-align:center; padding:8px; border:2px solid {RAG_GREEN};
                                            border-radius:6px; background:rgba(26,92,40,0.08); margin-bottom:4px;">
                                    <div style="font-size:24px;">\u2705</div>
                                    <div style="font-size:11px; font-weight:bold; color:{NAVY};">{cid}</div>
                                    <div style="font-size:9px; color:{GRAY_400};">{name}</div>
                                    <div style="font-size:9px; font-weight:bold; color:{RAG_GREEN};">GO</div>
                                </div>
                                """, unsafe_allow_html=True)
                            elif cid in detail["eligible"]:
                                # Eligible — amber indicator
                                st.markdown(f"""
                                <div style="text-align:center; padding:8px; border:2px solid {RAG_AMBER};
                                            border-radius:6px; background:rgba(184,104,16,0.08); margin-bottom:4px;">
                                    <div style="font-size:24px;">\U0001F7E1</div>
                                    <div style="font-size:11px; font-weight:bold; color:{NAVY};">{cid}</div>
                                    <div style="font-size:9px; color:{GRAY_400};">{name}</div>
                                    <div style="font-size:9px; font-weight:bold; color:{RAG_AMBER};">ELIGIBLE</div>
                                </div>
                                """, unsafe_allow_html=True)
                            else:
                                # Locked — gray
                                st.markdown(f"""
                                <div style="text-align:center; padding:8px; border:2px solid {GRAY_400};
                                            border-radius:6px; background:rgba(122,136,168,0.06); margin-bottom:4px;">
                                    <div style="font-size:24px;">\U0001F512</div>
                                    <div style="font-size:11px; font-weight:bold; color:{GRAY_400};">{cid}</div>
                                    <div style="font-size:9px; color:{GRAY_400};">{name}</div>
                                    <div style="font-size:9px; color:{GRAY_400};">LOCKED</div>
                                </div>
                                """, unsafe_allow_html=True)

                st.markdown(
                    "\u2705 **GO** &nbsp;&nbsp; \U0001F7E1 **ELIGIBLE** &nbsp;&nbsp; "
                    "\U0001F512 **LOCKED** (prereqs not met)"
                )

                # Completion details table
                if detail["completions"]:
                    st.subheader("Completion History")
                    # Filter to active view
                    filtered_comps = [c for c in detail["completions"] if c["course_id"] in active_courses]
                    if filtered_comps:
                        df_c = pd.DataFrame(filtered_comps)
                        st.dataframe(
                            df_c.rename(columns={
                                "course_id": "Course", "course_name": "Name",
                                "result": "Result", "evaluation_date": "Date",
                                "evaluator_name": "Evaluator",
                            }),
                            use_container_width=True, hide_index=True,
                        )

                # Next recommended — scoped to active view
                eligible_in_view = [c for c in detail["eligible"] if c in active_courses]
                if eligible_in_view:
                    st.subheader("Next Recommended Courses")
                    for cid in eligible_in_view:
                        name = COURSE_CATALOG.get(cid, (cid, 0))[0]
                        hours = COURSE_CATALOG.get(cid, (cid, 0))[1]
                        st.markdown(f"- **{cid}** — {name} ({hours} hrs)")


# =============================================================================
# TAB: CSV Upload
# =============================================================================
elif active_tab == "CSV Upload":
    st.title("CSV Upload")

    def api_post(endpoint, files=None):
        try:
            resp = requests.post(f"{API_BASE}{endpoint}", files=files, timeout=30)
            return resp
        except requests.ConnectionError:
            st.error(f"Cannot reach API at {API_BASE}.")
            return None

    st.subheader("Upload Roster")
    st.caption("Columns: dodid, last_name, first_name, rank, unit, mos")
    roster_file = st.file_uploader("Roster CSV", type=["csv"], key="roster")
    if roster_file:
        if st.button("Upload Roster", key="btn_roster"):
            resp = api_post("/upload/roster",
                            files={"file": ("roster.csv", roster_file.getvalue(), "text/csv")})
            if resp and resp.status_code == 200:
                result = resp.json()
                st.success(f"Accepted: {result['accepted']} | Rejected: {result['rejected']}")
                if result.get("errors"):
                    with st.expander("Errors"):
                        for e in result["errors"]:
                            st.text(e)
                st.cache_data.clear()
            elif resp:
                st.error(f"Upload failed: {resp.text}")

    st.markdown("---")

    st.subheader("Upload Completions")
    st.caption("Columns: dodid, course_id, result, evaluation_date, evaluator_name")
    comp_file = st.file_uploader("Completions CSV", type=["csv"], key="comps")
    if comp_file:
        if st.button("Upload Completions", key="btn_comps"):
            resp = api_post("/upload/completions",
                            files={"file": ("completions.csv", comp_file.getvalue(), "text/csv")})
            if resp and resp.status_code == 200:
                result = resp.json()
                st.success(f"Accepted: {result['accepted']} | Rejected: {result['rejected']}")
                if result.get("errors"):
                    with st.expander("Errors"):
                        for e in result["errors"]:
                            st.text(e)
                st.cache_data.clear()
            elif resp:
                st.error(f"Upload failed: {resp.text}")


# =============================================================================
# TAB: Export
# =============================================================================
elif active_tab == "Export":
    st.title("Export Data")

    st.subheader("Download Completions CSV")
    unit_filter = st.text_input("Filter by unit (leave blank for all)", key="export_unit")

    if st.button("Generate CSV"):
        params = {}
        if unit_filter.strip():
            params["unit"] = unit_filter.strip().upper()
        try:
            resp = requests.get(f"{API_BASE}/export/csv", params=params, timeout=10)
            if resp.status_code == 200:
                st.download_button(
                    label="Download CSV",
                    data=resp.content,
                    file_name="readiness_export.csv",
                    mime="text/csv",
                )
            else:
                st.error(f"Export failed: {resp.text}")
        except requests.ConnectionError:
            st.error("Cannot reach API server.")

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="app-footer">USAREUR-AF OPERATIONAL DATA TEAM — MSS TRAINING READINESS</div>',
    unsafe_allow_html=True,
)
