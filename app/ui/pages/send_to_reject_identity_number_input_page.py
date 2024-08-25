from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout

from app.lib.system_logger import SingletonSystemLogger
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.lib.enums.page_number import PageNumber
from app.ui.components.numeric_keyboard_component import NumericKeyboardComponent
from app.ui.components.numeric_otp_inputs_component import NumericOTPInputsComponent
from app.ui.components.picksy_wall_title_header_component import PicksyWallTitleHeaderComponent


class SendToRejectIdentityNumberInputPage(QtWidgets.QWidget):
    def __init__(self, stacked_widget: BaseQStackedWidget):
        super().__init__()
        self.singleton_system_logger = SingletonSystemLogger()
        self.singleton_system_logger.log()

        self.stacked_widget = stacked_widget

        main_layout = QVBoxLayout(self)
        v_box = QVBoxLayout()

        header = PicksyWallTitleHeaderComponent(
            back_button_on_click_handler=lambda: self.stacked_widget.go_by_page_number(
                PageNumber.SEND_TO_REJECT_IDENTITY_NUMBER_INPUT, PageNumber.HOME)
        )
        footer = None

        # Header
        if header:
            header.set_title("T.C. Kimlik Numaranızı Giriniz")
            v_box.addWidget(header)

        '''
        begin - content
        '''
        # Spacing for content
        v_box.addSpacing(50)

        # OTP Input
        self.otp_input_box = NumericOTPInputsComponent(11, "identity_number_input_")
        self.otp_input_box.set_submit_function(lambda: print("custom submit method: ", self.otp_input_box.get_value()))
        v_box.addWidget(self.otp_input_box)

        # Spacing for content
        v_box.addSpacing(70)

        # Numeric Keyboard Component
        numeric_keyboard_component = NumericKeyboardComponent()
        v_box.addWidget(numeric_keyboard_component)

        # Stretch for layout spacing
        v_box.addStretch()
        '''
        end - content
        '''

        # Footer
        if footer:
            v_box.addWidget(footer)

        main_layout.addLayout(v_box)
        self.setLayout(main_layout)

    def on_shown(self):
        self.otp_input_box.clear_inputs()
        self.otp_input_box.set_focus_first_input()
