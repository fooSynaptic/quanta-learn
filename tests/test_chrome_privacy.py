"""Tests for Chrome tagging, redaction, and blocklist skip rules."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import chrome_privacy  # noqa: E402
from chrome_privacy import (  # noqa: E402
    build_chrome_tags,
    filter_and_sanitize,
    redact_profile_path,
    redact_text,
    redact_url,
    sanitize_chrome_item,
    should_skip_chrome_item,
)


@pytest.fixture
def blocklist(monkeypatch, tmp_path):
    """Install a temporary blocklist and reset the cache."""

    def _install(patterns: list[str]) -> None:
        path = tmp_path / "blocklist.txt"
        path.write_text("\n".join(patterns) + "\n", encoding="utf-8")
        monkeypatch.setattr(chrome_privacy, "BLOCKLIST_FILE", path)
        monkeypatch.delenv(chrome_privacy.BLOCKLIST_ENV, raising=False)
        chrome_privacy.load_blocklist.cache_clear()

    yield _install
    chrome_privacy.load_blocklist.cache_clear()


def test_no_blocklist_keeps_everything(blocklist):
    blocklist([])
    assert not should_skip_chrome_item(url="https://internal.example.com/x")


def test_blocklist_matches_url_title_and_folder(blocklist):
    blocklist([r"blockedcorp", r"\binternal portal\b"])
    assert should_skip_chrome_item(url="https://wiki.blockedcorp.net/foo")
    assert should_skip_chrome_item(title="BlockedCorp weekly sync")
    assert should_skip_chrome_item(source_path="bookmark_bar/blockedcorp/docs")
    assert should_skip_chrome_item(title="Internal Portal home")
    assert not should_skip_chrome_item(url="https://github.com/foo/bar")


def test_blocklist_from_env(monkeypatch, tmp_path):
    monkeypatch.setattr(chrome_privacy, "BLOCKLIST_FILE", tmp_path / "missing.txt")
    monkeypatch.setenv(chrome_privacy.BLOCKLIST_ENV, "secretco, another")
    chrome_privacy.load_blocklist.cache_clear()
    try:
        assert should_skip_chrome_item(url="https://secretco.example/x")
        assert should_skip_chrome_item(title="another thing")
        assert not should_skip_chrome_item(url="https://arxiv.org/abs/1")
    finally:
        chrome_privacy.load_blocklist.cache_clear()


def test_redact_url_strips_tokens_and_userinfo():
    url = "https://user:secret@api.example.com/v1?token=abc&page=2#frag"
    cleaned = redact_url(url)
    assert "secret" not in cleaned
    assert "abc" not in cleaned
    assert "[redacted]" in cleaned
    assert "page=2" in cleaned
    assert "#" not in cleaned  # fragment dropped


def test_redact_text_email_and_home():
    text = "notes for alice@company.com under /Users/someone/codes/secret"
    cleaned = redact_text(text)
    assert "alice@company.com" not in cleaned
    assert "[redacted-email]" in cleaned
    assert "/Users/someone" not in cleaned
    assert "[redacted-home]" in cleaned


def test_redact_profile_path():
    assert "[redacted-home]" in redact_profile_path(
        "/Users/someone/Library/Application Support/Google/Chrome/Default"
    )


def test_build_chrome_tags_folder_and_domain():
    tags = build_chrome_tags(
        source="chrome-bookmark",
        url="https://github.com/fooSynaptic/quanta-learn",
        source_path="bookmark_bar/ML/RLHF",
    )
    assert "chrome-bookmark" in tags
    assert "github" in tags
    assert "ml" in tags
    assert "rlhf" in tags
    assert "bookmark_bar" not in tags


def test_sanitize_drops_blocked_keeps_public(blocklist):
    blocklist([r"blockedcorp"])
    raw = [
        {
            "id": "read-a",
            "title": "Public paper",
            "url": "https://arxiv.org/abs/1234.5678?token=leak",
            "source": "chrome-bookmark",
            "source_path": "bookmark_bar/Papers",
            "tags": [],
        },
        {
            "id": "read-b",
            "title": "Internal",
            "url": "https://docs.blockedcorp.net/secret",
            "source": "chrome-history",
            "source_path": "history",
            "tags": [],
        },
    ]
    kept, stats = filter_and_sanitize(raw)
    assert stats["skipped_blocklist"] == 1
    assert len(kept) == 1
    item = kept[0]
    assert item["url"].startswith("https://arxiv.org/")
    assert "leak" not in item["url"]
    assert "arxiv" in item["tags"]
    assert item["privacy"]["redacted"] is True


def test_sanitize_chrome_item_none_for_blocked(blocklist):
    blocklist([r"blockedcorp"])
    assert (
        sanitize_chrome_item(
            {
                "title": "x",
                "url": "https://portal.blockedcorp.com/",
                "source": "chrome-session",
                "source_path": "Session_1",
            }
        )
        is None
    )
