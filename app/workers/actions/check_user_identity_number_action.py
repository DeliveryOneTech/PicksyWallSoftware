import re
from PyQt5.QtCore import pyqtSignal
from app.lib.d1_result import D1Result
from app.workers.abstracts.d1_action import D1Action
from app.workers.thread_manager import ThreadName


class CheckUserIdentityNumberAction(D1Action):
    result_signal = pyqtSignal(D1Result)
    is_loading_signal = pyqtSignal(bool)
    is_thread_executed = False

    def __init__(self, thread_name: str = ThreadName.CHECK_USER_IDENTITY_NUMBER_ACTION.value):
        super().__init__()
        self.thread_name = thread_name

    def execute(self, identity_number: str):
        self.is_loading_signal.emit(True)

        # Check if the identity number is valid
        if not re.match(r"^\d{11}$", identity_number):
            self.result_signal.emit(D1Result(False, "Invalid identity number."))
            return

        if int(identity_number[0]) == 0:
            self.result_signal.emit(D1Result(False, "Invalid identity number."))
            return

        if int(identity_number[10]) % 2 == 0:
            self.result_signal.emit(D1Result(False, "Invalid identity number."))
            return

        self.result_signal.emit(D1Result(True, "Valid identity number."))

        self.is_loading_signal.emit(False)
