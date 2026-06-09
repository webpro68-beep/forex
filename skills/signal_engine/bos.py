"""Break of structure (BOS) signal generation skill."""

from typing import List


def detect_break_of_structure(highs: List[float], lows: List[float]) -> str:
    if len(highs) < 2 or len(lows) < 2:
        return "hold"

    if highs[-1] > highs[-2]:
        return "bullish"
    if lows[-1] < lows[-2]:
        return "bearish"
    return "hold"
