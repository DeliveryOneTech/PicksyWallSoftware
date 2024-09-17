from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QSpacerItem, QSizePolicy
from app.enums.page_number import PageNumber
from app.lib.console_logger import ConsoleLogger
from app.styles import Styles
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.components.keyboard_component import KeyboardComponent
from app.ui.components.picksy_wall_title_header_component import PicksyWallTitleHeaderComponent


class SendToCargoCustomerAddressPage(QWidget):
    def __init__(self, stacked_widget: BaseQStackedWidget):
        super().__init__()

        self.stacked_widget = stacked_widget
        self.console_logger = ConsoleLogger()
        self.console_logger.log()

        main_layout = QGridLayout()

        header = PicksyWallTitleHeaderComponent()

        if header is not None:
            header.back_button_clicked.connect(lambda: stacked_widget.go_by_page_number(
                PageNumber.SEND_TO_CARGO_CUSTOMER_ADDRESS,
                PageNumber.HOME
            ))
            header.set_title("Gönderici Adres Bilgilerini Giriniz")
            main_layout.addWidget(header, 0, 0, 1, 4)

        '''
        begin - content
        '''
        city_label = QLabel("İl:")
        city_label.setStyleSheet(Styles.label())
        main_layout.addWidget(city_label, 1, 0)

        self.city_input = QLineEdit()
        self.city_input.setStyleSheet(Styles.bg_gray_input())
        main_layout.addWidget(self.city_input, 1, 1)

        district_label = QLabel("İlçe:")
        district_label.setStyleSheet(Styles.label())
        main_layout.addWidget(district_label, 2, 0)

        self.district_input = QLineEdit()
        self.district_input.setStyleSheet(Styles.bg_gray_input())
        main_layout.addWidget(self.district_input, 2, 1)

        neighborhood_label = QLabel("Mahalle:")
        neighborhood_label.setStyleSheet(Styles.label())
        main_layout.addWidget(neighborhood_label, 3, 0)

        self.neighborhood_input = QLineEdit()
        self.neighborhood_input.setStyleSheet(Styles.bg_gray_input())
        main_layout.addWidget(self.neighborhood_input, 3, 1)

        address_label = QLabel("Adres:")
        address_label.setStyleSheet(Styles.label())
        main_layout.addWidget(address_label, 1, 2, 3, 1)

        self.address_input = QTextEdit()
        self.address_input.setStyleSheet(Styles.bg_gray_input())
        main_layout.addWidget(self.address_input, 1, 3, 3, 1)

        keyboard_component = KeyboardComponent()
        main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Fixed, QSizePolicy.Expanding), 4, 1, 1, 4)
        keyboard_component.return_pressed.connect(lambda: stacked_widget.go_by_page_number(
            PageNumber.SEND_TO_CARGO_CUSTOMER_ADDRESS,
            PageNumber.SEND_TO_CARGO_RECEIVER_INFO
        ))
        main_layout.addWidget(keyboard_component, 5, 0, 1, 4)

        '''
        end - content
        '''

        self.setLayout(main_layout)

    def on_shown(self):
        self.city_input.clear()
        self.district_input.clear()
        self.neighborhood_input.clear()
        self.address_input.clear()
        self.city_input.setFocus()
