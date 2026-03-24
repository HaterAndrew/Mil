"""
Tests for build/audit scripts — sanitization, validation, error handling,
and manifest logic.

Covers:
  - build_pdfs._sanitize_html()
  - build_pdfs._should_rebuild()
  - rewrite_sharepoint_links URL validation (via subprocess)
  - audit.scan_text() error handling
"""

import os
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

# Allow imports from scripts/
SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))


# ══════════════════════════════════════════════════════════════════════════════
# build_pdfs._sanitize_html
# ══════════════════════════════════════════════════════════════════════════════

class TestSanitizeHtml:
    """Tests for the _sanitize_html() function in build_pdfs.py."""

    @pytest.fixture(autouse=True)
    def _import(self):
        from build_pdfs import _sanitize_html
        self.sanitize = _sanitize_html

    # -- Dangerous content stripped --

    def test_strips_script_tag(self):
        html = '<p>Hello</p><script>alert("xss")</script><p>World</p>'
        result = self.sanitize(html)
        assert "<script" not in result.lower()
        assert "alert" not in result
        assert "<p>Hello</p>" in result
        assert "<p>World</p>" in result

    def test_strips_script_self_closing(self):
        result = self.sanitize('<div><script src="evil.js"/></div>')
        assert "<script" not in result.lower()

    def test_strips_script_multiline(self):
        html = textwrap.dedent("""\
            <p>Before</p>
            <script>
              var x = 1;
              document.write(x);
            </script>
            <p>After</p>""")
        result = self.sanitize(html)
        assert "<script" not in result.lower()
        assert "document.write" not in result

    def test_strips_iframe_tag(self):
        html = '<iframe src="https://evil.example.com"></iframe>'
        result = self.sanitize(html)
        assert "<iframe" not in result.lower()

    def test_strips_iframe_self_closing(self):
        result = self.sanitize('<iframe src="https://evil.example.com"/>')
        assert "<iframe" not in result.lower()

    def test_strips_onerror_attribute(self):
        html = '<img src="x.png" onerror="alert(1)" alt="photo">'
        result = self.sanitize(html)
        assert "onerror" not in result.lower()
        assert 'src="x.png"' in result

    def test_strips_onload_attribute(self):
        html = '<body onload="init()">'
        result = self.sanitize(html)
        assert "onload" not in result.lower()

    def test_strips_javascript_uri_double_quotes(self):
        html = '<a href="javascript:alert(1)">Click</a>'
        result = self.sanitize(html)
        assert "javascript:" not in result.lower()
        assert 'href="#"' in result

    def test_strips_javascript_uri_single_quotes(self):
        html = "<a href='javascript:void(0)'>Link</a>"
        result = self.sanitize(html)
        assert "javascript:" not in result.lower()

    # -- Valid HTML preserved --

    def test_preserves_paragraph(self):
        html = "<p>This is a paragraph.</p>"
        assert self.sanitize(html) == html

    def test_preserves_heading(self):
        html = "<h2>Section Title</h2>"
        assert self.sanitize(html) == html

    def test_preserves_https_link(self):
        html = '<a href="https://example.com">Link</a>'
        assert self.sanitize(html) == html

    def test_preserves_complex_valid_html(self):
        html = textwrap.dedent("""\
            <h1>Title</h1>
            <p>Paragraph with <strong>bold</strong> and <em>italic</em>.</p>
            <ul><li>Item 1</li><li>Item 2</li></ul>
            <a href="https://army.mil/doc.pdf">Download</a>""")
        assert self.sanitize(html) == html

    def test_preserves_empty_string(self):
        assert self.sanitize("") == ""

    # -- Case insensitivity --

    def test_strips_script_uppercase(self):
        result = self.sanitize('<SCRIPT>alert(1)</SCRIPT>')
        assert "<script" not in result.lower()

    def test_strips_mixed_case_iframe(self):
        result = self.sanitize('<IFrame src="x"></IFrame>')
        assert "<iframe" not in result.lower()


# ══════════════════════════════════════════════════════════════════════════════
# build_pdfs._should_rebuild
# ══════════════════════════════════════════════════════════════════════════════

class TestShouldRebuild:
    """Tests for the manifest hash comparison logic in _should_rebuild()."""

    @pytest.fixture(autouse=True)
    def _setup(self, tmp_path, monkeypatch):
        import build_pdfs
        self.tmp = tmp_path
        # Point OUT_DIR to tmp so _should_rebuild checks PDFs there
        monkeypatch.setattr(build_pdfs, "OUT_DIR", tmp_path / "pdf")
        (tmp_path / "pdf").mkdir()
        self._should_rebuild = build_pdfs._should_rebuild
        self._file_hash = build_pdfs._file_hash

    def _write(self, path: Path, content: str = "hello"):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        return path

    def test_missing_source_returns_false(self):
        """If source file does not exist, skip (do not rebuild)."""
        src = self.tmp / "missing.md"
        assert self._should_rebuild(src, "missing", {}) is False

    def test_missing_pdf_returns_true(self):
        """If PDF output does not exist, always rebuild."""
        src = self._write(self.tmp / "source.md")
        assert self._should_rebuild(src, "source", {}) is True

    def test_unchanged_hash_returns_false(self):
        """If manifest hash matches current hash, no rebuild needed."""
        src = self._write(self.tmp / "source.md", "content-v1")
        self._write(self.tmp / "pdf" / "source.pdf", "fake pdf")
        manifest = {str(src): self._file_hash(src)}
        assert self._should_rebuild(src, "source", manifest) is False

    def test_changed_hash_returns_true(self):
        """If source has changed since manifest was written, rebuild."""
        src = self._write(self.tmp / "source.md", "content-v1")
        self._write(self.tmp / "pdf" / "source.pdf", "fake pdf")
        old_hash = self._file_hash(src)
        manifest = {str(src): old_hash}
        # Modify the source
        src.write_text("content-v2")
        assert self._should_rebuild(src, "source", manifest) is True

    def test_empty_manifest_triggers_rebuild(self):
        """Empty manifest means no prior build info — should rebuild."""
        src = self._write(self.tmp / "source.md")
        self._write(self.tmp / "pdf" / "source.pdf", "fake pdf")
        assert self._should_rebuild(src, "source", {}) is True


# ══════════════════════════════════════════════════════════════════════════════
# rewrite_sharepoint_links URL validation (subprocess)
# ══════════════════════════════════════════════════════════════════════════════

REWRITE_SCRIPT = SCRIPTS_DIR / "rewrite_sharepoint_links.py"


class TestSharepointUrlValidation:
    """URL validation in rewrite_sharepoint_links.py — tested via subprocess."""

    def _run(self, url: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(REWRITE_SCRIPT), url],
            capture_output=True, text=True,
        )

    def test_https_url_accepted(self, tmp_path, monkeypatch):
        """Valid https:// URL should not produce a scheme error."""
        # The script reads index.html — create a minimal one so it doesn't
        # error on file-not-found before reaching validation.
        monkeypatch.chdir(tmp_path)
        index_dir = tmp_path / "maven_training" / "mss_info_app"
        index_dir.mkdir(parents=True)
        (index_dir / "index.html").write_text('<a href="../pdf/TEST.pdf">link</a>')
        result = self._run("https://army.sharepoint.mil/docs")
        # Should succeed (exit 0) — not fail on scheme validation
        assert result.returncode == 0
        assert "ERROR" not in result.stdout

    def test_javascript_scheme_rejected(self):
        result = self._run("javascript:alert(1)")
        assert result.returncode != 0
        assert "ERROR" in result.stdout

    def test_data_scheme_rejected(self):
        result = self._run("data:text/html,<h1>hi</h1>")
        assert result.returncode != 0
        assert "ERROR" in result.stdout

    def test_http_scheme_rejected(self):
        result = self._run("http://example.com/docs")
        assert result.returncode != 0
        assert "ERROR" in result.stdout

    def test_relative_url_rejected(self):
        result = self._run("../pdf/somefile.pdf")
        assert result.returncode != 0
        assert "ERROR" in result.stdout

    def test_empty_url_rejected(self):
        """Empty string should print usage and exit non-zero."""
        # No arg at all — script expects exactly 1 arg
        result = subprocess.run(
            [sys.executable, str(REWRITE_SCRIPT)],
            capture_output=True, text=True,
        )
        assert result.returncode != 0


# ══════════════════════════════════════════════════════════════════════════════
# audit.scan_text error handling
# ══════════════════════════════════════════════════════════════════════════════

class TestScanText:
    """Tests for audit.scan_text() graceful error handling."""

    @pytest.fixture(autouse=True)
    def _setup(self, monkeypatch):
        # Reimport audit with a clean module state each test to reset globals
        import importlib

        import audit as audit_mod
        importlib.reload(audit_mod)
        self.audit = audit_mod
        # Point ROOT to a temp-safe value so relative_to() doesn't choke
        monkeypatch.setattr(audit_mod, "ROOT", Path("/"))

    def test_readable_file_yields_lines(self, tmp_path):
        f = tmp_path / "test.md"
        f.write_text("line one\nline two\nline three\n")
        lines = list(self.audit.scan_text(f))
        assert len(lines) == 3
        assert lines[0] == (1, "line one\n")
        assert lines[2] == (3, "line three\n")

    def test_skips_archive_directory(self, tmp_path):
        archive = tmp_path / "_archive"
        archive.mkdir()
        f = archive / "old.md"
        f.write_text("should not appear")
        lines = list(self.audit.scan_text(f))
        assert lines == []

    def test_skips_pdf_directory(self, tmp_path):
        pdf_dir = tmp_path / "pdf"
        pdf_dir.mkdir()
        f = pdf_dir / "doc.md"
        f.write_text("should not appear")
        lines = list(self.audit.scan_text(f))
        assert lines == []

    @pytest.mark.skipif(
        os.getuid() == 0, reason="Root can read any file; permission test invalid"
    )
    def test_unreadable_file_warns_and_increments_counter(self, tmp_path, capsys):
        f = tmp_path / "locked.md"
        f.write_text("secret")
        f.chmod(0o000)
        try:
            lines = list(self.audit.scan_text(f))
            assert lines == []
            assert self.audit._skipped_files == 1
            captured = capsys.readouterr()
            assert "WARN" in captured.out
            assert "locked.md" in captured.out
        finally:
            # Restore permissions so tmp_path cleanup works
            f.chmod(0o644)

    def test_empty_file_yields_nothing(self, tmp_path):
        f = tmp_path / "empty.md"
        f.write_text("")
        lines = list(self.audit.scan_text(f))
        assert lines == []


# ══════════════════════════════════════════════════════════════════════════════
# generate_dep_map.add() HTML escaping
# ══════════════════════════════════════════════════════════════════════════════

class TestDepMapAdd:
    """Tests for HTML escaping in generate_dep_map.add()."""

    @pytest.fixture(autouse=True)
    def _setup(self):
        import generate_dep_map as gdm
        self.gdm = gdm
        # Save and restore NODES list
        self._orig_nodes = gdm.NODES.copy()
        yield
        gdm.NODES[:] = self._orig_nodes

    def test_add_escapes_label(self):
        self.gdm.NODES.clear()
        self.gdm.add("TEST1", '<script>alert("xss")</script>', "path.md", "TM", 0, "test")
        node = self.gdm.NODES[-1]
        assert "<script>" not in node["label"]
        assert "&lt;script&gt;" in node["label"]

    def test_add_escapes_path(self):
        self.gdm.NODES.clear()
        self.gdm.add("TEST2", "Label", 'path/<img onerror="x">.md', "TM", 0, "test")
        node = self.gdm.NODES[-1]
        # The angle brackets are escaped, neutralizing the tag
        assert "<img" not in node["path"]
        assert "&lt;img" in node["path"]

    def test_add_escapes_track(self):
        self.gdm.NODES.clear()
        self.gdm.add("TEST3", "Label", "path.md", "TM", 0, '"><script>')
        node = self.gdm.NODES[-1]
        assert "<script>" not in node["track"]

    def test_add_escapes_node_type(self):
        self.gdm.NODES.clear()
        self.gdm.add("TEST4", "Label", "path.md", "<b>bold</b>", 0, "test")
        node = self.gdm.NODES[-1]
        assert "<b>" not in node["type"]
        assert "&lt;b&gt;" in node["type"]

    def test_add_preserves_clean_strings(self):
        self.gdm.NODES.clear()
        self.gdm.add("TM10", "TM_10\nMAVEN USER", "tm/TM_10.md", "TM", 1, "TM-10")
        node = self.gdm.NODES[-1]
        assert node["label"] == "TM_10\nMAVEN USER"
        assert node["path"] == "tm/TM_10.md"
        assert node["type"] == "TM"
        assert node["track"] == "TM-10"

    def test_add_column_is_int_not_escaped(self):
        """Column is numeric — verify it passes through as-is."""
        self.gdm.NODES.clear()
        self.gdm.add("TEST5", "Label", "path.md", "TM", 3, "test")
        node = self.gdm.NODES[-1]
        assert node["col"] == 3
