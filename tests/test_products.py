from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

EXPECTED_PRODUCTS = [
    {"id": 1, "name": "Rice", "in_stock": True},
    {"id": 2, "name": "Milk", "in_stock": False},
    {"id": 3, "name": "Coffee", "in_stock": True},
    {"id": 4, "name": "Bread", "in_stock": False},
]

def test_list_products_returns_all_products_by_default():
    response = client.get("/products")

    assert response.status_code == 200
    assert response.json() == EXPECTED_PRODUCTS


def test_list_products_filters_in_stock_products_when_requested():
    response = client.get("/products?in_stock_only=true")

    assert response.status_code == 200
    assert response.json() == [EXPECTED_PRODUCTS[0], EXPECTED_PRODUCTS[2]]


def test_list_products_returns_all_products_when_filter_is_false():
    response = client.get("/products?in_stock_only=false")

    assert response.status_code == 200
    assert response.json() == EXPECTED_PRODUCTS
