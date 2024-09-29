from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QSpacerItem, QSizePolicy
from app.enums.page_number import PageNumber
from app.lib.console_logger import ConsoleLogger
from app.styles import Styles
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.components.keyboard_component import KeyboardComponent
from app.ui.components.picksy_wall_title_header_component import PicksyWallTitleHeaderComponent
from app.ui.components.wizard_component import WizardComponent, WizardItemViewModel


class SendToCargoReceiverInfoPage(QWidget):
    def __init__(self, stacked_widget: BaseQStackedWidget):
        super().__init__()

        self.stacked_widget = stacked_widget
        self.console_logger = ConsoleLogger()
        self.console_logger.log()

        main_layout = QGridLayout()

        header = PicksyWallTitleHeaderComponent()

        if header is not None:
            header.back_button_clicked.connect(lambda: stacked_widget.go_by_page_number(
                PageNumber.SEND_TO_CARGO_RECEIVER_INFO,
                PageNumber.HOME
            ))
            header.set_title("Alıcı Bilgilerini Giriniz")
            main_layout.addWidget(header, 0, 0, 1, 4)

        '''
        begin - content
        '''
        self.wizard = WizardComponent("send_to_cargo_receiver_info_page_", [
            WizardItemViewModel(1, "Kimlik No"),
            WizardItemViewModel(2, "Gönderici Bilgileri"),
            WizardItemViewModel(3, "Alıcı Bilgileri"),
        ], True)

        main_layout.addWidget(self.wizard, 1, 0, 1, 4)

        main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Fixed, QSizePolicy.Expanding), 2, 0)

        name_label = QLabel("Ad:")
        name_label.setStyleSheet(Styles.label())
        main_layout.addWidget(name_label, 3, 0)

        self.name_input = QLineEdit()
        self.name_input.setStyleSheet(Styles.bg_gray_input())
        main_layout.addWidget(self.name_input, 3, 1)

        surname_label = QLabel("Soyad:")
        surname_label.setStyleSheet(Styles.label())
        main_layout.addWidget(surname_label, 4, 0)

        self.surname_input = QLineEdit()
        self.surname_input.setStyleSheet(Styles.bg_gray_input())
        main_layout.addWidget(self.surname_input, 4, 1)

        phone_label = QLabel("Telefon:")
        phone_label.setStyleSheet(Styles.label())
        main_layout.addWidget(phone_label, 5, 0)

        self.phone_input = QLineEdit()
        self.phone_input.setStyleSheet(Styles.bg_gray_input())
        main_layout.addWidget(self.phone_input, 5, 1)

        keyboard_component = KeyboardComponent()
        keyboard_component.return_pressed.connect(lambda: stacked_widget.go_by_page_number(
            PageNumber.SEND_TO_CARGO_RECEIVER_INFO,
            PageNumber.SEND_TO_CARGO_RECEIVER_ADDRESS
        ))
        main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Fixed, QSizePolicy.Expanding), 6, 0, 1, 3)
        main_layout.addWidget(keyboard_component, 7, 0, 1, 3)
        main_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding), 8, 0, 1, 3)
        '''
        end - content
        '''

        self.setLayout(main_layout)

    def on_shown(self):
        self.name_input.clear()
        self.surname_input.clear()
        self.phone_input.clear()
        self.name_input.setFocus()
        self.wizard.go_to_step(2)
