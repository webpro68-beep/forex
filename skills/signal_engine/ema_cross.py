"""Signal generation using exponential moving average (EMA) crossovers."""

from typing import List


def calculate_ema(prices: List[float], period: int) -> List[float]:
    if not prices or period <= 0:
        return []

    alpha = 2.0 / (period + 1)
    ema_values = [prices[0]]
    for price in prices[1:]:
        ema_values.append(price * alpha + ema_values[-1] * (1 - alpha))
    return ema_values


def detect_ema_cross(short_ema: List[float], long_ema: List[float]) -> str:
    if len(short_ema) < 2 or len(long_ema) < 2:
        return "hold"

    if short_ema[-2] <= long_ema[-2] and short_ema[-1] > long_ema[-1]:
        return "buy"
    if short_ema[-2] >= long_ema[-2] and short_ema[-1] < long_ema[-1]:
        return "sell"
    return "hold"
