"""Backtesting metrics calculation skill."""

from typing import List


def calculate_return(start_balance: float, end_balance: float) -> float:
    return (end_balance - start_balance) / max(start_balance, 1.0)


def calculate_sharpe(returns: List[float], risk_free_rate: float = 0.0) -> float:
    if not returns:
        return 0.0
    mean_return = sum(returns) / len(returns)
    variance = sum((r - mean_return) ** 2 for r in returns) / len(returns)
    std_dev = variance ** 0.5
    return 0.0 if std_dev == 0 else (mean_return - risk_free_rate) / std_dev
