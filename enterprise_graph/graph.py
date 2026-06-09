from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Any
from pathlib import Path
import json
import re


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

    def populate_from_skills(self, base_path: str | Path) -> None:
        base = Path(base_path)
        if not base.exists() or not base.is_dir():
            return

        for child in sorted(base.iterdir()):
            if not child.is_dir():
                continue
            if not (child / "__init__.py").exists():
                continue
            node_id = child.name
            meta: Dict[str, Any] = {"category": "skill"}
            readme_file = child / "README.md"
            if readme_file.exists():
                text = readme_file.read_text(encoding="utf-8")
                first_line = next((line.strip() for line in text.splitlines() if line.strip()), "")
                if first_line:
                    meta["description"] = first_line.lstrip("# ")
            self.register_node(node_id, meta)

    def populate_from_imports(self, base_path: str | Path, skills_root: str = "skills", backend_root: str = "backend/app") -> None:
        base = Path(base_path)
        skills_dir = base / skills_root
        backend_dir = base / backend_root

        def import_to_skill_node(import_path: str) -> str:
            parts = import_path.split(".")
            if len(parts) >= 2 and parts[0] == "skills":
                return ".".join(parts[:2])
            return import_path

        if backend_dir.exists():
            for path in backend_dir.rglob("*.py"):
                try:
                    text = path.read_text(encoding="utf-8")
                except Exception:
                    continue
                module_id = path.relative_to(base).with_suffix("").as_posix().replace("/", ".")
                self.register_node(module_id, {"category": "agent", "source": str(path.relative_to(base))})
                for imported in self._parse_imports(text):
                    if imported.startswith("skills."):
                        skill_node = import_to_skill_node(imported)
                        self.register_node(skill_node, {"category": "skill"})
                        self.add_edge(module_id, skill_node, label="depends_on")

        if skills_dir.exists():
            for path in skills_dir.rglob("*.py"):
                try:
                    text = path.read_text(encoding="utf-8")
                except Exception:
                    continue
                module_id = path.relative_to(base).with_suffix("").as_posix().replace("/", ".")
                self.register_node(module_id, {"category": "skill", "source": str(path.relative_to(base))})
                for imported in self._parse_imports(text):
                    if imported.startswith("skills."):
                        imported_node = import_to_skill_node(imported)
                        self.register_node(imported_node, {"category": "skill"})
                        self.add_edge(module_id, imported_node, label="depends_on")

    @staticmethod
    def _parse_imports(source: str) -> List[str]:
        pattern = re.compile(r"^(?:from|import)\s+([\w\.]+)", re.MULTILINE)
        imports: List[str] = []
        for match in pattern.finditer(source):
            imports.append(match.group(1))
        return imports

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
