from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Manufacturing Quality API is running"


def test_get_identifiers():
    response = client.get("/identifiers")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_existing_identifier():
    response = client.get("/identifiers/88823141")
    assert response.status_code == 200

    data = response.json()
    assert data["identifier_name"] == "88823141"
    assert data["description"] == "Shampoo Product"
    assert data["identifier_type"] == "Finished Product Part"


def test_get_nonexistent_identifier():
    response = client.get("/identifiers/99999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Identifier not found"


def test_create_identifier():
    new_identifier = {
        "identifier_name": "TEST001",
        "description": "Test Product",
        "identifier_type": "Test Type"
    }

    response = client.post("/identifiers", json=new_identifier)

    assert response.status_code == 200

    data = response.json()
    assert data["identifier_name"] == "TEST001"
    assert data["description"] == "Test Product"
    assert data["identifier_type"] == "Test Type"


def test_delete_identifier():
    response = client.delete("/identifiers/TEST001")

    assert response.status_code == 200
    assert response.json()["message"] == "Identifier deleted successfully"


def test_delete_nonexistent_identifier():
    response = client.delete("/identifiers/NOT_FOUND")

    assert response.status_code == 404
    assert response.json()["detail"] == "Identifier not found"