import unittest
from your_project.repository import YourRepositoryClass
from your_project.models import YourModelClass

class TestYourRepository(unittest.TestCase):
    def setUp(self):
        self.repo = YourRepositoryClass()
        self.sample_data = YourModelClass(id=1, name="Sample")

    def tearDown(self):
        pass

def test_create(self):
    result = self.repo.create(self.sample_data)
    self.assertIsNotNone(result.id)  
    self.assertEqual(result.name, "Sample")  

def test_get_by_id(self):
    self.repo.create(self.sample_data)
    result = self.repo.get_by_id(1)
    self.assertIsNotNone(result)
    self.assertEqual(result.id, 1)

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_contacts():
    response = client.get("/contacts")
    assert response.status_code == 200
    assert isinstance(response.json(), list) 
    if response.json():
        for contact in response.json():
            assert "name" in contact
            assert "email" in contact
            assert "phone" in contact

def test_get_contact_by_id():
    contact_id = 1  
    response = client.get(f"/contacts/{contact_id}")
    assert response.status_code == 200
    assert "name" in response.json()
    assert "email" in response.json()
    assert "phone" in response.json()

def test_get_contact_by_id_not_found():
    contact_id = 999  
    response = client.get(f"/contacts/{contact_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Contact not found"}

def test_create_contact():
    new_contact = {
        "name": "Test User",
        "email": "testuser@example.com",
        "phone": "1234567890"
    }
    response = client.post("/contacts", json=new_contact)
    assert response.status_code == 201
    assert response.json()["name"] == "Test User"
    assert response.json()["email"] == "testuser@example.com"
    assert response.json()["phone"] == "1234567890"

def test_create_contact_invalid_data():
    new_contact = {
        "name": "",
        "email": "invalid-email",
        "phone": "123"  
    }
    response = client.post("/contacts", json=new_contact)
    assert response.status_code == 422 

def test_update_contact():
    contact_id = 1  
    updated_contact = {
        "name": "Updated User",
        "email": "updateduser@example.com",
        "phone": "0987654321"
    }
    response = client.put(f"/contacts/{contact_id}", json=updated_contact)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated User"
    assert response.json()["email"] == "updateduser@example.com"
    assert response.json()["phone"] == "0987654321"

def test_update_contact_not_found():
    contact_id = 999 
    updated_contact = {
        "name": "Updated User",
        "email": "updateduser@example.com",
        "phone": "0987654321"
    }
    response = client.put(f"/contacts/{contact_id}", json=updated_contact)
    assert response.status_code == 404
    assert response.json() == {"detail": "Contact not found"}

def test_delete_contact():
    contact_id = 1 
    response = client.delete(f"/contacts/{contact_id}")
    assert response.status_code == 204 

def test_delete_contact_not_found():
    contact_id = 999  
    response = client.delete(f"/contacts/{contact_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Contact not found"}

def test_rate_limiting():
    new_contact = {
        "name": "Rate Limited User",
        "email": "ratelimiteduser@example.com",
        "phone": "1111111111"
    }
    for _ in range(10):  
        response = client.post("/contacts", json=new_contact)
    
    response = client.post("/contacts", json=new_contact)
    assert response.status_code == 429  

def test_email_verification():
    response = client.get("/verify-email/token")
    assert response.status_code == 200
    assert response.json() == {"message": "Email verified successfully"}

def test_email_verification_invalid_token():
    response = client.get("/verify-email/invalidtoken")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid token"}

def test_update_avatar():
    contact_id = 1  
    avatar_url = "http://example.com/avatar.jpg"
    response = client.put(f"/contacts/{contact_id}/avatar", json={"avatar_url": avatar_url})
    assert response.status_code == 200
    assert response.json()["avatar_url"] == avatar_url


