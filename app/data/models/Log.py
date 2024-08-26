from datetime import datetime
from app.data.models.DbModel import DbModel
from app.data.utils.sql_query_generator import SqlQueryGenerator


class Log(DbModel):
    table_name = 'Logs'

    def __init__(self,
                 message: str,
                 logLevel: int,
                 logType: int,
                 createdDateTime: datetime,
                 id: int = None):
        super().__init__(id)
        self.logLevel = logLevel
        self.logType = logType
        self.message = message
        self.createdDateTime = createdDateTime

    @staticmethod
    def get_column_name_and_sql_type_dict_for_table():
        return {
            'id': 'INTEGER PRIMARY KEY',
            'message': 'TEXT',
            'logLevel': 'INTEGER',
            'logType': 'INTEGER',
            'createdDateTime': 'TEXT'
        }

    @staticmethod
    def get_create_table_sql_query() -> str:
        return SqlQueryGenerator.get_create_table_query(Log.table_name,
                                                        Log.get_column_name_and_sql_type_dict_for_table())
