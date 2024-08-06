import pytest
from app import create_user, get_user
from settings import DATABASE

def setup_function():
    DATABASE.clear()

def test_create_user():
    user = create_user("Alice", 30)
    assert user.name == "Alice"
    assert user.age == 30
    assert len(DATABASE) == 1

def test_get_user():
    create_user("Bob", 25)
    user = get_user("Bob")
    assert user is not None
    assert user.name == "Bob"
    assert user.age == 25

def test_get_user_not_found():
    user = get_user("Charlie")
    assert user is None
