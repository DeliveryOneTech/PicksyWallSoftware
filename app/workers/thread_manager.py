from PyQt5.QtCore import QThread
from app.lib.decorators.singleton_decorator import Singleton
from app.workers.abstracts.d1_action import D1Action
from app.lib.console_logger import ConsoleLogger


@Singleton
class ThreadManager:
    __active_threads: list[QThread] = []
    __active_actions: list[D1Action] = []

    def __init__(self):
        self.console_logger = ConsoleLogger()
        self.console_logger.log("i'm created babbbooo")

    def add_thread_action_pair(self, action: D1Action, thread: QThread):
        self.__active_actions.append(action)
        self.__active_threads.append(thread)
        self.console_logger.log(f"Active threads: {self.active_threads_count}")

    def kill_executed_threads(self):
        threads_to_kill = []
        actions_to_kill = []

        for action, thread in zip(self.__active_actions, self.__active_threads):
            if action.is_thread_executed:
                self.console_logger.log(thread)
                if thread.isRunning():
                    self.kill_thread(thread)
                threads_to_kill.append(thread)
                actions_to_kill.append(action)

        for action in actions_to_kill:
            self.__active_actions.remove(action)

        for thread in threads_to_kill:
            self.__active_threads.remove(thread)

        self.console_logger.log(f"Active threads: {self.active_threads_count}")

    def remove_redundant_thread_action_pairs(self):
        for action, thread in zip(self.__active_actions, self.__active_threads):
            if not thread.isRunning():
                self.__active_actions.remove(action)
                self.__active_threads.remove(thread)

        self.console_logger.log(f"Active threads: {self.active_threads_count}")

    def find_worker_and_thread_pair_by_thread_name(self, thread_name: str):
        for worker, thread in zip(self.__active_actions, self.__active_threads):
            if worker.thread_name == thread_name:
                return worker, thread

        return None, None

    def get_active_threads(self):
        return self.__active_threads

    def get_active_actions(self):
        return self.__active_actions

    @staticmethod
    def kill_thread(thread: QThread):
        thread.quit()
        thread.wait()

    @property
    def active_threads_count(self):
        return len(self.__active_threads)

    @property
    def active_actions_count(self):
        return len(self.__active_actions)
