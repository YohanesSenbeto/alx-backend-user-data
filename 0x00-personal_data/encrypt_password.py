#!/usr/bin/env python3
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes the provided password.

    Args:
        password (str): A string representing the password to be hashed

    Returns:
        bytes: The hashed password as a byte string.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if the provided password matches the hashed password.

    Args:
        hashed_password (bytes): A byte string representing the hashed passwod
        password (str): A string representing the password to be checked.

    Returns:
        bool: True if the password matches the hashed password, False otherwis
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
