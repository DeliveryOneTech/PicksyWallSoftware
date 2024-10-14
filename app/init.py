import logging
from PyQt5.QtWidgets import QApplication
import sys
from app.communication.iot.mqtt_subscriber import MqttSubscriber
from app.communication.iot.mqtt_context import MqttContext
from app.ui.main_window import MainWindow
from app.lib.console_logger import ConsoleLogger
from app.services.log_service import LogService


def __on_close_app():
    MqttSubscriber().unsubscribe_all()
    MqttContext().disconnect()
    ConsoleLogger().log("Application is closing.")
    LogService().create_system_log("Application is closing.")


def run() -> int:
    """
    Initializes the application and runs it.

    Returns:
        int: The exit status code.
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()

    app.aboutToQuit.connect(__on_close_app)
    return sys.exit(app.exec())
