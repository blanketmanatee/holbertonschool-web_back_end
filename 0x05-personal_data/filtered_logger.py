#!/usr/bin/env python3
"""
Personally Identifiable Information
"""
from posix import environ
from types import DynamicClassAttribute
from typing import List
import re
import logging
import os
import mysql.connector
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        return filter_datum(self.fields, self.REDACTION,
                     super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, 
                     message: str, separator: str) -> str:
    """ uses a regex to replace occurrences of certain field values"""
    for item in fields:
        message = re.sub(fr'{item}=.+?{separator}',
                        f'{item}={redaction}{separator}', message)
    return message

def get_logger() -> logging.Logger:
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger

def get_db() -> mysql.connector.connection.MySQLConnection:
    return mysql.connector.connect(
        host=os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.environ.get('PERSONAL_DATA_DB_NAME', 'root'),
        user=os.environ.get('PERSONAL_DATA_DB_USERNAME'),
        password=os.environ.get('PERSONAL_DATA_DB_PASSWORD', ''))