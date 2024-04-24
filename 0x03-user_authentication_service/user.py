#!/usr/bin/env python3
"""
User model module.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    User SQLAlchemy model.

    Attributes:
        id (int): The integer primary key.
        email (str): The non-nullable string for email.
        hashed_password (str): The non-nullable string for hashed password.
        session_id (str): The nullable string for session ID.
        reset_token (str): The nullable string for reset token.
    """

    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(250), nullable=False)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: str = Column(String(250), nullable=True)
    reset_token: str = Column(String(250), nullable=True)
