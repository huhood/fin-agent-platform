from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_info() -> None:
    response = client.get("/api/info")

    assert response.status_code == 200
    assert response.json() == {
        "name": "fin-agent-platform",
        "version": "0.1.0",
    }


def test_create_agent() -> None:
    payload = {
        "name": "market-analysis-agent",
        "description": "分析金融市场数据",
    }

    response = client.post("/api/agents", json=payload)

    assert response.status_code == 200
    assert response.json() == payload


def test_create_agent_without_name() -> None:
    response = client.post(
        "/api/agents",
        json={"description": "缺少必填名称"},
    )

    assert response.status_code == 422