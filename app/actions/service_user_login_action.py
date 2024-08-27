from PyQt5.QtCore import pyqtSignal
from app.actions.abstracts.d1_action import D1Action
from app.actions.models.action_result_model import ActionResultModel


class ServiceUserLoginAction(D1Action):
    result_signal = pyqtSignal(ActionResultModel)
    is_loading_signal = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

    def execute(self, password: str):
        self.is_loading_signal.emit(True)
        import time
        time.sleep(5)
        self.result_signal.emit(ActionResultModel(False, "Operation failed."))
        self.is_loading_signal.emit(False)

    def run_in_thread(self, password: str):
        import threading
        thread = threading.Thread(target=self.execute, args=(password,))
        thread.start()
        return thread
