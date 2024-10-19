import sys
from app.lib.utils.utils import Utils
from PyQt5.QtWidgets import QApplication
from app.ui.main_window import MainWindow
from app.services.log_service import LogService
from app.lib.utils.console_logger import ConsoleLogger
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget


def __on_close_app(stacked_widget: BaseQStackedWidget):
    stacked_widget.mqtt_worker.unsubscribe_all()
    stacked_widget.mqtt_worker.disconnect()
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

    app.aboutToQuit.connect(
        lambda: __on_close_app(window.stacked_widget)
    )
    return sys.exit(app.exec())
