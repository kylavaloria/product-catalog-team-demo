from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_products_returns_all_products_by_default():
    response = client.get("/products")

    assert response.status_code == 200
    assert [item["name"] for item in response.json()] == [
        "Rice",
        "Milk",
        "Coffee",
        "Bread",
    ]
