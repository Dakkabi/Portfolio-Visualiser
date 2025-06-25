import base64
from bcrypt import hashpw, gensalt, checkpw
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def hash_password(password : str) -> str:
    return hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")

def verify_password(plain_password : str, hashed_password : str) -> bool:
    return checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

def generate_salt() -> bytes:
    """
    Create a random salt.

    :return: Random salt.
    """
    return gensalt()

def generate_key_from_password(password : str, salt : bytes) -> bytes:
    """
    Derive an encryption key from a password.
    """
    key = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    return base64.urlsafe_b64encode(key.derive(password.encode("utf-8")))