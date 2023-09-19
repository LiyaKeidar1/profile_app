import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_add_url(client):
    response = client.post('/submit', data={
        'url': 'https://example.com',
        'title': 'Example',
        'description': 'An example website',
    }, follow_redirects=True)
    assert response.status_code == 200

if __name__ == '__main__':
    pytest.main()

