from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from app.ui.styles import Styles
from app.enums.page_number import PageNumber
from PyQt5.QtWidgets import QVBoxLayout, QLineEdit, QSpacerItem, QSizePolicy, QHBoxLayout
from app.lib.utils.console_logger import ConsoleLogger
from app.ui.components.numeric_keyboard_component import NumericKeyboardComponent
from app.ui.components.picksy_wall_title_header_component import PicksyWallTitleHeaderComponent
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget


class RejectionIdPage(QtWidgets.QWidget):
    def __init__(self, stacked_widget: BaseQStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.console_logger = ConsoleLogger()
        self.console_logger.log()

        v_box = QVBoxLayout()

        header = PicksyWallTitleHeaderComponent()
        footer = None

        if header:
            header.back_button_clicked.connect(lambda: stacked_widget.go_by_page_number(
                PageNumber.REJECTION_ID_PAGE, PageNumber.HOME_PAGE
            ))
            header.set_title("İade Teslimat Kodunu Giriniz")
            v_box.addWidget(header)

        '''
        begin - content
        '''
        v_box.addSpacing(50)

        h_box = QHBoxLayout()
        spacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_box.addItem(spacer1)
        self.reject_code_input = QLineEdit()
        self.reject_code_input.setStyleSheet(Styles.bordered_input())
        self.reject_code_input.setAlignment(Qt.AlignCenter)
        self.reject_code_input.setFixedHeight(65)
        self.reject_code_input.setFixedWidth(650)
        self.reject_code_input.setAlignment(Qt.AlignHCenter)
        h_box.addWidget(self.reject_code_input)
        spacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_box.addItem(spacer2)
        v_box.addLayout(h_box)

        v_box.addSpacing(70)

        keyboard = NumericKeyboardComponent()
        v_box.addWidget(keyboard)

        v_box.addStretch()
        '''
        end - content
        '''

        if footer:
            v_box.addWidget(footer)

        self.setLayout(v_box)

    def on_shown(self):
        self.reject_code_input.setFocus()
