from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from skills.memory.schemas import MemoryQuery, MemoryRecord, MemoryType
from skills.memory.long_term import query_memory


def save_trade_context(agent: Any, symbol: str, timeframe: str, trade_context: dict[str, Any], tags: list[str] | None = None) -> MemoryRecord:
    payload = {
        "kind": "trade_context",
        "symbol": symbol,
        "timeframe": timeframe,
        "saved_at": datetime.now(timezone.utc).isoformat(),
        "trade_context": trade_context,
    }
    return agent.remember(payload, memory_type=MemoryType.LONG_TERM, tags=(tags or ["trade_context", symbol, timeframe]))


def query_market_insight(agent: Any, query_value: str, tags: list[str] | None = None) -> list[MemoryRecord]:
    query = MemoryQuery(query=query_value, tags=(tags or ["market_insight"]), memory_type=MemoryType.LONG_TERM)
    return query_memory(str(agent.path), query)
