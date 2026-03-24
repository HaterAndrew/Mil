"""
Dashboard Launcher Service — starts Streamlit apps on demand and
serves the MSS Training Hub.

Run:  python apps/launcher.py
      Double-click "MSS Training Hub" desktop shortcut

Opens http://localhost:8400 in the default browser.
Dashboard clicks auto-start the corresponding Streamlit app.
"""

import hmac
import subprocess
import socket
import sys
import os
import signal
import json
import webbrowser
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import unquote

PORT = 8400
ROOT = Path(__file__).resolve().parent.parent  # repo root
HUB_DIR = ROOT / "maven_training" / "mss_info_app"

# App registry: dashboard_port -> config
APPS = {
    8501: {"name": "readiness_tracker",   "api_port": 8001},
    8502: {"name": "exam_analytics",      "api_port": 8002},
    8503: {"name": "aar_aggregator",      "api_port": 8003},
    8504: {"name": "progress_tracker",    "api_port": 8004},
    8505: {"name": "mtt_scheduler",       "api_port": 8005},
    8506: {"name": "xref_validator",      "api_port": 8006},
    8507: {"name": "glossary_search",     "api_port": 8007},
    8508: {"name": "offline_packager",    "api_port": 8008},
    8509: {"name": "sharepoint_sync",     "api_port": 8009},
    8510: {"name": "data_quality",        "api_port": 8010},
    8511: {"name": "instructor_manager",  "api_port": 8011},
    8512: {"name": "enrollment_manager",  "api_port": 8012},
    8513: {"name": "curriculum_tracker",  "api_port": 8013},
    8514: {"name": "lessons_learned",     "api_port": 8014},
    8515: {"name": "training_metrics",    "api_port": 8015},
}

# Track running processes: port -> subprocess.Popen
running = {}


def port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("localhost", port)) == 0


def start_app(dashboard_port: int) -> dict:
    if dashboard_port not in APPS:
        return {"ok": False, "error": f"Unknown port {dashboard_port}"}

    cfg = APPS[dashboard_port]
    name = cfg["name"]
    api_port = cfg["api_port"]
    results = []

    # Start API server if not already running
    if not port_in_use(api_port):
        api_module = f"apps.{name}.api:app"
        api_proc = subprocess.Popen(
            [sys.executable, "-m", "uvicorn", api_module,
             "--port", str(api_port), "--host", "127.0.0.1"],
            cwd=str(ROOT),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        running[api_port] = api_proc
        results.append(f"API started on :{api_port}")
    else:
        results.append(f"API already running on :{api_port}")

    # Start Streamlit dashboard if not already running
    if not port_in_use(dashboard_port):
        dash_path = f"apps/{name}/dashboard.py"
        dash_proc = subprocess.Popen(
            [sys.executable, "-m", "streamlit", "run", dash_path,
             "--server.port", str(dashboard_port),
             "--server.headless", "true",
             "--server.address", "127.0.0.1"],
            cwd=str(ROOT),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        running[dashboard_port] = dash_proc
        results.append(f"Dashboard started on :{dashboard_port}")
    else:
        results.append(f"Dashboard already running on :{dashboard_port}")

    return {"ok": True, "name": name, "port": dashboard_port, "details": results}


def stop_all():
    for port, proc in running.items():
        proc.terminate()
    running.clear()


class LauncherHandler(BaseHTTPRequestHandler):
    # Allowed CORS origins — launcher and all dashboard ports
    _ALLOWED_ORIGINS = {
        f"http://localhost:{p}" for p in [PORT] | set(APPS.keys())
    } | {
        f"http://127.0.0.1:{p}" for p in [PORT] | set(APPS.keys())
    }

    def _cors(self):
        origin = self.headers.get("Origin", "")
        if origin in self._ALLOWED_ORIGINS:
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def _json_response(self, code, data):
        body = json.dumps(data).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self._cors()
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def _serve_file(self, file_path):
        """Serve a static file from HUB_DIR."""
        if not file_path.is_file():
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")
            return
        content_type, _ = mimetypes.guess_type(str(file_path))
        content_type = content_type or "application/octet-stream"
        data = file_path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self._cors()
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == "/status":
            status = {}
            for port, cfg in APPS.items():
                status[str(port)] = {
                    "name": cfg["name"],
                    "dashboard": port_in_use(port),
                    "api": port_in_use(cfg["api_port"]),
                }
            self._json_response(200, {"ok": True, "apps": status})
        elif self.path == "/health":
            self._json_response(200, {"ok": True})
        elif self.path in ("/", "/index.html"):
            self._serve_file(HUB_DIR / "index.html")
        elif self.path.startswith("/"):
            # Serve static assets from HUB_DIR (images, css, js, etc.)
            safe_path = unquote(self.path.lstrip("/"))
            if ".." not in safe_path:
                full_path = HUB_DIR / safe_path
                resolved = full_path.resolve()
                if not resolved.is_relative_to(HUB_DIR.resolve()):
                    self.send_error(403, "Forbidden")
                    return
                self._serve_file(full_path)
            else:
                self._json_response(403, {"ok": False, "error": "Forbidden"})

    def do_POST(self):
        if self.path == "/start":
            length = int(self.headers.get("Content-Length", 0))
            if length > 1048576:  # 1 MB limit
                self._json_response(413, {"ok": False, "error": "Request body too large. Maximum size is 1 MB."})
                return
            body = self.rfile.read(length) if length else b"{}"
            try:
                data = json.loads(body)
            except json.JSONDecodeError:
                self._json_response(400, {"ok": False, "error": "Invalid JSON"})
                return
            port = data.get("port")
            if not isinstance(port, int):
                self._json_response(400, {"ok": False, "error": "Missing 'port' (int)"})
                return
            result = start_app(port)
            self._json_response(200 if result["ok"] else 400, result)
        elif self.path == "/stop-all":
            api_key = os.environ.get("API_KEY", "")
            provided = self.headers.get("X-API-Key", "")
            if api_key and not hmac.compare_digest(provided, api_key):
                self._json_response(401, {"ok": False, "error": "Unauthorized"})
                return
            stop_all()
            self._json_response(200, {"ok": True, "message": "All apps stopped"})
        else:
            self._json_response(404, {"ok": False, "error": "Not found"})

    def log_message(self, format, *args):
        print(f"[launcher] {args[0]}")


def main():
    if port_in_use(PORT):
        # Already running — just open the browser
        print(f"[launcher] Already running on port {PORT} — opening browser.")
        webbrowser.open(f"http://localhost:{PORT}")
        sys.exit(0)

    server = HTTPServer(("127.0.0.1", PORT), LauncherHandler)
    url = f"http://localhost:{PORT}"
    print(f"[launcher] Dashboard Launcher running on {url}")
    print(f"[launcher] {len(APPS)} apps registered (ports 8501-8515)")
    print(f"[launcher] Serving Training Hub from {HUB_DIR}")
    print(f"[launcher] Ctrl+C to stop")
    webbrowser.open(url)

    def shutdown(sig, frame):
        print("\n[launcher] Shutting down...")
        stop_all()
        server.server_close()
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        shutdown(None, None)


if __name__ == "__main__":
    main()
