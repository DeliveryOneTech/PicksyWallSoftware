from PyQt5.QtWidgets import QWidget, QGridLayout, QSpacerItem, QSizePolicy
from app.enums.page_number import PageNumber
from app.lib.utils.console_logger import ConsoleLogger
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.components.approve_with_checkbox_input_component import ApproveWithCheckboxInputComponent
from app.ui.components.numeric_keyboard_component import NumericKeyboardComponent
from app.ui.components.numeric_otp_inputs_component import NumericOTPInputsComponent
from app.ui.components.picksy_wall_title_header_component import PicksyWallTitleHeaderComponent
from app.ui.components.wizard_component import WizardItemViewModel, WizardComponent


class SenderIdentificationPage(QWidget):

    def __init__(self, stacked_widget: BaseQStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.console_logger = ConsoleLogger()
        self.console_logger.log()

        main_layout = QGridLayout()

        header = PicksyWallTitleHeaderComponent()

        if header is not None:
            header.back_button_clicked.connect(lambda: stacked_widget.go_by_page_number(
                PageNumber.SENDER_IDENTIFICATION_PAGE,
                PageNumber.HOME_PAGE
            ))
            header.set_title("T.C. Kimlik Numaranızı Giriniz")
            main_layout.addWidget(header, 0, 0, 1, 3)

        '''
        begin - content
        '''
        self.wizard = WizardComponent("send_to_cargo_identity_number_input_page_", [
            WizardItemViewModel(1, "Kimlik No"),
            WizardItemViewModel(2, "Gönderici Bilgileri"),
            WizardItemViewModel(3, "Alıcı Bilgileri"),
        ], True)

        main_layout.addWidget(self.wizard, 1, 0, 1, 3)

        self.otp_input_box = NumericOTPInputsComponent(11, "send_to_cargo_identity_number_input_")
        main_layout.addWidget(self.otp_input_box, 2, 0, 1, 3)

        numeric_keyboard_component = NumericKeyboardComponent()
        main_layout.addWidget(numeric_keyboard_component, 3, 0, 1, 3)
        numeric_keyboard_component.return_pressed.connect(lambda: stacked_widget.go_by_page_number(
            PageNumber.SENDER_IDENTIFICATION_PAGE,
            PageNumber.SENDER_INFORMATION_PAGE
        ))

        self.approve_with_checkbox_component = ApproveWithCheckboxInputComponent()

        # add space
        main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Fixed, QSizePolicy.Expanding), 4, 0, 1, 3)
        main_layout.addWidget(self.approve_with_checkbox_component, 5, 0, 1, 3)
        '''
        end - content
        '''

        # add spacer for header to be fixed at the top

        self.setLayout(main_layout)

    def on_shown(self):
        self.otp_input_box.clear_inputs()
        self.otp_input_box.set_focus_first_input()
        self.approve_with_checkbox_component.condition_checkbox.setChecked(False)
        self.wizard.go_to_step(0)
