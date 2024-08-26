import logging
from PyQt5.QtCore import QMutex
from app.lib.console_logger import SingletonConsoleLogger


class AppConfigContextMutex:
    def __init__(self):
        self.mutex = QMutex()

    def lock(self):
        self.mutex.lock()

    def unlock(self):
        self.mutex.unlock()

    def tryLock(self):
        return self.mutex.tryLock()


class SingletonAppConfigContextMutex:
    __instance = None

    @staticmethod
    def getInstance():
        if SingletonAppConfigContextMutex.__instance is None:
            SingletonAppConfigContextMutex()
        return SingletonAppConfigContextMutex.__instance

    def __init__(self):
        try:
            if SingletonAppConfigContextMutex.__instance is not None:
                raise Exception("This class is a singleton!")
            else:
                SingletonAppConfigContextMutex.__instance = AppConfigContextMutex()
        except Exception as e:
            SingletonConsoleLogger().log(e, logging.ERROR)
