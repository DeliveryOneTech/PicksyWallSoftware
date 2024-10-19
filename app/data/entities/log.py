from datetime import datetime
from app.data.abstracts.db_model import DbModel
from app.lib.utils.sql_query_generator import SqlQueryGenerator


class Log(DbModel):
    table_name = 'Logs'

    def __init__(self,
                 message: str,
                 log_level: int,
                 log_type: int,
                 created_date_time: datetime,
                 id: int = None):
        super().__init__(id)
        self.id = id
        self.log_level = log_level
        self.log_type = log_type
        self.message = message
        self.created_date_time = created_date_time

    @staticmethod
    def get_column_name_and_sql_type_dict_for_table():
        return {
            'id': 'INTEGER PRIMARY KEY',
            'message': 'TEXT',
            'log_level': 'INTEGER',
            'log_type': 'INTEGER',
            'created_date_time': 'TEXT'
        }

    @staticmethod
    def get_create_table_sql_query() -> str:
        return SqlQueryGenerator.get_create_table_query(Log.table_name,
                                                        Log.get_column_name_and_sql_type_dict_for_table())

    @staticmethod
    def to_log(row: tuple):
        return Log(row[1], row[2], row[3], row[4], row[0])
