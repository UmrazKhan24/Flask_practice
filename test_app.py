import pytest
import json
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, Bijaiya World!V2" in response.data


    
def test_predict(client):
    test_data={'Gender':"Male", 'Married':"Unmarried",'Credit_History' : "Unclear Debts",'ApplicantIncome':100000,'LoanAmount':2000000}
    resp=client.post('/prediction', json=test_data)
    assert resp.status_code == 200
    assert resp.json=={'loan_approval_status': 'Rejected'}

def test_ping(client):
    """Test the ping endpoint"""
    response = client.get("/ping")
    assert response.status_code == 200
    assert b"Ping Bijaiya ping ping ping!" in response.data

def test_aboutus(client):
    """Test the aboutus endpoint"""
    response = client.get("/aboutus")
    assert response.status_code == 200
    assert b"We are the Bijaiya team. We are here to help you with your IT needs." in response.data
    



