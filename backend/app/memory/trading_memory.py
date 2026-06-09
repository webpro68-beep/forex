from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4

from app.core.models import WinnerGene
from app.core.state_store import GeneStore
from skills.memory.long_term import MemoryQuery, MemoryRecord, MemoryType, load_memory, persist_memory, query_memory
from skills.shared.memory import list_winner_genes, promote_gene, remember_gene


class WinnerGenesMemoryAgent:
    def __init__(self, store: GeneStore):
        self.store = store

    def remember(self, gene: WinnerGene) -> WinnerGene:
        return remember_gene(self.store, gene)

    def winners(self) -> list[WinnerGene]:
        return list_winner_genes(self.store)

    def promote(self, symbol: str, timeframe: str) -> WinnerGene | None:
        return promote_gene(self.store, symbol, timeframe)


class MemoryOsAgent:
    def __init__(self, path: str):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.write_text("[]", encoding="utf-8")

    def remember(self, content: dict[str, Any], memory_type: MemoryType = MemoryType.LONG_TERM, tags: list[str] | None = None) -> MemoryRecord:
        record = MemoryRecord(
            memory_id=str(uuid4()),
            created_at=datetime.now(timezone.utc).isoformat(),
            memory_type=memory_type,
            content=content,
            tags=tags or [],
        )
        return persist_memory(str(self.path), record)

    def recall(self, query: MemoryQuery) -> list[MemoryRecord]:
        return query_memory(str(self.path), query)

    def all(self) -> list[MemoryRecord]:
        return load_memory(str(self.path))
