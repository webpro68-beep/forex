from __future__ import annotations

from fastapi import APIRouter, Query
from typing import Optional

from enterprise_graph import EnterpriseGraphManager

router = APIRouter(prefix="/api/v1/graph", tags=["enterprise_graph"])

# in-memory singleton for simple usage
graph_agent = EnterpriseGraphManager()

DEFAULT_STORE_PATH = "data/enterprise_graph.json"


@router.get("/status")
def graph_status():
    return {"ok": True, "nodes": len(graph_agent.nodes), "edges": len(graph_agent.edges)}


@router.post("/register/{node_id}")
def register_node(node_id: str):
    graph_agent.register_node(node_id)
    return {"ok": True, "node": node_id}


@router.post("/edge/{src}/{dst}")
def add_edge(src: str, dst: str):
    graph_agent.add_edge(src, dst)
    return {"ok": True, "edge": {"src": src, "dst": dst}}


@router.get("/dump")
def dump_graph():
    return graph_agent.get_graph()


@router.post("/save")
def save_graph(path: Optional[str] = Query(None)):
    p = path or DEFAULT_STORE_PATH
    graph_agent.save(p)
    return {"ok": True, "path": p}


@router.post("/load")
def load_graph(path: Optional[str] = Query(None)):
    p = path or DEFAULT_STORE_PATH
    graph_agent.load(p)
    return {"ok": True, "path": p}


@router.get("/subgraph")
def subgraph(node: Optional[str] = Query(None), category: Optional[str] = Query(None)):
    g = graph_agent.get_subgraph(node_id=node, category=category)
    return g
