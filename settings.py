import os
import logging

logger = logging.getLogger(__name__)

ENV = os.environ.get("ENV", "local")

# DB
SQLITE_PATH = "mnt/efs/bmt_recharging.db"
if ENV == "local":
    SQLITE_PATH = "resources/bmt_recharging.db"
DDL_PATH = "resources/ddl.sql"
DML_PATH = "resources/dml.sql"
