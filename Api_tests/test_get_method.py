import requests
from .consts import URL

API_URL = URL

def test_get_all_posts():
    # Test case №1: Получение всех постов
    response = requests.get(API_URL + "posts")
    assert response.status_code == 200

    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) > 0

def test_get_post_by_id():
    # Test case №2: Получение поста по id
    post_id = 1
    response = requests.get(API_URL + f"posts/{post_id}")
    assert response.status_code == 200

    post = response.json()
    assert isinstance(post, dict)
    assert post["id"] == post_id

def test_get_posts_with_parameters():
    # Test case №3: Получение постов с определенными параметрами
    params = {
        "userId": 1,
        "title": "Test Title"
    }
    response = requests.get(API_URL + "posts", params=params)
    assert response.status_code == 200

    posts = response.json()
    assert isinstance(posts, list)

    for post in posts:
        assert post["userId"] == params["userId"]
        assert params["title"] in post["title"]
