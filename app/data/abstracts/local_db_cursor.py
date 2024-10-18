import logging
import sqlite3

from app.lib.utils.console_logger import ConsoleLogger
from app.mutexs.local_db_mutex import LocalDbCursorMutex


class LocalDbCursor(sqlite3.Cursor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cursor_mutex = LocalDbCursorMutex()

    def execute(self, sql, parameters=()):
        self.cursor_mutex.lock()
        try:
            return super().execute(sql, parameters)
        except Exception as e:
            ConsoleLogger().log(f"{e}", logging.ERROR)
            return None
        finally:
            self.cursor_mutex.unlock()

    def fetchone(self):
        self.cursor_mutex.lock()
        try:
            return super().fetchone()
        except Exception as e:
            ConsoleLogger().log(f"{e}", logging.ERROR)
            return None
        finally:
            self.cursor_mutex.unlock()

    def fetchall(self):
        self.cursor_mutex.lock()
        try:
            return super().fetchall()
        except Exception as e:
            ConsoleLogger().log(f"{e}", logging.ERROR)
            return None
        finally:
            self.cursor_mutex.unlock()

    def close(self):
        self.cursor_mutex.lock()
        try:
            return super().close()
        except Exception as e:
            ConsoleLogger().log(f"{e}", logging.ERROR)
            return None
        finally:
            self.cursor_mutex.unlock()
