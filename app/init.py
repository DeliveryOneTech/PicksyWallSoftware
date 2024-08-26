from PyQt5.QtWidgets import QApplication
import sys
from app.ui.main_window import MainWindow
from app.lib.console_logger import SingletonConsoleLogger
from app.services.log_service import SingletonLogService


def run() -> int:
    """
    Initializes the application and runs it.

    Returns:
        int: The exit status code.
    """
    db_logger = SingletonLogService()
    logger = SingletonConsoleLogger()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    logger.log("Application is started.")
    db_logger.create_system_log("Application is started.")

    return sys.exit(app.exec())
