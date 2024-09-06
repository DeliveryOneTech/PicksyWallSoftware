import os.path
import sqlite3
from app.data.models.log import Log
from app.lib.singleton_design import SingletonDesign
from app.lib.console_logger import ConsoleLogger
from app.data.abstracts.local_db_cursor import LocalDbCursor
from app.data.abstracts.local_db_connection import LocalDbConnection


class LocalDbContext(metaclass=SingletonDesign):
    def __init__(self):
        db_name = 'local.db'
        db_path = os.path.join("./", db_name)

        singleton_system_logger = ConsoleLogger()

        try:
            self.connection = LocalDbConnection(db_path, check_same_thread=False, timeout=10)
            self.cursor = LocalDbCursor(self.connection)
            singleton_system_logger.log("Connection & Cursor created.")
        except sqlite3.Error as e:
            raise e

        try:
            self.create_tables_if_not_exists()
            singleton_system_logger.log("Created tables if not exists.")
        except sqlite3.Error as e:
            raise e

    def create_tables_if_not_exists(self):
        self.cursor.execute(Log.get_create_table_sql_query())
        self.connection.commit()

    def run_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()
