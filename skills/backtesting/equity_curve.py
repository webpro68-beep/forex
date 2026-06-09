"""Equity curve generation skill."""

from typing import List


def build_equity_curve(prices: List[float], positions: List[float]) -> List[float]:
    return [price * position for price, position in zip(prices, positions)]
