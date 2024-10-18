from PyQt5.QtCore import QMutex
from app.lib.decorators.singleton_decorator import Singleton


@Singleton
class LocalDbConnectionMutex:
    def __init__(self):
        self.mutex = QMutex()

    def lock(self):
        self.mutex.lock()

    def unlock(self):
        self.mutex.unlock()

    def tryLock(self):
        return self.mutex.tryLock()


@Singleton
class LocalDbCursorMutex:
    def __init__(self):
        self.mutex = QMutex()

    def lock(self):
        self.mutex.lock()

    def unlock(self):
        self.mutex.unlock()

    def tryLock(self):
        return self.mutex.tryLock()

