from backend.src.core.services.auth.cryptography_service import verify_password


def test_verify_password():
    assert not verify_password("", "")