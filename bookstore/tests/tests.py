import pytest
from django.urls import reverse

from bookstore.models import Book


@pytest.mark.django_db
def test_get_book_list(api_client, book) -> None:
    response = api_client.get("/books", format="json")
    assert response.status_code == 200
    assert len(response.data) == 1

@pytest.mark.django_db
def test_get_book_empty_list(api_client) -> None:
    response = api_client.get("/books", format="json")
    assert response.status_code == 200
    assert response.data == []

@pytest.mark.django_db
def test_post_book_admin(api_client, admin, author, publisher) -> None:
    api_client.force_authenticate(user=admin)

    response = api_client.post("/books",
        {
            "name": "New Book",
            "author": author.id,
            "publisher": publisher.id,
            "genre": "fantasy",
            "price": 150,
            "popularity": 50,
            "description": "A new book for testing."
        }, format="json")

    assert response.status_code == 201
    assert Book.objects.count() == 1
    assert Book.objects.first().name == "New Book"

@pytest.mark.django_db
def test_post_book_regular_user(api_client, user, author, publisher) -> None:
    api_client.force_authenticate(user=user)

    response = api_client.post("/books",
        {
            "name": "New Book",
            "author": author.id,
            "publisher": publisher.id,
            "genre": "fantasy",
            "price": 150,
            "popularity": 50,
            "description": "A new book for testing."
        }, format="json")

    assert response.status_code == 403
    assert Book.objects.count() == 0

@pytest.mark.django_db
def test_get_book_id_with_auth(api_client, user, book) -> None:
    login_url = reverse('token_obtain_pair')
    tokens = api_client.post(login_url, {
        'username': 'user', 'password': '12345678'
    }, format="json").data

    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
    response = api_client.get(f"/books/{book.id}", format="json")

    assert response.status_code == 200
    assert response.data["name"] == book.name

@pytest.mark.django_db
def test_get_non_existing_book(api_client, user) -> None:
    login_url = reverse('token_obtain_pair')
    tokens = api_client.post(login_url, {
        'username': 'user', 'password': '12345678'
    }, format="json").data

    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
    response = api_client.get(f"/books/10", format="json")

    assert response.status_code == 404

@pytest.mark.django_db
def test_get_book_id_invalid_token(api_client, user, book) -> None:
    login_url = reverse('token_obtain_pair')
    api_client.post(login_url, {
        'username': 'user', 'password': '12345678'
    }, format="json")

    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer invalidtoken')
    response = api_client.get(f"/books/{book.id}", format="json")

    assert response.status_code == 401

@pytest.mark.django_db
def test_put_book_admin(api_client, admin, author, publisher, book) -> None:
    api_client.force_authenticate(user=admin)

    response = api_client.put(f"/books/{book.id}",
        {
            "name": "New Book",
            "author": author.id,
            "publisher": publisher.id,
            "genre": "fantasy",
            "price": 200,
            "popularity": 50,
            "description": "A new book for testing."
        }, format="json")

    assert response.status_code == 200
    assert Book.objects.first().price == 200

@pytest.mark.django_db
def test_put_book_regular_user(api_client, user, author, publisher, book) -> None:
    api_client.force_authenticate(user=user)

    response = api_client.put(f"/books/{book.id}",
        {
            "name": "New Book",
            "author": author.id,
            "publisher": publisher.id,
            "genre": "fantasy",
            "price": 200,
            "popularity": 50,
            "description": "A new book for testing."
        }, format="json")

    assert response.status_code == 403

@pytest.mark.django_db
def test_put_non_existing_book(api_client, admin, author, publisher, book) -> None:
    api_client.force_authenticate(user=admin)

    response = api_client.put(f"/books/10",
        {
            "name": "New Book",
            "author": author.id,
            "publisher": publisher.id,
            "genre": "fantasy",
            "price": 200,
            "popularity": 50,
            "description": "A new book for testing."
        }, format="json")

    assert response.status_code == 404

@pytest.mark.django_db
def test_delete_book_admin(api_client, admin, book):
    api_client.force_authenticate(user=admin)
    response = api_client.delete(f"/books/{book.id}")

    assert response.status_code == 204
    assert Book.objects.filter(id=book.id).exists() is False

@pytest.mark.django_db
def test_delete_book_user(api_client, user, book):
    api_client.force_authenticate(user=user)
    response = api_client.delete(f"/books/{book.id}")

    assert response.status_code in [401, 403]
    assert Book.objects.filter(id=book.id).exists() is True

@pytest.mark.django_db
def test_delete_non_existing_book(api_client, admin):
    api_client.force_authenticate(user=admin)
    response = api_client.delete("/books/10")

    assert response.status_code == 404