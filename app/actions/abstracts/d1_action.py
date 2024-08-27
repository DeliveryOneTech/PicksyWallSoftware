from PyQt5.QtCore import QObject, pyqtSignal
from abc import abstractmethod
from app.actions.models.action_result_model import ActionResultModel


class D1Action(QObject):
    def __init__(self):
        super().__init__()

    @property
    @abstractmethod
    def is_loading_signal(self) -> pyqtSignal(bool): pass

    @property
    @abstractmethod
    def result_signal(self) -> pyqtSignal(ActionResultModel): pass

    @abstractmethod
    def execute(self, *args, **kwargs): pass

    @abstractmethod
    def run_in_thread(self, *args, **kwargs): pass
