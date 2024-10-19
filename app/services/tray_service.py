from datetime import datetime
from app.data.entities.tray import Tray
from app.data.local_db_context import LocalDbContext
from app.lib.utils.sql_query_generator import SqlQueryGenerator
from app.lib.decorators.singleton_decorator import Singleton
from app.lib.extensions.boolean_extension import BooleanExtension


@Singleton
class TrayService:
    def __init__(self):
        self.__local_db_context = LocalDbContext()

    def get_all_trays(self):
        query = SqlQueryGenerator.get_select_all_query(Tray.table_name)
        self.__local_db_context.run_query(query)
        return self.__local_db_context.cursor.fetchall()

    def get_tray(self, tray_id):
        query, values = SqlQueryGenerator.get_select_query(Tray.table_name, 'id', tray_id)
        self.__local_db_context.cursor.execute(query)
        return self.__local_db_context.cursor.fetchone()

    def create_tray(self, door_no: str, is_clean: bool) -> object:
        """
        Create a tray.
        :param door_no:
        :param is_clean:
        :return: -> lastrowid
        """
        tray = Tray(door_no, BooleanExtension.to_integer(is_clean), datetime.now())
        query, values = SqlQueryGenerator.get_insert_query(Tray.table_name, tray.__dict__)
        self.__local_db_context.cursor.execute(query, values)
        self.__local_db_context.connection.commit()
        return self.__local_db_context.cursor.lastrowid

    def update_tray(self, tray_id, door_no: str, is_clean: bool) -> object:
        """
        Update a tray.
        :param tray_id:
        :param door_no:
        :param is_clean:
        :return: -> lastrowid
        """
        tray = Tray(door_no, BooleanExtension.to_integer(is_clean), datetime.now(), tray_id)
        query, values = SqlQueryGenerator.get_update_query(Tray.table_name, tray.__dict__, 'id', tray_id)
        self.__local_db_context.cursor.execute(query, values)
        self.__local_db_context.connection.commit()
        return tray_id

    def delete_tray(self, tray_id):
        """
        Delete a tray.
        :param tray_id:
        :return:
        """
        query, values = SqlQueryGenerator.get_delete_query(Tray.table_name, 'id', tray_id)
        self.__local_db_context.cursor.execute(query, values)
        self.__local_db_context.connection.commit()
        return self.__local_db_context.cursor.lastrowid
