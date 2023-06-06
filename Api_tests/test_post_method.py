import requests
from .consts import URL

API_URL = URL

def test_create_post_success():
    # Test case №1: Создание поста
    data = {
        "title": "Test Post",
        "body": "This is a test post",
        "userId": 1
    }
    response = requests.post(API_URL + "posts", json=data)
    assert response.status_code == 201

    created_post = response.json()
    assert isinstance(created_post, dict)
    assert created_post["title"] == data["title"]
    assert created_post["body"] == data["body"]
    assert created_post["userId"] == data["userId"]


def test_create_post_missing_field():
    # Test case №2: Создание поста с отсутствующим обязательным полем
    data = {
        "title": "Test Post",
        # Отсутствующее поле "body"
        "userId": 1
    }
    response = requests.post(API_URL + "posts", json=data)
    
    assert response.status_code == 400, f"Expected status code 400, but received {response.status_code}"

    error_message = response.json()
    assert "body" in error_message, "Expected 'body' field to be in the error message"
    assert "required" in error_message["body"], "Expected 'body' field to be marked as required in the error message"

def test_create_post_additional_field():
    # Test case №3: Создание поста с дополнительным необязательным полем
    data = {
        "title": "Test Post",
        "body": "This is a test post",
        "userId": 1,
        "extraField": "Additional field value"
    }
    response = requests.post(API_URL + "posts", json=data)

    assert response.status_code == 201, f"Expected status code 201, but received {response.status_code}"

    created_post = response.json()
    assert "id" in created_post, "Expected 'id' field in the created post"
    assert created_post["extraField"] == data["extraField"], "Unexpected value for the additional field in the created post"

def test_create_post_empty_payload():
    # Test case №4: Создание поста с пустыми данными
    data = {}
    response = requests.post(API_URL + "posts", json=data)

    assert response.status_code == 400, f"Expected status code 400, but received {response.status_code}"

    error_message = response.json()
    assert "title" in error_message, "Expected 'title' field to be in the error message"
    assert "required" in error_message["title"], "Expected 'title' field to be marked as required in the error message"


