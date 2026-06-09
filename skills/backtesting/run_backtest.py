"""Backtesting engine entry point."""

from typing import List, Dict

from .schemas import BacktestResult


def run_backtest(prices: List[float], signals: List[str]) -> BacktestResult:
    capital = 10000.0
    position = 0.0
    trade_log = []

    for index, signal in enumerate(signals):
        price = prices[index]
        if signal == "buy" and position == 0:
            position = capital / price
            trade_log.append({"type": "buy", "price": price})
        elif signal == "sell" and position > 0:
            capital = position * price
            trade_log.append({"type": "sell", "price": price})
            position = 0.0

    return BacktestResult(final_balance=capital, trades=trade_log)
