from fastapi.testclient import TestClient
from backend.app.main import app


def test_graph_endpoints():
    client = TestClient(app)
    r = client.get("/api/v1/graph/status")
    assert r.status_code == 200
    data = r.json()
    assert "ok" in data and data["ok"] is True

    r = client.post("/api/v1/graph/register/nodeA")
    assert r.status_code == 200
    r = client.post("/api/v1/graph/register/nodeB")
    assert r.status_code == 200
    r = client.post("/api/v1/graph/edge/nodeA/nodeB")
    assert r.status_code == 200

    r = client.get("/api/v1/graph/dump")
    assert r.status_code == 200
    graph = r.json()
    assert "nodes" in graph and "nodeA" in graph["nodes"]
    assert "edges" in graph and any(e["src"] == "nodeA" and e["dst"] == "nodeB" for e in graph["edges"]) 

    # save graph to disk
    r = client.post("/api/v1/graph/save")
    assert r.status_code == 200
    path = r.json().get("path")
    assert path is not None

    # clear in-memory and load back
    r = client.post("/api/v1/graph/load")
    assert r.status_code == 200

    # subgraph by node
    r = client.get("/api/v1/graph/subgraph", params={"node": "nodeA"})
    assert r.status_code == 200
    sub = r.json()
    assert "nodes" in sub and "nodeA" in sub["nodes"]

    # subgraph by category (no nodes yet with category)
    r = client.get("/api/v1/graph/subgraph", params={"category": "capability"})
    assert r.status_code == 200
    sub2 = r.json()
    assert "nodes" in sub2 and isinstance(sub2["nodes"], dict)
