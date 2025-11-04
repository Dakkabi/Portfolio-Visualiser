import base64
import os

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

def get_key_in_bytes(key: str) -> bytes:
    return base64.b64decode(key.encode("utf-8"))

def generate_nonce(size: int = 16) -> bytes:
    return os.urandom(size)

AES_SECRET_KEY = get_key_in_bytes(settings.AES_SECRET_KEY)
CHACHA = ChaCha20Poly1305(AES_SECRET_KEY)

def encrypt_api_key(api_key: str) -> str:
    nonce = generate_nonce()
    ciphertext = CHACHA.encrypt(nonce, api_key.encode("utf-8"), b"")
    return f"{base64.b64encode(ciphertext).decode("utf-8")}::{nonce.decode("utf-8")}"

def decrypt_api_key(encrypted_api_key: str) -> str:
    ciphertext, nonce = encrypted_api_key.split("::")
    ciphertext = base64.b64decode(ciphertext.encode("utf-8"))
    return CHACHA.decrypt(nonce.encode("utf-8"), ciphertext, b"").decode("utf-8")

if __name__ == "__main__":
    print(generate_symmetric_key())