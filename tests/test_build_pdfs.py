"""Tests for scripts/build_pdfs.py — HTML sanitizer, metadata extraction, manifest logic.

Does NOT invoke Chrome or produce actual PDFs. Tests the pure-Python helpers.
"""

import hashlib
import json
from pathlib import Path

import pytest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from build_pdfs import (
    _sanitize_html,
    extract_title,
    get_pub_meta,
    _file_hash,
    _load_manifest,
    _save_manifest,
    _should_rebuild,
)


# ---------------------------------------------------------------------------
# HTML sanitizer
# ---------------------------------------------------------------------------
class TestSanitizeHtml:
    def test_strips_script_tags(self):
        html = '<p>Hello</p><script>alert("xss")</script><p>World</p>'
        result = _sanitize_html(html)
        assert "<script" not in result
        assert "alert" not in result
        assert "<p>Hello</p>" in result
        assert "<p>World</p>" in result

    def test_strips_iframe_tags(self):
        html = '<iframe src="http://evil.com"></iframe>'
        result = _sanitize_html(html)
        assert "<iframe" not in result

    def test_strips_self_closing_script(self):
        html = '<script src="evil.js"/>'
        result = _sanitize_html(html)
        assert "<script" not in result

    def test_strips_onerror_attribute(self):
        html = '<img src="x" onerror="alert(1)">'
        result = _sanitize_html(html)
        assert "onerror" not in result

    def test_strips_onload_attribute(self):
        html = '<body onload="init()">'
        result = _sanitize_html(html)
        assert "onload" not in result

    def test_strips_javascript_uri(self):
        html = '<a href="javascript:alert(1)">click</a>'
        result = _sanitize_html(html)
        assert "javascript:" not in result
        assert 'href="#"' in result

    def test_preserves_clean_html(self):
        html = '<h1>Title</h1><p>Body text</p><table><tr><td>data</td></tr></table>'
        result = _sanitize_html(html)
        assert result == html

    def test_strips_multiline_script(self):
        html = '<script>\nvar x = 1;\nalert(x);\n</script>'
        result = _sanitize_html(html)
        assert "<script" not in result
        assert "alert" not in result


# ---------------------------------------------------------------------------
# Title extraction
# ---------------------------------------------------------------------------
class TestExtractTitle:
    def test_basic_title(self):
        md = "# My Publication\n\nBody text here."
        title, subtitle = extract_title(md)
        assert title == "My Publication"
        assert subtitle == ""

    def test_title_with_subtitle(self):
        md = "# Main Title\n## Subtitle Here\n\nBody."
        title, subtitle = extract_title(md)
        assert title == "Main Title"
        assert subtitle == "Subtitle Here"

    def test_no_title(self):
        md = "Just some text without headings."
        title, subtitle = extract_title(md)
        assert title == "PUBLICATION"
        assert subtitle == ""

    def test_stops_at_hr(self):
        md = "# Title\n---\n## This is a section, not subtitle"
        title, subtitle = extract_title(md)
        assert title == "Title"
        assert subtitle == ""

    def test_multiple_h2_takes_first(self):
        md = "# Title\n## First\n## Second"
        title, subtitle = extract_title(md)
        assert subtitle == "First"


# ---------------------------------------------------------------------------
# Publication metadata
# ---------------------------------------------------------------------------
class TestGetPubMeta:
    def test_tm_10(self):
        pub_type, pub_number = get_pub_meta("TM_10_MAVEN_USER")
        assert pub_type == "TECHNICAL MANUAL"
        assert pub_number == "SL 1"

    def test_syllabus(self):
        pub_type, pub_number = get_pub_meta("SYLLABUS_TM40G")
        assert pub_type == "COURSE SYLLABUS"
        assert pub_number == "SL 4G"

    def test_exercise(self):
        pub_type, pub_number = get_pub_meta("EX_40H")
        assert pub_type == "PRACTICAL EXERCISE"
        assert pub_number == "EX-40H"

    def test_unknown_stem(self):
        pub_type, pub_number = get_pub_meta("SOMETHING_RANDOM")
        assert pub_type == "PUBLICATION"


# ---------------------------------------------------------------------------
# Manifest helpers
# ---------------------------------------------------------------------------
class TestManifestHelpers:
    def test_file_hash_deterministic(self, tmp_path):
        f = tmp_path / "test.md"
        f.write_text("Hello, world!")
        h1 = _file_hash(f)
        h2 = _file_hash(f)
        assert h1 == h2
        expected = hashlib.sha256(b"Hello, world!").hexdigest()
        assert h1 == expected

    def test_load_manifest_empty(self, tmp_path):
        import build_pdfs
        orig = build_pdfs.MANIFEST_PATH
        build_pdfs.MANIFEST_PATH = tmp_path / "nonexistent.json"
        result = _load_manifest()
        assert result == {}
        build_pdfs.MANIFEST_PATH = orig

    def test_load_manifest_valid(self, tmp_path):
        import build_pdfs
        orig = build_pdfs.MANIFEST_PATH
        manifest_file = tmp_path / ".manifest.json"
        manifest_file.write_text(json.dumps({"file.md": "abc123"}))
        build_pdfs.MANIFEST_PATH = manifest_file
        result = _load_manifest()
        assert result == {"file.md": "abc123"}
        build_pdfs.MANIFEST_PATH = orig

    def test_should_rebuild_missing_pdf(self, tmp_path):
        import build_pdfs
        orig_out = build_pdfs.OUT_DIR
        build_pdfs.OUT_DIR = tmp_path / "pdf"
        build_pdfs.OUT_DIR.mkdir()

        src = tmp_path / "source.md"
        src.write_text("content")
        # No PDF exists → should rebuild
        assert _should_rebuild(src, "source", {}) is True
        build_pdfs.OUT_DIR = orig_out

    def test_should_rebuild_unchanged(self, tmp_path):
        import build_pdfs
        orig_out = build_pdfs.OUT_DIR
        build_pdfs.OUT_DIR = tmp_path / "pdf"
        build_pdfs.OUT_DIR.mkdir()

        src = tmp_path / "source.md"
        src.write_text("content")
        (build_pdfs.OUT_DIR / "source.pdf").write_bytes(b"%PDF")
        current_hash = _file_hash(src)
        # Hash matches → skip
        assert _should_rebuild(src, "source", {str(src): current_hash}) is False
        build_pdfs.OUT_DIR = orig_out

    def test_should_rebuild_changed(self, tmp_path):
        import build_pdfs
        orig_out = build_pdfs.OUT_DIR
        build_pdfs.OUT_DIR = tmp_path / "pdf"
        build_pdfs.OUT_DIR.mkdir()

        src = tmp_path / "source.md"
        src.write_text("content v2")
        (build_pdfs.OUT_DIR / "source.pdf").write_bytes(b"%PDF")
        # Old hash differs → rebuild
        assert _should_rebuild(src, "source", {str(src): "old_hash"}) is True
        build_pdfs.OUT_DIR = orig_out

    def test_should_rebuild_missing_source(self, tmp_path):
        src = tmp_path / "missing.md"
        assert _should_rebuild(src, "missing", {}) is False
