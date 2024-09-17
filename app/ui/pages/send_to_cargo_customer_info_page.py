from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QSpacerItem, QSizePolicy
from app.enums.page_number import PageNumber
from app.lib.console_logger import ConsoleLogger
from app.styles import Styles
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.components.keyboard_component import KeyboardComponent
from app.ui.components.picksy_wall_title_header_component import PicksyWallTitleHeaderComponent


class SendToCargoCustomerInfoPage(QWidget):
    def __init__(self, stacked_widget: BaseQStackedWidget):
        super().__init__()

        self.stacked_widget = stacked_widget
        self.console_logger = ConsoleLogger()
        self.console_logger.log()

        main_layout = QGridLayout()

        header = PicksyWallTitleHeaderComponent()

        if header is not None:
            header.back_button_clicked.connect(lambda: stacked_widget.go_by_page_number(
                PageNumber.SEND_TO_CARGO_CUSTOMER_INFO,
                PageNumber.HOME
            ))
            header.set_title("Gönderici Bilgilerini Giriniz")
            main_layout.addWidget(header, 0, 0, 1, 4)

        '''
        begin - content
        '''
        name_label = QLabel("Ad:")
        name_label.setStyleSheet(Styles.label())
        main_layout.addWidget(name_label, 1, 0)

        self.name_input = QLineEdit()
        self.name_input.setStyleSheet(Styles.bg_gray_input())
        main_layout.addWidget(self.name_input, 1, 1)

        surname_label = QLabel("Soyad:")
        surname_label.setStyleSheet(Styles.label())
        main_layout.addWidget(surname_label, 2, 0)

        self.surname_input = QLineEdit()
        self.surname_input.setStyleSheet(Styles.bg_gray_input())
        main_layout.addWidget(self.surname_input, 2, 1)

        birth_year_label = QLabel("Doğum Yılı:")
        birth_year_label.setStyleSheet(Styles.label())
        main_layout.addWidget(birth_year_label, 3, 0)

        self.birth_year_input = QLineEdit()
        self.birth_year_input.setStyleSheet(Styles.bg_gray_input())
        main_layout.addWidget(self.birth_year_input, 3, 1)

        keyboard_component = KeyboardComponent()
        keyboard_component.return_pressed.connect(lambda: stacked_widget.go_by_page_number(
            PageNumber.SEND_TO_CARGO_CUSTOMER_INFO,
            PageNumber.SEND_TO_CARGO_CUSTOMER_ADDRESS
        ))
        main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Fixed, QSizePolicy.Expanding), 4, 0, 1, 4)
        main_layout.addWidget(keyboard_component, 5, 0, 1, 4)
        '''
        end - content
        '''

        self.setLayout(main_layout)

    def on_shown(self):
        self.name_input.clear()
        self.surname_input.clear()
        self.birth_year_input.clear()
        self.name_input.setFocus()
