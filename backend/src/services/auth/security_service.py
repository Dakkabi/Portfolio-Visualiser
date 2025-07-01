import base64
from hashlib import sha256

from bcrypt import hashpw, gensalt, checkpw
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def hash_password(password : str) -> str:
    return hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")

def verify_password(plain_password : str, hashed_password : str) -> bool:
    return checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

def generate_key_from_password(user_id: int, password : str) -> str:
    """
    Derive an encryption key from a password.

    :param user_id: User ID to generate a deterministic salt from.
    :param password: The password to derive an encryption key from.
    :return: A base64 url-safe encoded key.
    """
    salt = sha256(str(user_id).encode("utf-8")).digest()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )

    key = kdf.derive(password.encode("utf-8"))
    encoded_key = base64.urlsafe_b64encode(key).decode("utf-8")
    return encoded_key

def encrypt_data(plaintext, secret_key : str) -> str:
    """
    Encrypt data using a salt and password as key.

    :param plaintext: Plaintext data to encrypt into ciphertext.
    :param secret_key: Secret key to encrypt the plaintext with.

    :return: Encrypted ciphertext as String.
    """
    fernet = Fernet(secret_key)

    plaintext = plaintext.encode("utf-8")
    token = fernet.encrypt(plaintext)

    return token.decode("utf-8")

def decrypt_data(ciphertext : str, secret_key : str) -> str:
    """
    Decrypt encrypted data using a salt and password as key.

    :param ciphertext: Encrypted data to decrypt into plaintext.
    :param secret_key: Secret key to decrypt the ciphertext with.

    :return: Decrypted plaintext as String.

    :raises InvalidToken: The key is incorrect and has returned junk.
    """
    fernet = Fernet(secret_key)

    plaintext = fernet.decrypt(ciphertext)

    return plaintext.decode("utf-8")