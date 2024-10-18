from PyQt5.QtWidgets import QApplication
import sys
from app.communication.iot.mqtt_subscriber import MqttSubscriber
from app.communication.iot.mqtt_context import MqttContext
from app.lib.utils.utils import Utils
from app.ui.main_window import MainWindow
from app.lib.utils.console_logger import ConsoleLogger
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
    application_mode = Utils.get_value_from_app_config('ApplicationMode')
    app = QApplication(sys.argv)
    window = MainWindow()

    if application_mode == 'development':
        window.show()
    else:
        window.showFullScreen()

    app.aboutToQuit.connect(__on_close_app)
    return sys.exit(app.exec())
