import requests
from .consts import URL

API_URL = URL

def test_delete_existing_post():
    # Test case №1: Удаление существующего поста
    post_id = 1
    response = requests.delete(API_URL + f"posts/{post_id}")
    
    assert response.status_code == 200, f"Expected status code 200, but received {response.status_code}"


def test_delete_nonexistent_post():
    # Test case №2: Удаление несуществующего поста
    post_id = 1000
    response = requests.delete(API_URL + f"posts/{post_id}")
  
    assert response.status_code == 404, f"Expected status code 404, but received {response.status_code}"


def test_delete_multiple_posts():
    # Test case №3: Удаление нескольких постов
    post_ids = [1, 2, 3]  # ID постов для удаления
    for post_id in post_ids:
        response = requests.delete(API_URL + f"posts/{post_id}")

        assert response.status_code == 200, f"Expected status code 200, but received {response.status_code}"
