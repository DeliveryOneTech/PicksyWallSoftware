from PyQt5.QtCore import QThread
from app.actions.abstracts.d1_action import D1Action
from app.lib.console_logger import SingletonConsoleLogger
from enum import Enum


class ThreadName(Enum):
    SERVICE_USER_LOGIN_ACTION = "ServiceUserLoginAction"


class ThreadManager:
    __active_threads: list[QThread] = []
    __active_actions: list[D1Action] = []

    def __init__(self):
        self.console_logger = SingletonConsoleLogger()
        self.console_logger.log()

    def add_thread_action_pair(self, action: D1Action, thread: QThread):
        self.__active_actions.append(action)
        self.__active_threads.append(thread)

    def kill_executed_threads(self):
        threads_to_kill = []
        actions_to_kill = []

        for action, thread in zip(self.__active_actions, self.__active_threads):
            if action.is_thread_executed_signal:
                self.console_logger.log(thread)
                if thread.isRunning():
                    thread.quit()
                    thread.wait()
                threads_to_kill.append(thread)
                actions_to_kill.append(action)

        for action in actions_to_kill:
            self.__active_actions.remove(action)

        for thread in threads_to_kill:
            self.__active_threads.remove(thread)

    def find_worker_and_thread_pair_by_thread_name(self, thread_name: str):
        for worker, thread in zip(self.__active_actions, self.__active_threads):
            if worker.thread_name == thread_name:
                return worker, thread

        return None, None


class SingletonThreadManager(ThreadManager):
    __instance = None

    def __new__(cls):
        if SingletonThreadManager.__instance is None:
            SingletonThreadManager.__instance = ThreadManager()
        return SingletonThreadManager.__instance
