from PyQt5.QtWidgets import QApplication
import sys
from app.communication.iot.mqtt_subscriber import MqttSubscriber
from app.communication.iot.mqtt_context import MqttContext
from app.ui.main_window import MainWindow
from app.lib.console_logger import ConsoleLogger
from app.services.log_service import LogService
from app.workers.actions.subscribe_to_all_topics_action import SubscribeToAllTopicsAction
from app.workers.loops.check_internet_connection_loop import CheckInternetConnectionLoop


def __on_close_app():
    MqttSubscriber().unsubscribe_all()
    MqttContext().disconnect()
    ConsoleLogger().log("Application is closing.")
    LogService().create_system_log("Application is closing.")


def __on_start_app():
    subscribe_to_all_topics_action, subscribe_to_all_topics_action_thread = SubscribeToAllTopicsAction().run_in_thread(
        auto_start=False, run_with_thread_manager=False
    )
    check_internet_connection_loop, check_internet_connection_loop_thread = CheckInternetConnectionLoop().run_in_thread(
        auto_start=False, run_with_thread_manager=False
    )

    subscribe_to_all_topics_action_thread.start()
    check_internet_connection_loop_thread.start()

    ConsoleLogger().log("Application is started.")
    LogService().create_system_log("Application is started.")


def run() -> int:
    """
    Initializes the application and runs it.

    Returns:
        int: The exit status code.
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()

    window.app_ready.connect(__on_start_app)
    app.aboutToQuit.connect(__on_close_app)
    return sys.exit(app.exec())
