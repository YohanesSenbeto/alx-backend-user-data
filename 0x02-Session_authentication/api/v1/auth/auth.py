#!/usr/bin/env python3
"""
Auth class
"""

from tabnanny import check
from flask import request
from typing import TypeVar, List

User = TypeVar("User")


class Auth:
    """
    A class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if the given path requires authentication.
        Returns False if the path is in the excluded_paths list, or if the path
        """
        check_path = path
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            check_path += "/"
        if check_path in excluded_paths or path in excluded_paths:
            return False
        return True

    def authorization_header(self, request_obj=None) -> str:
        """
        Retrieves the authorization header from the given request.
        Returns None if the request is None.
        """
        if request_obj is None:
            return None
        return request_obj.headers.get("Authorization")

    def current_user(self, request_obj=None) -> User:
        """
        Retrieves the current user from the given request.
        Returns None if the request is None.
        """
        return None
