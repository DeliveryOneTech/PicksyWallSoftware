class SqlQueryGenerator:
    @staticmethod
    def get_create_table_query(table_name: str,
                               properties: dict) -> str:
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        for key, value in properties.items():
            query += f"{key} {value}, "
        query = query[:-2] + ")"
        return query
