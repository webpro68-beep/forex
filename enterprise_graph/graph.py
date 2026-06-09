from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Any
from pathlib import Path
import json


@dataclass
class EnterpriseGraphManager:
    nodes: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    edges: List[Dict[str, str]] = field(default_factory=list)

    def register_node(self, node_id: str, meta: Dict[str, Any] | None = None) -> None:
        self.nodes.setdefault(node_id, {})
        if meta:
            self.nodes[node_id].update(meta)

    def add_edge(self, src: str, dst: str, label: str | None = None) -> None:
        self.edges.append({"src": src, "dst": dst, "label": label or ""})

    def get_graph(self) -> Dict[str, Any]:
        return {"nodes": self.nodes, "edges": self.edges}

    def clear(self) -> None:
        self.nodes.clear()
        self.edges.clear()

    def save(self, path: str | Path) -> None:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(self.get_graph(), indent=2), encoding="utf-8")

    def load(self, path: str | Path) -> None:
        p = Path(path)
        if not p.exists():
            return
        data = json.loads(p.read_text(encoding="utf-8"))
        self.nodes = data.get("nodes", {})
        self.edges = data.get("edges", [])
