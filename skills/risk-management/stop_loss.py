"""Stop loss skill to calculate stop placement."""


def calculate_stop_loss(entry_price: float, volatility: float, multiplier: float = 1.5) -> float:
    return entry_price - abs(volatility * multiplier)
