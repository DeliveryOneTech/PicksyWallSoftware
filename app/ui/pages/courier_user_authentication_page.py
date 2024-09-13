from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QHBoxLayout, QSpacerItem, QSizePolicy, QLabel
from app.styles import Styles
from app.enums.page_number import PageNumber
from app.lib.console_logger import ConsoleLogger
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.components.numeric_keyboard_component import NumericKeyboardComponent
from app.ui.components.picksy_wall_title_header_component import PicksyWallTitleHeaderComponent


class CourierUserAuthenticationPage(QWidget):
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
                PageNumber.COURIER_USER_AUTHENTICATION, PageNumber.OTHERS_MAIN
            ))
            self.header.set_title("Kullanıcı Bilgilerini Giriniz")
            self.v_box.addWidget(self.header)

        '''
        begin - content
        '''
        self.v_box.addSpacing(50)

        h_box = QHBoxLayout()

        spacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_box.addItem(spacer1)

        user_name_v_box = QVBoxLayout()
        user_name_label = QLabel("Kullanıcı Adı")
        user_name_label.setStyleSheet(Styles.label())
        user_name_label.setAlignment(Qt.AlignCenter)
        user_name_label.setFixedHeight(65)
        self.user_name_input = QLineEdit()
        self.user_name_input.setStyleSheet(Styles.bg_gray_input())
        self.user_name_input.setAlignment(Qt.AlignCenter)
        self.user_name_input.setFixedHeight(65)
        self.user_name_input.setFixedWidth(650)
        self.user_name_input.setAlignment(Qt.AlignHCenter)
        user_name_v_box.addWidget(user_name_label)
        user_name_v_box.addWidget(self.user_name_input)

        h_box.addLayout(user_name_v_box)

        spacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_box.addItem(spacer2)

        password_v_box = QVBoxLayout()
        password_label = QLabel("Şifre")
        password_label.setStyleSheet(Styles.label())
        password_label.setAlignment(Qt.AlignCenter)
        password_label.setFixedHeight(65)
        self.password_input = QLineEdit()
        self.password_input.setStyleSheet(Styles.bg_gray_input())
        self.password_input.setAlignment(Qt.AlignCenter)
        self.password_input.setFixedHeight(65)
        self.password_input.setFixedWidth(650)
        self.password_input.setAlignment(Qt.AlignHCenter)
        password_v_box.addWidget(password_label)
        password_v_box.addWidget(self.password_input)

        h_box.addLayout(password_v_box)

        spacer3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_box.addItem(spacer3)

        self.v_box.addLayout(h_box)

        self.v_box.addSpacing(70)

        numeric_keyboard_component = NumericKeyboardComponent()
        numeric_keyboard_component.return_pressed.connect(lambda: self.console_logger.log(self.user_name_input.text() + " " + self.password_input.text()))

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
        self.user_name_input.clear()
        self.password_input.clear()
        self.user_name_input.setFocus()
