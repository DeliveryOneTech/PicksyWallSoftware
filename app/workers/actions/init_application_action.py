from PyQt5.QtCore import pyqtSignal, QThread
from app.lib.models.d1_result_data_model import D1Result
from app.workers.abstracts.d1_action import D1Action
from app.workers.thread_manager import ThreadManager
from app.enums.thread_name import ThreadName


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
        time.sleep(1)
        self.result_signal.emit(D1Result(True, "Init process completed."))
        self.is_loading_signal.emit(False)

    @staticmethod
    def run_in_thread(auto_start: bool = False, run_with_thread_manager: bool = True) -> tuple[D1Action, QThread]:
        action = InitApplicationAction()
        thread = QThread()
        thread.setObjectName(action.thread_name)

        action.is_thread_executed = run_with_thread_manager
        action.moveToThread(thread)
        thread.started.connect(action.execute)

        if auto_start:
            thread.start()

        if run_with_thread_manager:
            thread_manager = ThreadManager()
            action.is_loading_signal.connect(
                lambda is_loading: thread_manager.kill_thread(thread) if not is_loading else None
            )
            thread.finished.connect(lambda: thread_manager.remove_redundant_thread_action_pairs())
            thread_manager.add_thread_action_pair(action, thread)

        return action, thread
