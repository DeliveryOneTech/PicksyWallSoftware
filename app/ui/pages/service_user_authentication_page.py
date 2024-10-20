from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QHBoxLayout, QSpacerItem, QSizePolicy
from app.ui.styles import Styles
from app.enums.page_number import PageNumber
from app.lib.utils.console_logger import ConsoleLogger
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.components.numeric_keyboard_component import NumericKeyboardComponent
from app.ui.components.picksy_wall_title_header_component import PicksyWallTitleHeaderComponent


class ServiceUserAuthenticationPage(QWidget):
    def __init__(self, stacked_widget: BaseQStackedWidget):
        super().__init__()
        self.console_logger = ConsoleLogger()
        self.console_logger.log()

        self.v_box = QVBoxLayout()

        self.header = PicksyWallTitleHeaderComponent()
        footer = None

        # Header
        if self.header:
            self.header.back_button_clicked.connect(lambda: stacked_widget.go_by_page_number(
                PageNumber.SERVICE_USER_AUTHENTICATION_PAGE, PageNumber.HOME_PAGE
            ))
            self.header.set_title("Servis Personeli Şifresini Giriniz.")
            self.v_box.addWidget(self.header)

        '''
        begin - content
        '''
        self.v_box.addSpacing(50)

        h_box = QHBoxLayout()
        spacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_box.addItem(spacer1)
        self.password_input = QLineEdit()
        self.password_input.setStyleSheet(Styles.bordered_input())
        self.password_input.setAlignment(Qt.AlignCenter)
        self.password_input.setFixedHeight(65)
        self.password_input.setPlaceholderText("*" * 7)
        self.password_input.setFixedWidth(650)
        self.password_input.setAlignment(Qt.AlignHCenter)
        h_box.addWidget(self.password_input)
        spacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_box.addItem(spacer2)
        self.v_box.addLayout(h_box)

        self.v_box.addSpacing(70)

        numeric_keyboard_component = NumericKeyboardComponent()
        numeric_keyboard_component.return_pressed.connect(lambda: stacked_widget.go_by_page_number(
            PageNumber.SERVICE_USER_AUTHENTICATION_PAGE, PageNumber.SERVICE_MAIN_PAGE
        ))

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
