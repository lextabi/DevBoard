import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]


def test_health_endpoint():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_signup_missing_email():
    """Test signup with missing email"""
    response = client.post(
        "/api/v1/auth/signup",
        json={"password": "password123"}
    )
    assert response.status_code in [400, 422]


def test_login_missing_credentials():
    """Test login with missing credentials"""
    response = client.post(
        "/api/v1/auth/login",
        json={}
    )
    assert response.status_code in [400, 422]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
