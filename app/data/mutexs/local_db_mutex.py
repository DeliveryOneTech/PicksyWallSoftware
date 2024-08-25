from PyQt5.QtCore import QMutex


class LocalDbConnectionMutex:
    def __init__(self):
        self.mutex = QMutex()

    def lock(self):
        self.mutex.lock()

    def unlock(self):
        self.mutex.unlock()

    def tryLock(self):
        return self.mutex.tryLock()


class SingletonLocalDbConnectionMutex:
    __instance = None

    @staticmethod
    def getInstance():
        if SingletonLocalDbConnectionMutex.__instance is None:
            SingletonLocalDbConnectionMutex()
        return SingletonLocalDbConnectionMutex.__instance

    def __init__(self):
        try:
            if SingletonLocalDbConnectionMutex.__instance is not None:
                raise Exception("This class is a singleton!")
            else:
                SingletonLocalDbConnectionMutex.__instance = LocalDbConnectionMutex()
        except Exception as e:
            print(e.args)


class LocalDbCursorMutex:
    def __init__(self):
        self.mutex = QMutex()

    def lock(self):
        self.mutex.lock()

    def unlock(self):
        self.mutex.unlock()

    def tryLock(self):
        return self.mutex.tryLock()


class SingletonLocalDbCursorMutex:
    __instance = None

    @staticmethod
    def getInstance():
        if SingletonLocalDbCursorMutex.__instance is None:
            SingletonLocalDbCursorMutex()
        return SingletonLocalDbCursorMutex.__instance

    def __init__(self):
        try:
            if SingletonLocalDbCursorMutex.__instance is not None:
                raise Exception("This class is a singleton!")
            else:
                SingletonLocalDbCursorMutex.__instance = LocalDbCursorMutex()
        except Exception as e:
            print(e.args)
