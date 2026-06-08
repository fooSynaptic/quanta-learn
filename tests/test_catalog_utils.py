"""Tests for shared catalog helpers."""

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

pytest.importorskip("yaml")

from _catalog_utils import (  # noqa: E402
    infer_language,
    infer_topics_from_name,
    load_yaml,
    merge_by_key,
    save_yaml,
    slugify,
    today,
)


def test_slugify_basic():
    assert slugify("Hello World!") == "hello-world"
    assert slugify("  多个   空格 abc ") == "abc"
    assert slugify("") == "item"


def test_infer_language():
    assert infer_language(Path("a.py")) == "python"
    assert infer_language(Path("a.c")) == "c"
    assert infer_language(Path("a.cpp")) == "cpp"
    assert infer_language(Path("a.rs")) == "unknown"


def test_infer_topics_from_name():
    assert "sorting" in infer_topics_from_name("merge_sort.py")
    assert "linked-list" in infer_topics_from_name("MyLinkedList.py")
    assert infer_topics_from_name("random123") == []


def test_save_and_load_roundtrip(tmp_path):
    path = tmp_path / "items.yaml"
    items = [{"id": "a", "value": 1}, {"id": "b", "value": 2}]
    save_yaml(path, items)
    loaded = load_yaml(path)
    assert loaded == items


def test_merge_by_key_adds_and_merges():
    existing = [{"id": "a", "tags": ["x"], "updated_at": "2000-01-01"}]
    incoming = [
        {"id": "a", "tags": ["y"]},
        {"id": "b", "name": "new"},
    ]
    merged = merge_by_key(existing, incoming, "id")
    by_id = {m["id"]: m for m in merged}

    assert by_id["a"]["tags"] == ["x", "y"]
    assert by_id["a"]["updated_at"] == today()  # changed -> bumped
    assert by_id["b"]["name"] == "new"
    assert by_id["b"]["created_at"] == today()


def test_merge_by_key_no_change_keeps_timestamp():
    existing = [{"id": "a", "tags": ["x"], "updated_at": "2000-01-01"}]
    incoming = [{"id": "a", "tags": ["x"]}]  # identical -> no bump
    merged = merge_by_key(existing, incoming, "id")
    assert merged[0]["updated_at"] == "2000-01-01"
