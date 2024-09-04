from PyQt5.QtCore import pyqtSignal, QThread
from app.workers.abstracts.d1_action import D1Action
from app.workers.thread_manager import ThreadName
from app.lib.d1_result import D1Result


class ServiceUserLoginAction(D1Action):
    result_signal = pyqtSignal(D1Result)
    is_loading_signal = pyqtSignal(bool)
    is_thread_executed = False

    def __init__(self, thread_name: str = ThreadName.SERVICE_USER_LOGIN_ACTION.value):
        super().__init__()
        self.thread_name = thread_name

    def execute(self, password: str):
        self.is_loading_signal.emit(True)
        import time
        time.sleep(5)
        self.result_signal.emit(D1Result(False, "Operation failed."))
        self.is_loading_signal.emit(False)

    @staticmethod
    def run_in_thread(auto_start: bool = False, is_thread_executed: bool = True) -> tuple[D1Action, QThread]:
        action = ServiceUserLoginAction()
        thread = QThread()
        action.moveToThread(thread)
        thread.started.connect(action.execute)
        if auto_start:
            thread.start()
        return action, thread
