"""Exam Analytics Dashboard — Streamlit application.

Professional exam analysis with cohort comparison, item discrimination,
question improvement tracking, and detailed score distributions.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

_app_dir = Path(__file__).resolve().parent
if str(_app_dir.parent) not in sys.path:
    sys.path.insert(0, str(_app_dir.parent))

import pandas as pd
import streamlit as st

try:
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    HAS_PLOTLY = True
except ImportError:
    HAS_PLOTLY = False

from exam_analytics.db import (
    ExamSession,
    SessionLocal,
    cohort_summary,
    compute_gain_scores,
    cross_cohort_comparison,
    init_db,
    item_discrimination,
    question_difficulty,
    question_improvement,
)

from theme import inject_branding, apply_plotly_theme, NAVY, NAVY_DARK, NAVY_LIGHT, NAVY_MID, GOLD, GOLD_DARK, GOLD_LIGHT, RAG_GREEN, RAG_AMBER, RAG_RED, GRAY_400, GRAY_700, WARNING_RED, CAUTION_AMBER, GREEN_OK

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
API_BASE = os.environ.get("EXAM_ANALYTICS_API_URL", "http://localhost:8002")

st.set_page_config(
    page_title="MSS Exam Analytics",
    page_icon="\U0001F4CA",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_branding("MSS Exam Analytics")


# ---------------------------------------------------------------------------
# Direct DB access for dashboard
# ---------------------------------------------------------------------------
@st.cache_data(ttl=30)
def load_sessions():
    init_db()
    db = SessionLocal()
    try:
        sessions = db.query(ExamSession).order_by(ExamSession.administration_date).all()
        return [{
            "id": s.id,
            "course_id": s.course_id,
            "form_type": s.form_type,
            "date": s.administration_date.isoformat(),
            "cohort_label": s.cohort_label,
            "n_results": len(s.results),
            "label": f"[{s.id}] {s.course_id} {s.form_type} — {s.cohort_label}",
        } for s in sessions]
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_cohort_summary(session_id: int):
    db = SessionLocal()
    try:
        return cohort_summary(session_id, db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_results(session_id: int):
    db = SessionLocal()
    try:
        session = db.query(ExamSession).filter(ExamSession.id == session_id).first()
        if not session:
            return []
        return [{
            "trainee_id": r.trainee_id,
            "total_score": r.total_score,
            "total_possible": r.total_possible,
            "score_percent": r.score_percent,
            "result": r.result,
        } for r in session.results]
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_gains(pre_id: int, post_id: int):
    db = SessionLocal()
    try:
        return compute_gain_scores(pre_id, post_id, db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_questions(session_id: int):
    db = SessionLocal()
    try:
        return question_difficulty(session_id, db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_discrimination(session_id: int):
    db = SessionLocal()
    try:
        return item_discrimination(session_id, db)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_cohort_comparison(course_id: str | None = None):
    db = SessionLocal()
    try:
        return cross_cohort_comparison(db, course_id)
    finally:
        db.close()


@st.cache_data(ttl=30)
def load_question_improvement(pre_id: int, post_id: int):
    db = SessionLocal()
    try:
        return question_improvement(pre_id, post_id, db)
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Foundation / All course filter
# ---------------------------------------------------------------------------
FOUNDATION_COURSES = ["SL 1", "SL 2", "SL 3"]

TRACK_OPTIONS = {
    "Foundation (SL 1/2/3)": FOUNDATION_COURSES,
    "All Courses": None,  # None = no filter
}


def track_selector(key: str = "track_view") -> list[str] | None:
    """Render track view selector. Returns course list or None for all."""
    selected = st.radio(
        "Track View",
        list(TRACK_OPTIONS.keys()),
        index=0,
        horizontal=True,
        key=key,
    )
    return TRACK_OPTIONS[selected]


def filter_sessions_by_track(sessions: list[dict], track_courses: list[str] | None) -> list[dict]:
    """Filter sessions to only those matching the active track."""
    if track_courses is None:
        return sessions
    return [s for s in sessions if s["course_id"] in track_courses]


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
st.sidebar.title("MSS Exam Analytics")
st.sidebar.caption("USAREUR-AF Operational Data Team")
st.sidebar.markdown("---")

tab_names = [
    "Dashboard Overview",
    "Cohort Deep-Dive",
    "Gain Score Analysis",
    "Question Analysis",
    "Item Discrimination",
    "Cohort Comparison",
]
active_tab = st.sidebar.radio("Navigate", tab_names)


# Helper
def session_selector(sessions, key_prefix="", form_type_filter=None):
    filtered = sessions
    if form_type_filter:
        filtered = [s for s in sessions if s["form_type"] == form_type_filter]
    if not filtered:
        return None
    options = [s["label"] for s in filtered]
    lookup = {s["label"]: s for s in filtered}
    selected = st.selectbox(
        f"Select {'PRE' if form_type_filter == 'PRE' else 'POST' if form_type_filter == 'POST' else ''} Session",
        options, key=f"{key_prefix}_session")
    return lookup[selected]


# =============================================================================
# TAB: Dashboard Overview
# =============================================================================
if active_tab == "Dashboard Overview":
    st.title("Exam Analytics — Overview")

    active_track = track_selector(key="overview_track")

    with st.spinner("Loading data..."):
        sessions = filter_sessions_by_track(load_sessions(), active_track)
    if not sessions:
        st.info("No exam sessions found. Seed the database to get started.")
        st.stop()

    # High-level KPIs
    total_sessions = len(sessions)
    total_results = sum(s["n_results"] for s in sessions)
    courses = list(set(s["course_id"] for s in sessions))
    post_sessions = [s for s in sessions if s["form_type"] == "POST"]

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Sessions", total_sessions)
    c2.metric("Total Exam Results", total_results)
    c3.metric("Courses Assessed", len(courses))
    c4.metric("POST Sessions", len(post_sessions))

    st.markdown("---")

    # Cohort comparison — filtered to active track
    comparison = load_cohort_comparison()
    if active_track is not None:
        comparison = [c for c in comparison if c["course_id"] in active_track]
    if comparison and HAS_PLOTLY:
        col_l, col_r = st.columns(2)

        with col_l:
            st.subheader("Average Scores by Session")
            df_comp = pd.DataFrame(comparison)
            # Color by form type
            colors = [NAVY_MID if ft == "PRE" else GREEN_OK if ft == "POST" else "#999"
                      for ft in df_comp["form_type"]]
            fig = go.Figure(data=[go.Bar(
                x=[f"{r['course_id']} {r['form_type']}<br>{r['cohort_label']}" for _, r in df_comp.iterrows()],
                y=df_comp["avg_score"],
                marker_color=colors,
                text=[f"{s:.0f}%" for s in df_comp["avg_score"]],
                textposition="auto",
                error_y=dict(type="data", array=df_comp["std_dev"].tolist(), visible=True),
            )])
            fig.update_layout(height=400, xaxis_tickangle=-45, yaxis_range=[0, 105],
                              yaxis_title="Avg Score (%)")
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

        with col_r:
            st.subheader("Pass Rates (POST Sessions Only)")
            df_post = df_comp[df_comp["form_type"] == "POST"]
            if not df_post.empty:
                fig = go.Figure(data=[go.Bar(
                    x=[f"{r['course_id']}<br>{r['cohort_label']}" for _, r in df_post.iterrows()],
                    y=df_post["pass_rate"],
                    marker_color=[GREEN_OK if pr >= 80 else CAUTION_AMBER if pr >= 60 else WARNING_RED
                                  for pr in df_post["pass_rate"]],
                    text=[f"{pr:.0f}%" for pr in df_post["pass_rate"]],
                    textposition="auto",
                )])
                fig.update_layout(height=400, xaxis_tickangle=-45, yaxis_range=[0, 105],
                                  yaxis_title="Pass Rate (%)")
                fig.add_hline(y=70, line_dash="dash", line_color="red",
                              annotation_text="70% standard")
                apply_plotly_theme(fig)
                st.plotly_chart(fig, use_container_width=True)

    # Session inventory table (already filtered by track)
    st.subheader("Session Inventory")
    df_sessions = pd.DataFrame(sessions)
    st.dataframe(
        df_sessions[["course_id", "form_type", "date", "cohort_label", "n_results"]].rename(columns={
            "course_id": "Course", "form_type": "Type", "date": "Date",
            "cohort_label": "Cohort", "n_results": "Students",
        }),
        use_container_width=True, hide_index=True,
    )


# =============================================================================
# TAB: Cohort Deep-Dive
# =============================================================================
elif active_tab == "Cohort Deep-Dive":
    st.title("Cohort Deep-Dive")

    active_track = track_selector(key="cohort_track")
    sessions = filter_sessions_by_track(load_sessions(), active_track)
    selected = session_selector(sessions, "cohort")
    if not selected:
        st.info("No sessions available.")
        st.stop()

    summary = load_cohort_summary(selected["id"])
    results = load_results(selected["id"])

    if not results:
        st.info("No results for this session.")
        st.stop()

    # KPIs
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Students", summary["num_students"])
    c2.metric("Avg Score", f"{summary['avg_score']}%")
    c3.metric("Median", f"{summary['median_score']}%")
    c4.metric("Pass Rate", f"{summary['pass_rate']}%" if selected["form_type"] == "POST" else "N/A (PRE)")
    c5.metric("Range", f"{summary['min_score']}%–{summary['max_score']}%")

    st.markdown("---")

    if HAS_PLOTLY:
        col_l, col_r = st.columns(2)

        with col_l:
            # Score distribution histogram
            df = pd.DataFrame(results)
            fig = px.histogram(
                df, x="score_percent", nbins=12,
                title="Score Distribution",
                labels={"score_percent": "Score (%)"},
                color_discrete_sequence=[NAVY_MID],
            )
            if selected["form_type"] == "POST":
                fig.add_vline(x=70, line_dash="dash", line_color="red",
                              annotation_text="70% passing")
            fig.update_layout(height=350, yaxis_title="Count")
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

        with col_r:
            # Box plot
            fig = go.Figure(data=[go.Box(
                y=[r["score_percent"] for r in results],
                name=selected["cohort_label"],
                marker_color=NAVY_MID,
                boxpoints="all", jitter=0.3, pointpos=-1.5,
            )])
            fig.update_layout(title="Score Distribution (Box Plot)",
                              height=350, yaxis_title="Score (%)", yaxis_range=[0, 105])
            if selected["form_type"] == "POST":
                fig.add_hline(y=70, line_dash="dash", line_color="red")
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

    # Results table
    st.subheader("Individual Results")
    df = pd.DataFrame(results)
    st.dataframe(
        df.rename(columns={
            "trainee_id": "DODID", "total_score": "Score",
            "total_possible": "Possible", "score_percent": "Percent",
            "result": "Result",
        }),
        use_container_width=True, hide_index=True,
    )


# =============================================================================
# TAB: Gain Score Analysis
# =============================================================================
elif active_tab == "Gain Score Analysis":
    st.title("Gain Score Analysis")

    active_track = track_selector(key="gain_track")
    sessions = filter_sessions_by_track(load_sessions(), active_track)
    pre_sessions = [s for s in sessions if s["form_type"] == "PRE"]
    post_sessions = [s for s in sessions if s["form_type"] == "POST"]

    if not pre_sessions or not post_sessions:
        st.info("Need both PRE and POST sessions to compute gain scores.")
        st.stop()

    col1, col2 = st.columns(2)
    with col1:
        pre = session_selector(sessions, "gain_pre", "PRE")
    with col2:
        post = session_selector(sessions, "gain_post", "POST")

    if not pre or not post:
        st.stop()

    threshold = st.slider("Low Gain Threshold (%)", 0.0, 50.0, 10.0, 1.0)

    gains = load_gains(pre["id"], post["id"])
    q_improvement = load_question_improvement(pre["id"], post["id"])

    if not gains:
        st.warning("No matched trainees between selected sessions.")
        st.stop()

    df = pd.DataFrame(gains)

    # KPIs
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Matched Trainees", len(df))
    c2.metric("Avg Absolute Gain", f"{df['absolute_gain'].mean():.1f}%")
    c3.metric("Avg Normalized Gain", f"{df['normalized_gain'].mean():.1f}%")
    flagged = df[df["normalized_gain"] < threshold]
    c4.metric("Flagged (low gain)", len(flagged),
              delta=f"< {threshold}%", delta_color="inverse")

    st.markdown("---")

    if HAS_PLOTLY:
        col_l, col_r = st.columns(2)

        with col_l:
            # Scatter: pre vs post
            fig = px.scatter(
                df, x="pre_percent", y="post_percent",
                color="normalized_gain",
                color_continuous_scale="RdYlGn",
                title="Pre vs Post Score",
                labels={"pre_percent": "PRE Score (%)", "post_percent": "POST Score (%)"},
                hover_data=["trainee_id", "absolute_gain", "normalized_gain"],
            )
            fig.add_shape(type="line", x0=0, y0=0, x1=100, y1=100,
                          line=dict(color="gray", dash="dash"))
            if post["form_type"] == "POST":
                fig.add_hline(y=70, line_dash="dot", line_color="red",
                              annotation_text="Passing")
            fig.update_layout(height=400, xaxis_range=[0, 105], yaxis_range=[0, 105])
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

        with col_r:
            # Gain distribution
            fig = px.histogram(
                df, x="normalized_gain", nbins=15,
                title="Normalized Gain Distribution",
                labels={"normalized_gain": "Normalized Gain (%)"},
                color_discrete_sequence=[GREEN_OK],
            )
            fig.add_vline(x=threshold, line_dash="dash", line_color="red",
                          annotation_text=f"Threshold ({threshold}%)")
            fig.update_layout(height=400)
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

    # Question improvement waterfall
    if q_improvement and HAS_PLOTLY:
        st.subheader("Question-Level Improvement (PRE to POST)")
        df_qi = pd.DataFrame(q_improvement)
        colors = [GREEN_OK if imp > 0 else WARNING_RED for imp in df_qi["improvement"]]
        fig = go.Figure(data=[go.Bar(
            x=[f"Q{q}" for q in df_qi["question_number"]],
            y=df_qi["improvement"],
            marker_color=colors,
            text=[f"{imp:+.0f}%" for imp in df_qi["improvement"]],
            textposition="auto",
        )])
        fig.update_layout(height=350, xaxis_title="Question",
                          yaxis_title="Improvement (% points)",
                          title="Per-Question Improvement (sorted by impact)")
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # Tables
    st.subheader("Gain Scores")
    st.dataframe(df.rename(columns={
        "trainee_id": "DODID", "pre_percent": "PRE %",
        "post_percent": "POST %", "absolute_gain": "Absolute Gain",
        "normalized_gain": "Normalized Gain",
    }), use_container_width=True, hide_index=True)

    if not flagged.empty:
        st.subheader(f"Flagged: Normalized Gain < {threshold}%")
        st.dataframe(flagged, use_container_width=True, hide_index=True)


# =============================================================================
# TAB: Question Analysis
# =============================================================================
elif active_tab == "Question Analysis":
    st.title("Question Difficulty Analysis")

    active_track = track_selector(key="q_track")
    sessions = filter_sessions_by_track(load_sessions(), active_track)
    selected = session_selector(sessions, "q_analysis")
    if not selected:
        st.info("No sessions available.")
        st.stop()

    questions = load_questions(selected["id"])
    if not questions:
        st.info("No question data for this session.")
        st.stop()

    df = pd.DataFrame(questions)

    if HAS_PLOTLY:
        # Sorted difficulty bar chart
        df_sorted = df.sort_values("percent_correct")
        colors = [WARNING_RED if p < 50 else CAUTION_AMBER if p < 70 else GREEN_OK
                  for p in df_sorted["percent_correct"]]

        fig = go.Figure(data=[go.Bar(
            x=[f"Q{q} ({t})" for q, t in zip(df_sorted["question_number"], df_sorted["question_type"])],
            y=df_sorted["percent_correct"],
            marker_color=colors,
            text=[f"{p:.0f}%" for p in df_sorted["percent_correct"]],
            textposition="auto",
        )])
        fig.update_layout(
            title="Question Difficulty (sorted by % correct)",
            height=400, yaxis_range=[0, 105],
            xaxis_title="Question", yaxis_title="% Correct",
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # Most missed
    col_l, col_r = st.columns(2)
    with col_l:
        st.subheader("5 Hardest Questions")
        hardest = df.sort_values("percent_correct").head(5)
        for _, q in hardest.iterrows():
            st.error(f"**Q{q['question_number']}** ({q['question_type']}): "
                     f"{q['percent_correct']:.0f}% correct — avg {q['avg_points']:.1f} pts")

    with col_r:
        st.subheader("5 Easiest Questions")
        easiest = df.sort_values("percent_correct", ascending=False).head(5)
        for _, q in easiest.iterrows():
            st.success(f"**Q{q['question_number']}** ({q['question_type']}): "
                       f"{q['percent_correct']:.0f}% correct — avg {q['avg_points']:.1f} pts")

    # Full table
    with st.expander("All Questions"):
        st.dataframe(df.rename(columns={
            "question_number": "Q#", "question_type": "Type",
            "percent_correct": "% Correct", "avg_points": "Avg Pts",
            "num_responses": "Responses",
        }), use_container_width=True, hide_index=True)


# =============================================================================
# TAB: Item Discrimination
# =============================================================================
elif active_tab == "Item Discrimination":
    st.title("Item Discrimination Analysis")
    st.caption("Measures how well each question differentiates between high and low performers. "
               "High discrimination (> 0.3) = good question. Low (< 0.1) = poor question.")

    active_track = track_selector(key="disc_track")
    sessions = filter_sessions_by_track(load_sessions(), active_track)
    selected = session_selector(sessions, "disc")
    if not selected:
        st.info("No sessions available.")
        st.stop()

    disc = load_discrimination(selected["id"])
    if not disc:
        st.info("Need at least 3 results for discrimination analysis.")
        st.stop()

    df = pd.DataFrame(disc)

    # Summary KPIs
    good = len(df[df["quality"] == "GOOD"])
    acceptable = len(df[df["quality"] == "ACCEPTABLE"])
    marginal = len(df[df["quality"] == "MARGINAL"])
    poor = len(df[df["quality"] == "POOR"])

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Good (> 0.3)", good)
    c2.metric("Acceptable (0.2-0.3)", acceptable)
    c3.metric("Marginal (0.1-0.2)", marginal)
    c4.metric("Poor (< 0.1)", poor)

    st.markdown("---")

    if HAS_PLOTLY:
        # Discrimination index bar chart
        quality_colors = {
            "GOOD": GREEN_OK, "ACCEPTABLE": NAVY_MID,
            "MARGINAL": CAUTION_AMBER, "POOR": WARNING_RED,
        }
        colors = [quality_colors[q] for q in df["quality"]]

        fig = go.Figure(data=[go.Bar(
            x=[f"Q{q} ({t})" for q, t in zip(df["question_number"], df["question_type"])],
            y=df["discrimination_index"],
            marker_color=colors,
            text=[f"{d:.2f}" for d in df["discrimination_index"]],
            textposition="auto",
        )])
        fig.update_layout(
            title="Discrimination Index by Question",
            height=400,
            xaxis_title="Question", yaxis_title="Discrimination Index",
        )
        # Reference lines
        fig.add_hline(y=0.3, line_dash="dash", line_color=GREEN_OK,
                      annotation_text="Good (0.3)")
        fig.add_hline(y=0.1, line_dash="dash", line_color=WARNING_RED,
                      annotation_text="Poor (0.1)")
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # Top/Bottom group comparison
    if HAS_PLOTLY:
        st.subheader("Top vs Bottom Group Performance")
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name="Top 50%",
            x=[f"Q{q}" for q in df["question_number"]],
            y=df["top_avg"],
            marker_color=GREEN_OK,
        ))
        fig.add_trace(go.Bar(
            name="Bottom 50%",
            x=[f"Q{q}" for q in df["question_number"]],
            y=df["bottom_avg"],
            marker_color=WARNING_RED,
        ))
        fig.update_layout(
            barmode="group", height=350,
            xaxis_title="Question", yaxis_title="Avg Points",
        )
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # Problem questions callout
    poor_questions = df[df["quality"].isin(["POOR", "MARGINAL"])]
    if not poor_questions.empty:
        st.subheader("Questions Needing Review")
        for _, q in poor_questions.iterrows():
            st.warning(
                f"**Q{q['question_number']}** ({q['question_type']}): "
                f"Discrimination = {q['discrimination_index']:.3f} ({q['quality']}). "
                f"Top avg: {q['top_avg']:.1f}, Bottom avg: {q['bottom_avg']:.1f}"
            )

    # Full table
    with st.expander("Full Discrimination Table"):
        st.dataframe(df.rename(columns={
            "question_number": "Q#", "question_type": "Type",
            "discrimination_index": "Disc. Index",
            "top_avg": "Top Avg", "bottom_avg": "Bottom Avg",
            "quality": "Quality",
        }), use_container_width=True, hide_index=True)


# =============================================================================
# TAB: Cohort Comparison
# =============================================================================
elif active_tab == "Cohort Comparison":
    st.title("Cross-Cohort Comparison")

    active_track = track_selector(key="comp_track")
    sessions = filter_sessions_by_track(load_sessions(), active_track)
    courses = sorted(set(s["course_id"] for s in sessions))

    course_filter = st.selectbox("Filter by Course", ["All Courses"] + courses)
    cid = course_filter if course_filter != "All Courses" else None

    comparison = load_cohort_comparison(cid)
    if active_track is not None:
        comparison = [c for c in comparison if c["course_id"] in active_track]
    if not comparison:
        st.info("No comparison data available.")
        st.stop()

    df = pd.DataFrame(comparison)

    if HAS_PLOTLY:
        # Avg score trend
        fig = px.line(
            df, x="date", y="avg_score",
            color="course_id", symbol="form_type",
            title="Average Score Trend Over Time",
            labels={"avg_score": "Avg Score (%)", "date": "Date"},
            markers=True,
        )
        fig.update_layout(height=400, yaxis_range=[0, 105])
        fig.add_hline(y=70, line_dash="dash", line_color="red",
                      annotation_text="70% passing")
        apply_plotly_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

        # Std dev comparison — shows if cohort consistency is improving
        col_l, col_r = st.columns(2)
        with col_l:
            fig = px.bar(
                df, x="cohort_label", y="std_dev",
                color="form_type",
                title="Score Variability (Std Dev)",
                barmode="group",
            )
            fig.update_layout(height=350, xaxis_tickangle=-45)
            apply_plotly_theme(fig)
            st.plotly_chart(fig, use_container_width=True)

        with col_r:
            df_post = df[df["form_type"] == "POST"]
            if not df_post.empty:
                fig = px.bar(
                    df_post, x="cohort_label", y="pass_rate",
                    color="pass_rate",
                    color_continuous_scale="RdYlGn",
                    title="POST Session Pass Rates",
                    range_color=[0, 100],
                )
                fig.update_layout(height=350, xaxis_tickangle=-45,
                                  yaxis_range=[0, 105])
                fig.add_hline(y=70, line_dash="dash", line_color="red")
                apply_plotly_theme(fig)
                st.plotly_chart(fig, use_container_width=True)

    # Comparison table
    st.subheader("Detailed Comparison")
    st.dataframe(
        df.rename(columns={
            "course_id": "Course", "form_type": "Type",
            "cohort_label": "Cohort", "date": "Date",
            "n_students": "N", "avg_score": "Avg %",
            "median_score": "Median %", "std_dev": "Std Dev",
            "pass_rate": "Pass Rate %", "min_score": "Min %",
            "max_score": "Max %",
        }),
        use_container_width=True, hide_index=True,
    )

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="app-footer">USAREUR-AF OPERATIONAL DATA TEAM — MSS EXAM ANALYTICS</div>',
    unsafe_allow_html=True,
)
