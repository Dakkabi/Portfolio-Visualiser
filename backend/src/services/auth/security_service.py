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

def encrypt_data(plaintext, password : str, salt : bytes) -> str:
    """
    Encrypt data using a salt and password as key.

    :param plaintext: Plaintext data to encrypt into ciphertext.
    :param password: Password to derive an encryption key.
    :param salt: Salt to use for key generation.

    :return: Encrypted data as String.
    """
    key = generate_key_from_password(password, salt)
    fernet = Fernet(key)

    plaintext = plaintext.encode("utf-8")
    token = fernet.encrypt(plaintext)

    return token.decode("utf-8")

def decrypt_data(ciphertext : str, password : str, salt : bytes) -> str:
    """
    Decrypt encrypted data using a salt and password as key.

    :param ciphertext: Encrypted data to decrypt into plaintext.
    :param password: Password to derive an encryption key.
    :param salt: Salt to use for key generation.

    :return: Decrypted data as String.

    :raises InvalidToken: The key is incorrect and has returned junk.
    """
    key = generate_key_from_password(password, salt)
    fernet = Fernet(key)

    plaintext = fernet.decrypt(ciphertext)

    return plaintext.decode("utf-8")