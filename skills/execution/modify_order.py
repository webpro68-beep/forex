"""Modify order execution skill."""

from typing import Dict, Optional


def build_modify_order(order_id: str, new_price: Optional[float] = None, new_quantity: Optional[float] = None) -> Dict[str, object]:
    payload = {"order_id": order_id}
    if new_price is not None:
        payload["price"] = new_price
    if new_quantity is not None:
        payload["quantity"] = new_quantity
    return payload
