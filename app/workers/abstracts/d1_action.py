from PyQt5.QtCore import QObject, pyqtSignal, QThread
from abc import abstractmethod
from app.lib.d1_result import D1Result


class D1Action(QObject):
    def __init__(self):
        super().__init__()

    @property
    @abstractmethod
    def is_loading_signal(self) -> pyqtSignal(bool): pass

    @property
    @abstractmethod
    def is_thread_executed(self) -> bool: pass

    @property
    @abstractmethod
    def result_signal(self) -> pyqtSignal(D1Result): pass

    @abstractmethod
    def execute(self, *args, **kwargs): pass

    @staticmethod
    @abstractmethod
    def run_in_thread(auto_start: bool = False, run_with_thread_manager: bool = True) -> tuple[QObject, QThread]: pass

    @is_thread_executed.setter
    def is_thread_executed(self, value):
        self.is_thread_executed = value
