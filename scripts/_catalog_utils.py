"""Shared helpers for quanta-learn catalog scripts."""

from __future__ import annotations

import re
import unicodedata
from datetime import date
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None  # type: ignore


ROOT = Path(__file__).resolve().parents[1]
CATALOG_DIR = ROOT / "catalog"


def today() -> str:
    return date.today().isoformat()


def slugify(text: str, max_len: int = 60) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return (text or "item")[:max_len].strip("-")


def load_yaml(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    if yaml is None:
        raise RuntimeError("PyYAML is required. Install with: pip install pyyaml")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not data:
        return []
    if isinstance(data, dict) and "items" in data:
        return data["items"]
    if isinstance(data, list):
        return data
    return []


def save_yaml(path: Path, items: list[dict[str, Any]], key: str = "items") -> None:
    if yaml is None:
        raise RuntimeError("PyYAML is required. Install with: pip install pyyaml")
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {key: items, "updated_at": today()}
    path.write_text(
        yaml.dump(payload, allow_unicode=True, sort_keys=False, default_flow_style=False),
        encoding="utf-8",
    )


def merge_by_key(
    existing: list[dict[str, Any]],
    incoming: list[dict[str, Any]],
    key: str,
) -> list[dict[str, Any]]:
    merged: dict[str, dict[str, Any]] = {item[key]: item for item in existing if key in item}
    for item in incoming:
        item_id = item.get(key)
        if not item_id:
            continue
        if item_id in merged:
            base = merged[item_id]
            for k, v in item.items():
                if v in (None, "", [], {}):
                    continue
                if k == "tags" and isinstance(v, list):
                    base["tags"] = sorted(set(base.get("tags", []) + v))
                elif k == "related" and isinstance(v, dict):
                    rel = base.setdefault("related", {})
                    for rk, rv in v.items():
                        rel[rk] = sorted(set(rel.get(rk, []) + (rv or [])))
                else:
                    base[k] = v
            base["updated_at"] = today()
        else:
            item.setdefault("created_at", today())
            item["updated_at"] = today()
            merged[item_id] = item
    return sorted(merged.values(), key=lambda x: x.get("id", ""))


def infer_language(path: Path) -> str:
    suffix = path.suffix.lower()
    return {
        ".py": "python",
        ".c": "c",
        ".cpp": "cpp",
        ".md": "markdown",
    }.get(suffix, "unknown")


def infer_topics_from_name(name: str) -> list[str]:
    stem = Path(name).stem.lower()
    topic_map = {
        "tree": "tree",
        "link": "linked-list",
        "list": "linked-list",
        "sort": "sorting",
        "heap": "heap",
        "graph": "graph",
        "dp": "dp",
        "climb": "dp",
        "trie": "trie",
        "matrix": "matrix",
        "string": "string",
        "pal": "string",
        "bst": "tree",
        "binary": "binary-search",
        "merge": "merge",
        "top_k": "heap",
        "dijkstra": "graph",
        "floyd": "graph",
        "svm": "ml",
        "smo": "ml",
    }
    tags: list[str] = []
    for key, tag in topic_map.items():
        if key in stem:
            tags.append(tag)
    return sorted(set(tags))
