from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4

from memory.schemas import MemoryQuery, MemoryRecord, MemoryType
from memory.short_term import MemoryStore
from memory.long_term import load_memory, persist_memory, query_memory


@dataclass
class MemoryManager:
    path: str
    short_term: MemoryStore

    def __init__(self, path: str, short_term: MemoryStore | None = None):
        self.path = path
        self.short_term = short_term or MemoryStore()

    def remember(self, content: dict[str, Any], memory_type: MemoryType = MemoryType.LONG_TERM, tags: list[str] | None = None) -> MemoryRecord:
        record = MemoryRecord(
            memory_id=str(uuid4()),
            created_at=datetime.now(timezone.utc).isoformat(),
            memory_type=memory_type,
            content=content,
            tags=tags or [],
        )
        return persist_memory(self.path, record)

    def recall(self, query_value: str, tags: list[str] | None = None, memory_type: MemoryType | None = None) -> list[MemoryRecord]:
        query = MemoryQuery(query=query_value, tags=tags or [], memory_type=memory_type)
        return query_memory(self.path, query)

    def recent_short_term(self, limit: int = 10) -> list[MemoryRecord]:
        return self.short_term.recent(limit)
