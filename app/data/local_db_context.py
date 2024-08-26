import logging
import os.path
import sqlite3
from app.data.models.Log import Log
from app.lib.console_logger import SingletonConsoleLogger
from app.data.abstracts.local_db_cursor import LocalDbCursor
from app.data.abstracts.local_db_connection import LocalDbConnection


class LocalDbContext:
    def __init__(self):
        db_name = 'local.db'
        db_path = os.path.join("./", db_name)

        singleton_system_logger = SingletonConsoleLogger()

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


class SingletonLocalDbContext:
    __instance = None
    __singleton_local_db_context = SingletonConsoleLogger()

    @staticmethod
    def getInstance():
        try:
            if SingletonLocalDbContext.__instance is None:
                SingletonLocalDbContext()
            return SingletonLocalDbContext.__instance
        except Exception as e:
            SingletonLocalDbContext.__singleton_local_db_context.log(e, logging.ERROR)

    def __init__(self):
        try:
            if SingletonLocalDbContext.__instance is not None:
                raise Exception("This class is a singleton!")
            else:
                SingletonLocalDbContext.__instance = LocalDbContext()
        except Exception as e:
            SingletonLocalDbContext.__singleton_local_db_context.log(e, logging.ERROR)
