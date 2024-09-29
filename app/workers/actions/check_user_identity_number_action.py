import re
from PyQt5.QtCore import pyqtSignal, QThread
from app.lib.models.d1_result_data_model import D1Result
from app.workers.abstracts.d1_action import D1Action
from app.workers.thread_manager import ThreadManager
from app.enums.thread_name import ThreadName


class CheckUserIdentityNumberAction(D1Action):
    result_signal = pyqtSignal(D1Result)
    is_loading_signal = pyqtSignal(bool)
    is_thread_executed = False

    def __init__(self, thread_name: str = ThreadName.CHECK_USER_IDENTITY_NUMBER_ACTION.value):
        super().__init__()
        self.thread_name = thread_name

    def execute(self, identity_number: str, kvkk_approval: bool):
        self.is_loading_signal.emit(True)

        if not kvkk_approval:
            self.is_loading_signal.emit(False)
            self.result_signal.emit(D1Result(False, "KVKK onayı vermelisiniz."))
            return

        # Check if the identity number is valid
        if not re.match(r"^\d{11}$", identity_number):
            self.is_loading_signal.emit(False)
            self.result_signal.emit(D1Result(False, "Geçersiz kimlik numarası."))
            return

        if int(identity_number[0]) == 0:
            self.is_loading_signal.emit(False)
            self.result_signal.emit(D1Result(False, "Geçersiz kimlik numarası."))
            return

        if int(identity_number[10]) % 2 == 0:
            self.is_loading_signal.emit(False)
            self.result_signal.emit(D1Result(False, "Geçersiz kimlik numarası."))
            return

        self.is_loading_signal.emit(False)
        self.result_signal.emit(D1Result(True, "Kimlik numarası geçerli."))

    @staticmethod
    def run_in_thread(auto_start: bool = False, run_with_thread_manager: bool = True, execute_func_params: list = None) -> tuple[
        D1Action, QThread]:
        action = CheckUserIdentityNumberAction()
        thread = QThread()
        thread.setObjectName(action.thread_name)

        action.is_thread_executed = run_with_thread_manager
        action.moveToThread(thread)
        if execute_func_params:
            thread.started.connect(lambda: action.execute(*execute_func_params))
        else:
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
