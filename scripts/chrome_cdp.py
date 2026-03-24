"""
chrome_cdp.py — Chrome DevTools Protocol (CDP) utilities for headless PDF generation.

Provides html_file_to_pdf(), which launches a Chrome subprocess, navigates to
a local HTML file, and uses Page.printToPDF via CDP to produce a PDF.

Separated from build_pdfs.py so the PDF build logic and CSS can be maintained
independently of the CDP plumbing.
"""

import base64
import json
import os
import socket
import subprocess
import time
import urllib.request
from pathlib import Path

# Maximum decoded PDF size (100 MB). Base64 encodes ~33% overhead,
# so the encoded string limit is ~133 MB.
_MAX_PDF_BYTES = 100 * 1024 * 1024

import websocket


def _free_port() -> int:
    """Return an available TCP port on localhost."""
    with socket.socket() as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def _wait_for_browser_ws(port: int, retries: int = 20) -> str:
    """Return the browser-level WebSocket URL from /json/version."""
    last_err = None
    for attempt in range(1, retries + 1):
        try:
            data = json.loads(
                urllib.request.urlopen(
                    f"http://localhost:{port}/json/version", timeout=2
                ).read()
            )
            return data["webSocketDebuggerUrl"]
        except Exception as exc:
            last_err = exc
            time.sleep(0.4)
    raise RuntimeError(
        f"Chrome CDP not ready on port {port} after {retries} attempts: {last_err}"
    )


def _send(ws, method: str, params: dict = None, cmd_id: int = 1,
          session_id: str = None, timeout: int = 90) -> dict:
    """Send a CDP command and wait for its matching response (skipping events)."""
    msg = {"id": cmd_id, "method": method, "params": params or {}}
    if session_id:
        msg["sessionId"] = session_id
    ws.send(json.dumps(msg))
    deadline = time.time() + timeout
    while time.time() < deadline:
        raw = ws.recv()
        resp = json.loads(raw)
        if resp.get("id") == cmd_id and resp.get("sessionId", session_id) == session_id:
            if "error" in resp:
                raise RuntimeError(f"CDP error in {method}: {resp['error']}")
            return resp.get("result", {})
    raise TimeoutError(f"CDP timeout waiting for {method}")


def html_file_to_pdf(
    html_path: Path,
    pdf_path: Path,
    header_html: str,
    footer_html: str,
    chrome_binary: str,
    pdf_params: dict = None,
) -> bool:
    """
    Convert a local HTML file to a PDF using Chrome headless CDP.

    Args:
        html_path:      Path to the input HTML file.
        pdf_path:       Destination path for the output PDF.
        header_html:    CDP header template HTML string (rendered in top margin).
        footer_html:    CDP footer template HTML string (rendered in bottom margin).
        chrome_binary:  Path or name of the Chrome/Chromium executable.

    Returns:
        True on success, False on any error (error is printed to stdout).
    """
    port = _free_port()
    chrome_args = [
        chrome_binary,
        f"--remote-debugging-port={port}",
        "--headless=new",
        "--disable-gpu",
        "--disable-dev-shm-usage",
        "--disable-extensions",
        "--remote-allow-origins=*",
        f"--user-data-dir=/tmp/chrome-pdf-{port}",
    ]
    # Only disable the Chrome sandbox when running in containerized environments
    # (Docker, CI runners) where the kernel sandbox is unavailable.
    # Set CHROME_NO_SANDBOX=1 to enable this flag; default is sandboxed.
    if os.environ.get("CHROME_NO_SANDBOX") == "1":
        chrome_args.append("--no-sandbox")
    proc = subprocess.Popen(
        chrome_args,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        browser_ws = _wait_for_browser_ws(port)
        ws = websocket.create_connection(browser_ws, timeout=30)
        try:
            # Create a new page target
            r = _send(ws, "Target.createTarget", {"url": "about:blank"}, cmd_id=1)
            target_id = r["targetId"]

            # Attach to it with flat session protocol
            r = _send(ws, "Target.attachToTarget",
                      {"targetId": target_id, "flatten": True}, cmd_id=2)
            sid = r["sessionId"]

            # Enable Page domain on the session
            _send(ws, "Page.enable", cmd_id=3, session_id=sid)

            # Navigate to the HTML file
            _send(ws, "Page.navigate",
                  {"url": f"file://{html_path.resolve()}"},
                  cmd_id=4, session_id=sid)

            # Poll readyState until complete
            for _ in range(40):
                r = _send(ws, "Runtime.evaluate",
                          {"expression": "document.readyState", "returnByValue": True},
                          cmd_id=5, session_id=sid)
                if r.get("result", {}).get("value") == "complete":
                    break
                time.sleep(0.4)
            time.sleep(0.5)  # let JS post-processing run

            defaults = {
                "landscape":           False,
                "displayHeaderFooter": True,
                "headerTemplate":      header_html,
                "footerTemplate":      footer_html,
                "printBackground":     True,
                "scale":               1.0,
                "paperWidth":          8.5,
                "paperHeight":         11.0,
                "marginTop":           0.72,
                "marginBottom":        0.58,
                "marginLeft":          0.85,
                "marginRight":         0.85,
                "transferMode":        "ReturnAsBase64",
            }
            if pdf_params:
                _ALLOWED_PDF_KEYS = {
                    "landscape", "displayHeaderFooter", "headerTemplate",
                    "footerTemplate", "printBackground", "scale", "paperWidth",
                    "paperHeight", "marginTop", "marginBottom", "marginLeft",
                    "marginRight", "pageRanges", "preferCSSPageSize",
                    "transferMode",
                }
                bad_keys = set(pdf_params) - _ALLOWED_PDF_KEYS
                if bad_keys:
                    raise ValueError(f"Unsupported PDF params: {bad_keys}")
                defaults.update(pdf_params)
            result = _send(
                ws,
                "Page.printToPDF",
                defaults,
                cmd_id=6, session_id=sid, timeout=120,
            )
        finally:
            ws.close()

        b64_data = result["data"]
        # Estimate decoded size: base64 inflates by ~4/3, so decoded ≈ len * 3/4
        estimated_size = len(b64_data) * 3 // 4
        if estimated_size > _MAX_PDF_BYTES:
            raise ValueError(
                f"PDF data too large ({estimated_size / (1024*1024):.1f} MB); "
                f"limit is {_MAX_PDF_BYTES / (1024*1024):.0f} MB"
            )
        pdf_path.write_bytes(base64.b64decode(b64_data))
        return True
    except Exception as exc:
        import traceback
        print(f"      ERROR: {exc}")
        traceback.print_exc()
        return False
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()
