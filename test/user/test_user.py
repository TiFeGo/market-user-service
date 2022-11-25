import pytest
from httpx import AsyncClient
from faker import Faker

from src.endpoints.auth.jwt import create_access_token
from test.conf_test_db import app


@pytest.mark.asyncio
async def test_all_users():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        user_access_token = create_access_token({"sub": "alex@gmail.com"})
        response = await ac.get("/users/", headers={'Authorization': f'Bearer {user_access_token}'})
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_registration():
    fake = Faker()
    data = {
        "name": fake.name(),
        "email": fake.email(),
        "password": fake.password()
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/users/", json=data)
    assert response.status_code == 201
