from core.security import hash_password, verify_password

def test_hash_and_verify():
    password1 = "unittesting"
    password2 = "test_hash1"

    assert verify_password(password1, hash_password(password1))
    assert not verify_password(password1, hash_password(password2))