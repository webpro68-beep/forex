from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from skills.memory.schemas import MemoryRecord, MemoryType


class MemoryStore:
    def __init__(self) -> None:
        self.records: list[MemoryRecord] = []

    def add(self, content: dict[str, Any], tags: list[str] | None = None) -> MemoryRecord:
        record = MemoryRecord(
            memory_id=str(uuid4()),
            created_at=datetime.now(timezone.utc).isoformat(),
            memory_type=MemoryType.SHORT_TERM,
            content=content,
            tags=tags or [],
        )
        self.records.append(record)
        return record

    def recent(self, limit: int = 10) -> list[MemoryRecord]:
        return list(reversed(self.records[-limit:]))


def add_short_term_memory(store: MemoryStore, content: dict[str, Any], tags: list[str] | None = None) -> MemoryRecord:
    return store.add(content, tags)


def recall_recent_memories(store: MemoryStore, limit: int = 10) -> list[MemoryRecord]:
    return store.recent(limit)
