import pytest
from Receipt_processor import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_process_receipt(client):
    response = client.post('/receipts/process', json={
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [{"shortDescription": "Mountain Dew 12PK", "price": "6.50"},
                  {"shortDescription": "Emils Cheese Pizza","price": "12.25"}],
        "total": "18.75"
    })
    assert response.status_code == 200
    assert "id" in response.get_json()

def test_get_receipt_points(client):
    post_response = client.post('/receipts/process', json={
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [{"shortDescription": "Mountain Dew 12PK", "price": "6.50"},
                  {"shortDescription": "Emils Cheese Pizza","price": "12.25"}],
        "total": "18.75"
    })
    receipt_id = post_response.get_json().get("id")

    get_response = client.get(f'/receipts/{receipt_id}/points')
    assert get_response.status_code == 200
    assert "points" in get_response.get_json()