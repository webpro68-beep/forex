"""Open order execution skill."""

from typing import Dict


def build_open_order(symbol: str, quantity: float, side: str, price: float = None) -> Dict[str, object]:
    return {
        "symbol": symbol,
        "quantity": quantity,
        "side": side,
        "type": "market" if price is None else "limit",
        "price": price,
    }
