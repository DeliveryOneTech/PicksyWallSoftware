from datetime import datetime
from app.data.abstracts.db_model import DbModel
from app.data.utils.sql_query_generator import SqlQueryGenerator


class Tray(DbModel):
    table_name = 'Trays'

    def __init__(self,
                 default_location_code: str,
                 is_clean: int,
                 created_date_time: datetime,
                 id: int = None):
        super().__init__(id)
        self.location = default_location_code
        self.is_clean = is_clean
        self.created_date_time = created_date_time

    @staticmethod
    def get_column_name_and_sql_type_dict_for_table():
        return {
            'id': 'INTEGER PRIMARY KEY',
            'default_location_code': 'TEXT',
            'is_clean': 'INTEGER',
            'created_date_time': 'TEXT'
        }

    @staticmethod
    def get_create_table_sql_query() -> str:
        return SqlQueryGenerator.get_create_table_query(Tray.table_name,
                                                        Tray.get_column_name_and_sql_type_dict_for_table())
