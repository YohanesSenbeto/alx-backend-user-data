#!/usr/bin/env python3
"""Module containing user views"""

import os
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def auth_session():
    """
    Handle user login
    Returns:
        Dictionary representation of user if found else error message
    """
    email = request.form.get("email")  # Retrieve email from form data
    password = request.form.get("password")  # Retrieve password from form data
    if email is None or email == "":
        return (
            jsonify({"error": "email missing"}),
            400,
        )  # Return error if email is missing
    if password is None or password == "":
        return (
            jsonify({"error": "password missing"}),
            400,
        )  # Return error if password is missing
    users = User.search({"email": email})  # Search for users with the given email
    if not users or users == []:
        return (
            jsonify({"error": "no user found for this email"}),
            404,
        )  # Return error if no user found
    for user in users:
        if user.is_valid_password(password):  # Check if the provided password is valid
            from api.v1.app import auth

            session_id = auth.create_session(
                user.id
            )  # Create a session ID for the user
            resp = jsonify(user.to_json())
            session_name = os.getenv("SESSION_NAME")
            resp.set_cookie(session_name, session_id)  # Set the session ID as a cookie
            return resp
    return (
        jsonify({"error": "wrong password"}),
        401,
    )  # Return error if password is incorrect


@app_views.route("/auth_session/logout", methods=["DELETE"], strict_slashes=False)
def handle_logout():
    """
    Handle user logout
    """
    from api.v1.app import auth

    if auth.destroy_session(request):  # Destroy the user session
        return jsonify({}), 200  # Return success response
    abort(404)  # Return error if session destruction fails
