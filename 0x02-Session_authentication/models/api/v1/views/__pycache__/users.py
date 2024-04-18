#!/usr/bin/env python3
"""User module containing User class"""

import hashlib
from models.base import Base


class User(Base):
    """User class representing a user entity"""

    def __init__(self, *args: list, **kwargs: dict):
        """Initialize a User instance"""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email')  # Email of the user
        self._password = kwargs.get('_password')  # Encrypted password
        self.first_name = kwargs.get('first_name')  # First name of the user
        self.last_name = kwargs.get('last_name')  # Last name of the user

    @property
    def password(self) -> str:
        """Getter method for the password"""
        return self._password

    @password.setter
    def password(self, pwd: str):
        """Setter method for the password, encrypts in SHA256"""
        if pwd is None or not isinstance(pwd, str):
            self._password = None
        else:
            self._password = hashlib.sha256(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd: str) -> bool:
        """Validate a password"""
        if pwd is None or not isinstance(pwd, str):
            return False
        if self.password is None:
            return False
        return hashlib.sha256(pwd.encode()).hexdigest().lower() == self.password

    def display_name(self) -> str:
        """Display User name based on email/first_name/last_name"""
        if not any([self.email, self.first_name, self.last_name]):
            return ""
        if not self.first_name and not self.last_name:
            return "{}".format(self.email)
        if not self.last_name:
            return "{}".format(self.first_name)
        if not self.first_name:
            return "{}".format(self.last_name)
        return "{} {}".format(self.first_name, self.last_name)
