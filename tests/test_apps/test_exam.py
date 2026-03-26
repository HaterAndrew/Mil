"""Tests for the Exam Analytics Dashboard."""

from __future__ import annotations

import pytest


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def create_session(client, course_id="SL 4G", form_type="PRE", cohort="Test Cohort"):
    resp = client.post("/sessions", json={
        "course_id": course_id,
        "form_type": form_type,
        "administration_date": "2026-02-10",
        "cohort_label": cohort,
    })
    assert resp.status_code == 201
    return resp.json()


def build_question_scores(mc_scores: list[int], sa_scores: list[int]):
    """Build question_scores list from MC (15) and SA (5) point lists."""
    qs = []
    for i, pts in enumerate(mc_scores, start=1):
        qs.append({"question_number": i, "question_type": "MC",
                    "points_possible": 2, "points_awarded": pts})
    for i, pts in enumerate(sa_scores, start=16):
        qs.append({"question_number": i, "question_type": "SA",
                    "points_possible": 6, "points_awarded": pts})
    return qs


def record_result(client, session_id, trainee_id, mc_scores, sa_scores):
    total = sum(mc_scores) + sum(sa_scores)
    pct = round(total / 60 * 100, 1)
    qs = build_question_scores(mc_scores, sa_scores)
    resp = client.post(f"/results/{session_id}", json={
        "trainee_id": trainee_id,
        "total_score": total,
        "total_possible": 60,
        "score_percent": pct,
        "result": "DIAGNOSTIC",
        "question_scores": qs,
    })
    return resp


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
class TestHealth:
    def test_health(self, exam_client):
        resp = exam_client.get("/health")
        assert resp.status_code == 200


# ---------------------------------------------------------------------------
# Sessions
# ---------------------------------------------------------------------------
class TestSessions:
    def test_create_session(self, exam_client):
        data = create_session(exam_client)
        assert data["course_id"] == "SL 4G"
        assert data["form_type"] == "PRE"

    def test_list_sessions(self, exam_client):
        create_session(exam_client, form_type="PRE")
        create_session(exam_client, form_type="POST")
        resp = exam_client.get("/sessions")
        assert len(resp.json()) == 2

    def test_filter_by_form_type(self, exam_client):
        create_session(exam_client, form_type="PRE")
        create_session(exam_client, form_type="POST")
        resp = exam_client.get("/sessions", params={"form_type": "PRE"})
        assert len(resp.json()) == 1
        assert resp.json()[0]["form_type"] == "PRE"


# ---------------------------------------------------------------------------
# Results
# ---------------------------------------------------------------------------
class TestResults:
    def test_record_result_with_questions(self, exam_client):
        session = create_session(exam_client)
        mc = [2, 0, 2, 2, 0, 2, 2, 0, 2, 0, 2, 2, 0, 2, 2]  # 20 pts
        sa = [4, 5, 3, 6, 2]  # 20 pts
        resp = record_result(exam_client, session["id"], "TRAINEE_A", mc, sa)
        assert resp.status_code == 201
        assert resp.json()["total_score"] == 40

    def test_list_results(self, exam_client):
        session = create_session(exam_client)
        mc = [2] * 15
        sa = [6] * 5
        record_result(exam_client, session["id"], "T1", mc, sa)
        record_result(exam_client, session["id"], "T2", mc, sa)
        resp = exam_client.get(f"/results/{session['id']}")
        assert len(resp.json()) == 2


# ---------------------------------------------------------------------------
# Gain Scores
# ---------------------------------------------------------------------------
class TestGainScores:
    def test_gain_score_computation(self, exam_client):
        pre = create_session(exam_client, form_type="PRE", cohort="Pre")
        post = create_session(exam_client, form_type="POST", cohort="Post")

        # PRE: 30/60 = 50%
        mc_pre = [2, 0] * 7 + [2]  # 8 * 2 = 16
        sa_pre = [3, 3, 3, 3, 2]   # 14
        record_result(exam_client, pre["id"], "TRAINEE_X", mc_pre, sa_pre)

        # POST: 48/60 = 80%
        mc_post = [2] * 12 + [0, 0, 0]  # 24
        sa_post = [6, 4, 5, 5, 4]       # 24
        record_result(exam_client, post["id"], "TRAINEE_X", mc_post, sa_post)

        resp = exam_client.get("/gain-scores", params={
            "pre_session_id": pre["id"],
            "post_session_id": post["id"],
        })
        assert resp.status_code == 200
        gains = resp.json()
        assert len(gains) == 1
        g = gains[0]
        assert g["trainee_id"] == "TRAINEE_X"
        assert g["absolute_gain"] == pytest.approx(30.0, abs=1)
        assert g["normalized_gain"] > 0

    def test_normalized_gain_pre_100(self, exam_client):
        """Edge case: pre=100% → normalized gain should be 0."""
        pre = create_session(exam_client, form_type="PRE", cohort="Pre100")
        post = create_session(exam_client, form_type="POST", cohort="Post100")

        mc_perfect = [2] * 15
        sa_perfect = [6] * 5

        record_result(exam_client, pre["id"], "PERFECT", mc_perfect, sa_perfect)
        record_result(exam_client, post["id"], "PERFECT", mc_perfect, sa_perfect)

        resp = exam_client.get("/gain-scores", params={
            "pre_session_id": pre["id"],
            "post_session_id": post["id"],
        })
        gains = resp.json()
        assert len(gains) == 1
        assert gains[0]["normalized_gain"] == 0.0

    def test_flagged_low_gain(self, exam_client):
        pre = create_session(exam_client, form_type="PRE", cohort="PreFlag")
        post = create_session(exam_client, form_type="POST", cohort="PostFlag")

        # Trainee with high pre (55/60=91.7%) and same post → low gain
        mc = [2] * 15
        sa_high = [5, 5, 5, 5, 5]
        sa_same = [5, 5, 5, 5, 5]

        record_result(exam_client, pre["id"], "PLATEAU", mc, sa_high)
        record_result(exam_client, post["id"], "PLATEAU", mc, sa_same)

        resp = exam_client.get("/gain-scores/flagged", params={
            "pre_session_id": pre["id"],
            "post_session_id": post["id"],
            "threshold": 5.0,
        })
        flagged = resp.json()
        assert len(flagged) == 1
        assert flagged[0]["trainee_id"] == "PLATEAU"


# ---------------------------------------------------------------------------
# Question Difficulty
# ---------------------------------------------------------------------------
class TestQuestionDifficulty:
    def test_question_difficulty_ranking(self, exam_client):
        session = create_session(exam_client)

        # 2 trainees: both miss Q3, both get Q1
        mc_a = [2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        mc_b = [2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        sa = [6, 6, 6, 6, 6]

        record_result(exam_client, session["id"], "A", mc_a, sa)
        record_result(exam_client, session["id"], "B", mc_b, sa)

        resp = exam_client.get(f"/sessions/{session['id']}/questions")
        assert resp.status_code == 200
        questions = resp.json()
        assert len(questions) == 20

        # Q3 should have 0% correct (both missed)
        q3 = next(q for q in questions if q["question_number"] == 3)
        assert q3["percent_correct"] == 0.0

        # Q1 should have 100% correct
        q1 = next(q for q in questions if q["question_number"] == 1)
        assert q1["percent_correct"] == 100.0


# ---------------------------------------------------------------------------
# Cohort Summary
# ---------------------------------------------------------------------------
class TestCohortSummary:
    def test_summary_stats(self, exam_client):
        session = create_session(exam_client, form_type="POST", cohort="Summary")

        # 42/60 = 70% → PASS
        mc_pass = [2] * 15  # 30
        sa_pass = [3, 2, 3, 2, 2]  # 12; total=42
        resp = record_result(exam_client, session["id"], "PASSER", mc_pass, sa_pass)
        # Manually set result to PASS (auto-computed by upload, not by direct result endpoint)
        # The result was set to DIAGNOSTIC in our helper — let's use the summary to check counts

        summary = exam_client.get(f"/sessions/{session['id']}/summary").json()
        assert summary["num_students"] == 1
        assert summary["avg_score"] == pytest.approx(70.0, abs=1)


# ---------------------------------------------------------------------------
# CSV Upload
# ---------------------------------------------------------------------------
class TestCSVUpload:
    def test_upload_results_csv(self, exam_client):
        session = create_session(exam_client, form_type="POST", cohort="CSV Upload")
        csv_content = (
            "trainee_id,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20\n"
            "T1,2,2,0,2,2,2,0,2,2,2,2,0,2,2,2,4,5,3,6,2\n"
            "T2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,6,6,6,6\n"
        )
        resp = exam_client.post(
            f"/upload/results/{session['id']}",
            files={"file": ("results.csv", csv_content.encode(), "text/csv")},
        )
        assert resp.status_code == 200
        data = resp.json()
        assert data["accepted"] == 2
        assert data["rejected"] == 0

        # Verify T2 got PASS (60/60 = 100%)
        results = exam_client.get(f"/results/{session['id']}").json()
        t2 = next(r for r in results if r["trainee_id"] == "T2")
        assert t2["result"] == "PASS"
        assert t2["total_score"] == 60

    def test_upload_invalid_mc_score(self, exam_client):
        session = create_session(exam_client, form_type="POST", cohort="Bad CSV")
        csv_content = (
            "trainee_id,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20\n"
            "BAD,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,6,6,6,6\n"  # q1=1 is invalid for MC
        )
        resp = exam_client.post(
            f"/upload/results/{session['id']}",
            files={"file": ("bad.csv", csv_content.encode(), "text/csv")},
        )
        assert resp.status_code == 200
        assert resp.json()["rejected"] == 1
