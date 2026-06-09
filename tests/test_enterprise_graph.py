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
