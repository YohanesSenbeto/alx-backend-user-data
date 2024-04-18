#!/usr/bin/env python3
"""
Module containing views for user authentication
"""

import os
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def auth_session():
    """
    Handle user login
    Returns:
        dict: A dictionary representation of the user if found, else an error message
    """
    email = request.form.get("email")
    password = request.form.get("password")

    # Check if email is provided
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400

    # Check if password is provided
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    # Search for users with the provided email
    users = User.search({"email": email})

    # If no users found, return an error
    if not users or users == []:
        return jsonify({"error": "no user found for this email"}), 404

    # Check each user's password
    for user in users:
        if user.is_valid_password(password):
            # If password is valid, create a session for the user
            from api.v1.app import auth

            session_id = auth.create_session(user.id)
            resp = jsonify(user.to_json())
            session_name = os.getenv("SESSION_NAME")
            resp.set_cookie(session_name, session_id)
            return resp

    # If no user with the provided password is found, return an error
    return jsonify({"error": "wrong password"}), 401


@app_views.route("/auth_session/logout", methods=["DELETE"], strict_slashes=False)
def handle_logout():
    """
    Handle user logout
    Returns:
        dict: An empty dictionary (with a 200 status code) if logout is successful,
              else raise a 404 error
    """
    from api.v1.app import auth

    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
