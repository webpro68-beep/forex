from __future__ import annotations

from skills.shared.optimizer import run_optimization


class BacktestOptimizationAgent:
    """Deterministic enough fake optimizer for MVP API wiring.

    Replace with vectorbt/backtrader engine before using real capital.
    """

    def run(self, symbol: str, timeframe: str, step_range: list[float], x_range: list[int], risk_range: list[float]):
        return run_optimization(symbol=symbol, timeframe=timeframe, step_range=step_range, x_range=x_range, risk_range=risk_range)
