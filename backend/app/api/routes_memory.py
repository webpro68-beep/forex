from __future__ import annotations

from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.core.runtime import memory_agent
from skills.memory.schemas import MemoryQuery, MemoryType
from skills.memory.workflows import query_market_insight, save_trade_context

router = APIRouter(prefix="/api/v1/memory", tags=["memory"])


class MemorySaveRequest(BaseModel):
    kind: str = Field(default="generic", description="Type of memory record")
    content: dict[str, Any] = Field(default_factory=dict)
    memory_type: MemoryType = Field(default=MemoryType.LONG_TERM)
    tags: list[str] = Field(default_factory=list)


class TradeContextRequest(BaseModel):
    symbol: str
    timeframe: str
    trade_context: dict[str, Any]
    tags: list[str] = Field(default_factory=list)


class MemoryQueryRequest(BaseModel):
    query: str
    tags: list[str] = Field(default_factory=list)
    memory_type: MemoryType | None = None


@router.post("/save")
def save_memory(record: MemorySaveRequest):
    saved = memory_agent.remember(
        {"kind": record.kind, "content": record.content},
        memory_type=record.memory_type,
        tags=record.tags,
    )
    return {"saved_memory": saved.to_dict()}


@router.post("/save-trade-context")
def save_trade_context_endpoint(payload: TradeContextRequest):
    saved = save_trade_context(
        memory_agent,
        symbol=payload.symbol,
        timeframe=payload.timeframe,
        trade_context=payload.trade_context,
        tags=payload.tags,
    )
    return {"saved_memory": saved.to_dict()}


@router.post("/query")
def query_memory(payload: MemoryQueryRequest):
    query = MemoryQuery(query=payload.query, tags=payload.tags, memory_type=payload.memory_type)
    results = memory_agent.recall(query)
    return {"results": [record.to_dict() for record in results]}


@router.get("/all")
def get_all_memory():
    records = memory_agent.all()
    return {"records": [record.to_dict() for record in records]}


@router.post("/market-insight")
def query_market_insight_endpoint(payload: MemoryQueryRequest):
    results = query_market_insight(memory_agent, query_value=payload.query, tags=payload.tags)
    return {"market_insights": [record.to_dict() for record in results]}
