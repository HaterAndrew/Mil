"""Cross-Reference Validator — Streamlit dashboard.

Provides scan execution, issue browsing, trend analysis, prereq chain
audit, and scan history for the maven_training documentation corpus.
"""

from __future__ import annotations

import sys
from collections import Counter
from datetime import datetime
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

from xref_validator.db import (
    PREREQ_CHAIN,
    VALID_TM_IDS,
    get_filtered_issues,
    get_scan_history,
    get_scan_result,
    init_db,
    run_full_scan,
)
from xref_validator.models import (
    MAVEN_TRAINING_DEFAULT,
    IssueType,
    Severity,
    ValidationIssue,
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
)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
API_BASE = "http://localhost:8006"

st.set_page_config(
    page_title="Cross-Reference Validator",
    page_icon="\U0001f517",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_branding("Cross-Reference Validator")

# Ensure DB exists
init_db()

# ---------------------------------------------------------------------------
# Severity color map
# ---------------------------------------------------------------------------
SEVERITY_COLORS = {
    "ERROR": RAG_RED,
    "WARNING": RAG_AMBER,
    "INFO": NAVY_MID,
}

ISSUE_TYPE_LABELS = {
    "BROKEN_LINK": "Broken Link",
    "STALE_REF": "Stale Reference",
    "MISSING_FILE": "Missing File",
    "PREREQ_MISMATCH": "Prereq Mismatch",
    "CHAPTER_REF_ERROR": "Chapter Ref Error",
}


# ---------------------------------------------------------------------------
# Sidebar navigation
# ---------------------------------------------------------------------------
with st.sidebar:
    st.caption("DOCUMENTATION QUALITY")
    page = st.radio(
        "Navigate",
        [
            "Run Scan",
            "Issues Browser",
            "Trend Analysis",
            "Prereq Audit",
            "Scan History",
        ],
        label_visibility="collapsed",
    )


# ---------------------------------------------------------------------------
# Page: Run Scan
# ---------------------------------------------------------------------------
def page_run_scan():
    st.header("Run Validation Scan")
    st.markdown(
        "Scan the documentation corpus for broken links, stale references, "
        "chapter errors, and prereq chain inconsistencies."
    )

    col1, col2 = st.columns([3, 1])
    with col1:
        root_path = st.text_input(
            "Root Path",
            value=MAVEN_TRAINING_DEFAULT,
            help="Path to the documentation corpus root directory.",
        )
    with col2:
        st.markdown("")  # spacer
        st.markdown("")
        scan_btn = st.button("EXECUTE SCAN", use_container_width=True)

    if scan_btn:
        with st.spinner("Scanning corpus... this may take a moment."):
            result = run_full_scan(root_path)

        st.success(
            f"Scan complete: {result.total_files} files scanned, "
            f"{result.issues_found} issues found."
        )

        # Summary metrics
        st.subheader("Results Summary")
        cols = st.columns(5)
        type_order = [
            "BROKEN_LINK", "STALE_REF", "MISSING_FILE",
            "PREREQ_MISMATCH", "CHAPTER_REF_ERROR",
        ]
        for i, itype in enumerate(type_order):
            count = result.summary_by_type.get(itype, 0)
            cols[i].metric(
                ISSUE_TYPE_LABELS.get(itype, itype),
                count,
            )

        # Severity breakdown
        sev_cols = st.columns(3)
        for i, sev in enumerate(["ERROR", "WARNING", "INFO"]):
            count = result.summary_by_severity.get(sev, 0)
            sev_cols[i].metric(f"{sev}", count)

        # Quick issue table
        if result.issues:
            st.subheader("Issues Found")
            df = _issues_to_df(result.issues)
            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "severity": st.column_config.TextColumn("Severity", width="small"),
                    "issue_type": st.column_config.TextColumn("Type", width="medium"),
                    "file_path": st.column_config.TextColumn("File", width="large"),
                    "line_number": st.column_config.NumberColumn("Line", width="small"),
                    "description": st.column_config.TextColumn("Description", width="large"),
                },
            )


# ---------------------------------------------------------------------------
# Page: Issues Browser
# ---------------------------------------------------------------------------
def page_issues_browser():
    st.header("Issues Browser")

    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        type_filter = st.selectbox(
            "Issue Type",
            ["All"] + list(ISSUE_TYPE_LABELS.values()),
        )
    with col2:
        sev_filter = st.selectbox(
            "Severity",
            ["All", "ERROR", "WARNING", "INFO"],
        )
    with col3:
        file_filter = st.text_input("File Path Contains", "")

    # Map display label back to enum value
    type_val = None
    if type_filter != "All":
        for k, v in ISSUE_TYPE_LABELS.items():
            if v == type_filter:
                type_val = k
                break

    sev_val = sev_filter if sev_filter != "All" else None

    issues = get_filtered_issues(issue_type=type_val, severity=sev_val)

    # Apply file path filter
    if file_filter:
        issues = [i for i in issues if file_filter.lower() in i.file_path.lower()]

    st.metric("Total Issues Matching", len(issues))

    if issues:
        df = _issues_to_df(issues)
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "severity": st.column_config.TextColumn("Severity", width="small"),
                "issue_type": st.column_config.TextColumn("Type", width="medium"),
                "file_path": st.column_config.TextColumn("File", width="large"),
                "line_number": st.column_config.NumberColumn("Line", width="small"),
                "description": st.column_config.TextColumn("Description", width="large"),
                "suggested_fix": st.column_config.TextColumn("Suggested Fix", width="large"),
            },
        )

        # Breakdown charts
        if HAS_PLOTLY:
            st.subheader("Issue Distribution")
            c1, c2 = st.columns(2)

            with c1:
                type_counts = Counter(i.issue_type.value for i in issues)
                fig = px.bar(
                    x=list(type_counts.keys()),
                    y=list(type_counts.values()),
                    labels={"x": "Issue Type", "y": "Count"},
                    title="By Type",
                    color=list(type_counts.keys()),
                    color_discrete_map={
                        "BROKEN_LINK": WARNING_RED,
                        "STALE_REF": CAUTION_AMBER,
                        "MISSING_FILE": RAG_RED,
                        "PREREQ_MISMATCH": NAVY_MID,
                        "CHAPTER_REF_ERROR": GOLD_DARK,
                    },
                )
                apply_plotly_theme(fig)
                fig.update_layout(showlegend=False)
                st.plotly_chart(fig, use_container_width=True)

            with c2:
                sev_counts = Counter(i.severity.value for i in issues)
                fig = px.pie(
                    names=list(sev_counts.keys()),
                    values=list(sev_counts.values()),
                    title="By Severity",
                    color=list(sev_counts.keys()),
                    color_discrete_map=SEVERITY_COLORS,
                )
                apply_plotly_theme(fig)
                st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No issues found matching the current filters.")


# ---------------------------------------------------------------------------
# Page: Trend Analysis
# ---------------------------------------------------------------------------
def page_trend_analysis():
    st.header("Trend Analysis")
    st.markdown("Track issue counts across scan history to measure documentation quality improvement.")

    history = get_scan_history()
    if len(history) < 1:
        st.warning("No scan history available. Run a scan first.")
        return

    # Build a time-series dataframe
    rows = []
    for item in reversed(history):  # oldest first
        rows.append({
            "scan_id": item.scan_id,
            "timestamp": item.timestamp,
            "total_files": item.total_files,
            "issues_found": item.issues_found,
        })
    df = pd.DataFrame(rows)

    # Summary metrics for latest vs previous
    if len(history) >= 2:
        latest = history[0]
        previous = history[1]
        delta = latest.issues_found - previous.issues_found
        cols = st.columns(3)
        cols[0].metric("Latest Scan Issues", latest.issues_found, delta=delta, delta_color="inverse")
        cols[1].metric("Files Scanned", latest.total_files)
        cols[2].metric("Total Scans", len(history))
    else:
        latest = history[0]
        cols = st.columns(3)
        cols[0].metric("Latest Scan Issues", latest.issues_found)
        cols[1].metric("Files Scanned", latest.total_files)
        cols[2].metric("Total Scans", len(history))

    if HAS_PLOTLY:
        # Issues over time
        fig = px.line(
            df,
            x="timestamp",
            y="issues_found",
            markers=True,
            title="Issues Found Over Time",
            labels={"timestamp": "Scan Date", "issues_found": "Issues"},
        )
        fig.update_traces(line_color=NAVY, marker_color=GOLD)
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

        # Per-type breakdown over time (load full results for each scan)
        st.subheader("Issues by Type Over Time")
        type_rows = []
        for item in reversed(history):
            result = get_scan_result(item.scan_id)
            if result:
                for itype, count in result.summary_by_type.items():
                    type_rows.append({
                        "timestamp": item.timestamp,
                        "issue_type": itype,
                        "count": count,
                    })
        if type_rows:
            tdf = pd.DataFrame(type_rows)
            fig2 = px.line(
                tdf,
                x="timestamp",
                y="count",
                color="issue_type",
                markers=True,
                title="Issue Types Over Time",
                labels={"timestamp": "Scan Date", "count": "Count"},
            )
            apply_plotly_theme(fig2)
            st.plotly_chart(fig2, use_container_width=True)
    else:
        st.dataframe(df, use_container_width=True, hide_index=True)


# ---------------------------------------------------------------------------
# Page: Prereq Audit
# ---------------------------------------------------------------------------
def page_prereq_audit():
    st.header("Prereq Chain Audit")
    st.markdown(
        "Visual representation of the authoritative TM prereq chain with "
        "pass/fail indicators from the latest scan."
    )

    # Load latest scan issues for prereq mismatches
    prereq_issues = get_filtered_issues(issue_type="PREREQ_MISMATCH")
    stale_issues = get_filtered_issues(issue_type="STALE_REF")

    # Determine which TMs have issues
    tms_with_prereq_issues: set[str] = set()
    for issue in prereq_issues:
        # Extract TM from description
        import re
        m = re.search(r"(TM-\d{2}[A-M]?)\s+doc", issue.description)
        if m:
            tms_with_prereq_issues.add(m.group(1))

    tms_with_stale_refs: set[str] = set()
    for issue in stale_issues:
        # Flag based on file path
        import re
        m = re.search(r"TM[-_]?(\d{2})[-_]?([A-M])?", issue.file_path, re.IGNORECASE)
        if m:
            number = m.group(1)
            suffix = (m.group(2) or "").upper()
            tm_id = f"TM-{number}{suffix}" if suffix else f"TM-{number}"
            tms_with_stale_refs.add(tm_id)

    # Render the chain diagram
    st.subheader("Prereq Chain")

    # Foundation tier
    st.markdown("### Foundation")
    cols = st.columns(4)
    _render_tm_card(cols[0], "TM-10", tms_with_prereq_issues, tms_with_stale_refs)
    _render_tm_card(cols[1], "TM-20", tms_with_prereq_issues, tms_with_stale_refs)
    _render_tm_card(cols[2], "TM-30", tms_with_prereq_issues, tms_with_stale_refs)
    _render_tm_card(cols[3], "BSP", tms_with_prereq_issues, tms_with_stale_refs)

    st.markdown("---")

    # WFF tracks (TM-40A through TM-40F)
    st.markdown("### WFF Tracks (TM-40A through TM-40F)")
    cols = st.columns(6)
    for i, suffix in enumerate("ABCDEF"):
        _render_tm_card(cols[i], f"TM-40{suffix}", tms_with_prereq_issues, tms_with_stale_refs)

    st.markdown("---")

    # Specialist tracks (TM-40G through TM-40M)
    st.markdown("### Specialist Tracks (TM-40G through TM-40M)")
    cols = st.columns(7)
    for i, suffix in enumerate("GHMJKL"):
        _render_tm_card(cols[i], f"TM-40{suffix}", tms_with_prereq_issues, tms_with_stale_refs)

    st.markdown("---")

    # Advanced tracks (TM-50G through TM-50M)
    st.markdown("### Advanced Specialist (TM-50G through TM-50M)")
    cols = st.columns(7)
    for i, suffix in enumerate("GHMJKL"):
        _render_tm_card(cols[i], f"TM-50{suffix}", tms_with_prereq_issues, tms_with_stale_refs)

    # Issue details
    if prereq_issues:
        st.markdown("---")
        st.subheader("Prereq Mismatch Details")
        df = _issues_to_df(prereq_issues)
        st.dataframe(df, use_container_width=True, hide_index=True)

    if stale_issues:
        st.markdown("---")
        st.subheader("Stale Reference Details")
        df = _issues_to_df(stale_issues)
        st.dataframe(df, use_container_width=True, hide_index=True)


def _render_tm_card(
    col,
    tm_id: str,
    prereq_issues: set[str],
    stale_issues: set[str],
):
    """Render a TM card with pass/fail indicator."""
    has_prereq = tm_id in prereq_issues
    has_stale = tm_id in stale_issues

    if has_prereq or has_stale:
        status_color = WARNING_RED
        status_icon = "FAIL"
        bg_color = "#fdf0f0"
    else:
        status_color = RAG_GREEN
        status_icon = "PASS"
        bg_color = "#f0f9f1"

    prereqs = PREREQ_CHAIN.get(tm_id, [])
    prereq_text = ", ".join(prereqs) if prereqs else "None"

    col.markdown(
        f"""<div style="
            background: {bg_color};
            border: 2px solid {status_color};
            border-radius: 4px;
            padding: 10px;
            text-align: center;
            margin-bottom: 8px;
        ">
            <div style="font-weight: bold; color: {NAVY}; font-size: 14px;">{tm_id}</div>
            <div style="color: {status_color}; font-weight: bold; font-size: 12px;
                         letter-spacing: 1px; margin: 4px 0;">{status_icon}</div>
            <div style="color: {GRAY_400}; font-size: 10px;">Prereq: {prereq_text}</div>
        </div>""",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Page: Scan History
# ---------------------------------------------------------------------------
def page_scan_history():
    st.header("Scan History")

    history = get_scan_history()
    if not history:
        st.info("No scans recorded yet. Run a scan to populate history.")
        return

    # History table
    rows = []
    for item in history:
        rows.append({
            "Scan ID": item.scan_id,
            "Timestamp": item.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "Files Scanned": item.total_files,
            "Issues Found": item.issues_found,
        })
    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True, hide_index=True)

    # Drill-down
    st.subheader("Drill Down")
    scan_ids = [h.scan_id for h in history]
    selected_id = st.selectbox("Select Scan ID", scan_ids)

    if selected_id:
        result = get_scan_result(selected_id)
        if result:
            cols = st.columns(4)
            cols[0].metric("Files Scanned", result.total_files)
            cols[1].metric("Total Issues", result.issues_found)
            cols[2].metric("Errors", result.summary_by_severity.get("ERROR", 0))
            cols[3].metric("Warnings", result.summary_by_severity.get("WARNING", 0))

            if result.issues:
                st.subheader(f"Issues for Scan #{selected_id}")
                idf = _issues_to_df(result.issues)
                st.dataframe(idf, use_container_width=True, hide_index=True)
        else:
            st.error(f"Could not load scan {selected_id}")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _issues_to_df(issues: list[ValidationIssue]) -> pd.DataFrame:
    """Convert a list of ValidationIssue to a DataFrame for display."""
    return pd.DataFrame([
        {
            "severity": i.severity.value,
            "issue_type": ISSUE_TYPE_LABELS.get(i.issue_type.value, i.issue_type.value),
            "file_path": i.file_path,
            "line_number": i.line_number,
            "description": i.description,
            "suggested_fix": i.suggested_fix,
        }
        for i in issues
    ])


# ---------------------------------------------------------------------------
# Router
# ---------------------------------------------------------------------------
if page == "Run Scan":
    page_run_scan()
elif page == "Issues Browser":
    page_issues_browser()
elif page == "Trend Analysis":
    page_trend_analysis()
elif page == "Prereq Audit":
    page_prereq_audit()
elif page == "Scan History":
    page_scan_history()

# Footer
st.markdown(
    '<div class="app-footer">USAREUR-AF OPERATIONAL DATA TEAM — CROSS-REFERENCE VALIDATOR v1.0</div>',
    unsafe_allow_html=True,
)
