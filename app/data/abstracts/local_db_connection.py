import sqlite3
from app.mutexs.local_db_mutex import SingletonLocalDbConnectionMutex


class LocalDbConnection(sqlite3.Connection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connection_mutex = SingletonLocalDbConnectionMutex.getInstance()

    def commit(self):
        self.connection_mutex.lock()
        try:
            return super().commit()
        except Exception as e:
            print(e)
            return None
        finally:
            self.connection_mutex.unlock()

    def close(self):
        self.connection_mutex.lock()
        try:
            return super().close()
        except Exception as e:
            print(e)
            return None
        finally:
            self.connection_mutex.unlock()
