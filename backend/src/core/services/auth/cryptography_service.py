from cryptography.fernet import Fernet
from bcrypt import hashpw, gensalt, checkpw

def generate_key() -> str:
    """Generates a URL-safe base64-encoded 32-byte key, and returns it decoded to string."""
    return Fernet.generate_key().decode("utf-8")

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
