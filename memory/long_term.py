from __future__ import annotations

import json
from pathlib import Path

from memory.schemas import MemoryQuery, MemoryRecord, MemoryType


def _read_store(path: str) -> list[MemoryRecord]:
    store_path = Path(path)
    if not store_path.exists():
        return []
    raw = json.loads(store_path.read_text(encoding="utf-8"))
    return [MemoryRecord.from_dict(item) for item in raw]


def _write_store(path: str, records: list[MemoryRecord]) -> None:
    store_path = Path(path)
    store_path.parent.mkdir(parents=True, exist_ok=True)
    store_path.write_text(json.dumps([record.to_dict() for record in records], indent=2), encoding="utf-8")


def persist_memory(path: str, record: MemoryRecord) -> MemoryRecord:
    records = _read_store(path)
    records.append(record)
    _write_store(path, records)
    return record


def load_memory(path: str, memory_type: MemoryType | None = None) -> list[MemoryRecord]:
    records = _read_store(path)
    if memory_type is None:
        return records
    return [record for record in records if record.memory_type is memory_type]


def query_memory(path: str, query: MemoryQuery) -> list[MemoryRecord]:
    records = load_memory(path, query.memory_type)
    query_terms = [term.lower() for term in query.query.split() if term]
    tags = [tag.lower() for tag in query.tags]

    def matches(record: MemoryRecord) -> bool:
        serialized = json.dumps(record.content, ensure_ascii=False).lower()
        searchable = f"{serialized} {' '.join(record.tags).lower()}"
        return all(term in searchable for term in query_terms) and all(tag in searchable for tag in tags)

    return [record for record in records if matches(record)]
