import pytest
from fastapi.testclient import TestClient
from warehouse.main import app

client = TestClient(app)


def test_create_product():
    response = client.post("/products/", json={
        "name": "Test Product",
        "description": "This is a test product",
        "price": 99.99,
        "quantity": 10
    })
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["price"] == 99.99
    assert data["quantity"] == 10


def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_get_product_by_id():
    response = client.post("/products/", json={
        "name": "Another Test Product",
        "description": "This is another test product",
        "price": 49.99,
        "quantity": 5
    })
    product_id = response.json()["id"]
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Another Test Product"
    assert data["price"] == 49.99


def test_update_product():
    response = client.post("/products/", json={
        "name": "Product to Update",
        "description": "This product will be updated",
        "price": 19.99,
        "quantity": 8
    })
    product_id = response.json()["id"]
    response = client.put(f"/products/{product_id}", json={
        "name": "Updated Product",
        "description": "This product has been updated",
        "price": 29.99,
        "quantity": 15
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Product"
    assert data["price"] == 29.99
    assert data["quantity"] == 15


def test_delete_product():
    response = client.post("/products/", json={
        "name": "Product to Delete",
        "description": "This product will be deleted",
        "price": 15.99,
        "quantity": 3
    })
    product_id = response.json()["id"]
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 204
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 404
