"""Take profit skill to calculate profit target levels."""


def calculate_take_profit(entry_price: float, risk_distance: float, reward_ratio: float = 2.0) -> float:
    return entry_price + abs(risk_distance) * reward_ratio
