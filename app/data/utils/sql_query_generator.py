from typing import Any


class SqlQueryGenerator:
    @staticmethod
    def get_create_table_query(table_name: str, properties: dict) -> str:
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        for key, value in properties.items():
            query += f"{key} {value}, "
        query = query[:-2] + ")"
        return query

    @staticmethod
    def get_insert_query(table_name: str, data: dict) -> tuple[str, list[Any]]:
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data])
        values = list(data.values())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        return query, values

    @staticmethod
    def get_update_query(table_name: str, data: dict, id_column: str, id_value: object) -> tuple[str, list[object]]:
        set_clause = ', '.join([f"{key} = ?" for key in data.keys()])
        values = list(data.values()) + [id_value]
        query = f"UPDATE {table_name} SET {set_clause} WHERE {id_column} = ?"
        return query, values

    @staticmethod
    def get_select_all_query(table_name: str) -> str:
        query = f"SELECT * FROM {table_name}"
        return query

    @staticmethod
    def get_delete_query(table_name: str, id_column: str, id_value: object) -> tuple[str, list[object]]:
        query = f"DELETE FROM {table_name} WHERE {id_column} = ?"
        return query, [id_value]

    @staticmethod
    def get_select_query(table_name: str, id_column: str, id_value: object) -> tuple[str, list[object]]:
        query = f"SELECT * FROM {table_name} WHERE {id_column} = ?"
        return query, [id_value]
