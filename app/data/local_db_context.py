import logging
import os.path
import sqlite3
from app.data.models.SystemLog import SystemLog
from app.data.mutexs.local_db_connection import LocalDbConnection
from app.lib.system_logger import SingletonSystemLogger


class LocalDbContext:
    def __init__(self):
        db_name = 'local.db'
        db_path = os.path.join("./", db_name)

        singleton_system_logger = SingletonSystemLogger()

        try:
            self.connection = LocalDbConnection(db_path, check_same_thread=False, timeout=10)
            self.cursor = self.connection.cursor()
            singleton_system_logger.log("Connection & Cursor created.")
        except sqlite3.Error as e:
            raise e

        try:
            self.create_tables_if_not_exists()
            singleton_system_logger.log("Tables created.")
        except sqlite3.Error as e:
            raise e

    def create_tables_if_not_exists(self):
        self.cursor.execute(SystemLog.get_create_table_sql_query())
        self.connection.commit()

    def run_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()


class SingletonLocalDbContext:
    __instance = None
    __singleton_local_db_context = SingletonSystemLogger()

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
