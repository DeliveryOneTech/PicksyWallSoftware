from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QHBoxLayout, QSpacerItem, QSizePolicy
from app.lib.enums.page_number import PageNumber
from app.lib.system_logger import SingletonSystemLogger
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.components.numeric_keyboard_component import NumericKeyboardComponent
from app.ui.components.picksy_wall_title_header_component import PicksyWallTitleHeaderComponent


class ReceivePackageAuthenticationPage(QWidget):
    def __init__(self, stacked_widget: BaseQStackedWidget):
        super().__init__()
        self.singleton_system_logger = SingletonSystemLogger()
        self.singleton_system_logger.log()

        self.v_box = QVBoxLayout()

        header = PicksyWallTitleHeaderComponent(
            back_button_on_click_handler=lambda: stacked_widget.go_by_page_number(
                PageNumber.RECEIVE_PACKAGE_AUTHENTICATION, PageNumber.HOME)
        )
        footer = None

        # Header
        if header:
            header.set_title("Tek Kullanımlık Şifreyi Giriniz.")
            self.v_box.addWidget(header)

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
        self.password_input.returnPressed.connect(lambda: print("custom submit method: ", self.password_input.text()))
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
