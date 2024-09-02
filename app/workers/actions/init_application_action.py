from PyQt5.QtCore import pyqtSignal
from app.lib.d1_result import D1Result
from app.workers.abstracts.d1_action import D1Action
from app.workers.thread_manager import ThreadName


class InitApplicationAction(D1Action):
    is_loading_signal = pyqtSignal(bool)
    is_thread_executed = False
    result_signal = pyqtSignal(D1Result)

    def __init__(self, thread_name: str = ThreadName.INIT_APPLICATION_ACTION.value):
        super().__init__()
        self.thread_name = thread_name

    def execute(self):
        self.is_loading_signal.emit(True)
        import time
        time.sleep(5)
        self.result_signal.emit(D1Result(True, "Init process completed."))
        self.is_loading_signal.emit(False)
