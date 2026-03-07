import pytest
from httpx import AsyncClient, ASGITransport
from src.app import app

@pytest.mark.anyio
async def test_list_activities():
    # Arrange
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Act
        response = await ac.get("/activities")
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

@pytest.mark.anyio
async def test_signup_for_activity():
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Act
        response = await ac.post(f"/activities/{activity_name}/signup", params={"email": email})
    # Assert
    assert response.status_code in (200, 201, 400)
    assert response.status_code != 404
