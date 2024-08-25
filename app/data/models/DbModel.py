class DbModel:
    def __init__(self, id: object):
        self.id = id

    @staticmethod
    def get_column_name_and_sql_type_dict_for_table():
        return {
            'id': 'INTEGER PRIMARY KEY'
        }
