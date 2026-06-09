from fastapi.testclient import TestClient
from backend.app.main import app


def test_graph_endpoints(tmp_path):
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

    # populate graph from skill packages and import dependencies
    r = client.post("/api/v1/graph/populate")
    assert r.status_code == 200
    pop = r.json()
    assert pop["ok"] is True
    assert "market_analysis" in client.get("/api/v1/graph/dump").json()["nodes"]
    assert pop["edges"] > 0

    graph = client.get("/api/v1/graph/dump").json()
    assert any(
        e["src"] == "backend.app.guard.risk_guard" and e["dst"] == "skills.risk_management"
        for e in graph["edges"]
    )

    # save/load using a temp path
    temp_path = tmp_path / "enterprise_graph.json"
    r = client.post("/api/v1/graph/save", params={"path": str(temp_path)})
    assert r.status_code == 200
    assert temp_path.exists()

    r = client.post("/api/v1/graph/load", params={"path": str(temp_path)})
    assert r.status_code == 200

    r = client.get("/api/v1/graph/subgraph", params={"node": "market_analysis"})
    assert r.status_code == 200
    sdata = r.json()
    assert "nodes" in sdata and "market_analysis" in sdata["nodes"]
