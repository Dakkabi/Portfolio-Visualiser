import pytest
from cryptography.fernet import InvalidToken

from backend.src.services.auth.security_service import *


def test_hash_and_verify():
    password1 = "unittesting"
    password2 = "test_hash1"

    assert verify_password(password1, hash_password(password1))
    assert not verify_password(password1, hash_password(password2))

def test_generate_key_from_password():
    password1 = "unittesting"
    password2 = "iscool"

    salt = generate_salt()
    new_salt = generate_salt()

    assert new_salt != salt

    key1 = generate_key_from_password(password1, salt)
    key2 = generate_key_from_password(password2, salt)

    assert key1 != key2
    assert isinstance(key1, bytes)

def test_encrypt_and_decrypt():
    salt = generate_salt()

    password = "unittesting"

    plaintext = "Inconceivable!"

    ciphertext = encrypt_data(plaintext, password, salt)

    assert plaintext != ciphertext
    assert plaintext == decrypt_data(ciphertext, password, salt)

    with pytest.raises(InvalidToken):
        decrypt_data(ciphertext, "WrongPassword?", salt)
