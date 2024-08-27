from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QHBoxLayout, QSpacerItem, QSizePolicy
from app.actions.service_user_login_action import ServiceUserLoginAction
from app.ui.enums.page_number import PageNumber
from app.lib.console_logger import SingletonConsoleLogger
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.components.numeric_keyboard_component import NumericKeyboardComponent
from app.ui.components.picksy_wall_title_header_component import PicksyWallTitleHeaderComponent
from app.ui.utils.ui_utils import lock_ui, unlock_ui


class ServiceUserAuthenticationPage(QWidget):
    def __init__(self, stacked_widget: BaseQStackedWidget):
        super().__init__()
        self.singleton_console_logger = SingletonConsoleLogger()
        self.singleton_console_logger.log()

        self.v_box = QVBoxLayout()

        self.header = PicksyWallTitleHeaderComponent()
        footer = None

        # Header
        if self.header:
            self.header.back_button_clicked.connect(lambda: stacked_widget.go_by_page_number(
                PageNumber.SERVICE_USER_AUTHENTICATION, PageNumber.HOME
            ))
            self.header.set_title("Servis Personeli Şifresini Giriniz.")
            self.v_box.addWidget(self.header)

        login_action = ServiceUserLoginAction()
        login_action.result_signal.connect(lambda result: (
            stacked_widget.go_by_page_number(PageNumber.SERVICE_USER_AUTHENTICATION, PageNumber.HOME) if result.success
            else None
        ))
        login_action.is_loading_signal.connect(lambda is_loading: lock_ui(self) if is_loading else unlock_ui(self))

        '''
        begin - content
        '''
        self.v_box.addSpacing(50)

        h_box = QHBoxLayout()
        spacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_box.addItem(spacer1)
        self.password_input = QLineEdit()
        self.password_input.setStyleSheet(
            "font-size: 25px; padding: 10px; border: 1px solid #000; border-radius: 5px; background-color: transparent;")
        self.password_input.setAlignment(Qt.AlignCenter)
        self.password_input.setFixedHeight(65)
        self.password_input.setPlaceholderText("*" * 7)
        self.password_input.setFixedWidth(650)
        self.password_input.setAlignment(Qt.AlignHCenter)
        self.password_input.returnPressed.connect(lambda: login_action.run_in_thread(self.password_input.text()))
        h_box.addWidget(self.password_input)
        spacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_box.addItem(spacer2)
        self.v_box.addLayout(h_box)

        self.v_box.addSpacing(70)

        numeric_keyboard_component = NumericKeyboardComponent()
        self.v_box.addWidget(numeric_keyboard_component)

        self.v_box.addStretch()
        '''
        end - content
        '''

        # Footer
        if footer:
            self.v_box.addWidget(footer)

        self.setLayout(self.v_box)

    def on_shown(self):
        self.password_input.clear()
        self.password_input.setFocus()
