import json
import sqlite3


def create_players_table():
    conn = sqlite3.connect("/mnt/efs/bmt_recharging.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            weight REAL NOT NULL DEFAULT 1.0
        )
    ''')
    conn.commit()
    conn.close()

def lambda_handler(event, context):
    # Example: Read from SQLite (mounted via EFS at /mnt/sqlite/shared.db)
    try:
        conn = sqlite3.connect("/mnt/efs/bmt_recharging.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sessions LIMIT 5")
        rows = cursor.fetchall()
        conn.close()
        return {
            "statusCode": 200,
            "body": json.dumps(rows)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }


if __name__ == "__main__":
    # Test event
    test_event = {}
    print(lambda_handler(test_event, None))
