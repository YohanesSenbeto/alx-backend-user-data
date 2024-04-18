#!/usr/bin/env python3
"""
Basic Auth module
"""

from api.v1.auth.auth import Auth
from typing import TypeVar, List
from models.user import User
import base64
import binascii


class BasicAuth(Auth):
    """
    A class for Basic Authentication
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header for a Basi
        Returns None if the header is None, not a string, or does not start
        """
        if (
            authorization_header is None
            or not isinstance(authorization_header, str)
            or not authorization_header.startswith("Basic")
        ):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        Decodes the value of a Base64 string.
        Returns None if the input is not a valid Base64 string.
        """
        b64_auth_header = base64_authorization_header
        if b64_auth_header and isinstance(b64_auth_header, str):
            try:
                encode = b64_auth_header.encode("utf-8")
                base = base64.b64decode(encode)
                return base.decode("utf-8")
            except binascii.Error:
                return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Extracts the user email and password from the Base64 decoded value.
        Returns (None, None) if the decoded value is not in the correct format.
        """
        decoded_64 = decoded_base64_authorization_header
        if decoded_64 and isinstance(decoded_64, str) and ":" in decoded_64:
            res = decoded_64.split(":", 1)
            return (res[0], res[1])
        return (None, None)

    def user_object_from_credentials(
        self, user_email: str, user_password: str
    ) -> TypeVar("User"):
        """
        Retrieves the User instance based on the provided email and password.
        Returns None if the user is not found or the password is invalid.
        """
        try:
            users: List[User] = User.search({"email": user_email})
            if len(users) > 0 and users[0].is_valid_password(user_password):
                return users[0]
        except Exception:
            return None
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Overrides the current_user method from the Auth class.
        Retrieves the User instance for the given request.
        """
        header = self.authorization_header(request)
        b64header = self.extract_base64_authorization_header(header)
        decoded = self.decode_base64_authorization_header(b64header)
        user_creds = self.extract_user_credentials(decoded)
        return self.user_object_from_credentials(*user_creds)
