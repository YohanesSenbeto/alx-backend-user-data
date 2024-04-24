#!/usr/bin/env python3
""" Flask class
"""

from auth import Auth
from flask import Flask, jsonify, request, abort, redirect
import logging

# Initialize Flask app
app = Flask(__name__)

# Initialize Auth instance
AUTH = Auth()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def welcome() -> str:
    """GET /
    Return:
      - welcome
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.route("/users", methods=["POST"], strict_slashes=False)
def user() -> str:
    """POST /users
    Return:
      - message
    """
    email = request.form.get("email")
    password = request.form.get("password")

    # Validate email and password
    if not email or not password:
        abort(400, "Email and password are required.")

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except Exception as e:
        logger.error(f"Error registering user: {e}")
        return jsonify({"message": "Error registering user."}), 500


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """POST /sessions
    Return:
      - message
    """
    email = request.form.get("email")
    password = request.form.get("password")

    # Validate email and password
    if not email or not password:
        abort(400, "Email and password are required.")

    valid_login = AUTH.valid_login(email, password)
    if valid_login:
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401, "Invalid email or password.")


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> str:
    """DELETE /sessions
    Return:
      - message
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")
    else:
        abort(403, "Invalid session.")


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile() -> str:
    """GET /profile
    Return:
      - message
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403, "Unauthorized access.")


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token() -> str:
    """POST /reset_password
    Return:
      - message
    """
    email = request.form.get("email")
    if not email:
        abort(400, "Email is required.")

    user = AUTH.create_session(email)
    if not user:
        abort(403, "User not found.")
    else:
        token = AUTH.get_reset_password_token(email)
        # Send email with reset token here
        return jsonify({"email": email, "reset_token": token})


@app.route("/reset_password", methods=["PUT"], strict_slashes=False)
def update_password() -> str:
    """PUT /reset_password
    Return:
      - message
    """
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")

    # Validate inputs
    if not email or not reset_token or not new_password:
        abort(400, "Email, reset token, and new password are required.")

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except Exception as e:
        logger.error(f"Error updating password: {e}")
        abort(500, "Error updating password.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
