from PyQt5.QtCore import QThread, Qt, QPropertyAnimation, QEasingCurve, QPoint, QRect, QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGraphicsOpacityEffect, QSpacerItem, QSizePolicy, QHBoxLayout
from app.lib.console_logger import SingletonConsoleLogger
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.enums.page_number import PageNumber
from app.ui.utils import ui_utils
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

        h_box = QHBoxLayout()

        spacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_box.addItem(spacer_1)

        logo_label = QLabel()
        logo_label.setPixmap(ui_utils.get_pixmap(":/logos/assets/gray-d1-logo.png"))
        # tam ortaya al
        logo_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        logo_label.setFixedSize(600, 120)
        logo_label.setScaledContents(True)

        h_box.addWidget(logo_label)

        spacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_box.addItem(spacer_2)

        self.create_pulse_animation(logo_label)

        self.setLayout(h_box)

    # UI METHODS
    def create_pulse_animation(self, label):
        # Apply opacity effect to the label
        opacity_effect = QGraphicsOpacityEffect(label)
        label.setGraphicsEffect(opacity_effect)

        # Create property animation for opacity
        self.animation = QPropertyAnimation(opacity_effect, b"opacity")
        self.animation.setDuration(1000)  # Duration for one pulse cycle

        # Set animation keyframes: from fully visible to partially transparent and back
        self.animation.setStartValue(0.9)
        self.animation.setKeyValueAt(0.9, 0.4)
        self.animation.setEndValue(0.9)

        # Set easing curve and infinite loop
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.setLoopCount(-1)

        # Start the animation
        self.animation.start()

    # LOGIC METHODS

    def on_finish_init_application_action(self):
        pass

    def handle_init_application_action_result_signal(self, result):
        if result.success:
            self.stacked_widget.go_by_page_number(PageNumber.APPLICATION_LOADING, PageNumber.HOME)
        else:
            pass

    def on_shown(self):
        self.init_application_action_thread.start()
