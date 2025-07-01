import pytest
from cryptography.fernet import InvalidToken

from backend.src.services.auth.security_service import *


def test_hash_and_verify():
    password1 = "unittesting"
    password2 = "test_hash1"

    assert verify_password(password1, hash_password(password1))
    assert not verify_password(password1, hash_password(password2))

def test_generate_key_from_password():
    user1 = {
        "user_id": 1,
        "password": "secret"
    }
    user2 = {
        "user_id": 2,
        "password": "Montoya"
    }

    result_user1 = generate_key_from_password(user1["user_id"], user1["password"])
    result_user2 = generate_key_from_password(user2["user_id"], user2["password"])

    assert not result_user1 == result_user2

    assert result_user1 == generate_key_from_password(user1["user_id"], user1["password"]) # Deterministic?

    # Assert that another user using the same password as a previous user does not result
    # in the same key.
    assert not generate_key_from_password(user2["user_id"], user1["password"]) == result_user1

def test_encrypt_and_decrypt():
    pass
