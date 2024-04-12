#!/usr/bin/env python3
import logging
import re

from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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
        message = super().format(record)
        for field in self.fields:
            message = re.sub(
                rf"{field}=(.*?){self.SEPARATOR}",
                f"{field}={self.REDACTION}{self.SEPARATOR}",
                message,
            )
        return message


def main() -> None:
    """Main function."""
    # Your main function logic goes here


if __name__ == "__main__":
    main()
