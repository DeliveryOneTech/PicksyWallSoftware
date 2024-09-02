from PyQt5.QtCore import QThread, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from app.lib.console_logger import SingletonConsoleLogger
from app.styles import Styles
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.enums.page_number import PageNumber
from app.workers.actions.init_application_action import InitApplicationAction
from app.workers.thread_manager import SingletonThreadManager


class ApplicationLoadingPage(QWidget):
    def __init__(self, stacked_widget: BaseQStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.singleton_console_logger = SingletonConsoleLogger()
        self.singleton_console_logger.log()

        self.init_application_action = InitApplicationAction()
        self.init_application_action_thread = QThread()
        self.init_application_action.moveToThread(self.init_application_action_thread)
        self.init_application_action_thread.started.connect(self.init_application_action.execute)
        self.init_application_action.is_loading_signal.connect(self.on_finish_init_application_action)
        self.init_application_action.result_signal.connect(self.handle_init_application_action_result_signal)
        self.init_application_action.is_thread_executed = True
        thread_manager = SingletonThreadManager()
        thread_manager.add_thread_action_pair(self.init_application_action, self.init_application_action_thread)

        v_box = QVBoxLayout()

        loading_text_label = QLabel("PicksyWall başlatılıyor...")
        loading_text_label.setStyleSheet(Styles.header())
        loading_text_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        v_box.addWidget(loading_text_label)

        self.setLayout(v_box)

    def on_finish_init_application_action(self):
        pass

    def handle_init_application_action_result_signal(self, result):
        if result.success:
            self.stacked_widget.go_by_page_number(PageNumber.APPLICATION_LOADING, PageNumber.HOME)
        else:
            pass

    def on_shown(self):
        self.init_application_action_thread.start()
