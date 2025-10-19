import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from bookstore.models import Book, Author, Publisher

@pytest.fixture(scope="function")
def api_client() -> APIClient:
    yield APIClient()

@pytest.fixture(scope="function")
def user() -> User:
    yield User.objects.create_user(
        username='user',
        password='12345678',
        email='user@gmail.com',
    )

@pytest.fixture(scope="function")
def admin() -> User:
    yield User.objects.create_superuser(
        username='admin',
        password='12345678',
        email='admin@gmail.com',
    )

@pytest.fixture(scope="function")
def author() -> Author:
    return Author.objects.create(name="Test Author")


@pytest.fixture(scope="function")
def publisher() -> Publisher:
    return Publisher.objects.create(name="Test Publisher")

@pytest.fixture(scope="function")
def book(author, publisher) -> Book:
    return Book.objects.create(
        id=1,
        name="Book 1",
        author=author,
        publisher=publisher,
        genre="fantasy",
        price=200,
        popularity=5,
        description="Test book",
    )