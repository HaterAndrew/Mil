"""Tests for the Data Quality Monitor."""

from __future__ import annotations


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
PIPELINE_PAYLOAD = {
    "name": "SITREP Ingest",
    "description": "Daily SITREP ingest from upstream",
    "owner": "MAJ SMITH",
    "schedule": "daily 0600Z",
    "source_system": "GCSS-Army",
    "target_system": "OPDATA Warehouse",
}


def create_pipeline(client, **overrides):
    payload = {**PIPELINE_PAYLOAD, **overrides}
    resp = client.post("/pipelines", json=payload)
    assert resp.status_code == 201
    return resp.json()


# ---------------------------------------------------------------------------
# Pipeline CRUD
# ---------------------------------------------------------------------------
class TestPipelines:
    def test_create_pipeline(self, dq_client):
        data = create_pipeline(dq_client)
        assert data["name"] == "SITREP Ingest"
        assert data["status"] == "UNKNOWN"

    def test_duplicate_pipeline(self, dq_client):
        create_pipeline(dq_client)
        resp = dq_client.post("/pipelines", json=PIPELINE_PAYLOAD)
        assert resp.status_code == 409

    def test_list_pipelines(self, dq_client):
        create_pipeline(dq_client, name="Pipeline A")
        create_pipeline(dq_client, name="Pipeline B")
        resp = dq_client.get("/pipelines")
        assert resp.status_code == 200
        assert len(resp.json()) == 2

    def test_get_pipeline(self, dq_client):
        data = create_pipeline(dq_client)
        resp = dq_client.get(f"/pipelines/{data['id']}")
        assert resp.status_code == 200
        assert resp.json()["name"] == "SITREP Ingest"

    def test_get_pipeline_404(self, dq_client):
        resp = dq_client.get("/pipelines/999")
        assert resp.status_code == 404

    def test_update_pipeline(self, dq_client):
        data = create_pipeline(dq_client)
        updated = {**PIPELINE_PAYLOAD, "description": "Updated description"}
        resp = dq_client.put(f"/pipelines/{data['id']}", json=updated)
        assert resp.status_code == 200
        assert resp.json()["description"] == "Updated description"

    def test_delete_pipeline(self, dq_client):
        data = create_pipeline(dq_client)
        resp = dq_client.delete(f"/pipelines/{data['id']}")
        assert resp.status_code == 204
        resp = dq_client.get(f"/pipelines/{data['id']}")
        assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------
class TestMetrics:
    def test_record_metric_pass(self, dq_client):
        pipe = create_pipeline(dq_client)
        resp = dq_client.post("/metrics", json={
            "pipeline_id": pipe["id"],
            "metric_type": "COMPLETENESS",
            "value": 99.5,
            "threshold": 95.0,
        })
        assert resp.status_code == 201
        assert resp.json()["status"] == "PASS"

    def test_record_metric_fail_creates_alert(self, dq_client):
        pipe = create_pipeline(dq_client)
        dq_client.post("/metrics", json={
            "pipeline_id": pipe["id"],
            "metric_type": "COMPLETENESS",
            "value": 80.0,
            "threshold": 95.0,
        })
        # A FAIL metric should auto-create an alert
        resp = dq_client.get("/alerts")
        assert resp.status_code == 200
        alerts = resp.json()
        assert len(alerts) >= 1
        assert alerts[0]["severity"] == "CRITICAL"

    def test_get_metrics_trend(self, dq_client):
        pipe = create_pipeline(dq_client)
        dq_client.post("/metrics", json={
            "pipeline_id": pipe["id"],
            "metric_type": "FRESHNESS",
            "value": 10.0,
            "threshold": 60.0,
        })
        resp = dq_client.get(f"/metrics/{pipe['id']}", params={"type": "FRESHNESS"})
        assert resp.status_code == 200
        assert len(resp.json()) >= 1

    def test_get_metrics_pipeline_404(self, dq_client):
        resp = dq_client.get("/metrics/999")
        assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------
class TestHealth:
    def test_health_empty(self, dq_client):
        resp = dq_client.get("/health")
        assert resp.status_code == 200
        assert isinstance(resp.json(), list)

    def test_pipeline_health(self, dq_client):
        pipe = create_pipeline(dq_client)
        dq_client.post("/metrics", json={
            "pipeline_id": pipe["id"],
            "metric_type": "COMPLETENESS",
            "value": 99.0,
            "threshold": 95.0,
        })
        resp = dq_client.get(f"/health/{pipe['id']}")
        assert resp.status_code == 200
        assert resp.json()["pipeline_id"] == pipe["id"]

    def test_pipeline_health_404(self, dq_client):
        resp = dq_client.get("/health/999")
        assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Alerts
# ---------------------------------------------------------------------------
class TestAlerts:
    def test_acknowledge_alert(self, dq_client):
        pipe = create_pipeline(dq_client)
        # Create a FAIL metric to trigger an alert
        dq_client.post("/metrics", json={
            "pipeline_id": pipe["id"],
            "metric_type": "ACCURACY",
            "value": 50.0,
            "threshold": 95.0,
        })
        alerts = dq_client.get("/alerts").json()
        assert len(alerts) >= 1
        alert_id = alerts[0]["id"]

        resp = dq_client.post(f"/alerts/{alert_id}/ack", params={"ack_by": "SGT DOE"})
        assert resp.status_code == 200
        assert resp.json()["acknowledged"] is True

        # After ack, active alerts list should be empty
        resp = dq_client.get("/alerts")
        assert len(resp.json()) == 0

    def test_ack_alert_404(self, dq_client):
        resp = dq_client.post("/alerts/9999/ack")
        assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Dashboard stats
# ---------------------------------------------------------------------------
class TestDashboard:
    def test_dashboard_stats_empty(self, dq_client):
        resp = dq_client.get("/dashboard-stats")
        assert resp.status_code == 200
        data = resp.json()
        assert data["total_pipelines"] == 0
        assert data["health_pct"] == 0.0

    def test_dashboard_stats_with_data(self, dq_client):
        create_pipeline(dq_client, name="P1")
        create_pipeline(dq_client, name="P2")
        resp = dq_client.get("/dashboard-stats")
        data = resp.json()
        assert data["total_pipelines"] == 2
