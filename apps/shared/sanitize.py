"""HTML sanitization utilities for Streamlit dashboards."""
import html as _html


def safe_html(text: str) -> str:
    """Escape user-provided text for safe HTML rendering."""
    return _html.escape(str(text))


def safe_markdown(template: str, **kwargs: str) -> str:
    """Format a markdown template with escaped user values.

    Usage: safe_markdown("Name: **{name}**", name=user_input)
    """
    escaped = {k: _html.escape(str(v)) for k, v in kwargs.items()}
    return template.format(**escaped)
