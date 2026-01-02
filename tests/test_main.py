import pytest
from httpx import ASGITransport, AsyncClient

from nexus_ai_gateway.main import app


@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client


@pytest.mark.asyncio
async def test_health_check(client):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "version": "1.0.0",
        "mode": "production",
    }


@pytest.mark.asyncio
async def test_predict_success(client):
    payload = {"input_text": "Explain quantum physics", "model_name": "gpt-4-turbo"}
    response = await client.post("/predict", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "AI processing complete" in data["result"]


@pytest.mark.asyncio
async def test_predict_validation_error(client):
    payload = {"input_text": "hi", "model_name": "gpt-4-turbo"}
    response = await client.post("/predict", json=payload)

    assert response.status_code == 422
    assert "String should have at least 5 characters" in response.text
