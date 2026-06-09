from __future__ import annotations

from app.core.models import WinnerGene
from app.core.state_store import GeneStore
from skills.shared.memory import list_winner_genes, promote_gene, remember_gene


class WinnerGenesMemoryAgent:
    def __init__(self, store: GeneStore):
        self.store = store

    def remember(self, gene: WinnerGene) -> WinnerGene:
        return remember_gene(self.store, gene)

    def winners(self) -> list[WinnerGene]:
        return list_winner_genes(self.store)

    def promote(self, symbol: str, timeframe: str) -> WinnerGene | None:
        return promote_gene(self.store, symbol, timeframe)
