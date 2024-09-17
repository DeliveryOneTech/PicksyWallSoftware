from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QHBoxLayout, QSpacerItem, QSizePolicy, QLabel, QGridLayout
from app.styles import Styles
from app.enums.page_number import PageNumber
from app.lib.console_logger import ConsoleLogger
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.components.keyboard_component import KeyboardComponent
from app.ui.components.picksy_wall_title_header_component import PicksyWallTitleHeaderComponent


class CourierUserAuthenticationPage(QWidget):
    def __init__(self, stacked_widget: BaseQStackedWidget):
        super().__init__()
        self.console_logger = ConsoleLogger()
        self.console_logger.log()

        main_layout = QGridLayout()

        header = PicksyWallTitleHeaderComponent()

        if header is not None:
            header.back_button_clicked.connect(lambda: stacked_widget.go_by_page_number(
                PageNumber.COURIER_USER_AUTHENTICATION,
                PageNumber.HOME
            ))
            header.set_title("Kurye Kullanıcı Bilgilerini Giriniz")
            main_layout.addWidget(header, 0, 0, 1, 4)

        '''
        begin - content
        '''
        user_name_label = QLabel("Kullanıcı Adı:")
        user_name_label.setStyleSheet(Styles.label())
        main_layout.addWidget(user_name_label, 1, 0)

        self.user_name_input = QLineEdit()
        self.user_name_input.setStyleSheet(Styles.bg_gray_input())
        main_layout.addWidget(self.user_name_input, 1, 1)

        password_label = QLabel("Şifre:")
        password_label.setStyleSheet(Styles.label())
        main_layout.addWidget(password_label, 2, 0)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(Styles.bg_gray_input())
        main_layout.addWidget(self.password_input, 2, 1)

        keyboard_component = KeyboardComponent()
        keyboard_component.return_pressed.connect(lambda: stacked_widget.go_by_page_number(
            PageNumber.COURIER_USER_AUTHENTICATION,
            PageNumber.OTHERS_MAIN
        ))
        main_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding), 3, 0, 1, 4)
        main_layout.addWidget(keyboard_component, 4, 0, 1, 4)
        main_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding), 5, 0, 1, 4)

        '''
        end - content
        '''

        self.setLayout(main_layout)

    def on_shown(self):
        self.user_name_input.clear()
        self.password_input.clear()
        self.user_name_input.setFocus()
