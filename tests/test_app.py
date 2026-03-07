import pytest
from httpx import AsyncClient
from src.app import app

@pytest.mark.asyncio
async def test_list_activities():
    # Arrange
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Act
        response = await ac.get("/activities")
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

@pytest.mark.asyncio
async def test_signup_activity():
    # Arrange
    payload = {"activity": "Chess Club", "email": "newstudent@mergington.edu"}
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Act
        response = await ac.post("/signup", json=payload)
    # Assert
    assert response.status_code in (200, 201, 400)
    assert "message" in response.json()
