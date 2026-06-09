"""Trade statistics calculation skill."""

from typing import List


def calculate_win_rate(results: List[bool]) -> float:
    if not results:
        return 0.0
    return sum(1 for r in results if r) / len(results)


def average_return(returns: List[float]) -> float:
    if not returns:
        return 0.0
    return sum(returns) / len(returns)
