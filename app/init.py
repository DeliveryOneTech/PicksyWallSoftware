from PyQt5.QtWidgets import QApplication
import sys
from app.ui.main_window import MainWindow
from app.lib.system_logger import SingletonSystemLogger


def run() -> int:
    """
    Initializes the application and runs it.

    Returns:
        int: The exit status code.
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    logger = SingletonSystemLogger()
    logger.log("Application is started.")

    return sys.exit(app.exec())
