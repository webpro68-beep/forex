"""Support and resistance detection skill implementations."""

from typing import List, Tuple


def find_support_resistance(prices: List[float], window: int = 5) -> Tuple[List[float], List[float]]:
    """Identify simple support and resistance levels from recent price data."""
    if len(prices) < window * 2 + 1:
        return [], []

    supports = []
    resistances = []
    for i in range(window, len(prices) - window):
        current = prices[i]
        before = prices[i - window: i]
        after = prices[i + 1: i + 1 + window]

        if current <= min(before + after):
            supports.append(current)
        if current >= max(before + after):
            resistances.append(current)

    return supports, resistances
