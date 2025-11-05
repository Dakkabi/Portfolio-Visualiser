import base64
import os
from typing import Optional

from bcrypt import hashpw, gensalt, checkpw
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305

from backend.src.core.config_loader import settings

def get_password_hash(password: str) -> str:
    return hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))
    except ValueError:
        return False

def generate_symmetric_key() -> str:
    return base64.b64encode(ChaCha20Poly1305.generate_key()).decode("utf-8")

def decode_to_bytes(data: str) -> bytes:
    return base64.b64decode(data.encode("utf-8"))

def encode_to_str(data: bytes) -> str:
    return base64.b64encode(data).decode("utf-8")

def generate_nonce(size: int = 12) -> bytes:
    return os.urandom(size)

AES_SECRET_KEY = decode_to_bytes(settings.AES_SECRET_KEY)
CHACHA = ChaCha20Poly1305(AES_SECRET_KEY)

def encrypt_api_key(api_key: str) -> str:
    nonce = generate_nonce()
    ciphertext = CHACHA.encrypt(nonce, api_key.encode("utf-8"), b"")
    return f"{encode_to_str(ciphertext)}::{encode_to_str(nonce)}"

def maybe_encrypt_api_key(api_key: Optional[str]) -> str | None:
    """Check if the input is not a None object before encrypting, good for areas where a None attribute is valid."""
    if api_key is None:
        return None
    return encrypt_api_key(api_key)

def decrypt_api_key(encrypted_api_key: str) -> str:
    ciphertext, nonce = encrypted_api_key.split("::")
    return CHACHA.decrypt(decode_to_bytes(nonce), decode_to_bytes(ciphertext), b"").decode("utf-8")

def maybe_decrypt_api_key(api_key: Optional[str]) -> str | None:
    """Check if the input is not a None object before decrypting, good for areas where a None attribute is valid."""
    if api_key is None:
        return None
    return decrypt_api_key(api_key)

if __name__ == "__main__":
    print(generate_symmetric_key())