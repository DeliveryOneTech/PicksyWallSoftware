import logging
from PyQt5.QtCore import pyqtSignal, QObject, QThread
from app.communication.iot.init_subscribers import InitSubscribers
from app.communication.iot.mqtt_context import MqttContext
from app.data.enums.log_level import LogLevel
from app.lib.console_logger import ConsoleLogger
from app.lib.d1_result import D1Result
from app.services.log_service import LogService
from app.workers.abstracts.d1_action import D1Action
from app.workers.thread_manager import ThreadName, ThreadManager
import urllib.request


class CheckInternetConnectionLoop(D1Action):
    result_signal = pyqtSignal(D1Result)
    is_loading_signal = pyqtSignal(bool)
    is_thread_executed = False

    def __init__(self, thread_name=ThreadName.CHECK_INTERNET_CONNECTION_LOOP):
        super().__init__()
        self.thread_name = thread_name

    def execute(self, *args, **kwargs):
        last_internet_state = self.__get_internet_connection_state()
        while True:
            self.is_loading_signal.emit(True)

            current_internet_state = self.__get_internet_connection_state()

            if last_internet_state != current_internet_state and last_internet_state == False:
                MqttContext().reconnect()
                InitSubscribers()

            if not current_internet_state:
                self.result_signal.emit(D1Result(False))
            else:
                self.result_signal.emit(D1Result(True))

            self.is_loading_signal.emit(False)
            QThread.msleep(5000)

    @staticmethod
    def __get_internet_connection_state() -> bool:
        try:
            urllib.request.urlopen("https://www.google.com")
            ConsoleLogger().log("Checking internet connection state. Internet state: ON")
            return True
        except Exception as e:
            ConsoleLogger().log(f"Internet connection is lost. Error: {e}", logging.ERROR)
            LogService().create_system_log("Internet connection is lost.", LogLevel.ERROR)
            return False

    @staticmethod
    def run_in_thread(auto_start: bool = False, is_thread_executed: bool = True) -> tuple[QObject, QThread]:
        action = CheckInternetConnectionLoop()
        thread = QThread()
        thread_manager = ThreadManager()

        action.is_thread_executed = True
        action.moveToThread(thread)
        thread.started.connect(action.execute)

        if auto_start:
            thread.start()

        if is_thread_executed:
            thread.finished.connect(lambda: thread_manager.remove_redundant_thread_action_pairs())
            ThreadManager().add_thread_action_pair(action, thread)

        return action, thread
