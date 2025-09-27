import os
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

ENV = os.environ.get("ENV", "local")

# DB
SQLITE_PATH = "/mnt/efs/bmt_recharging.db"
DDL_PATH = os.path.join("/var/task", "resources", "ddl.sql")
DML_PATH = os.path.join("/var/task", "resources", "dml.sql")
if ENV == "local":
    SQLITE_PATH = "resources/bmt_recharging.db"
    DDL_PATH = os.path.join("resources", "ddl.sql")
    DML_PATH = os.path.join("resources", "dml.sql")

# run aws lambda in local
logger.info("Running in local environment")
SQLITE_PATH = os.path.join(os.pardir, "resources", "bmt_recharging.db")
DDL_PATH = os.path.join(os.pardir, "resources", "ddl.sql")
DML_PATH = os.path.join(os.pardir, "resources", "dml.sql")
