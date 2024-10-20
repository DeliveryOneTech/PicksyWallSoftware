import os.path
import sqlite3
from app.data.entities.log import Log
from app.data.entities.tray import Tray
from app.lib.decorators.singleton_decorator import Singleton
from app.lib.utils.console_logger import ConsoleLogger
from app.data.abstracts.local_db_cursor import LocalDbCursor
from app.data.abstracts.local_db_connection import LocalDbConnection


@Singleton
class LocalDbContext:
    def __init__(self):
        db_name = 'local.db'
        db_path = os.path.join("./", db_name)

        console_logger = ConsoleLogger()

        try:
            self.connection = LocalDbConnection(db_path, check_same_thread=False, timeout=10)
            self.cursor = LocalDbCursor(self.connection)
            console_logger.log("Connection & Cursor created.")
        except sqlite3.Error as e:
            raise e

        try:
            self.create_tables_if_not_exists()
            console_logger.log("Created tables if not exists.")
        except sqlite3.Error as e:
            raise e

        try:
            self.seed_data()
            console_logger.log("Seeded data.")
        except sqlite3.Error as e:
            raise e

    def create_tables_if_not_exists(self):
        self.cursor.execute(Log.get_create_table_sql_query())
        self.cursor.execute(Tray.get_create_table_sql_query())
        self.connection.commit()

    def run_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def seed_data(self):
        """
        Seed data for bulk operations or initial data
        :return:
        """
        pass
