"""Breakout signal generation skill."""

from typing import List


def detect_breakout(prices: List[float], lookback: int = 20) -> str:
    if len(prices) < lookback + 1:
        return "hold"

    recent = prices[-lookback:]
    high = max(recent)
    low = min(recent)
    current = prices[-1]

    if current > high:
        return "buy"
    if current < low:
        return "sell"
    return "hold"
