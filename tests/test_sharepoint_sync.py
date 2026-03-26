"""Tests for scripts/check_sharepoint_sync.py."""

from pathlib import Path
from unittest.mock import patch

import pytest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import check_sharepoint_sync as sp_sync


class TestDiffFiles:
    def test_identical_files(self, tmp_path):
        a = tmp_path / "a.html"
        b = tmp_path / "b.html"
        content = "<html><head></head><body><h1>Title</h1></body></html>"
        a.write_text(content)
        b.write_text(content)
        expected, unexpected = sp_sync.diff_files(a, b)
        assert len(expected) == 0
        assert len(unexpected) == 0

    def test_csp_only_difference(self, tmp_path):
        a = tmp_path / "a.html"
        b = tmp_path / "b.html"
        a.write_text(
            '<html><head>\n'
            '<meta http-equiv="Content-Security-Policy" content="default-src \'self\'; frame-src \'self\' http://localhost:*">\n'
            '</head><body>Same</body></html>'
        )
        b.write_text(
            '<html><head>\n'
            '<meta http-equiv="Content-Security-Policy" content="default-src \'self\' https://sharepoint-mil.us; frame-src \'self\' https://sharepoint-mil.us">\n'
            '</head><body>Same</body></html>'
        )
        expected, unexpected = sp_sync.diff_files(a, b)
        assert len(expected) == 1
        assert len(unexpected) == 0

    def test_content_divergence(self, tmp_path):
        a = tmp_path / "a.html"
        b = tmp_path / "b.html"
        a.write_text("<html><body><h1>Title A</h1></body></html>")
        b.write_text("<html><body><h1>Title B</h1></body></html>")
        expected, unexpected = sp_sync.diff_files(a, b)
        assert len(unexpected) >= 1

    def test_line_count_difference(self, tmp_path):
        a = tmp_path / "a.html"
        b = tmp_path / "b.html"
        a.write_text("<html>\n<body>\n</body>\n</html>")
        b.write_text("<html>\n<body>\n<p>Extra</p>\n</body>\n</html>")
        expected, unexpected = sp_sync.diff_files(a, b)
        assert any("Line count" in d for d in unexpected)

    def test_whitespace_normalized(self, tmp_path):
        a = tmp_path / "a.html"
        b = tmp_path / "b.html"
        a.write_text("<div>  Hello   World  </div>")
        b.write_text("<div> Hello  World </div>")
        expected, unexpected = sp_sync.diff_files(a, b)
        assert len(unexpected) == 0


class TestNormalize:
    def test_collapses_whitespace(self):
        assert sp_sync._normalize("  hello   world  ") == "hello world"

    def test_strips_trailing(self):
        assert sp_sync._normalize("text  \n") == "text"
