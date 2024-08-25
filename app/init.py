from PyQt5.QtWidgets import QApplication
import sys
from app.ui.main_window import MainWindow
from app.lib.system_logger import SingletonSystemLogger
from app.services.system_log_service import SingletonSystemLogService


def run() -> int:
    """
    Initializes the application and runs it.

    Returns:
        int: The exit status code.
    """
    db_logger = SingletonSystemLogService()
    logger = SingletonSystemLogger()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    logger.log("Application is started.")
    db_logger.create_system_log("Application is started.")

    return sys.exit(app.exec())
