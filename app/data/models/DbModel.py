from datetime import datetime


def __python_type_convert_to_sql_type__(value: object):
    if isinstance(value, str):
        return "TEXT"
    elif isinstance(value, int):
        return "INTEGER"
    elif isinstance(value, float):
        return "REAL"
    elif isinstance(value, bool):
        return "INTEGER"
    elif isinstance(value, datetime):
        return "TEXT"
    else:
        return "TEXT"


class DbModel:
    def __init__(self, table_name: str, _id: object, **kwargs):
        self.table_name = table_name
        self.id = _id

    def __prop_names__(self):
        return [key for key in self.__dict__.keys()]

    @property
    def get_create_table_sql_query(self):
        id_sql_type = __python_type_convert_to_sql_type__(self.id)
        query = f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
        if id_sql_type == "INTEGER":
            query += "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        else:
            query += "id TEXT PRIMARY KEY,"
        for key in self.__prop_names__():
            query += f"{key} {__python_type_convert_to_sql_type__(self.__dict__[key])},"
        query = query[:-1]
        query += ")"
        return query

    @property
    def get_insert_sql_query(self):
        query = f"INSERT INTO {self.table_name} ("
        for key in self.__prop_names__():
            query += f"{key},"
        query = query[:-1]
        query += ") VALUES ("
        for key in self.__prop_names__():
            query += f"'{self.__dict__[key]}',"
        query = query[:-1]
        query += ")"
        return query

    @property
    def get_update_sql_query(self):
        query = f"UPDATE {self.table_name} SET "
        for key in self.__prop_names__():
            query += f"{key} = '{self.__dict__[key]}',"
        query = query[:-1]
        query += f" WHERE id = '{self.id}'"
        return query

    @property
    def get_delete_sql_query(self):
        return f"DELETE FROM {self.table_name} WHERE id = '{self.id}'"

    @property
    def get_select_sql_query(self):
        return f"SELECT * FROM {self.table_name} WHERE id = '{self.id}'"

    @property
    def get_select_all_sql_query(self):
        return f"SELECT * FROM {self.table_name}"

    def __dict__(self):
        return self.__dict__
