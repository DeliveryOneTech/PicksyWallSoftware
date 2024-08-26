from abc import abstractmethod


class DbModel:
    def __init__(self, id: object = None):
        pass

    @property
    @abstractmethod
    def table_name(self): pass

    @staticmethod
    @abstractmethod
    def get_column_name_and_sql_type_dict_for_table(): pass
