"""Chrome ingest: tagging, redaction, and skip rules."""

from __future__ import annotations

import os
import re
from functools import lru_cache
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]

# Local-only blocklist: URL / title / folder patterns that must never enter the
# catalog. Keep actual entries out of the repo (see config/blocklist.example.txt).
BLOCKLIST_FILE = Path(
    os.environ.get("QUANTA_BLOCKLIST_FILE", ROOT / "config" / "blocklist.local.txt")
)
BLOCKLIST_ENV = "QUANTA_BLOCKLIST"


@lru_cache(maxsize=1)
def load_blocklist() -> tuple[re.Pattern[str], ...]:
    """Regex patterns from env (comma-separated) plus an optional local file."""
    raw: list[str] = []
    env_value = os.environ.get(BLOCKLIST_ENV, "")
    raw.extend(part.strip() for part in env_value.split(",") if part.strip())
    if BLOCKLIST_FILE.is_file():
        for line in BLOCKLIST_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                raw.append(line)
    patterns: list[re.Pattern[str]] = []
    for item in raw:
        try:
            patterns.append(re.compile(item, re.IGNORECASE))
        except re.error:
            patterns.append(re.compile(re.escape(item), re.IGNORECASE))
    return tuple(patterns)

# Query keys that often carry secrets or personal identifiers.
SENSITIVE_QUERY_KEYS = frozenset(
    {
        "access_token",
        "api_key",
        "apikey",
        "auth",
        "authorization",
        "code",
        "email",
        "id_token",
        "key",
        "password",
        "refresh_token",
        "secret",
        "session",
        "sid",
        "signature",
        "token",
        "user",
        "username",
        "x-api-key",
    }
)

EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
BEARER_RE = re.compile(r"(?i)\b(bearer|token|api[_-]?key)\s*[:=]\s*\S+")
HOME_PATH_RE = re.compile(r"(?i)(/Users/[^/\s]+|/home/[^/\s]+|C:\\Users\\[^\\\s]+)")
JWT_RE = re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b")

DOMAIN_TAG_RULES: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile(r"(^|\.)github\.com$", re.I), "github"),
    (re.compile(r"(^|\.)gitlab\.com$", re.I), "gitlab"),
    (re.compile(r"(^|\.)arxiv\.org$", re.I), "arxiv"),
    (re.compile(r"(^|\.)huggingface\.co$", re.I), "huggingface"),
    (re.compile(r"(^|\.)leetcode\.(com|cn)$", re.I), "leetcode"),
    (re.compile(r"(^|\.)stackoverflow\.com$", re.I), "stackoverflow"),
    (re.compile(r"(^|\.)wikipedia\.org$", re.I), "wikipedia"),
    (re.compile(r"(^|\.)youtube\.com$|(^|\.)youtu\.be$", re.I), "youtube"),
    (re.compile(r"(^|\.)medium\.com$", re.I), "blog"),
    (re.compile(r"(^|\.)docs\.", re.I), "docs"),
    (re.compile(r"(^|\.)readthedocs\.(io|org)$", re.I), "docs"),
)

SOURCE_TAGS = {
    "chrome-bookmark": "chrome-bookmark",
    "chrome-history": "chrome-history",
    "chrome-session": "chrome-session",
}


def should_skip_chrome_item(
    *,
    url: str = "",
    title: str = "",
    source_path: str = "",
) -> bool:
    """Return True when the item matches a configured blocklist pattern."""
    patterns = load_blocklist()
    if not patterns:
        return False
    haystack = " ".join([url or "", title or "", source_path or ""])
    return any(p.search(haystack) for p in patterns)


def redact_text(text: str) -> str:
    """Strip emails, tokens, and home-directory paths from free text."""
    if not text:
        return ""
    out = EMAIL_RE.sub("[redacted-email]", text)
    out = JWT_RE.sub("[redacted-jwt]", out)
    out = BEARER_RE.sub(r"\1=[redacted]", out)
    out = HOME_PATH_RE.sub("[redacted-home]", out)
    return out


def redact_url(url: str) -> str:
    """Drop sensitive query params and redact credentials in the netloc."""
    if not url:
        return ""
    try:
        parts = urlsplit(url)
    except ValueError:
        return redact_text(url)

    netloc = parts.netloc
    if "@" in netloc:
        # user:pass@host → [redacted]@host
        host = netloc.rsplit("@", 1)[-1]
        netloc = f"[redacted]@{host}"

    query_pairs: list[tuple[str, str]] = []
    for key, value in parse_qsl(parts.query, keep_blank_values=True):
        if key.lower() in SENSITIVE_QUERY_KEYS or any(
            s in key.lower() for s in ("token", "secret", "password", "auth", "key")
        ):
            query_pairs.append((key, "[redacted]"))
        else:
            query_pairs.append((key, value))

    path = redact_text(parts.path)
    fragment = ""  # fragments often carry tokens; drop them
    cleaned = urlunsplit(
        (
            parts.scheme,
            netloc,
            path,
            urlencode(query_pairs, doseq=True),
            fragment,
        )
    )
    return cleaned


def redact_profile_path(path: str) -> str:
    """Avoid leaking the local username in manifests / logs."""
    return HOME_PATH_RE.sub("[redacted-home]", path or "")


def domain_tags(url: str) -> list[str]:
    try:
        host = urlsplit(url).hostname or ""
    except ValueError:
        return []
    host = host.lower().lstrip(".")
    tags: list[str] = []
    for pattern, tag in DOMAIN_TAG_RULES:
        if pattern.search(host):
            tags.append(tag)
    if host and not tags:
        # Keep a coarse host label without full FQDN PII noise.
        parts = [p for p in host.split(".") if p and p != "www"]
        if len(parts) >= 2:
            tags.append(parts[-2])
        elif parts:
            tags.append(parts[0])
    return tags


def folder_tags(source_path: str, *, limit: int = 5) -> list[str]:
    parts: list[str] = []
    for raw in (source_path or "").split("/"):
        part = raw.strip().lower()
        if not part or part in {"bookmark_bar", "other", "synced", "history"}:
            continue
        # Drop home-looking segments if they somehow appear in folder names.
        part = HOME_PATH_RE.sub("home", part)
        part = re.sub(r"[^a-z0-9._+-]+", "-", part).strip("-")
        if part:
            parts.append(part[:40])
        if len(parts) >= limit:
            break
    return parts


def build_chrome_tags(
    *,
    source: str,
    url: str = "",
    source_path: str = "",
    extra: list[str] | None = None,
) -> list[str]:
    tags: set[str] = set()
    if source in SOURCE_TAGS:
        tags.add(SOURCE_TAGS[source])
    tags.update(folder_tags(source_path))
    tags.update(domain_tags(url))
    for tag in extra or []:
        cleaned = (tag or "").strip().lower()
        if cleaned:
            tags.add(cleaned[:40])
    return sorted(tags)


def sanitize_chrome_item(item: dict[str, Any]) -> dict[str, Any] | None:
    """
    Apply skip + redaction + tags. Returns None when the item must be dropped.
    Mutates a shallow copy; does not modify the input dict.
    """
    url = item.get("url", "") or ""
    title = item.get("title", "") or ""
    source_path = item.get("source_path", "") or ""
    if should_skip_chrome_item(url=url, title=title, source_path=source_path):
        return None

    out = dict(item)
    clean_url = redact_url(url)
    out["url"] = clean_url
    out["title"] = redact_text(title) or clean_url
    out["source_path"] = redact_text(source_path)
    if "summary" in out and out["summary"]:
        out["summary"] = redact_text(str(out["summary"]))
    out["tags"] = build_chrome_tags(
        source=str(out.get("source", "")),
        url=clean_url,
        source_path=str(out.get("source_path", "")),
        extra=list(out.get("tags") or []),
    )
    out["privacy"] = {"redacted": True}
    return out


def filter_and_sanitize(items: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, int]]:
    kept: list[dict[str, Any]] = []
    skipped = 0
    for item in items:
        cleaned = sanitize_chrome_item(item)
        if cleaned is None:
            skipped += 1
            continue
        kept.append(cleaned)
    stats = {"kept": len(kept), "skipped_blocklist": skipped}
    return kept, stats
