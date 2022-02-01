import pytest
from httpx import AsyncClient

from app.main import app

BASE_URL="http://localhost"

@pytest.mark.anyio
async def test_root():
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "LLA DevOps test"}


@pytest.mark.anyio
async def test_people():
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        response = await ac.get("/people")
    assert response.status_code == 200
    assert response.json()['count'] > 0

@pytest.mark.anyio
async def test_people_serch():
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        response = await ac.get("/people?search=yoda")
    assert response.status_code == 200
    assert response.json()['count'] == 1

@pytest.mark.anyio
async def test_people_page():
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        response = await ac.get("/people?page=2")
    assert response.status_code == 200
    assert response.json()['previous'] != ""

@pytest.mark.anyio
async def test_person():
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        response = await ac.get("/people/1")
    assert response.status_code == 200
    assert response.json()['name'] == "Luke Skywalker"