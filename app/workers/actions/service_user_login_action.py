from PyQt5.QtCore import pyqtSignal, QThread
from app.workers.abstracts.d1_action import D1Action
from app.workers.thread_manager import ThreadName, ThreadManager
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
        singleton_thread_manager = ThreadManager()

        action.is_thread_executed = is_thread_executed
        action.moveToThread(thread)
        thread.started.connect(action.execute)

        if auto_start:
            thread.start()

        if is_thread_executed:
            action.is_loading_signal.connect(
                lambda is_loading: singleton_thread_manager.kill_thread(thread) if not is_loading else None
            )
            thread.finished.connect(lambda: singleton_thread_manager.remove_redundant_thread_action_pairs())
            ThreadManager().add_thread_action_pair(action, thread)

        return action, thread
