"""Liquidity analysis skill implementations."""

from typing import List


def calculate_average_volume(volumes: List[float]) -> float:
    """Compute average traded volume over the supplied history."""
    return sum(volumes) / max(len(volumes), 1)


def is_liquidity_spike(volumes: List[float], threshold: float = 2.0) -> bool:
    """Detect whether the latest volume is a spike versus recent history."""
    if len(volumes) < 2:
        return False

    average = calculate_average_volume(volumes[:-1])
    return average > 0 and volumes[-1] >= average * threshold
