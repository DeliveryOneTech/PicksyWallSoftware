from PyQt5.QtWidgets import QApplication
import sys
from app.communication.iot.init_subscribers import SingletonInitSubscribers
from app.communication.iot.mqtt_context import SingletonMqttContext
from app.ui.main_window import MainWindow
from app.lib.console_logger import SingletonConsoleLogger
from app.services.log_service import SingletonLogService
from app.workers.actions.subscribe_to_all_topics_action import SubscribeToAllTopicsAction


def __on_close_app():
    SingletonInitSubscribers().unsubscribe_all()
    SingletonMqttContext().disconnect()
    SingletonConsoleLogger().log("Application is closing.")
    SingletonLogService().create_system_log("Application is closing.")


def __on_start_app():
    subscribe_to_all_topics_action, subscribe_to_all_topics_action_thread = SubscribeToAllTopicsAction().run_in_thread(
        auto_start=True
    )
    SingletonConsoleLogger().log("Application is started.")
    SingletonLogService().create_system_log("Application is started.")


def run() -> int:
    """
    Initializes the application and runs it.

    Returns:
        int: The exit status code.
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    __on_start_app()

    app.aboutToQuit.connect(__on_close_app)
    return sys.exit(app.exec())
