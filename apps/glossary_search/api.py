"""FastAPI backend for Glossary Search.

Provides RESTful endpoints for searching, browsing, and managing
the glossary term index.

Run:  uvicorn apps.glossary_search.api:app --port 8007 --reload
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from shared.middleware import SecurityHeadersMiddleware

from . import db
from .models import (
    CategoryCount,
    IndexStats,
    SearchResult,
    TermCategory,
    TermEntry,
)

# Default corpus root — override via POST /reindex body if needed
CORPUS_ROOT = Path(__file__).resolve().parent.parent.parent / "maven_training"


# ---------------------------------------------------------------------------
# App lifecycle
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    db.init_db()
    yield


app = FastAPI(
    title="Glossary Search API",
    description="Full-text search across USAREUR-AF glossary, doctrine, and training terms.",
    version="1.0.0",
    lifespan=lifespan,
)
app.add_middleware(SecurityHeadersMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8500", "http://127.0.0.1:8500"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@app.get("/health")
def health() -> dict:
    """Health check."""
    stats = db.get_stats()
    return {"status": "ok", "indexed_terms": stats["total_terms"]}


@app.get("/search", response_model=SearchResult)
def search(
    q: str = Query(..., min_length=1, description="Search query"),
    category: Optional[TermCategory] = Query(default=None),
    limit: int = Query(default=20, ge=1, le=200),
) -> SearchResult:
    """Full-text search across term names and definitions."""
    results, elapsed = db.search_terms(
        query=q,
        category=category.value if category else None,
        limit=limit,
    )
    entries = [
        TermEntry(
            id=t.id,
            term=t.term,
            definition=t.definition,
            source_file=t.source_file,
            source_line=t.source_line,
            category=t.category,
        )
        for t in results
    ]
    return SearchResult(
        query=q,
        total_hits=len(entries),
        results=entries,
        search_time_ms=round(elapsed, 2),
    )


@app.get("/terms", response_model=list[TermEntry])
def list_terms(
    category: Optional[TermCategory] = Query(default=None),
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=50, ge=1, le=500),
) -> list[TermEntry]:
    """List all terms with optional category filter and pagination."""
    all_terms = db.get_all_terms(
        category=category.value if category else None,
    )
    page = all_terms[offset : offset + limit]
    return [
        TermEntry(
            id=t.id,
            term=t.term,
            definition=t.definition,
            source_file=t.source_file,
            source_line=t.source_line,
            category=t.category,
        )
        for t in page
    ]


@app.get("/terms/{term_id}", response_model=TermEntry)
def get_term(term_id: int) -> TermEntry:
    """Retrieve a single term by ID."""
    t = db.get_term_by_id(term_id)
    if t is None:
        raise HTTPException(status_code=404, detail="Term not found")
    return TermEntry(
        id=t.id,
        term=t.term,
        definition=t.definition,
        source_file=t.source_file,
        source_line=t.source_line,
        category=t.category,
    )


@app.get("/categories", response_model=list[CategoryCount])
def list_categories() -> list[CategoryCount]:
    """List distinct categories with counts."""
    cats = db.get_categories()
    return [CategoryCount(**c) for c in cats]


@app.post("/reindex")
def reindex() -> dict:
    """Drop and rebuild the term index from source markdown files."""
    if not CORPUS_ROOT.is_dir():
        raise HTTPException(
            status_code=400,
            detail=f"Corpus root not found: {CORPUS_ROOT}",
        )
    count = db.reindex(CORPUS_ROOT)
    return {"status": "ok", "terms_indexed": count}


@app.get("/stats", response_model=IndexStats)
def stats() -> IndexStats:
    """Aggregate index statistics."""
    s = db.get_stats()
    return IndexStats(
        total_terms=s["total_terms"],
        by_category=[CategoryCount(**c) for c in s["by_category"]],
        source_files=s["source_files"],
    )
