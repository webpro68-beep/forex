"""Close order execution skill."""

from typing import Dict


def build_close_order(symbol: str, quantity: float, side: str) -> Dict[str, object]:
    return {
        "symbol": symbol,
        "quantity": quantity,
        "side": side,
        "type": "market",
    }
