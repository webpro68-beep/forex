"""Risk/reward ratio calculation skill."""


def calculate_risk_reward(stop_distance: float, profit_distance: float) -> float:
    if stop_distance <= 0:
        return 0.0
    return profit_distance / stop_distance
