import json
from common.db_connection import connect_db
from settings import SQLITE_PATH, DDL_PATH, DML_PATH



def run_ddl():
    """Run DDL script to create tables in the SQLite database."""
    conn = connect_db(SQLITE_PATH)
    cursor = conn.cursor()

    with open(DDL_PATH, 'r') as file:
        ddl_script = file.read()
    cursor.executescript(ddl_script)
    conn.commit()
    conn.close()

def run_dml():
    """
    Run DML script to insert initial data into the SQLite database.
    Make sure to put unique constraints to avoid duplication.
    """

    conn = connect_db(SQLITE_PATH)
    cursor = conn.cursor()

    with open(DML_PATH, 'r') as file:
        ddl_script = file.read()
    cursor.executescript(ddl_script)
    conn.commit()
    conn.close()

db_strategies = {
    "run_ddl": run_ddl,
    "run_dml": run_dml
}

def get_help():
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "task_type field required with available value: " + ", ".join(db_strategies.keys())
        })
    }


def lambda_handler(event, context):
    # Example: Read from SQLite (mounted via EFS at /mnt/sqlite/shared.db)
    try:
        task_type = event.get("task_type", "")
        if not task_type or task_type not in db_strategies:
            return get_help()
        return {
            "statusCode": 200,
            "body": json.dumps("Done " + task_type)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }


if __name__ == "__main__":
    # Test event
    test_event = {
        "task_type": "run_ddl"
    }
    print(lambda_handler(test_event, None))
