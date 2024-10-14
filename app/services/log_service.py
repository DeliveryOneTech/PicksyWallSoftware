from datetime import datetime
from app.enums.log_level import LogLevel
from app.enums.log_type import LogType
from app.data.local_db_context import LocalDbContext
from app.data.entities.log import Log
from app.data.utils.sql_query_generator import SqlQueryGenerator
from app.lib.decorators.singleton_decorator import Singleton


@Singleton
class LogService:
    def __init__(self):
        self.__local_db_context = LocalDbContext()

    def get_all_logs(self):
        query = SqlQueryGenerator.get_select_all_query(Log.table_name)
        self.__local_db_context.run_query(query)
        return self.__local_db_context.cursor.fetchall()

    def get_log(self, log_id):
        query, values = SqlQueryGenerator.get_select_query(Log.table_name, 'id', log_id)
        self.__local_db_context.cursor.execute(query)
        return self.__local_db_context.cursor.fetchone()

    def create_system_log(self, message, logLevel=LogLevel.INFO) -> object:
        """
        Creates a system log.
        :param message:
        :param logLevel:
        :return: -> lastrowid
        """
        system_log = Log(message, logLevel.value, LogType.SYSTEM_LOG.value, datetime.now())
        query, values = SqlQueryGenerator.get_insert_query(Log.table_name, system_log.__dict__)
        self.__local_db_context.cursor.execute(query, values)
        self.__local_db_context.connection.commit()
        return self.__local_db_context.cursor.lastrowid

    def create_mqtt_log(self, message, logLevel=LogLevel.INFO) -> object:
        """
        Creates a mqtt log.
        :param message:
        :param logLevel:
        :return: -> lastrowid
        """
        mqtt_log = Log(message, logLevel.value, LogType.MQTT_LOG.value, datetime.now())
        query, values = SqlQueryGenerator.get_insert_query(Log.table_name, mqtt_log.__dict__)
        self.__local_db_context.cursor.execute(query, values)
        self.__local_db_context.connection.commit()
        return self.__local_db_context.cursor.lastrowid

    def create_ui_log(self, message, logLevel=LogLevel.INFO) -> object:
        """
        Creates a ui log.
        :param message:
        :param logLevel:
        :return: -> lastrowid
        """
        ui_log = Log(message, logLevel.value, LogType.UI_LOG.value, datetime.now())
        query, values = SqlQueryGenerator.get_insert_query(Log.table_name, ui_log.__dict__)
        self.__local_db_context.cursor.execute(query, values)
        self.__local_db_context.connection.commit()
        return self.__local_db_context.cursor.lastrowid

    def create_exception_log(self, message, logLevel=LogLevel.ERROR) -> object:
        """
        Creates an exception log.
        :param message:
        :param logLevel:
        :return: -> lastrowid
        """
        exception_log = Log(message, logLevel.value, LogType.EXCEPTION_LOG.value, datetime.now())
        query, values = SqlQueryGenerator.get_insert_query(Log.table_name, exception_log.__dict__)
        self.__local_db_context.cursor.execute(query, values)
        self.__local_db_context.connection.commit()
        return self.__local_db_context.cursor.lastrowid
