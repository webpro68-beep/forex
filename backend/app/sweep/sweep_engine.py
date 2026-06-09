from __future__ import annotations

from app.core.models import Order, RobotState
from skills.shared.sweep import detect_orphans, sweep_orders


class SweepAgent:
    def detect_orphans(self, state: RobotState, broker_orders: list[Order]) -> list[Order]:
        return detect_orphans(state=state, broker_orders=broker_orders)

    def sweep(self, orphans: list[Order]) -> list[Order]:
        return sweep_orders(orphans)
