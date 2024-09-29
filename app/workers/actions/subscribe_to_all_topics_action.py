from PyQt5.QtCore import pyqtSignal, QThread
from app.communication.iot.mqtt_subscriber import MqttSubscriber
from app.lib.models.d1_result_data_model import D1Result
from app.workers.abstracts.d1_action import D1Action
from app.enums.thread_name import ThreadName
from app.workers.thread_manager import ThreadManager


class SubscribeToAllTopicsAction(D1Action):
    is_loading_signal = pyqtSignal(bool)
    is_thread_executed = False
    result_signal = pyqtSignal(D1Result)

    def __init__(self, thread_name: str = ThreadName.SUBSCRIBE_TO_ALL_TOPICS_ACTION.value):
        super().__init__()
        self.thread_name = thread_name

    def execute(self):
        self.is_loading_signal.emit(True)

        MqttSubscriber()

        self.result_signal.emit(D1Result(True, "Subscribe process completed."))
        self.is_loading_signal.emit(False)

    @staticmethod
    def run_in_thread(auto_start: bool = False, run_with_thread_manager: bool = True, execute_func_params: list = None) -> tuple[D1Action, QThread]:
        action = SubscribeToAllTopicsAction()
        thread = QThread()
        thread_manager = ThreadManager()
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
            thread.finished.connect(lambda: thread_manager.remove_redundant_thread_action_pairs())
            thread_manager.add_thread_action_pair(action, thread)

        action.is_loading_signal.connect(
            lambda is_loading: thread_manager.kill_thread(thread) if not is_loading else None
        )
        return action, thread
