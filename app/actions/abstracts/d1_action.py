from PyQt5.QtCore import QObject, pyqtSignal
from abc import abstractmethod
from app.lib.d1_result_model import D1ResultModel


class D1Action(QObject):
    def __init__(self):
        super().__init__()

    @property
    @abstractmethod
    def is_loading_signal(self) -> pyqtSignal(bool): pass

    @property
    @abstractmethod
    def result_signal(self) -> pyqtSignal(D1ResultModel): pass

    @abstractmethod
    def execute(self, *args, **kwargs): pass

    @abstractmethod
    def run_in_thread(self, *args, **kwargs): pass
