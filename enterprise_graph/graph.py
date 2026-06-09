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

    def get_subgraph(self, node_id: str | None = None, category: str | None = None) -> Dict[str, Any]:
        """Return a subgraph filtered by node or category.

        - If `node_id` provided: return node and its immediate neighbors (in/out edges).
        - If `category` provided: return nodes whose meta.get('category') == category and edges between them.
        - If neither provided: return full graph.
        """
        if node_id:
            nodes = {}
            edges = []
            if node_id in self.nodes:
                nodes[node_id] = self.nodes[node_id]
            for e in self.edges:
                if e['src'] == node_id or e['dst'] == node_id:
                    edges.append(e)
                    nodes.setdefault(e['src'], self.nodes.get(e['src'], {}))
                    nodes.setdefault(e['dst'], self.nodes.get(e['dst'], {}))
            return {"nodes": nodes, "edges": edges}

        if category:
            nodes = {nid: meta for nid, meta in self.nodes.items() if meta.get('category') == category}
            node_keys = set(nodes.keys())
            edges = [e for e in self.edges if e['src'] in node_keys and e['dst'] in node_keys]
            return {"nodes": nodes, "edges": edges}

        return self.get_graph()
