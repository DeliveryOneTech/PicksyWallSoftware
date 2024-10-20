import logging
from PyQt5.QtCore import pyqtSignal, QThread
from app.communication.iot.mqtt_context import MqttContext
from app.enums.log_level import LogLevel
from app.lib.utils.console_logger import ConsoleLogger
from app.lib.models.d1_result_data_model import D1Result
from app.services.log_service import LogService
from app.workers.abstracts.d1_action import D1Action
from app.workers.thread_manager import ThreadManager
import urllib.request
from app.enums.thread_name import ThreadName


class CheckInternetConnectionLoop(D1Action):
    result_signal = pyqtSignal(D1Result)
    is_loading_signal = pyqtSignal(bool)
    is_thread_executed = False

    def __init__(self, thread_name=ThreadName.CHECK_INTERNET_CONNECTION_LOOP.value):
        super().__init__()
        self.thread_name = thread_name
        self.is_running = False

    def execute(self):
        self.is_running = True

        while self.is_running:
            self.is_loading_signal.emit(True)

            current_internet_state = self.get_internet_connection_state()

            if not current_internet_state:
                self.result_signal.emit(D1Result(False))
            else:
                self.result_signal.emit(D1Result(True))

            self.is_loading_signal.emit(False)
            QThread.msleep(5000)

    def stop_internet_connection_loop(self):
        self.is_running = False

    @staticmethod
    def get_internet_connection_state() -> bool:
        try:
            urllib.request.urlopen("https://www.google.com")
            ConsoleLogger().log("Checking internet connection state. STATE: ON")
            return True
        except urllib.error.URLError:
            ConsoleLogger().log(f"Internet connection is lost. STATE: OFF", logging.ERROR)
            LogService().create_system_log("Internet connection is lost.", LogLevel.ERROR)
            return False
        except Exception as e:
            ConsoleLogger().log(
                f"An unexpected error occurred while checking the internet connection. ERROR: {e}, STATE: OFF",
                logging.ERROR
            )
            LogService().create_system_log(
                f"An unexpected error occurred while checking the internet connection. ERROR: {e}, STATE: OFF",
                LogLevel.ERROR
            )
            return False

    @staticmethod
    def run_in_thread(auto_start: bool = False, run_with_thread_manager: bool = True,
                      execute_func_params: list = None) -> tuple[D1Action, QThread]:
        action = CheckInternetConnectionLoop()
        thread = QThread()
        thread.setObjectName(action.thread_name)
        thread_manager = ThreadManager()

        action.is_thread_executed = True
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

        return action, thread
