import logging
from PyQt5.QtCore import QMutex

from app.lib.singleton_design import SingletonDesign
from app.lib.console_logger import ConsoleLogger


class AppConfigContextMutex(metaclass=SingletonDesign):
    def __init__(self):
        self.mutex = QMutex()

    def lock(self):
        self.mutex.lock()

    def unlock(self):
        self.mutex.unlock()

    def tryLock(self):
        return self.mutex.tryLock()

