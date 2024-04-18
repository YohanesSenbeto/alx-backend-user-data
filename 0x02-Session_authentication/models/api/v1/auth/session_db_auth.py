#!/usr/bin/env python3
"""
Define SessionDBAuth class that extends SessionExpAuth and persists session data in a database
"""
from .session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """
    SessionDBAuth class extends SessionExpAuth to persist session data in a database
    """

    def create_session(self, user_id=None):
        """
        Create a session ID for a given user ID and save it in the database
        Args:
           user_id (str): User ID
        Returns:
            session_id (str): Session ID
        """
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        session_data = {"user_id": user_id, "session_id": session_id}
        user = UserSession(**session_data)
        user.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns the user ID associated with a session ID retrieved from the database
        Args:
            session_id (str): Session ID
        Returns:
            user_id (str): User ID
        """
        user_session = UserSession.search({"session_id": session_id})
        if user_session:
            return user_session[0].user_id
        return None

    def destroy_session(self, request=None):
        """
        Destroy a UserSession instance based on a Session ID from a request cookie
        Args:
            request: Request object containing the session cookie
        Returns:
            bool: True if session is destroyed successfully, False otherwise
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        user_session = UserSession.search({"session_id": session_id})
        if user_session:
            user_session[0].remove()
            return True
        return False
