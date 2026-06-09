"""Position sizing skill based on account equity and risk tolerance."""

from typing import Optional


def calculate_position_size(account_balance: float, risk_per_trade: float, stop_distance: float, price: float) -> Optional[float]:
    if account_balance <= 0 or risk_per_trade <= 0 or stop_distance <= 0 or price <= 0:
        return None

    risk_amount = account_balance * risk_per_trade
    position_size = risk_amount / (stop_distance * price)
    return max(position_size, 0.0)
