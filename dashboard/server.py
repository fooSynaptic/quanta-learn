#!/usr/bin/env python3
"""Local dashboard: reading kanban, problems, solved list. Binds 127.0.0.1 only."""

from __future__ import annotations

import json
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
STATIC = Path(__file__).resolve().parent / "static"
DATA_JSON = Path(__file__).resolve().parent / "data.json"

if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from _catalog_utils import CATALOG_DIR, load_yaml, save_yaml, today  # noqa: E402

READING_PATH = CATALOG_DIR / "reading-list.yaml"
PROBLEM_PATH = CATALOG_DIR / "problem-list.yaml"
SOLVED_PATH = CATALOG_DIR / "solved-list.yaml"
PORT = 8765


def refresh_data() -> None:
    subprocess.run(
        [sys.executable, str(SCRIPTS / "build_dashboard_stats.py")],
        cwd=ROOT,
        check=True,
    )


def update_item_status(catalog: Path, item_id: str, status: str) -> bool:
    items = load_yaml(catalog)
    for item in items:
        if item.get("id") == item_id:
            item["status"] = status
            item["updated_at"] = today()
            save_yaml(catalog, items)
            return True
    return False


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args: Any) -> None:
        print(f"[dashboard] {self.address_string()} - {fmt % args}")

    def _send_json(self, code: int, obj: Any) -> None:
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, path: Path, content_type: str) -> None:
        if not path.is_file():
            self.send_error(404)
            return
        data = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path in ("/", "/index.html"):
            return self._send_file(STATIC / "index.html", "text/html; charset=utf-8")
        if path.startswith("/static/"):
            rel = path[len("/static/") :]
            return self._send_file(STATIC / rel, self._guess_type(rel))
        if path == "/api/data":
            if not DATA_JSON.is_file():
                refresh_data()
            return self._send_json(200, json.loads(DATA_JSON.read_text(encoding="utf-8")))
        if path.startswith("/api/reading/") and path.endswith("/detail"):
            item_id = path.split("/")[3]
            for item in load_yaml(READING_PATH):
                if item.get("id") == item_id:
                    return self._send_json(200, item)
            return self._send_json(404, {"error": "not found"})
        if path.startswith("/api/solved/") and path.endswith("/detail"):
            item_id = path.split("/")[3]
            for item in load_yaml(SOLVED_PATH):
                if item.get("id") == item_id:
                    return self._send_json(200, item)
            return self._send_json(404, {"error": "not found"})
        if path.startswith("/api/problem/") and path.endswith("/detail"):
            item_id = path.split("/")[3]
            for item in load_yaml(PROBLEM_PATH):
                if item.get("id") == item_id:
                    return self._send_json(200, item)
            return self._send_json(404, {"error": "not found"})
        self.send_error(404)

    def do_PATCH(self) -> None:
        path = urlparse(self.path).path
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length) if length else b"{}"
        try:
            payload = json.loads(body.decode("utf-8"))
        except json.JSONDecodeError:
            return self._send_json(400, {"error": "invalid json"})

        status = payload.get("status")
        if not status:
            return self._send_json(400, {"error": "status required"})

        if path.startswith("/api/reading/") and path.endswith("/status"):
            item_id = path.split("/")[3]
            if update_item_status(READING_PATH, item_id, status):
                refresh_data()
                return self._send_json(200, {"ok": True, "id": item_id, "status": status})
            return self._send_json(404, {"error": "not found"})

        if path.startswith("/api/problem/") and path.endswith("/status"):
            item_id = path.split("/")[3]
            if update_item_status(PROBLEM_PATH, item_id, status):
                refresh_data()
                return self._send_json(200, {"ok": True, "id": item_id, "status": status})
            return self._send_json(404, {"error": "not found"})

        self.send_error(404)

    @staticmethod
    def _guess_type(name: str) -> str:
        if name.endswith(".css"):
            return "text/css; charset=utf-8"
        if name.endswith(".js"):
            return "application/javascript; charset=utf-8"
        return "application/octet-stream"


def main() -> None:
    refresh_data()
    host = "127.0.0.1"
    server = ThreadingHTTPServer((host, PORT), Handler)
    print(f"Quanta Learn Dashboard: http://{host}:{PORT}/")
    print("Ctrl+C to stop")
    server.serve_forever()


if __name__ == "__main__":
    main()
