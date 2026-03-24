"""
Rewrites ../pdf/FILENAME.pdf hrefs in index.html to absolute SharePoint URLs.

Usage:
    python3 scripts/rewrite_sharepoint_links.py <sharepoint_base_url>

Example:
    python3 scripts/rewrite_sharepoint_links.py \
      "https://armyeitaas.sharepoint-mil.us/sites/YOURSITE/Shared%20Documents/maven-pdfs"

Output:
    maven_training/mss_info_app/index_sharepoint.html  (original is untouched)
"""

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

INDEX_SRC = Path("maven_training/mss_info_app/index.html")
INDEX_OUT = Path("maven_training/mss_info_app/index_sharepoint.html")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/rewrite_sharepoint_links.py <sharepoint_base_url>")
        sys.exit(1)

    base_url = sys.argv[1].rstrip("/")

    # Validate URL: must be absolute https:// — reject javascript:, data:, relative URLs
    parsed = urlparse(base_url)
    if parsed.scheme != "https":
        print(f"ERROR: URL scheme must be https://, got '{parsed.scheme or '(none)'}://'")
        sys.exit(1)
    if not parsed.netloc:
        print("ERROR: URL must be absolute (include hostname)")
        sys.exit(1)
    lower_url = base_url.lower()
    for bad_scheme in ("javascript:", "data:"):
        if bad_scheme in lower_url:
            print(f"ERROR: URL must not contain '{bad_scheme}'")
            sys.exit(1)

    html = INDEX_SRC.read_text(encoding="utf-8")

    # Replace all ../pdf/FILENAME.pdf with absolute SharePoint URL
    def replace_link(match):
        filename = match.group(1)
        return f'href="{base_url}/{filename}"'

    updated, count = re.subn(r'href="\.\./pdf/([^"]+)"', replace_link, html)

    INDEX_OUT.write_text(updated, encoding="utf-8")
    print(f"Rewrote {count} links -> {INDEX_OUT}")
    print(f"Base URL used: {base_url}")


if __name__ == "__main__":
    main()
