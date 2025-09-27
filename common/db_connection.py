import os
import sqlite3
from settings import SQLITE_PATH, logger

def connect_db(db_path: str = SQLITE_PATH):

    if not os.path.exists(db_path):
        logger.info("Current working directory:", os.pardir)
        logger.error("Database file not found!")
        raise FileNotFoundError("Database file not found!")

    logger.info(f"Connecting to database at: {db_path}")
    conn = sqlite3.connect(db_path)
    logger.info("Connected to the database successfully.")
    return conn
