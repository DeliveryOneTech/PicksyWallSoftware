from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QHBoxLayout, QSpacerItem, QSizePolicy, QLabel

from app.ui.utils import ui_utils
from app.ui.utils.styles import Styles
from app.enums.page_number import PageNumber
from app.lib.console_logger import ConsoleLogger
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.components.numeric_keyboard_component import NumericKeyboardComponent
from app.ui.components.picksy_wall_title_header_component import PicksyWallTitleHeaderComponent


class PackageAuthenticationPage(QWidget):
    def __init__(self, stacked_widget: BaseQStackedWidget):
        super().__init__()
        self.console_logger = ConsoleLogger()
        self.console_logger.log()

        self.v_box = QVBoxLayout()

        header = PicksyWallTitleHeaderComponent()
        footer = None

        # Header
        if header:
            header.back_button_clicked.connect(lambda: stacked_widget.go_by_page_number(
                PageNumber.PACKAGE_AUTHENTICATION_PAGE, PageNumber.HOME_PAGE
            ))
            header.set_title("Paket Barkod Numarasını Giriniz.")
            self.v_box.addWidget(header)

        '''
        begin - content
        '''
        self.v_box.addSpacing(50)

        h_box = QHBoxLayout()
        spacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_box.addItem(spacer1)
        self.barcode_number_input = QLineEdit()
        self.barcode_number_input.setStyleSheet(Styles.bordered_input())
        self.barcode_number_input.setAlignment(Qt.AlignCenter)
        self.barcode_number_input.setFixedHeight(65)
        self.barcode_number_input.setPlaceholderText("*" * 7)
        self.barcode_number_input.setFixedWidth(650)
        self.barcode_number_input.setAlignment(Qt.AlignHCenter)
        h_box.addWidget(self.barcode_number_input)
        spacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_box.addItem(spacer2)
        self.v_box.addLayout(h_box)

        self.v_box.addSpacing(70)

        numeric_keyboard_component = NumericKeyboardComponent()
        numeric_keyboard_component.return_pressed.connect(lambda: self.console_logger.log(self.barcode_number_input.text()))
        self.v_box.addWidget(numeric_keyboard_component)

        self.v_box.addStretch()

        qr_h_box = QHBoxLayout()
        qr_code_image = QLabel()
        qr_code_image.setPixmap(ui_utils.get_pixmap(':/icons/assets/qr-code.svg'))
        qr_code_image.setFixedWidth(200)
        qr_code_image.setFixedHeight(200)
        message_label = QLabel("Veya,\nQR Kodunu Taratınız.")
        message_label.setStyleSheet(Styles.label())
        qr_h_box.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        qr_h_box.addWidget(message_label)
        qr_h_box.addWidget(qr_code_image)
        self.v_box.addLayout(qr_h_box)
        '''
        end - content
        '''

        # Footer
        if footer:
            self.v_box.addWidget(footer)

        self.setLayout(self.v_box)

    def on_shown(self):
        self.barcode_number_input.clear()
        self.barcode_number_input.setFocus()
