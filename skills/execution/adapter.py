"""Execution adapter decision logic moved out of the backend agent."""

from __future__ import annotations

from app.core.config import Settings
from app.core.models import OrderStatus


def determine_order_status(settings: Settings) -> OrderStatus:
    if settings.broker_mode != "mock" and not settings.allow_live_execution:
        return OrderStatus.REJECTED
    return OrderStatus.OPEN


def build_broker_order_id() -> str:
    from uuid import uuid4

    return f"MOCK-{uuid4()}"
