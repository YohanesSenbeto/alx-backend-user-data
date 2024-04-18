#!/usr/bin/env python3
"""
Define SessionExpAuth class that extends SessionAuth and adds expiration functionality to session IDs
"""
import os
from datetime import datetime, timedelta
from .session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """
    SessionExpAuth class extends SessionAuth to handle session expiration
    """

    def __init__(self):
        """
        Initializes the class with session duration
        """
        try:
            duration = int(os.getenv("SESSION_DURATION"))
        except Exception:
            duration = 0
        self.session_duration = duration

    def create_session(self, user_id=None):
        """
        Creates a session ID for a given user ID
        Args:
            user_id (str): User ID
        Returns:
            session_id (str): Session ID
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_data = {"user_id": user_id, "created_at": datetime.now()}
        self.user_id_by_session_id[session_id] = session_data
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns the user ID associated with a session ID
        Args:
            session_id (str): Session ID
        Returns:
            user_id (str): User ID
        """
        if session_id is None:
            return None
        session_data = self.user_id_by_session_id.get(session_id)
        if session_data is None or "created_at" not in session_data:
            return None
        if self.session_duration <= 0:
            return session_data.get("user_id")
        created_at = session_data.get("created_at")
        expiration_time = created_at + timedelta(seconds=self.session_duration)
        if expiration_time < datetime.now():
            return None
        return session_data.get("user_id")
