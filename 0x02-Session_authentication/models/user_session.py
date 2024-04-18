#!/usr/bin/env python3
"""Define the UserSession class for managing user session data"""

from models.base import Base


class UserSession(Base):
    """
    UserSession class for managing user session data
    """

    def __init__(self, *args: list, **kwargs: dict):
        """
        Initialize a UserSession instance
        Args:
            *args (list): List of positional arguments
            **kwargs (dict): Dictionary of keyword arguments
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get("user_id")
        self.session_id = kwargs.get("session_id")