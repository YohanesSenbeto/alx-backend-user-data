#!/usr/bin/env python3
""" 
Module for filtering sensitive data and logging.
"""

import re
import os
import mysql.connector
import logging

from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Replace sensitive data in a log message with a redaction string."""
    for entry in fields:
        message = re.sub(
            rf"{entry}=(.*?){separator}", f"{entry}={redaction}{separator}", message
        )
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        """Initialize the RedactingFormatter."""
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record, redacting sensitive fields."""
        return filter_datum(
            self.fields, self.REDACTION, super().format(record), self.SEPARATOR
        )


def get_logger() -> logging.Logger:
    """Create and configure a logger."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    formatter = RedactingFormatter(PII_FIELDS)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connect to the database."""
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")
    conn = mysql.connector.connect(host=host, user=username, password=password)
    return conn


def create_database(conn: mysql.connector.connection.MySQLConnection) -> None:
    """Create a database."""
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS your_database_name")
    cursor.close()


def main() -> None:
    """Read data from the database and log it with sensitive fields redacted."""
    logger = get_logger()
    db = get_db()
    create_database(db)
    db.close()


if __name__ == "__main__":
    main()
