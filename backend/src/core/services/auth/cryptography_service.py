from bcrypt import hashpw, gensalt, checkpw
from cryptography.fernet import Fernet

from backend.src.core.config import settings

FERNET_KEY = Fernet(settings.FERNET_MASTER_KEY.encode("utf-8"))

def encrypt_string(plaintext: str) -> str | None:
    """Encrypt a string input using Fernet, return None if no plaintext."""
    if plaintext is None: return None
    return FERNET_KEY.encrypt(plaintext.encode("utf-8")).decode("utf-8")

def decrypt_string(ciphertext: str) -> str | None:
    """Decrypt an encrypted string using Fernet, return None if no ciphertext."""
    if ciphertext is None: return None
    return FERNET_KEY.decrypt(ciphertext.encode("utf-8")).decode("utf-8")

def get_password_hash(password: str) -> str:
    """Return the hash of an input.

    :param password: The input to hash.
    :return: The hash of the password decoded to string.
    """
    return hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify the hash of the challenge input matches the hashed password.

    :param plain_password: The input to hash and compare against the hashed password.
    :param hashed_password: The hash.
    :return: A boolean, true if the hashes match, False otherwise.
    """
    try:
        return checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))
    except ValueError:
        return False
