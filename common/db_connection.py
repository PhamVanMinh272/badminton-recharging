import os
import sqlite3
from settings import SQLITE_PATH, logger

def connect_db(db_path: str = SQLITE_PATH):
    logger.info(f"Attempting to connect to database at: {db_path}")
    if not os.path.exists(db_path):
        raise FileNotFoundError("Database file not found!")

    logger.info(f"Connecting to database at: {db_path}")
    conn = sqlite3.connect(db_path)
    logger.info("Connected to the database successfully.")
    return conn


def initialize_db(db_path: str = SQLITE_PATH):
    """Initialize the SQLite database."""
    if os.path.exists(db_path):
        logger.info(f"Database already exists at: {db_path}")
        return
    else:
        logger.info(f"Creating new database at: {db_path}")
        conn = sqlite3.connect(db_path)
        conn.close()
        logger.info("Database created successfully.")
