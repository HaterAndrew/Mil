"""Streamlit dashboard for the Data Quality Monitor.

Run: streamlit run apps/data_quality/dashboard.py --server.port 8510
"""

from __future__ import annotations

import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Ensure repo root is on sys.path for sibling imports
_repo_root = Path(__file__).resolve().parents[2]
if str(_repo_root) not in sys.path:
    sys.path.insert(0, str(_repo_root))

from apps.theme import (
    GOLD,
    GRAY_400,
    NAVY,
    NAVY_LIGHT,
    NAVY_MID,
    RAG_AMBER,
    RAG_GREEN,
    RAG_RED,
    apply_plotly_theme,
    inject_branding,
)
from apps.data_quality.db import (
    PipelineRow,
    MetricRow,
    AlertRow,
    get_all_health,
    get_db,
    get_metric_trend,
    get_pipeline_health,
    get_active_alerts,
    acknowledge_alert,
    init_db,
)
from apps.data_quality.models import (
    MetricStatus,
    MetricType,
    PipelineStatus,
    AlertSeverity,
)
from apps.shared.sanitize import safe_html

# ---------------------------------------------------------------------------
# Page config & branding
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Data Quality Monitor",
    page_icon="\U0001f4ca",
    layout="wide",
)
inject_branding("Data Quality Monitor")

# Ensure DB exists
init_db()

# ---------------------------------------------------------------------------
# Color helpers
# ---------------------------------------------------------------------------
STATUS_COLORS = {
    PipelineStatus.HEALTHY.value: RAG_GREEN,
    PipelineStatus.DEGRADED.value: RAG_AMBER,
    PipelineStatus.FAILED.value: RAG_RED,
    PipelineStatus.UNKNOWN.value: GRAY_400,
}

METRIC_STATUS_COLORS = {
    MetricStatus.PASS.value: RAG_GREEN,
    MetricStatus.WARN.value: RAG_AMBER,
    MetricStatus.FAIL.value: RAG_RED,
}

SEVERITY_COLORS = {
    AlertSeverity.CRITICAL.value: RAG_RED,
    AlertSeverity.WARNING.value: RAG_AMBER,
    AlertSeverity.INFO.value: NAVY_MID,
}


def _status_badge(status: str) -> str:
    """Return an HTML badge span for a status value."""
    color = STATUS_COLORS.get(status, GRAY_400)
    return f'<span style="background:{color};color:#fff;padding:2px 10px;border-radius:3px;font-size:12px;font-weight:bold;letter-spacing:0.5px">{safe_html(status)}</span>'


def _severity_badge(severity: str) -> str:
    """Return an HTML badge span for alert severity."""
    color = SEVERITY_COLORS.get(severity, GRAY_400)
    return f'<span style="background:{color};color:#fff;padding:2px 10px;border-radius:3px;font-size:11px;font-weight:bold">{safe_html(severity)}</span>'


def _metric_badge(status: str) -> str:
    """Return an HTML badge span for metric status."""
    color = METRIC_STATUS_COLORS.get(status, GRAY_400)
    return f'<span style="background:{color};color:#fff;padding:2px 8px;border-radius:3px;font-size:11px;font-weight:bold">{safe_html(status)}</span>'


# ---------------------------------------------------------------------------
# Sidebar navigation
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown("---")
    page = st.radio(
        "Navigation",
        [
            "Pipeline Overview",
            "Pipeline Detail",
            "Alert Center",
            "Metric Trends",
            "Quality Scorecard",
            "Pipeline Manager",
        ],
    )
    st.caption("DATA QUALITY MONITOR v1.0")


# ===================================================================
# PAGE: Pipeline Overview
# ===================================================================
if page == "Pipeline Overview":
    st.title("Pipeline Overview")

    with st.spinner("Loading data..."):
        with get_db() as db:
            healths = get_all_health(db)
            active_alerts = get_active_alerts(db)

    if not healths:
        st.info("No pipelines registered. Use Pipeline Manager to add pipelines, or run the seed script.")
    else:
        # KPI row
        total = len(healths)
        healthy_ct = sum(1 for h in healths if h.overall_status == PipelineStatus.HEALTHY)
        degraded_ct = sum(1 for h in healths if h.overall_status == PipelineStatus.DEGRADED)
        failed_ct = sum(1 for h in healths if h.overall_status == PipelineStatus.FAILED)

        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("Total Pipelines", total)
        c2.metric("Healthy", healthy_ct)
        c3.metric("Degraded", degraded_ct)
        c4.metric("Failed", failed_ct)
        c5.metric("Active Alerts", len(active_alerts))

        st.markdown("---")

        # Pipeline cards in a grid (3 per row)
        for i in range(0, len(healths), 3):
            cols = st.columns(3)
            for j, col in enumerate(cols):
                idx = i + j
                if idx >= len(healths):
                    break
                h = healths[idx]
                with col:
                    st.markdown(
                        f"### {safe_html(h.name)} {_status_badge(h.overall_status.value)}",
                        unsafe_allow_html=True,
                    )
                    st.caption(f"Uptime: {h.uptime_pct}% | Avg latency: {h.avg_latency_ms} ms")

                    # Sparkline: last 30 days of completeness (or first available metric)
                    with get_db() as db:
                        # Try completeness first, fall back to any available type
                        for mt in [MetricType.COMPLETENESS, MetricType.ACCURACY,
                                   MetricType.TIMELINESS, MetricType.VOLUME]:
                            trend = get_metric_trend(db, h.pipeline_id, mt.value, days=30)
                            if trend:
                                break

                    if trend:
                        df = pd.DataFrame([
                            {"date": m.timestamp, "value": m.value}
                            for m in trend
                        ])
                        fig = px.line(df, x="date", y="value", height=100)
                        fig.update_traces(line_color=STATUS_COLORS.get(h.overall_status.value, NAVY))
                        fig.update_layout(
                            showlegend=False,
                            margin=dict(l=0, r=0, t=0, b=0),
                            xaxis=dict(visible=False),
                            yaxis=dict(visible=False),
                        )
                        apply_plotly_theme(fig)
                        # Restore hidden axes after theme application
                        fig.update_layout(
                            xaxis=dict(visible=False),
                            yaxis=dict(visible=False),
                            margin=dict(l=0, r=0, t=0, b=0),
                        )
                        st.plotly_chart(fig, use_container_width=True, key=f"spark_{idx}")

                    # Mini metric summary
                    if h.metrics_summary:
                        badges = " ".join(
                            f"{safe_html(mt)}: {_metric_badge(info['status'])}"
                            for mt, info in h.metrics_summary.items()
                        )
                        st.markdown(badges, unsafe_allow_html=True)


# ===================================================================
# PAGE: Pipeline Detail
# ===================================================================
elif page == "Pipeline Detail":
    st.title("Pipeline Detail")

    with get_db() as db:
        pipes = db.query(PipelineRow).order_by(PipelineRow.name).all()
        pipe_names = {p.name: p.id for p in pipes}

    if not pipe_names:
        st.info("No pipelines registered.")
    else:
        selected_name = st.selectbox("Select Pipeline", list(pipe_names.keys()))
        pid = pipe_names[selected_name]

        with get_db() as db:
            health = get_pipeline_health(db, pid)
            pipe = db.query(PipelineRow).filter(PipelineRow.id == pid).first()
            alerts = get_active_alerts(db, pipeline_id=pid)

        if health and pipe:
            st.markdown(
                f"**Status:** {_status_badge(health.overall_status.value)} &nbsp; "
                f"**Owner:** {safe_html(pipe.owner)} &nbsp; "
                f"**Schedule:** {safe_html(pipe.schedule)}",
                unsafe_allow_html=True,
            )
            st.caption(f"{safe_html(pipe.source_system)} -> {safe_html(pipe.target_system)} | {safe_html(pipe.description or '')}")

            c1, c2, c3 = st.columns(3)
            c1.metric("Uptime", f"{health.uptime_pct}%")
            c2.metric("Avg Latency", f"{health.avg_latency_ms} ms")
            c3.metric("Active Alerts", len(alerts))

            st.markdown("---")

            # Metric trend charts
            st.subheader("Metric Trends (30 days)")
            available_types = list(health.metrics_summary.keys()) if health.metrics_summary else []

            if available_types:
                chart_cols = st.columns(min(len(available_types), 2))
                for i, mt in enumerate(available_types):
                    with chart_cols[i % 2]:
                        with get_db() as db:
                            trend = get_metric_trend(db, pid, mt, days=30)
                        if trend:
                            df = pd.DataFrame([
                                {"date": m.timestamp, "value": m.value,
                                 "threshold": m.threshold, "status": m.status}
                                for m in trend
                            ])
                            fig = go.Figure()
                            fig.add_trace(go.Scatter(
                                x=df["date"], y=df["value"],
                                mode="lines+markers",
                                name="Value",
                                line=dict(color=NAVY, width=2),
                                marker=dict(
                                    size=5,
                                    color=[METRIC_STATUS_COLORS.get(s, GRAY_400) for s in df["status"]],
                                ),
                            ))
                            # Threshold line
                            fig.add_hline(
                                y=df["threshold"].iloc[0],
                                line_dash="dash",
                                line_color=RAG_AMBER,
                                annotation_text="Threshold",
                            )
                            fig.update_layout(title=mt, height=280)
                            apply_plotly_theme(fig)
                            st.plotly_chart(fig, use_container_width=True, key=f"detail_{mt}")

            # Recent alerts for this pipeline
            if alerts:
                st.markdown("---")
                st.subheader("Recent Alerts")
                for a in alerts[:10]:
                    ts_display = (
                        a['timestamp'].strftime('%d %b %H:%MZ')
                        if isinstance(a['timestamp'], datetime)
                        else safe_html(str(a['timestamp']))
                    )
                    st.markdown(
                        f"{_severity_badge(a['severity'])} **{safe_html(str(a['metric_type']))}** "
                        f"— value: {safe_html(str(a['value']))}, threshold: {safe_html(str(a['threshold']))} "
                        f"({ts_display})",
                        unsafe_allow_html=True,
                    )


# ===================================================================
# PAGE: Alert Center
# ===================================================================
elif page == "Alert Center":
    st.title("Alert Center")

    # Filters
    fc1, fc2 = st.columns(2)
    with fc1:
        sev_filter = st.selectbox("Severity", ["ALL", "CRITICAL", "WARNING", "INFO"])
    with fc2:
        with get_db() as db:
            pipes = db.query(PipelineRow).order_by(PipelineRow.name).all()
        pipe_options = {"ALL": None}
        pipe_options.update({p.name: p.id for p in pipes})
        pipe_filter_name = st.selectbox("Pipeline", list(pipe_options.keys()))

    sev_val = None if sev_filter == "ALL" else sev_filter
    pid_val = pipe_options[pipe_filter_name]

    with get_db() as db:
        alerts = get_active_alerts(db, severity=sev_val, pipeline_id=pid_val)

    if not alerts:
        st.success("No active alerts. All pipelines operating within thresholds.")
    else:
        st.warning(f"{len(alerts)} active alert(s)")

        for a in alerts:
            with st.container():
                ac1, ac2, ac3, ac4 = st.columns([2, 3, 3, 2])
                with ac1:
                    st.markdown(_severity_badge(a["severity"]), unsafe_allow_html=True)
                with ac2:
                    st.markdown(f"**{safe_html(str(a['pipeline_name']))}** — {safe_html(str(a['metric_type']))}")
                with ac3:
                    ts_str = (
                        a["timestamp"].strftime("%d %b %Y %H:%MZ")
                        if isinstance(a["timestamp"], datetime)
                        else safe_html(str(a["timestamp"]))
                    )
                    st.markdown(f"Value: **{safe_html(str(a['value']))}** (threshold: {safe_html(str(a['threshold']))}) | {ts_str}")
                with ac4:
                    if st.button("Acknowledge", key=f"ack_{a['id']}"):
                        with get_db() as db:
                            acknowledge_alert(db, a["id"], "dashboard_user")
                        st.rerun()
                st.markdown("---")


# ===================================================================
# PAGE: Metric Trends
# ===================================================================
elif page == "Metric Trends":
    st.title("Metric Trends")

    tc1, tc2, tc3 = st.columns(3)
    with tc1:
        metric_type = st.selectbox("Metric Type", [mt.value for mt in MetricType])
    with tc2:
        days = st.slider("Time Range (days)", 7, 90, 30)
    with tc3:
        with get_db() as db:
            pipes = db.query(PipelineRow).order_by(PipelineRow.name).all()
        pipe_names = [p.name for p in pipes]
        selected_pipes = st.multiselect("Pipelines", pipe_names, default=pipe_names[:4])

    # Build comparison chart
    if selected_pipes:
        fig = go.Figure()
        with get_db() as db:
            for pname in selected_pipes:
                pipe = db.query(PipelineRow).filter(PipelineRow.name == pname).first()
                if not pipe:
                    continue
                trend = get_metric_trend(db, pipe.id, metric_type, days=days)
                if trend:
                    dates = [m.timestamp for m in trend]
                    values = [m.value for m in trend]
                    fig.add_trace(go.Scatter(
                        x=dates, y=values,
                        mode="lines",
                        name=pname,
                        line=dict(width=2),
                    ))
                    # Add threshold reference from first observation
                    if trend and not fig.layout.shapes:
                        fig.add_hline(
                            y=trend[0].threshold,
                            line_dash="dash",
                            line_color=RAG_AMBER,
                            annotation_text="Threshold",
                        )

        fig.update_layout(
            title=f"{metric_type} — {days}-Day Comparison",
            xaxis_title="Date",
            yaxis_title=metric_type,
            height=450,
            legend=dict(orientation="h", y=-0.15),
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Select at least one pipeline to display trends.")


# ===================================================================
# PAGE: Quality Scorecard
# ===================================================================
elif page == "Quality Scorecard":
    st.title("Quality Scorecard")

    with get_db() as db:
        healths = get_all_health(db)

    if not healths:
        st.info("No pipeline data available.")
    else:
        # Build scorecard table
        metric_types = [mt.value for mt in MetricType]
        rows = []
        for h in healths:
            row = {"Pipeline": h.name, "Status": h.overall_status.value, "Uptime %": h.uptime_pct}
            for mt in metric_types:
                if mt in h.metrics_summary:
                    info = h.metrics_summary[mt]
                    row[mt] = f"{info['value']} ({info['status']})"
                else:
                    row[mt] = "N/A"
            rows.append(row)

        df = pd.DataFrame(rows)

        # Render as styled HTML table for RAG coloring
        def _color_cell(val: str) -> str:
            """Apply background color based on status in parentheses."""
            if "(PASS)" in str(val):
                return f"background-color: {RAG_GREEN}20; color: {RAG_GREEN}"
            if "(WARN)" in str(val):
                return f"background-color: {RAG_AMBER}20; color: {RAG_AMBER}"
            if "(FAIL)" in str(val):
                return f"background-color: {RAG_RED}20; color: {RAG_RED}"
            return ""

        def _color_status(val: str) -> str:
            """Color the Status column."""
            colors = {
                PipelineStatus.HEALTHY.value: f"background-color: {RAG_GREEN}; color: white; font-weight: bold",
                PipelineStatus.DEGRADED.value: f"background-color: {RAG_AMBER}; color: white; font-weight: bold",
                PipelineStatus.FAILED.value: f"background-color: {RAG_RED}; color: white; font-weight: bold",
            }
            return colors.get(str(val), "")

        styled = df.style.map(_color_status, subset=["Status"])
        for mt in metric_types:
            if mt in df.columns:
                styled = styled.map(_color_cell, subset=[mt])

        st.dataframe(styled, use_container_width=True, hide_index=True, height=300)

        # Summary bar chart
        st.markdown("---")
        st.subheader("Status Distribution")
        status_counts = df["Status"].value_counts().reset_index()
        status_counts.columns = ["Status", "Count"]
        fig = px.bar(
            status_counts, x="Status", y="Count",
            color="Status",
            color_discrete_map={
                PipelineStatus.HEALTHY.value: RAG_GREEN,
                PipelineStatus.DEGRADED.value: RAG_AMBER,
                PipelineStatus.FAILED.value: RAG_RED,
                PipelineStatus.UNKNOWN.value: GRAY_400,
            },
            height=300,
        )
        fig.update_layout(showlegend=False)
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)


# ===================================================================
# PAGE: Pipeline Manager
# ===================================================================
elif page == "Pipeline Manager":
    st.title("Pipeline Manager")

    st.subheader("Register New Pipeline")
    with st.form("new_pipeline"):
        name = st.text_input("Pipeline Name")
        description = st.text_area("Description")
        fc1, fc2 = st.columns(2)
        with fc1:
            owner = st.text_input("Owner (POC)")
            source_system = st.text_input("Source System")
        with fc2:
            schedule = st.text_input("Schedule (e.g. 'daily 0600Z')")
            target_system = st.text_input("Target System")

        submitted = st.form_submit_button("Register Pipeline")
        if submitted:
            if not all([name, owner, schedule, source_system, target_system]):
                st.error("All fields except Description are required.")
            else:
                with get_db() as db:
                    existing = db.query(PipelineRow).filter(PipelineRow.name == name).first()
                    if existing:
                        st.error(f"Pipeline '{name}' already exists.")
                    else:
                        row = PipelineRow(
                            name=name,
                            description=description,
                            owner=owner,
                            schedule=schedule,
                            source_system=source_system,
                            target_system=target_system,
                        )
                        db.add(row)
                st.success(f"Pipeline '{name}' registered.")
                st.rerun()

    st.markdown("---")
    st.subheader("Existing Pipelines")

    with get_db() as db:
        pipes = db.query(PipelineRow).order_by(PipelineRow.name).all()

    if not pipes:
        st.info("No pipelines registered.")
    else:
        for p in pipes:
            with st.expander(f"{safe_html(p.name)} — {safe_html(p.status)}"):
                st.markdown(f"**Owner:** {safe_html(p.owner)} | **Schedule:** {safe_html(p.schedule)}")
                st.markdown(f"**Source:** {safe_html(p.source_system)} | **Target:** {safe_html(p.target_system)}")
                st.markdown(f"**Description:** {safe_html(p.description or 'N/A')}")
                if p.last_run:
                    st.caption(f"Last run: {p.last_run} | Last success: {p.last_success or 'Never'}")


# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="app-footer">USAREUR-AF OPERATIONAL DATA TEAM — DATA QUALITY MONITOR</div>',
    unsafe_allow_html=True,
)
