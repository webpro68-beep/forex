"""Trend analysis skill implementations."""

from typing import List

from .schemas import TrendResult, TrendDirection


def detect_trend(prices: List[float], sensitivity: float = 0.005) -> TrendResult:
    """Detect a trend from a sequence of prices."""
    if len(prices) < 2:
        return TrendResult(direction=TrendDirection.NEUTRAL, confidence=0.0)

    delta = prices[-1] - prices[0]
    magnitude = abs(delta) / max(abs(prices[0]), 1.0)

    if magnitude < sensitivity:
        direction = TrendDirection.NEUTRAL
        confidence = 1.0 - magnitude / sensitivity
    elif delta > 0:
        direction = TrendDirection.BULLISH
        confidence = min(1.0, magnitude / (sensitivity * 5))
    else:
        direction = TrendDirection.BEARISH
        confidence = min(1.0, magnitude / (sensitivity * 5))

    return TrendResult(direction=direction, confidence=confidence)
