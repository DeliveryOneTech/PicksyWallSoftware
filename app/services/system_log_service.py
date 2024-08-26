from app.data.enums.log_level import LogLevel
from app.data.enums.log_type import LogType
from app.data.local_db_context import SingletonLocalDbContext
from app.data.models.Log import Log
from app.data.utils.sql_query_generator import SqlQueryGenerator
from app.lib.utils import Utils


class LogService:
    def __init__(self):
        self.__local_db_context = SingletonLocalDbContext.getInstance()

    def get_system_logs(self):
        query = SqlQueryGenerator.get_select_all_query(Log.table_name)
        self.__local_db_context.run_query(query)
        return self.__local_db_context.cursor.fetchall()

    def get_system_log(self, system_log_id):
        query, values = SqlQueryGenerator.get_select_query(Log.table_name, 'id', system_log_id)
        self.__local_db_context.cursor.execute(query)
        return self.__local_db_context.cursor.fetchone()

    def create_system_log(self, message, logLevel=LogLevel.INFO, logType=LogType.SYSTEM_LOG,
                          createdDateTime=None) -> object:
        """
        Creates a system log.
        :param message:
        :param logLevel:
        :param logType:
        :param createdDateTime:
        :return: -> lastrowid
        """
        if createdDateTime is None:
            createdDateTime = Utils.get_current_date_time_str()
        system_log = Log(message, logLevel.value, logType.value, createdDateTime)
        query, values = SqlQueryGenerator.get_insert_query(Log.table_name, system_log.__dict__)
        self.__local_db_context.cursor.execute(query, values)
        self.__local_db_context.connection.commit()
        return self.__local_db_context.cursor.lastrowid


class SingletonSystemLogService(LogService):
    __instance = None

    def __new__(cls):
        if SingletonSystemLogService.__instance is None:
            SingletonSystemLogService.__instance = LogService()
        return SingletonSystemLogService.__instance
