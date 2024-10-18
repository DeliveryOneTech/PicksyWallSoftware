import logging
import sqlite3

from app.lib.utils.console_logger import ConsoleLogger
from app.mutexs.local_db_mutex import LocalDbConnectionMutex


class LocalDbConnection(sqlite3.Connection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connection_mutex = LocalDbConnectionMutex()

    def commit(self):
        self.connection_mutex.lock()
        try:
            return super().commit()
        except Exception as e:
            ConsoleLogger.log(f"{e}", logging.ERROR)
            return None
        finally:
            self.connection_mutex.unlock()

    def close(self):
        self.connection_mutex.lock()
        try:
            return super().close()
        except Exception as e:
            ConsoleLogger.log(f"{e}", logging.ERROR)
            return None
        finally:
            self.connection_mutex.unlock()
