"""Training Metrics Executive Dashboard — Streamlit dashboard.

Senior-leader / CG briefing view: clean, sparse, decision-focused.
Aggregates data from all MSS Training apps into a single executive view.
Answers four questions: On Track? At Risk? What Changed? Decision Required?
"""

from __future__ import annotations

import json
import sys
from datetime import date, datetime
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

from training_metrics.db import (
    SessionLocal,
    collect_all_metrics,
    get_snapshot_history,
    init_db,
    save_snapshot,
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
    WHITE,
    GRAY_100,
)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
API_BASE = "http://localhost:8015"

st.set_page_config(
    page_title="MSS Training Executive Dashboard",
    page_icon="\u2B50",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_branding("MSS Training Executive Dashboard")

# RAG color map
RAG_COLORS = {
    "GREEN": RAG_GREEN,
    "AMBER": RAG_AMBER,
    "RED": RAG_RED,
}

# ---------------------------------------------------------------------------
# Initialize DB
# ---------------------------------------------------------------------------
init_db()

# ---------------------------------------------------------------------------
# Cached data loaders
# ---------------------------------------------------------------------------

@st.cache_data(ttl=30)
def load_metrics() -> dict:
    """Collect live metrics from all app DBs."""
    return collect_all_metrics()


@st.cache_data(ttl=30)
def load_snapshots() -> list[dict]:
    """Load snapshot history from local DB."""
    db = SessionLocal()
    try:
        snapshots = get_snapshot_history(db)
        result = []
        for s in snapshots:
            result.append({
                "id": s.id,
                "report_date": s.report_date.isoformat(),
                "report_type": s.report_type,
                "generated_by": s.generated_by,
                "notes": s.notes or "",
                "data": json.loads(s.data_json) if s.data_json else {},
            })
        return result
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Sidebar navigation
# ---------------------------------------------------------------------------
st.sidebar.title("Executive Dashboard")
st.sidebar.caption("USAREUR-AF Operational Data Team")
st.sidebar.markdown("---")

tab_names = [
    "Executive Summary",
    "Readiness Scorecard",
    "Risk Register",
    "Trend Analysis",
    "Report Generation",
]
active_tab = st.sidebar.radio("Navigate", tab_names)


# =============================================================================
# HELPER: RAG-colored card
# =============================================================================
def rag_card(title: str, content: str, rag: str = "GREEN"):
    """Render a RAG-colored answer card."""
    color = RAG_COLORS.get(rag, GRAY_400)
    bg_alpha = "0.06"
    st.markdown(f"""
    <div style="border-left: 5px solid {color}; padding: 12px 16px;
                background: rgba({_hex_to_rgb(color)}, {bg_alpha});
                border-radius: 0 4px 4px 0; margin-bottom: 12px;">
        <div style="font-size: 11px; font-weight: bold; text-transform: uppercase;
                    letter-spacing: 1.5px; color: {color}; margin-bottom: 4px;">
            {title}
        </div>
        <div style="font-size: 13px; color: {GRAY_700}; line-height: 1.5;">
            {content}
        </div>
    </div>
    """, unsafe_allow_html=True)


def _hex_to_rgb(hex_color: str) -> str:
    """Convert #RRGGBB to 'R, G, B' string for rgba()."""
    h = hex_color.lstrip("#")
    return f"{int(h[0:2], 16)}, {int(h[2:4], 16)}, {int(h[4:6], 16)}"


# =============================================================================
# TAB: Executive Summary
# =============================================================================
if active_tab == "Executive Summary":
    st.title("Executive Summary")

    metrics = load_metrics()
    summary = metrics.get("executive_summary", {})
    rag = summary.get("rag", "AMBER")
    score = summary.get("readiness_score", 0)

    # Top banner — overall readiness score
    banner_color = RAG_COLORS.get(rag, GRAY_400)
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {NAVY_DARK}, {NAVY});
                padding: 20px 28px; border-radius: 6px; margin-bottom: 20px;
                border-bottom: 4px solid {banner_color};">
        <div style="display: flex; align-items: center; justify-content: space-between;">
            <div>
                <div style="font-size: 11px; font-weight: bold; text-transform: uppercase;
                            letter-spacing: 2px; color: {GOLD_LIGHT};">
                    Overall Training Readiness
                </div>
                <div style="font-size: 36px; font-weight: bold; color: {WHITE}; margin-top: 4px;">
                    {score}%
                </div>
            </div>
            <div style="font-size: 14px; font-weight: bold; color: {banner_color};
                        background: rgba({_hex_to_rgb(banner_color)}, 0.15);
                        padding: 8px 20px; border-radius: 4px; letter-spacing: 2px;">
                {rag}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Four answer cards
    col1, col2 = st.columns(2)

    with col1:
        rag_card(
            "1. Are We On Track?",
            summary.get("on_track", "No data available."),
            rag,
        )
        rag_card(
            "3. What Changed?",
            summary.get("what_changed", "No changes reported."),
            "AMBER" if metrics.get("upcoming_events", 0) > 0 else "GREEN",
        )

    with col2:
        # At Risk card — RED if any HIGH risks
        risks = metrics.get("risks", [])
        high_risks = [r for r in risks if r["severity"] == "HIGH"]
        risk_rag = "RED" if high_risks else ("AMBER" if risks else "GREEN")
        rag_card(
            "2. What's At Risk?",
            summary.get("at_risk", "No risks identified."),
            risk_rag,
        )
        # Decision Required — RED if decisions needed
        decision_text = summary.get("decision_required", "No decisions required.")
        decision_rag = "RED" if "required" not in decision_text.lower() or "no" not in decision_text.lower()[:5] else "GREEN"
        rag_card(
            "4. What Do You Need From Me?",
            decision_text,
            decision_rag,
        )

    st.markdown("---")

    # Key metrics row
    st.subheader("Key Metrics")
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    c1.metric("Trainees", metrics.get("total_trainees", 0))
    c2.metric("Pass Rate", f"{metrics.get('exam_pass_rate', 'N/A')}%")
    c3.metric("Scheduled Events", metrics.get("upcoming_events", 0))
    c4.metric("Open Actions", metrics.get("open_action_items", 0))
    c5.metric("Active Alerts", metrics.get("active_alerts", 0))
    c6.metric("Overdue", metrics.get("overdue_milestones", 0))


# =============================================================================
# TAB: Readiness Scorecard
# =============================================================================
elif active_tab == "Readiness Scorecard":
    st.title("Readiness Scorecard")

    metrics = load_metrics()

    # Unit-level RAG table
    st.subheader("Unit Readiness Summary")
    unit_summary = metrics.get("unit_summary", [])

    if unit_summary:
        df_units = pd.DataFrame(unit_summary)
        # Add RAG status based on avg courses vs expected (5 = GREEN, 3 = AMBER, <3 = RED)
        def unit_rag(avg):
            if avg >= 4.0:
                return "GREEN"
            elif avg >= 2.5:
                return "AMBER"
            return "RED"

        df_units["rag"] = df_units["avg_courses"].apply(unit_rag)

        if HAS_PLOTLY:
            colors = [RAG_COLORS.get(r, GRAY_400) for r in df_units["rag"]]
            fig = go.Figure(data=[go.Bar(
                x=df_units["unit"],
                y=df_units["avg_courses"],
                marker_color=colors,
                text=[f"{v:.1f}" for v in df_units["avg_courses"]],
                textposition="auto",
            )])
            fig.update_layout(
                height=350,
                xaxis_title="", yaxis_title="Avg Courses Completed",
                margin=dict(l=10, r=10, t=10, b=10),
            )
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

        # Table view
        display_df = df_units.rename(columns={
            "unit": "Unit", "total_trainees": "Trainees",
            "avg_courses": "Avg Courses", "max_courses": "Max Courses",
            "zero_courses": "Zero Progress", "rag": "Status",
        })
        st.dataframe(display_df, use_container_width=True, hide_index=True)
    else:
        st.info("No unit data available. Seed the Readiness Tracker first.")

    st.markdown("---")

    # Training funnel visualization
    st.subheader("Training Funnel")
    funnel = metrics.get("funnel", [])

    if funnel and HAS_PLOTLY:
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
    elif not funnel:
        st.info("No funnel data available.")

    # Exam pass rate (if available)
    pass_rate = metrics.get("exam_pass_rate")
    sessions = metrics.get("exam_sessions_count", 0)
    if pass_rate is not None:
        st.markdown("---")
        st.subheader("Exam Performance")
        c1, c2 = st.columns(2)
        c1.metric("Overall Pass Rate", f"{pass_rate}%")
        c2.metric("Exam Sessions", sessions)


# =============================================================================
# TAB: Risk Register
# =============================================================================
elif active_tab == "Risk Register":
    st.title("Risk Register")
    st.caption("Auto-generated risks from all MSS Training apps, sorted by severity.")

    metrics = load_metrics()
    risks = metrics.get("risks", [])

    if not risks:
        st.success("No risks identified across all monitored systems.")
    else:
        # Summary counts
        high_count = sum(1 for r in risks if r["severity"] == "HIGH")
        med_count = sum(1 for r in risks if r["severity"] == "MEDIUM")
        low_count = sum(1 for r in risks if r["severity"] == "LOW")

        c1, c2, c3 = st.columns(3)
        c1.metric("HIGH", high_count)
        c2.metric("MEDIUM", med_count)
        c3.metric("LOW", low_count)

        st.markdown("---")

        # Render each risk as a styled card
        for i, risk in enumerate(risks, 1):
            severity = risk["severity"]
            color = RAG_COLORS.get(
                {"HIGH": "RED", "MEDIUM": "AMBER", "LOW": "GREEN"}[severity],
                GRAY_400,
            )
            st.markdown(f"""
            <div style="border-left: 5px solid {color}; padding: 10px 16px;
                        background: rgba({_hex_to_rgb(color)}, 0.04);
                        border-radius: 0 4px 4px 0; margin-bottom: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="font-size: 13px; font-weight: bold; color: {NAVY};">
                        {i}. {risk['description']}
                    </div>
                    <div style="font-size: 11px; font-weight: bold; color: {color};
                                background: rgba({_hex_to_rgb(color)}, 0.12);
                                padding: 2px 10px; border-radius: 3px;">
                        {severity}
                    </div>
                </div>
                <div style="font-size: 11px; color: {GRAY_400}; margin-top: 4px;">
                    Source: {risk['source_app']}
                </div>
                <div style="font-size: 12px; color: {GRAY_700}; margin-top: 4px;">
                    <b>Recommended Action:</b> {risk['recommended_action']}
                </div>
            </div>
            """, unsafe_allow_html=True)


# =============================================================================
# TAB: Trend Analysis
# =============================================================================
elif active_tab == "Trend Analysis":
    st.title("Trend Analysis")

    snapshots = load_snapshots()

    if len(snapshots) < 2:
        st.info(
            "Need at least 2 snapshots for trend analysis. "
            "Generate snapshots from the Report Generation tab or seed the database."
        )
    else:
        # Month-over-month training velocity from snapshot data
        st.subheader("Readiness Score Trend")

        dates = []
        scores = []
        trainee_counts = []
        overdue_counts = []

        for snap in reversed(snapshots):  # oldest first
            data = snap.get("data", {})
            summary = data.get("executive_summary", {})
            dates.append(snap["report_date"])
            scores.append(summary.get("readiness_score", 0))
            trainee_counts.append(data.get("total_trainees", 0))
            overdue_counts.append(data.get("overdue_milestones", 0))

        if HAS_PLOTLY:
            # Readiness score trend
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=dates, y=scores,
                mode="lines+markers",
                name="Readiness Score",
                line=dict(color=NAVY, width=3),
                marker=dict(size=10, color=GOLD),
            ))
            # Add RAG bands
            fig.add_hrect(y0=70, y1=100, fillcolor=RAG_GREEN, opacity=0.08,
                         layer="below", line_width=0)
            fig.add_hrect(y0=50, y1=70, fillcolor=RAG_AMBER, opacity=0.08,
                         layer="below", line_width=0)
            fig.add_hrect(y0=0, y1=50, fillcolor=RAG_RED, opacity=0.08,
                         layer="below", line_width=0)

            fig.update_layout(
                height=350, yaxis_range=[0, 105],
                yaxis_title="Readiness %",
                xaxis_title="Report Date",
                margin=dict(l=10, r=10, t=10, b=10),
            )
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

        # Snapshot comparison table
        st.subheader("Snapshot Comparison")
        comparison_data = []
        for snap in snapshots:
            data = snap.get("data", {})
            summary = data.get("executive_summary", {})
            comparison_data.append({
                "Date": snap["report_date"],
                "Type": snap["report_type"],
                "Score": summary.get("readiness_score", 0),
                "RAG": summary.get("rag", "N/A"),
                "Trainees": data.get("total_trainees", 0),
                "Overdue": data.get("overdue_milestones", 0),
                "Alerts": data.get("active_alerts", 0),
                "Risks": len(data.get("risks", [])),
            })

        df_comp = pd.DataFrame(comparison_data)
        st.dataframe(df_comp, use_container_width=True, hide_index=True)

        # Delta analysis between latest and previous
        if len(snapshots) >= 2:
            st.markdown("---")
            st.subheader("Week-over-Week Changes")
            latest = snapshots[0].get("data", {})
            previous = snapshots[1].get("data", {})

            c1, c2, c3, c4 = st.columns(4)

            latest_score = latest.get("executive_summary", {}).get("readiness_score", 0)
            prev_score = previous.get("executive_summary", {}).get("readiness_score", 0)
            c1.metric(
                "Readiness Score",
                f"{latest_score}%",
                delta=f"{latest_score - prev_score:+.1f}%",
            )

            c2.metric(
                "Trainees",
                latest.get("total_trainees", 0),
                delta=latest.get("total_trainees", 0) - previous.get("total_trainees", 0),
            )

            c3.metric(
                "Overdue",
                latest.get("overdue_milestones", 0),
                delta=latest.get("overdue_milestones", 0) - previous.get("overdue_milestones", 0),
                delta_color="inverse",
            )

            c4.metric(
                "Active Alerts",
                latest.get("active_alerts", 0),
                delta=latest.get("active_alerts", 0) - previous.get("active_alerts", 0),
                delta_color="inverse",
            )


# =============================================================================
# TAB: Report Generation
# =============================================================================
elif active_tab == "Report Generation":
    st.title("Report Generation")

    # Capture snapshot
    st.subheader("Capture Metrics Snapshot")
    col1, col2 = st.columns([2, 3])

    with col1:
        report_type = st.selectbox("Report Type", ["WEEKLY", "MONTHLY", "QUARTERLY"])
        generated_by = st.text_input("Generated By", value="", placeholder="MAJ SMITH")
        notes = st.text_area("Notes (optional)", placeholder="Weekly training status update...")

    with col2:
        st.markdown("""
        **Snapshot captures a point-in-time record of all metrics.**

        Use this to:
        - Preserve weekly readiness state for trend analysis
        - Generate briefing materials for command updates
        - Track progress against previous reporting periods
        """)

    if st.button("Capture Snapshot", type="primary"):
        if not generated_by.strip():
            st.error("Generated By field is required.")
        else:
            metrics = collect_all_metrics()
            db = SessionLocal()
            try:
                snapshot = save_snapshot(
                    report_type=report_type,
                    generated_by=generated_by.strip().upper(),
                    data=metrics,
                    db=db,
                    notes=notes.strip() or None,
                )
                st.success(f"Snapshot captured (ID: {snapshot.id}, Date: {snapshot.report_date})")
                st.cache_data.clear()
            finally:
                db.close()

    st.markdown("---")

    # Snapshot history
    st.subheader("Snapshot History")
    snapshots = load_snapshots()

    if snapshots:
        history_data = []
        for snap in snapshots:
            data = snap.get("data", {})
            summary = data.get("executive_summary", {})
            history_data.append({
                "ID": snap["id"],
                "Date": snap["report_date"],
                "Type": snap["report_type"],
                "By": snap["generated_by"],
                "Score": f"{summary.get('readiness_score', 0)}%",
                "RAG": summary.get("rag", "N/A"),
                "Notes": snap["notes"][:50] + "..." if len(snap.get("notes", "")) > 50 else snap.get("notes", ""),
            })
        df_history = pd.DataFrame(history_data)
        st.dataframe(df_history, use_container_width=True, hide_index=True)
    else:
        st.info("No snapshots yet. Capture one above or seed the database.")

    st.markdown("---")

    # Text-based briefing export
    st.subheader("Executive Briefing (BLUF Format)")

    if st.button("Generate Briefing"):
        metrics = load_metrics()
        summary = metrics.get("executive_summary", {})
        risks = metrics.get("risks", [])

        briefing_lines = []
        briefing_lines.append("=" * 72)
        briefing_lines.append("MSS TRAINING EXECUTIVE BRIEFING")
        briefing_lines.append(f"Date: {date.today().isoformat()}")
        briefing_lines.append("Classification: CUI // FOUO")
        briefing_lines.append("=" * 72)
        briefing_lines.append("")
        briefing_lines.append("BOTTOM LINE UP FRONT (BLUF)")
        briefing_lines.append("-" * 40)
        briefing_lines.append(
            f"Overall Readiness: {summary.get('rag', 'N/A')} ({summary.get('readiness_score', 0)}%)"
        )
        briefing_lines.append(f"  {summary.get('on_track', 'No data.')}")
        briefing_lines.append("")
        briefing_lines.append("1. ARE WE ON TRACK?")
        briefing_lines.append(f"   {summary.get('on_track', 'No data.')}")
        briefing_lines.append("")
        briefing_lines.append("2. WHAT'S AT RISK?")
        briefing_lines.append(f"   {summary.get('at_risk', 'No risks.')}")
        briefing_lines.append("")
        briefing_lines.append("3. WHAT CHANGED?")
        briefing_lines.append(f"   {summary.get('what_changed', 'No changes.')}")
        briefing_lines.append("")
        briefing_lines.append("4. WHAT DO YOU NEED FROM ME?")
        briefing_lines.append(f"   {summary.get('decision_required', 'None.')}")
        briefing_lines.append("")
        briefing_lines.append("KEY METRICS")
        briefing_lines.append("-" * 40)
        briefing_lines.append(f"  Total Trainees:      {metrics.get('total_trainees', 0)}")
        briefing_lines.append(f"  Exam Pass Rate:      {metrics.get('exam_pass_rate', 'N/A')}%")
        briefing_lines.append(f"  Upcoming Events:     {metrics.get('upcoming_events', 0)}")
        briefing_lines.append(f"  Overdue Milestones:  {metrics.get('overdue_milestones', 0)}")
        briefing_lines.append(f"  Active Alerts:       {metrics.get('active_alerts', 0)}")
        briefing_lines.append(f"  Open Action Items:   {metrics.get('open_action_items', 0)}")
        briefing_lines.append("")

        if risks:
            briefing_lines.append("RISK REGISTER")
            briefing_lines.append("-" * 40)
            for i, r in enumerate(risks, 1):
                briefing_lines.append(f"  {i}. [{r['severity']}] {r['description']}")
                briefing_lines.append(f"     Source: {r['source_app']}")
                briefing_lines.append(f"     Action: {r['recommended_action']}")
                briefing_lines.append("")

        briefing_lines.append("=" * 72)
        briefing_lines.append("END OF BRIEFING")
        briefing_lines.append("=" * 72)

        briefing_text = "\n".join(briefing_lines)
        st.code(briefing_text, language=None)

        st.download_button(
            label="Download Briefing (.txt)",
            data=briefing_text,
            file_name=f"MSS_Briefing_{date.today().isoformat()}.txt",
            mime="text/plain",
        )

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="app-footer">USAREUR-AF OPERATIONAL DATA TEAM — MSS TRAINING METRICS</div>',
    unsafe_allow_html=True,
)
