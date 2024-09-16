from PyQt5 import QtWidgets
from app.styles import Styles
from app.ui.components.keyboard_component import KeyboardComponent
from app.ui.components.wizard_component import WizardItemViewModel, WizardComponent
from app.enums.page_number import PageNumber
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QLabel, QLineEdit, QTextEdit
from app.lib.console_logger import ConsoleLogger
from app.ui.components.approve_with_checkbox_input_component import ApproveWithCheckboxInputComponent
from app.ui.components.numeric_keyboard_component import NumericKeyboardComponent
from app.ui.components.numeric_otp_inputs_component import NumericOTPInputsComponent
from app.ui.components.picksy_wall_title_header_component import PicksyWallTitleHeaderComponent
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget


class SendToCargoIdentityNumberInputPage(QtWidgets.QWidget):
    def __init__(self, stacked_widget: BaseQStackedWidget):
        super().__init__()
        self.active_wizard_index = 1
        self.step_1_title = "T.C. Kimlik Numaranızı Giriniz"
        self.step_2_title = "Kimlik Bilgilerinizi Giriniz"
        self.step_3_title = "Alıcı Bilgilerini Giriniz"
        self.step_4_title = "Alıcı Adres Bilgisini Giriniz"

        self.console_logger = ConsoleLogger()
        self.console_logger.log()

        self.stacked_widget = stacked_widget

        otp_widget = QtWidgets.QWidget()
        customer_info_widget = QtWidgets.QWidget()
        receiver_info_widget = QtWidgets.QWidget()
        receiver_address_widget = QtWidgets.QWidget()
        self.send_to_cargo_identity_number_inner_stack = QtWidgets.QStackedWidget()

        main_layout = QVBoxLayout(self)
        v_box = QVBoxLayout()

        self.header = PicksyWallTitleHeaderComponent()
        footer = None

        # Header
        if self.header:
            self.header.back_button_clicked.connect(lambda: self.stacked_widget.go_by_page_number(
                PageNumber.SEND_TO_CARGO_IDENTITY_NUMBER_INPUT, PageNumber.HOME
            ))
            self.header.set_title(self.step_1_title)
            v_box.addWidget(self.header)

        '''
        begin - content
        '''
        self.wizard_component = WizardComponent(
            "send_to_cargo_identity_number_input_step_",
            [
                WizardItemViewModel(1, "Kimlik No Doğrulama"),
                WizardItemViewModel(2, "Gönderici Bilgileri"),
                WizardItemViewModel(3, "Alıcı Bilgileri"),
                WizardItemViewModel(4, "Adres"),
            ])
        v_box.addWidget(self.wizard_component)
        self.wizard_component.emit_current_index_changed()
        self.wizard_component.current_index_changed.connect(lambda index: self.on_change_wizard_index(index))

        # Spacing for content
        v_box.addSpacing(25)

        '''
        begin - otp_widget
        '''
        otp_widget_layout = QVBoxLayout()
        otp_widget.setLayout(otp_widget_layout)
        # OTP Input
        self.otp_input_box = NumericOTPInputsComponent(11, "send_to_cargo_identity_number_input_")
        otp_widget_layout.addWidget(self.otp_input_box)
        # space
        otp_widget_layout.addSpacing(25)
        # Numeric Keyboard Component
        numeric_keyboard_component = NumericKeyboardComponent()
        numeric_keyboard_component.return_pressed.connect(lambda: self.console_logger.log("pressed_return"))
        otp_widget_layout.addWidget(numeric_keyboard_component)
        # approve_with_checkbox_input_component
        self.approve_with_checkbox_component = ApproveWithCheckboxInputComponent()
        otp_widget_layout.addStretch()
        otp_widget_layout.addWidget(self.approve_with_checkbox_component)
        '''
        end - otp_widget
        '''

        '''
        begin - customer_info_widget
        '''
        self.customer_info_keyboard_component = KeyboardComponent()
        self.customer_info_keyboard_component.return_pressed.connect(lambda: self.console_logger.log("pressed_return"))

        customer_info_widget_layout = QVBoxLayout()
        customer_info_widget.setLayout(customer_info_widget_layout)

        customer_info_grid_layout = QGridLayout()
        customer_info_widget_layout.addLayout(customer_info_grid_layout)

        # ad, soyad, doğum yılı, il, ilçe, mahalle, adres
        name_label = QLabel("Ad:")
        name_label.setStyleSheet(Styles.label())
        surname_label = QLabel("Soyad:")
        surname_label.setStyleSheet(Styles.label())
        birth_year_label = QLabel("Doğum Yılı:")
        birth_year_label.setStyleSheet(Styles.label())
        city_label = QLabel("İl:")
        city_label.setStyleSheet(Styles.label())
        district_label = QLabel("İlçe:")
        district_label.setStyleSheet(Styles.label())
        neighborhood_label = QLabel("Mahalle:")
        neighborhood_label.setStyleSheet(Styles.label())
        address_label = QLabel("Adres:")
        address_label.setStyleSheet(Styles.label())

        self.name_input = QLineEdit()
        self.name_input.setStyleSheet(Styles.bg_gray_input(15))
        self.surname_input = QLineEdit()
        self.surname_input.setStyleSheet(Styles.bg_gray_input(15))
        self.birth_year_input = QLineEdit()
        self.birth_year_input.setStyleSheet(Styles.bg_gray_input(15))
        self.city_input = QLineEdit()
        self.city_input.setStyleSheet(Styles.bg_gray_input(15))
        self.district_input = QLineEdit()
        self.district_input.setStyleSheet(Styles.bg_gray_input(15))
        self.neighborhood_input = QLineEdit()
        self.neighborhood_input.setStyleSheet(Styles.bg_gray_input(15))
        self.address_input = QTextEdit()
        self.address_input.setStyleSheet(Styles.bg_gray_input())

        customer_info_grid_layout.addWidget(name_label, 0, 0)
        customer_info_grid_layout.addWidget(self.name_input, 0, 1)
        customer_info_grid_layout.addWidget(surname_label, 1, 0)
        customer_info_grid_layout.addWidget(self.surname_input, 1, 1)
        customer_info_grid_layout.addWidget(birth_year_label, 2, 0)
        customer_info_grid_layout.addWidget(self.birth_year_input, 2, 1)
        customer_info_grid_layout.addWidget(city_label, 3, 0)
        customer_info_grid_layout.addWidget(self.city_input, 3, 1)
        customer_info_grid_layout.addWidget(district_label, 4, 0)
        customer_info_grid_layout.addWidget(self.district_input, 4, 1)
        customer_info_grid_layout.addWidget(neighborhood_label, 5, 0)
        customer_info_grid_layout.addWidget(self.neighborhood_input, 5, 1)

        customer_info_grid_layout.addWidget(address_label, 0, 2)
        customer_info_grid_layout.addWidget(self.address_input, 0, 3, 6, 1)

        customer_info_grid_layout.setSpacing(50)
        customer_info_grid_layout.setContentsMargins(10, 10, 10, 10)

        customer_info_widget_layout.addStretch()
        customer_info_widget_layout.addSpacing(25)
        customer_info_widget_layout.addWidget(self.customer_info_keyboard_component)

        customer_info_widget_layout.addStretch()

        '''
        end - customer_info_widget
        '''

        '''
        begin - receiver_info_widget
        '''
        self.receiver_info_keyboard_component = KeyboardComponent()
        self.receiver_info_keyboard_component.return_pressed.connect(lambda: self.console_logger.log("pressed_return"))

        receiver_info_widget_layout = QVBoxLayout()
        receiver_info_widget.setLayout(receiver_info_widget_layout)

        receiver_info_grid_layout = QGridLayout()
        receiver_info_widget_layout.addLayout(receiver_info_grid_layout)

        receiver_name_label = QLabel("Ad:")
        receiver_name_label.setStyleSheet(Styles.label())
        receiver_surname_label = QLabel("Soyad:")
        receiver_surname_label.setStyleSheet(Styles.label())
        receiver_phone_label = QLabel("Telefon:")
        receiver_phone_label.setStyleSheet(Styles.label())

        self.receiver_name_input = QLineEdit()
        self.receiver_name_input.setStyleSheet(Styles.bg_gray_input(15))
        self.receiver_surname_input = QLineEdit()
        self.receiver_surname_input.setStyleSheet(Styles.bg_gray_input(15))
        self.receiver_phone_input = QLineEdit()
        self.receiver_phone_input.setStyleSheet(Styles.bg_gray_input(15))

        receiver_info_grid_layout.addWidget(receiver_name_label, 0, 0)
        receiver_info_grid_layout.addWidget(self.receiver_name_input, 0, 1)
        receiver_info_grid_layout.addWidget(receiver_surname_label, 1, 0)
        receiver_info_grid_layout.addWidget(self.receiver_surname_input, 1, 1)
        receiver_info_grid_layout.addWidget(receiver_phone_label, 2, 0)
        receiver_info_grid_layout.addWidget(self.receiver_phone_input, 2, 1)

        receiver_info_grid_layout.setSpacing(50)
        receiver_info_grid_layout.setContentsMargins(10, 10, 10, 10)

        receiver_info_widget_layout.addStretch()
        receiver_info_widget_layout.addSpacing(25)
        receiver_info_widget_layout.addWidget(self.receiver_info_keyboard_component)

        receiver_info_widget_layout.addStretch()

        '''
        end - receiver_info_widget
        '''

        '''
        begin - receiver_address_widget
        '''
        self.receiver_address_keyboard_component = KeyboardComponent()
        self.receiver_address_keyboard_component.return_pressed.connect(
            lambda: self.console_logger.log("pressed_return"))

        receiver_address_widget_layout = QVBoxLayout()
        receiver_address_widget.setLayout(receiver_address_widget_layout)

        receiver_address_grid_layout = QGridLayout()
        receiver_address_widget_layout.addLayout(receiver_address_grid_layout)

        city_label = QLabel("İl:")
        city_label.setStyleSheet(Styles.label())
        district_label = QLabel("İlçe:")
        district_label.setStyleSheet(Styles.label())
        neighborhood_label = QLabel("Mahalle:")
        neighborhood_label.setStyleSheet(Styles.label())
        address_label = QLabel("Adres:")
        address_label.setStyleSheet(Styles.label())

        self.receiver_city_input = QLineEdit()
        self.receiver_city_input.setStyleSheet(Styles.bg_gray_input(15))
        self.receiver_district_input = QLineEdit()
        self.receiver_district_input.setStyleSheet(Styles.bg_gray_input(15))
        self.receiver_neighborhood_input = QLineEdit()
        self.receiver_neighborhood_input.setStyleSheet(Styles.bg_gray_input(15))
        self.receiver_address_input = QTextEdit()
        self.receiver_address_input.setStyleSheet(Styles.bg_gray_input())

        receiver_address_grid_layout.addWidget(city_label, 0, 0)
        receiver_address_grid_layout.addWidget(self.receiver_city_input, 0, 1)
        receiver_address_grid_layout.addWidget(district_label, 1, 0)
        receiver_address_grid_layout.addWidget(self.receiver_district_input, 1, 1)
        receiver_address_grid_layout.addWidget(neighborhood_label, 2, 0)
        receiver_address_grid_layout.addWidget(self.receiver_neighborhood_input, 2, 1)

        receiver_address_grid_layout.addWidget(address_label, 0, 2)
        receiver_address_grid_layout.addWidget(self.receiver_address_input, 0, 3, 3, 1)

        receiver_address_grid_layout.setSpacing(50)
        receiver_address_grid_layout.setContentsMargins(10, 10, 10, 10)

        receiver_address_widget_layout.addStretch()
        receiver_address_widget_layout.addSpacing(25)
        receiver_address_widget_layout.addWidget(self.receiver_address_keyboard_component)

        receiver_address_widget_layout.addStretch()
        '''
        end - receiver_address_widget
        '''

        self.send_to_cargo_identity_number_inner_stack.addWidget(otp_widget)
        self.send_to_cargo_identity_number_inner_stack.addWidget(customer_info_widget)
        self.send_to_cargo_identity_number_inner_stack.addWidget(receiver_info_widget)
        self.send_to_cargo_identity_number_inner_stack.addWidget(receiver_address_widget)
        v_box.addWidget(self.send_to_cargo_identity_number_inner_stack)

        '''
        end - content
        '''

        # Footer
        if footer:
            v_box.addWidget(footer)

        main_layout.addLayout(v_box)
        self.setLayout(main_layout)

    def on_change_wizard_index(self, index):
        self.console_logger.log(f"selected index: {index}")
        self.active_wizard_index = index
        self.send_to_cargo_identity_number_inner_stack.setCurrentIndex(index)
        if index == 0:
            self.header.set_title(self.step_1_title)
        elif index == 1:
            self.header.set_title(self.step_2_title)
        elif index == 2:
            self.header.set_title(self.step_3_title)
        elif index == 3:
            self.header.set_title(self.step_4_title)

    def on_shown(self):
        self.otp_input_box.clear_inputs()
        self.otp_input_box.set_focus_first_input()
        self.approve_with_checkbox_component.condition_checkbox.setChecked(False)
        self.wizard_component.go_to_step(0)
