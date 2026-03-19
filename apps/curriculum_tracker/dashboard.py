"""Curriculum Tracker — Streamlit dashboard.

Tracks curriculum document versions, review cycles, and content freshness
across the maven_training/ corpus.
"""

from __future__ import annotations

import os
import sys
from datetime import date, datetime, timedelta
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

from curriculum_tracker.db import (
    Document,
    ReviewCycle,
    ChangeLog,
    SessionLocal,
    get_freshness_report,
    get_overdue_reviews,
    get_review_summary,
    get_stale_documents,
    get_document_history,
    init_db,
    scan_directory,
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
    GRAY_400,
    GRAY_700,
    WARNING_RED,
    CAUTION_AMBER,
)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
API_BASE = os.environ.get("CURRICULUM_TRACKER_API_URL", "http://localhost:8013")

# Default scan target
_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
MAVEN_TRAINING_PATH = str(_REPO_ROOT / "maven_training")

st.set_page_config(
    page_title="MSS Curriculum Tracker",
    page_icon="\U0001F4DA",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_branding("MSS Curriculum Tracker")

# ---------------------------------------------------------------------------
# Direct DB access (avoids API round-trips for analytics)
# ---------------------------------------------------------------------------
init_db()


@st.cache_data(ttl=30)
def load_all_documents():
    db = SessionLocal()
    try:
        docs = db.query(Document).order_by(Document.file_path).all()
        result = []
        for d in docs:
            # Find latest review
            latest_review = (
                db.query(ReviewCycle)
                .filter(ReviewCycle.doc_id == d.doc_id)
                .order_by(ReviewCycle.review_date.desc())
                .first()
            )
            result.append({
                "doc_id": d.doc_id,
                "file_path": d.file_path,
                "doc_type": d.doc_type,
                "course_id": d.course_id or "",
                "title": d.title,
                "current_version": d.current_version,
                "last_modified": d.last_modified,
                "file_hash": d.file_hash or "",
                "review_status": latest_review.status if latest_review else "NEVER REVIEWED",
                "last_review_date": latest_review.review_date if latest_review else None,
                "reviewer": latest_review.reviewer_name if latest_review else "",
            })
        return result
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_freshness():
    db = SessionLocal()
    try:
        return get_freshness_report(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_review_summary():
    db = SessionLocal()
    try:
        return get_review_summary(db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_stale(days: int):
    db = SessionLocal()
    try:
        docs = get_stale_documents(days, db)
        return [{"doc_id": d.doc_id, "file_path": d.file_path,
                 "doc_type": d.doc_type, "title": d.title,
                 "last_modified": d.last_modified} for d in docs]
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_overdue():
    db = SessionLocal()
    try:
        reviews = get_overdue_reviews(db)
        return [{
            "id": r.id,
            "doc_id": r.doc_id,
            "reviewer_name": r.reviewer_name,
            "review_date": r.review_date,
            "next_review_date": r.next_review_date,
            "status": r.status,
            "notes": r.notes or "",
        } for r in reviews]
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_recent_changes(limit: int = 50):
    db = SessionLocal()
    try:
        entries = (
            db.query(ChangeLog)
            .order_by(ChangeLog.change_date.desc())
            .limit(limit)
            .all()
        )
        result = []
        for e in entries:
            doc = db.query(Document).filter(Document.doc_id == e.doc_id).first()
            result.append({
                "id": e.id,
                "doc_id": e.doc_id,
                "file_path": doc.file_path if doc else "",
                "title": doc.title if doc else "",
                "change_date": e.change_date,
                "change_summary": e.change_summary or "",
                "changed_by": e.changed_by or "",
                "previous_hash": (e.previous_hash or "")[:12],
                "new_hash": (e.new_hash or "")[:12],
            })
        return result
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_all_reviews():
    db = SessionLocal()
    try:
        reviews = (
            db.query(ReviewCycle)
            .order_by(ReviewCycle.review_date.desc())
            .all()
        )
        result = []
        for r in reviews:
            doc = db.query(Document).filter(Document.doc_id == r.doc_id).first()
            result.append({
                "id": r.id,
                "doc_id": r.doc_id,
                "file_path": doc.file_path if doc else "",
                "title": doc.title if doc else "",
                "review_type": r.review_type,
                "reviewer_name": r.reviewer_name,
                "review_date": r.review_date,
                "status": r.status,
                "notes": r.notes or "",
                "next_review_date": r.next_review_date,
            })
        return result
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
st.sidebar.title("MSS Curriculum Tracker")
st.sidebar.caption("USAREUR-AF Operational Data Team")
st.sidebar.markdown("---")

tab_names = [
    "Freshness Overview",
    "Document Browser",
    "Review Tracker",
    "Change History",
    "Scan & Sync",
]
active_tab = st.sidebar.radio("Navigate", tab_names)


# =============================================================================
# TAB: Freshness Overview
# =============================================================================
if active_tab == "Freshness Overview":
    st.title("Curriculum Freshness Overview")

    docs = load_all_documents()
    freshness = load_freshness()
    summary = load_review_summary()
    stale_docs = load_stale(90)
    overdue = load_overdue()

    if not docs:
        st.info("No documents loaded. Run a scan from the Scan & Sync tab, or seed the database.")
        st.stop()

    # --- KPI Row ---
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Documents", len(docs))

    # Last scan date (most recent change_date)
    changes = load_recent_changes(1)
    last_scan = changes[0]["change_date"].strftime("%Y-%m-%d") if changes else "Never"
    c2.metric("Last Scan", last_scan)

    c3.metric("Overdue Reviews", summary.get("OVERDUE", 0) + len(overdue),
              delta_color="inverse")
    c4.metric("Stale Docs (>90d)", len(stale_docs), delta_color="inverse")

    st.markdown("---")

    # --- Freshness gauge per doc type ---
    st.subheader("Content Freshness by Document Type")

    if freshness and HAS_PLOTLY:
        df_fresh = pd.DataFrame(freshness)

        col_chart, col_table = st.columns([3, 2])

        with col_chart:
            # Bar chart: avg days since last review per type
            chart_data = df_fresh[df_fresh["avg_days_since_review"].notna()].copy()
            if not chart_data.empty:
                # Color by freshness: green < 60d, amber 60-120d, red > 120d
                colors = []
                for days in chart_data["avg_days_since_review"]:
                    if days < 60:
                        colors.append(RAG_GREEN)
                    elif days < 120:
                        colors.append(RAG_AMBER)
                    else:
                        colors.append(RAG_RED)

                fig = go.Figure(data=[go.Bar(
                    x=chart_data["doc_type"],
                    y=chart_data["avg_days_since_review"],
                    marker_color=colors,
                    text=[f"{d:.0f}d" for d in chart_data["avg_days_since_review"]],
                    textposition="auto",
                )])
                fig.update_layout(
                    height=350,
                    xaxis_title="Document Type",
                    yaxis_title="Avg Days Since Review",
                )
                # Add threshold lines
                fig.add_hline(y=90, line_dash="dash", line_color=RAG_AMBER,
                              annotation_text="90d threshold")
                apply_plotly_theme(fig)
                st.plotly_chart(fig, use_container_width=True)

        with col_table:
            display_df = df_fresh.rename(columns={
                "doc_type": "Type",
                "doc_count": "Docs",
                "avg_days_since_review": "Avg Days",
                "never_reviewed": "Never Reviewed",
            })
            st.dataframe(display_df, use_container_width=True, hide_index=True)

    st.markdown("---")

    # --- Review status breakdown ---
    st.subheader("Review Status Summary")
    if summary:
        cols = st.columns(4)
        status_colors = {
            "APPROVED": RAG_GREEN,
            "CHANGES_REQUIRED": RAG_AMBER,
            "IN_REVIEW": NAVY_MID,
            "OVERDUE": RAG_RED,
        }
        for i, (stat, count) in enumerate(summary.items()):
            cols[i].metric(stat.replace("_", " ").title(), count)


# =============================================================================
# TAB: Document Browser
# =============================================================================
elif active_tab == "Document Browser":
    st.title("Document Browser")

    docs = load_all_documents()
    if not docs:
        st.info("No documents loaded.")
        st.stop()

    df = pd.DataFrame(docs)

    # Filters
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        type_filter = st.selectbox(
            "Filter by Type",
            ["All"] + sorted(df["doc_type"].unique().tolist()),
        )
    with col_f2:
        status_filter = st.selectbox(
            "Filter by Review Status",
            ["All"] + sorted(df["review_status"].unique().tolist()),
        )
    with col_f3:
        search = st.text_input("Search file path or title", "")

    filtered = df.copy()
    if type_filter != "All":
        filtered = filtered[filtered["doc_type"] == type_filter]
    if status_filter != "All":
        filtered = filtered[filtered["review_status"] == status_filter]
    if search:
        mask = (
            filtered["file_path"].str.contains(search, case=False, na=False)
            | filtered["title"].str.contains(search, case=False, na=False)
        )
        filtered = filtered[mask]

    # Display
    display_cols = [
        "doc_id", "doc_type", "course_id", "title", "last_modified",
        "review_status", "last_review_date", "reviewer",
    ]
    st.caption(f"Showing {len(filtered)} of {len(df)} documents")
    st.dataframe(
        filtered[display_cols].rename(columns={
            "doc_id": "ID", "doc_type": "Type", "course_id": "Course",
            "title": "Title", "last_modified": "Last Modified",
            "review_status": "Review Status", "last_review_date": "Last Review",
            "reviewer": "Reviewer",
        }),
        use_container_width=True,
        hide_index=True,
    )


# =============================================================================
# TAB: Review Tracker
# =============================================================================
elif active_tab == "Review Tracker":
    st.title("Review Tracker")

    reviews = load_all_reviews()
    overdue = load_overdue()

    # --- Overdue reviews (RED) ---
    st.subheader("Overdue Reviews")
    if overdue:
        for r in overdue:
            st.error(
                f"**Doc #{r['doc_id']}** — Reviewer: {r['reviewer_name']} | "
                f"Due: {r['next_review_date']} | Status: {r['status']}"
            )
    else:
        st.success("No overdue reviews.")

    st.markdown("---")

    # --- Upcoming reviews ---
    st.subheader("Upcoming Reviews")
    if reviews:
        upcoming = [
            r for r in reviews
            if r["next_review_date"] and r["next_review_date"] >= date.today()
            and r["status"] in ("IN_REVIEW", "APPROVED", "CHANGES_REQUIRED")
        ]
        if upcoming:
            df_up = pd.DataFrame(upcoming[:20])
            st.dataframe(
                df_up[["title", "review_type", "reviewer_name", "next_review_date", "status"]].rename(columns={
                    "title": "Document", "review_type": "Type",
                    "reviewer_name": "Reviewer", "next_review_date": "Next Review",
                    "status": "Status",
                }),
                use_container_width=True,
                hide_index=True,
            )
        else:
            st.info("No upcoming reviews scheduled.")

    st.markdown("---")

    # --- Recently completed reviews ---
    st.subheader("Recently Completed Reviews")
    if reviews:
        completed = [r for r in reviews if r["status"] == "APPROVED"][:20]
        if completed:
            df_comp = pd.DataFrame(completed)
            st.dataframe(
                df_comp[["title", "reviewer_name", "review_date", "review_type", "notes"]].rename(columns={
                    "title": "Document", "reviewer_name": "Reviewer",
                    "review_date": "Review Date", "review_type": "Type",
                    "notes": "Notes",
                }),
                use_container_width=True,
                hide_index=True,
            )
        else:
            st.info("No completed reviews found.")

    st.markdown("---")

    # --- All reviews table ---
    st.subheader("All Reviews")
    if reviews:
        df_all = pd.DataFrame(reviews)
        st.dataframe(
            df_all[["title", "review_type", "reviewer_name", "review_date", "status", "next_review_date"]].rename(columns={
                "title": "Document", "review_type": "Type",
                "reviewer_name": "Reviewer", "review_date": "Date",
                "status": "Status", "next_review_date": "Next Review",
            }),
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No reviews recorded yet.")


# =============================================================================
# TAB: Change History
# =============================================================================
elif active_tab == "Change History":
    st.title("Change History")

    changes = load_recent_changes(100)

    if not changes:
        st.info("No changes recorded. Run a scan to detect document changes.")
        st.stop()

    # Search
    search = st.text_input("Search by file path or summary", "", key="change_search")

    df_ch = pd.DataFrame(changes)

    if search:
        mask = (
            df_ch["file_path"].str.contains(search, case=False, na=False)
            | df_ch["change_summary"].str.contains(search, case=False, na=False)
        )
        df_ch = df_ch[mask]

    st.caption(f"Showing {len(df_ch)} change entries")

    # Timeline chart
    if HAS_PLOTLY and not df_ch.empty:
        st.subheader("Change Timeline")
        df_ch["date_only"] = pd.to_datetime(df_ch["change_date"]).dt.date
        daily = df_ch.groupby("date_only").size().reset_index(name="changes")
        fig = px.bar(
            daily, x="date_only", y="changes",
            color="changes", color_continuous_scale="Blues",
        )
        fig.update_layout(
            height=250, xaxis_title="", yaxis_title="Changes",
            showlegend=False,
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # Table
    st.subheader("Change Log")
    display_cols = ["change_date", "title", "file_path", "change_summary",
                    "previous_hash", "new_hash", "changed_by"]
    st.dataframe(
        df_ch[display_cols].rename(columns={
            "change_date": "Date", "title": "Document", "file_path": "Path",
            "change_summary": "Summary", "previous_hash": "Old Hash",
            "new_hash": "New Hash", "changed_by": "Changed By",
        }),
        use_container_width=True,
        hide_index=True,
    )


# =============================================================================
# TAB: Scan & Sync
# =============================================================================
elif active_tab == "Scan & Sync":
    st.title("Scan & Sync")
    st.caption("Scan the maven_training/ directory to detect new, changed, and unchanged documents.")

    st.markdown(f"**Scan target:** `{MAVEN_TRAINING_PATH}`")

    if st.button("Run Scan Now", type="primary"):
        with st.spinner("Scanning directory..."):
            db = SessionLocal()
            try:
                counts = scan_directory(MAVEN_TRAINING_PATH, db)
            finally:
                db.close()

            st.cache_data.clear()

            # Display results
            c1, c2, c3 = st.columns(3)
            c1.metric("New Documents", counts["new"])
            c2.metric("Changed", counts["changed"])
            c3.metric("Unchanged", counts["unchanged"])

            total = counts["new"] + counts["changed"] + counts["unchanged"]
            st.success(f"Scan complete. {total} .md files processed.")

            if counts["new"] > 0:
                st.info(f"{counts['new']} new documents added to tracking.")
            if counts["changed"] > 0:
                st.warning(f"{counts['changed']} documents have changed since last scan.")

    st.markdown("---")
    st.subheader("Current Document Counts")

    docs = load_all_documents()
    if docs:
        df = pd.DataFrame(docs)
        type_counts = df["doc_type"].value_counts().reset_index()
        type_counts.columns = ["Document Type", "Count"]
        st.dataframe(type_counts, use_container_width=True, hide_index=True)
    else:
        st.info("No documents in database. Run a scan to populate.")

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="app-footer">USAREUR-AF OPERATIONAL DATA TEAM — MSS CURRICULUM TRACKER</div>',
    unsafe_allow_html=True,
)
