"""Lessons Learned Pipeline — Streamlit dashboard.

Six-tab dashboard for structured lessons-learned analysis with full
tagging taxonomy, cross-reference matrix, and action item tracking.
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

from lessons_learned.db import (
    TAG_TYPES,
    TTP_CATEGORIES,
    ECHELONS,
    WFF_CATEGORIES,
    PRIORITIES,
    SOURCE_TYPES,
    STATUSES,
    ActionItem,
    Lesson,
    LessonTag,
    SessionLocal,
    get_action_item_status,
    get_cross_reference,
    get_lessons_by_tag,
    get_pipeline_stats,
    get_tag_frequency,
    get_trend_analysis,
    init_db,
)

from theme import (
    inject_branding,
    apply_plotly_theme,
    NAVY,
    NAVY_DARK,
    NAVY_LIGHT,
    NAVY_MID,
    NAVY_COLORSCALE,
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
    PLOTLY_MIXED_SEQ,
    PLOTLY_STATUS,
)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
API_BASE = os.environ.get("LESSONS_LEARNED_API_URL", "http://localhost:8014")

st.set_page_config(
    page_title="MSS Lessons Learned",
    page_icon="\U0001F4DD",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_branding("MSS Lessons Learned Pipeline")

# ---------------------------------------------------------------------------
# Direct DB access for dashboard (avoids API round-trips for analytics)
# ---------------------------------------------------------------------------
init_db()


# ---------------------------------------------------------------------------
# Cached data loaders
# ---------------------------------------------------------------------------
@st.cache_data(ttl=30)
def load_pipeline_stats():
    db = SessionLocal()
    try:
        return get_pipeline_stats(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_tag_frequency(tag_type: str):
    db = SessionLocal()
    try:
        return get_tag_frequency(tag_type, db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_cross_reference(type_a: str, type_b: str):
    db = SessionLocal()
    try:
        return get_cross_reference(type_a, type_b, db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_trend_analysis():
    db = SessionLocal()
    try:
        return get_trend_analysis(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_action_items():
    db = SessionLocal()
    try:
        items = (
            db.query(ActionItem)
            .order_by(ActionItem.due_date)
            .all()
        )
        result = []
        for a in items:
            lesson = a.lesson
            result.append({
                "id": a.id,
                "lesson_id": a.lesson_id,
                "lesson_title": lesson.title if lesson else "",
                "description": a.description,
                "assigned_to": a.assigned_to or "Unassigned",
                "due_date": a.due_date.isoformat() if a.due_date else "",
                "status": a.status,
                "completed_date": a.completed_date.isoformat() if a.completed_date else "",
                "overdue": (
                    a.due_date is not None
                    and a.due_date < date.today()
                    and a.status in ("OPEN", "IN_PROGRESS")
                ),
            })
        return result
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_all_lessons():
    db = SessionLocal()
    try:
        lessons = db.query(Lesson).order_by(Lesson.submit_date.desc()).all()
        result = []
        for l in lessons:
            tags_by_type = {}
            for t in l.tags:
                tags_by_type.setdefault(t.tag_type, []).append(t.tag_value)
            result.append({
                "id": l.id,
                "title": l.title,
                "description": l.description,
                "source_type": l.source_type,
                "source_reference": l.source_reference or "",
                "submitted_by": l.submitted_by,
                "submit_date": l.submit_date.isoformat(),
                "status": l.status,
                "priority": l.priority,
                "ttp_category": ", ".join(tags_by_type.get("TTP_CATEGORY", [])),
                "wff": ", ".join(tags_by_type.get("WFF", [])),
                "echelon": ", ".join(tags_by_type.get("ECHELON", [])),
                "doctrine_ref": ", ".join(tags_by_type.get("DOCTRINE_REF", [])),
                "course_id": ", ".join(tags_by_type.get("COURSE_ID", [])),
                "action_count": len(l.action_items),
                "comment_count": len(l.comments),
            })
        return result
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_lessons_by_tag(tag_type: str, tag_value: str):
    db = SessionLocal()
    try:
        lessons = get_lessons_by_tag(tag_type, tag_value, db)
        return [
            {
                "id": l.id,
                "title": l.title,
                "status": l.status,
                "priority": l.priority,
                "submit_date": l.submit_date.isoformat(),
                "source_type": l.source_type,
            }
            for l in lessons
        ]
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Status color mapping
# ---------------------------------------------------------------------------
STATUS_COLORS = {
    "NEW": NAVY_MID,
    "VALIDATED": GOLD,
    "ACTIONABLE": RAG_AMBER,
    "IMPLEMENTED": RAG_GREEN,
    "ARCHIVED": GRAY_400,
}

PRIORITY_COLORS = {
    "HIGH": WARNING_RED,
    "MEDIUM": RAG_AMBER,
    "LOW": RAG_GREEN,
}


# ---------------------------------------------------------------------------
# Sidebar navigation
# ---------------------------------------------------------------------------
st.sidebar.title("Lessons Learned Pipeline")
st.sidebar.caption("USAREUR-AF Operational Data Team")
st.sidebar.markdown("---")

tab_names = [
    "Pipeline Overview",
    "Tag Analysis",
    "Cross-Reference Matrix",
    "Action Tracker",
    "Lesson Browser",
    "Trend Analysis",
]
active_tab = st.sidebar.radio("Navigate", tab_names)


# =============================================================================
# TAB: Pipeline Overview
# =============================================================================
if active_tab == "Pipeline Overview":
    st.title("Lessons Learned Pipeline Overview")

    with st.spinner("Loading data..."):
        stats = load_pipeline_stats()
        actions = load_action_items()
        all_lessons = load_all_lessons()

    if not all_lessons:
        st.info("No lessons loaded. Seed the database to get started.")
        st.stop()

    # --- KPI Row ---
    total = stats["total_lessons"]
    open_actions = sum(1 for a in actions if a["status"] in ("OPEN", "IN_PROGRESS"))
    # Lessons this month
    this_month = date.today().strftime("%Y-%m")
    lessons_this_month = sum(1 for l in all_lessons if l["submit_date"].startswith(this_month))
    # Top TTP category
    ttp_freq = load_tag_frequency("TTP_CATEGORY")
    top_ttp = ttp_freq[0]["tag_value"] if ttp_freq else "N/A"

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Lessons", total)
    c2.metric("Open Action Items", open_actions)
    c3.metric("Lessons This Month", lessons_this_month)
    c4.metric("Top TTP Category", top_ttp)

    st.markdown("---")

    # --- Status Funnel ---
    col_left, col_right = st.columns([3, 2])

    with col_left:
        st.subheader("Status Pipeline Funnel")
        if HAS_PLOTLY:
            # Order: NEW -> VALIDATED -> ACTIONABLE -> IMPLEMENTED -> ARCHIVED
            funnel_order = ["NEW", "VALIDATED", "ACTIONABLE", "IMPLEMENTED", "ARCHIVED"]
            funnel_counts = [stats["by_status"].get(s, 0) for s in funnel_order]
            funnel_colors = [NAVY_DARK, NAVY, NAVY_MID, RAG_GREEN, GRAY_400]

            fig = go.Figure(go.Funnel(
                y=funnel_order,
                x=funnel_counts,
                textinfo="value+percent initial",
                marker=dict(color=funnel_colors),
            ))
            fig.update_layout(height=350, margin=dict(l=10, r=10, t=10, b=10))
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

    with col_right:
        st.subheader("By Priority")
        if HAS_PLOTLY:
            priorities = ["HIGH", "MEDIUM", "LOW"]
            pri_counts = [stats["by_priority"].get(p, 0) for p in priorities]
            colors = [PRIORITY_COLORS[p] for p in priorities]

            fig = go.Figure(data=[go.Bar(
                x=priorities,
                y=pri_counts,
                marker_color=colors,
                text=pri_counts,
                textposition="auto",
            )])
            fig.update_layout(height=350, xaxis_title="", yaxis_title="Count")
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # --- Source type breakdown ---
    st.subheader("Lessons by Source Type")
    if stats["by_source_type"] and HAS_PLOTLY:
        src_df = pd.DataFrame([
            {"Source Type": k, "Count": v}
            for k, v in sorted(stats["by_source_type"].items(), key=lambda x: -x[1])
        ])
        fig = px.bar(
            src_df, x="Source Type", y="Count",
            color="Count", color_continuous_scale="Blues",
        )
        fig.update_layout(height=300, showlegend=False)
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)


# =============================================================================
# TAB: Tag Analysis
# =============================================================================
elif active_tab == "Tag Analysis":
    st.title("Tag Frequency Analysis")

    # Tag type selector
    tag_type_display = {
        "TTP_CATEGORY": "TTP Category",
        "WFF": "Warfighting Function",
        "ECHELON": "Echelon",
        "DOCTRINE_REF": "Doctrine Reference",
        "COURSE_ID": "Course ID",
        "KEYWORD": "Keyword",
    }
    selected_type = st.selectbox(
        "Select Tag Type",
        list(tag_type_display.keys()),
        format_func=lambda x: tag_type_display[x],
    )

    freq = load_tag_frequency(selected_type)
    if not freq:
        st.info(f"No tags found for type: {tag_type_display[selected_type]}")
        st.stop()

    # Frequency bar chart
    if HAS_PLOTLY:
        df_freq = pd.DataFrame(freq)
        fig = go.Figure(data=[go.Bar(
            x=df_freq["tag_value"],
            y=df_freq["count"],
            marker_color=NAVY_MID,
            text=df_freq["count"],
            textposition="auto",
        )])
        fig.update_layout(
            height=400,
            xaxis_tickangle=-45,
            xaxis_title=tag_type_display[selected_type],
            yaxis_title="Lesson Count",
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # Drill-down: select a tag value to see associated lessons
    st.markdown("---")
    st.subheader("Drill Down by Tag Value")
    tag_values = [f["tag_value"] for f in freq]
    selected_value = st.selectbox("Select Value", tag_values)

    if selected_value:
        drill_lessons = load_lessons_by_tag(selected_type, selected_value)
        if drill_lessons:
            df_drill = pd.DataFrame(drill_lessons)
            st.dataframe(
                df_drill.rename(columns={
                    "id": "ID", "title": "Title", "status": "Status",
                    "priority": "Priority", "submit_date": "Date",
                    "source_type": "Source",
                }),
                use_container_width=True,
                hide_index=True,
            )
        else:
            st.info("No lessons found for this tag value.")


# =============================================================================
# TAB: Cross-Reference Matrix
# =============================================================================
elif active_tab == "Cross-Reference Matrix":
    st.title("Tag Cross-Reference Heatmap")
    st.caption("Co-occurrence analysis between two tag types across all lessons.")

    col_a, col_b = st.columns(2)
    tag_type_display = {
        "TTP_CATEGORY": "TTP Category",
        "WFF": "Warfighting Function",
        "ECHELON": "Echelon",
        "DOCTRINE_REF": "Doctrine Reference",
        "COURSE_ID": "Course ID",
    }

    with col_a:
        type_a = st.selectbox(
            "Row Axis (Tag Type A)",
            list(tag_type_display.keys()),
            index=1,  # Default: WFF
            format_func=lambda x: tag_type_display[x],
        )
    with col_b:
        type_b = st.selectbox(
            "Column Axis (Tag Type B)",
            list(tag_type_display.keys()),
            index=0,  # Default: TTP_CATEGORY
            format_func=lambda x: tag_type_display[x],
        )

    if type_a == type_b:
        st.warning("Select two different tag types for cross-reference analysis.")
        st.stop()

    xref = load_cross_reference(type_a, type_b)
    if not xref:
        st.info("No co-occurring tags found for this combination.")
        st.stop()

    if HAS_PLOTLY:
        df_xref = pd.DataFrame(xref)

        # Pivot for heatmap
        pivot = df_xref.pivot(index="tag_a", columns="tag_b", values="count").fillna(0)

        fig = go.Figure(data=go.Heatmap(
            z=pivot.values,
            x=pivot.columns.tolist(),
            y=pivot.index.tolist(),
            colorscale=NAVY_COLORSCALE,
            colorbar=dict(title="Co-occurrences"),
        ))

        # Add text annotations
        for i in range(len(pivot)):
            for j in range(len(pivot.columns)):
                val = int(pivot.iloc[i, j])
                if val > 0:
                    fig.add_annotation(
                        x=pivot.columns[j], y=pivot.index[i],
                        text=str(val),
                        showarrow=False,
                        font=dict(color="white" if val > 2 else NAVY, size=12),
                    )

        fig.update_layout(
            height=max(350, len(pivot) * 50 + 100),
            xaxis_tickangle=-45,
            margin=dict(l=10, r=10, t=10, b=10),
            xaxis_title=tag_type_display[type_b],
            yaxis_title=tag_type_display[type_a],
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)


# =============================================================================
# TAB: Action Tracker
# =============================================================================
elif active_tab == "Action Tracker":
    st.title("Action Item Tracker")

    actions = load_action_items()
    if not actions:
        st.info("No action items found.")
        st.stop()

    # --- KPIs ---
    total_actions = len(actions)
    open_count = sum(1 for a in actions if a["status"] == "OPEN")
    in_progress = sum(1 for a in actions if a["status"] == "IN_PROGRESS")
    completed = sum(1 for a in actions if a["status"] == "COMPLETED")
    overdue = sum(1 for a in actions if a["overdue"])

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Total Actions", total_actions)
    c2.metric("Open", open_count)
    c3.metric("In Progress", in_progress)
    c4.metric("Completed", completed)
    c5.metric("Overdue", overdue, delta_color="inverse",
              delta=f"{overdue/total_actions*100:.0f}%" if total_actions else "0%")

    st.markdown("---")

    # Filter options
    status_filter = st.multiselect(
        "Filter by Status",
        ["OPEN", "IN_PROGRESS", "COMPLETED", "CANCELLED"],
        default=["OPEN", "IN_PROGRESS"],
    )

    filtered = [a for a in actions if a["status"] in status_filter]

    if filtered:
        df_actions = pd.DataFrame(filtered)

        # Apply RAG color formatting for overdue status
        def _rag_style(row):
            """Return background color based on overdue status."""
            if row.get("overdue"):
                return [f"background-color: rgba(138,26,26,0.15)"] * len(row)
            elif row.get("status") == "IN_PROGRESS":
                return [f"background-color: rgba(184,104,16,0.10)"] * len(row)
            return [""] * len(row)

        display_cols = [
            "id", "lesson_title", "description", "assigned_to",
            "due_date", "status", "overdue",
        ]
        df_display = df_actions[display_cols].rename(columns={
            "id": "ID", "lesson_title": "Lesson", "description": "Action",
            "assigned_to": "Assigned To", "due_date": "Due Date",
            "status": "Status", "overdue": "Overdue",
        })

        st.dataframe(
            df_display.style.apply(_rag_style, axis=1),
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No action items match the selected filters.")


# =============================================================================
# TAB: Lesson Browser
# =============================================================================
elif active_tab == "Lesson Browser":
    st.title("Lesson Browser")

    all_lessons = load_all_lessons()
    if not all_lessons:
        st.info("No lessons found.")
        st.stop()

    # --- Filters ---
    col_f1, col_f2, col_f3 = st.columns(3)

    with col_f1:
        filter_status = st.multiselect("Status", STATUSES, default=STATUSES)
    with col_f2:
        filter_priority = st.multiselect("Priority", PRIORITIES, default=PRIORITIES)
    with col_f3:
        filter_source = st.multiselect("Source Type", SOURCE_TYPES, default=SOURCE_TYPES)

    # Text search
    search_text = st.text_input("Search titles and descriptions", placeholder="e.g., pipeline, visualization")

    # Apply filters
    filtered = all_lessons
    filtered = [l for l in filtered if l["status"] in filter_status]
    filtered = [l for l in filtered if l["priority"] in filter_priority]
    filtered = [l for l in filtered if l["source_type"] in filter_source]

    if search_text:
        search_lower = search_text.strip().lower()
        filtered = [
            l for l in filtered
            if search_lower in l["title"].lower() or search_lower in l["description"].lower()
        ]

    st.caption(f"Showing {len(filtered)} of {len(all_lessons)} lessons")

    if filtered:
        df = pd.DataFrame(filtered)
        display_cols = [
            "id", "title", "status", "priority", "source_type",
            "submit_date", "submitted_by", "ttp_category", "wff",
        ]
        df_display = df[display_cols].rename(columns={
            "id": "ID", "title": "Title", "status": "Status",
            "priority": "Priority", "source_type": "Source",
            "submit_date": "Date", "submitted_by": "Submitted By",
            "ttp_category": "TTP Category", "wff": "WFF",
        })
        st.dataframe(df_display, use_container_width=True, hide_index=True)

        # Detail expander for selected lesson
        lesson_ids = [l["id"] for l in filtered]
        selected_id = st.selectbox("Select Lesson ID for Detail", lesson_ids)
        if selected_id:
            lesson_detail = next((l for l in filtered if l["id"] == selected_id), None)
            if lesson_detail:
                with st.expander(f"Lesson #{selected_id}: {lesson_detail['title']}", expanded=True):
                    st.markdown(f"**Description:** {lesson_detail['description']}")
                    st.markdown(f"**Source:** {lesson_detail['source_type']} ({lesson_detail['source_reference']})")
                    st.markdown(f"**Status:** {lesson_detail['status']} | **Priority:** {lesson_detail['priority']}")
                    st.markdown(f"**Submitted:** {lesson_detail['submit_date']} by {lesson_detail['submitted_by']}")

                    # Tag summary
                    tag_parts = []
                    for tag_key in ["ttp_category", "wff", "echelon", "doctrine_ref", "course_id"]:
                        if lesson_detail[tag_key]:
                            tag_parts.append(f"**{tag_key.replace('_', ' ').title()}:** {lesson_detail[tag_key]}")
                    if tag_parts:
                        st.markdown(" | ".join(tag_parts))

                    st.markdown(f"Actions: {lesson_detail['action_count']} | Comments: {lesson_detail['comment_count']}")


# =============================================================================
# TAB: Trend Analysis
# =============================================================================
elif active_tab == "Trend Analysis":
    st.title("Submission Trend Analysis")
    st.caption("Lessons submitted per month, broken down by source type.")

    trend = load_trend_analysis()
    if not trend:
        st.info("No trend data available.")
        st.stop()

    if HAS_PLOTLY:
        df_trend = pd.DataFrame(trend)

        # Stacked bar by source type per month
        source_types = df_trend["source_type"].unique().tolist()
        months = sorted(df_trend["month"].unique().tolist())

        fig = go.Figure()
        colors = PLOTLY_MIXED_SEQ[:len(source_types)]

        for i, src in enumerate(source_types):
            src_data = df_trend[df_trend["source_type"] == src]
            # Ensure all months are represented
            month_counts = {row["month"]: row["count"] for _, row in src_data.iterrows()}
            counts = [month_counts.get(m, 0) for m in months]

            fig.add_trace(go.Bar(
                name=src,
                x=months,
                y=counts,
                marker_color=colors[i % len(colors)],
                text=counts,
                textposition="auto",
            ))

        fig.update_layout(
            barmode="stack",
            height=450,
            xaxis_title="Month",
            yaxis_title="Lessons Submitted",
            legend=dict(orientation="h", yanchor="bottom", y=1.02),
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # Monthly totals summary table
    st.markdown("---")
    st.subheader("Monthly Totals")
    if trend:
        df_trend = pd.DataFrame(trend)
        monthly = df_trend.groupby("month")["count"].sum().reset_index()
        monthly.columns = ["Month", "Total Lessons"]
        st.dataframe(monthly, use_container_width=True, hide_index=True)

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="app-footer">USAREUR-AF OPERATIONAL DATA TEAM — MSS LESSONS LEARNED</div>',
    unsafe_allow_html=True,
)
