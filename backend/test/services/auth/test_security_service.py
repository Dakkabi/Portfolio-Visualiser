import pytest
from cryptography.fernet import InvalidToken

from backend.src.services.auth.security_service import *


@pytest.fixture
def users():
    return [
        {
            "user_id": 1,
            "password": "secret"
        },
        {
            "user_id": 2,
            "password": "Montoya"
        }
    ]

def test_hash_and_verify():
    password1 = "unittesting"
    password2 = "test_hash1"

    assert verify_password(password1, hash_password(password1))
    assert not verify_password(password1, hash_password(password2))

def test_generate_key_from_password(users):

    result_user1 = generate_key_from_password(users[0]["user_id"], users[0]["password"])
    result_user2 = generate_key_from_password(users[1]["user_id"], users[1]["password"])

    assert not result_user1 == result_user2

    assert result_user1 == generate_key_from_password(users[0]["user_id"], users[0]["password"]) # Deterministic?

    # Assert that another user using the same password as a previous user does not result
    # in the same key.
    assert not generate_key_from_password(users[1]["user_id"], users[0]["password"]) == result_user1

def test_encrypt_and_decrypt(users):
    user1_plaintext = "Hello, World!"

    user1_key = generate_key_from_password(users[0]["user_id"], users[0]["password"])
    user2_key = generate_key_from_password(users[1]["user_id"], users[1]["password"])

    user1_ciphertext = encrypt_data(user1_plaintext, user1_key)
    user2_ciphertext = encrypt_data(user1_plaintext, user2_key)

    assert not user1_ciphertext == user1_plaintext
    assert not user2_ciphertext == user1_ciphertext

    assert decrypt_data(user1_ciphertext, user1_key) == user1_plaintext

    with pytest.raises(InvalidToken):
        decrypt_data(user2_ciphertext, user1_key)




