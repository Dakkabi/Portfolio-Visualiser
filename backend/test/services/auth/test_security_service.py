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