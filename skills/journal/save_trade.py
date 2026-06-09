"""Trade journaling skill."""

from typing import Dict


def save_trade_entry(entry: Dict[str, object], storage: list) -> None:
    storage.append(entry)
