from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from app.ui.styles import Styles


class NumericOTPInputsComponent(QtWidgets.QWidget):

    def __init__(self, otp_length: int, name_prefix: str = "otp_input_"):
        super().__init__()
        self.name_prefix = name_prefix

        h_otp_input_box = QtWidgets.QHBoxLayout()
        h_otp_input_box.setSpacing(15)
        h_otp_input_box.setAlignment(Qt.AlignCenter)

        for i in range(1, otp_length + 1):
            otp_input = QtWidgets.QLineEdit()
            otp_input.setObjectName(name_prefix + str(i))
            otp_input.setMaxLength(1)
            otp_input.setFixedSize(100, 100)
            otp_input.setStyleSheet(Styles.otp_input())
            otp_input.setAlignment(Qt.AlignCenter)
            otp_input.setValidator(QIntValidator())
            otp_input.setContextMenuPolicy(Qt.NoContextMenu)
            h_otp_input_box.addWidget(otp_input)
            otp_input.textChanged.connect(
                lambda value, input_name=name_prefix + str(i): self.__on_change(value, input_name)
            )
            otp_input.keyPressEvent = lambda event, input_name=name_prefix + str(i): \
                self.__on_key_press_event(event, input_name)

        h_otp_input_box.setSpacing(5)

        self.setLayout(h_otp_input_box)

    def set_focus_first_input(self):
        first_input = self.findChild(QtWidgets.QLineEdit, self.name_prefix + "1")
        if first_input:
            first_input.setFocus()

    def set_focus_last_input(self):
        last_input = self.findChild(QtWidgets.QLineEdit, self.name_prefix + str(len(self.name_prefix)))
        if last_input:
            last_input.setFocus()

    def get_value(self):
        all_inputs = self.findChildren(QtWidgets.QLineEdit)
        otp = ""
        for input_item in all_inputs:
            otp += input_item.text()
        return otp

    def clear_inputs(self):
        all_inputs = self.findChildren(QtWidgets.QLineEdit)
        for input_item in all_inputs:
            input_item.setText("")
        first_input = self.findChild(QtWidgets.QLineEdit, self.name_prefix + "1")
        if first_input:
            first_input.setFocus()

    def set_submit_function(self, submit_function):
        self.submit_function = submit_function

    def __on_change(self, value, input_name):
        if len(value) > 0:
            self.__focus_next_input(input_name)
        else:
            self.__focus_previous_input(input_name)

    def __focus_next_input(self, input_name):
        input_number = int(input_name.split("_")[-1])
        next_input = self.findChild(QtWidgets.QLineEdit, self.name_prefix + str(input_number + 1))
        if next_input:
            next_input.setFocus()

    def __focus_previous_input(self, input_name):
        input_number = int(input_name.split("_")[-1])
        previous_input = self.findChild(QtWidgets.QLineEdit, self.name_prefix + str(input_number - 1))
        if previous_input:
            previous_input.setFocus()

    def __on_key_press_event(self, event, input_name):
        QtWidgets.QLineEdit.keyPressEvent(self.findChild(QtWidgets.QLineEdit, input_name), event)
        current_input = self.findChild(QtWidgets.QLineEdit, input_name)

        if event.key() == Qt.Key_Backspace:
            self.__focus_previous_input(input_name)
            previous_input_name = self.name_prefix + str(int(input_name.split("_")[-1]) - 1)
            previous_input = self.findChild(QtWidgets.QLineEdit, previous_input_name)
            if previous_input:
                previous_input.setText("")
                previous_input.setFocus()
        elif len(current_input.text()) > 0:
            self.__focus_next_input(input_name)
            next_input_name = self.name_prefix + str(int(input_name.split("_")[-1]) + 1)
            next_input = self.findChild(QtWidgets.QLineEdit, next_input_name)
            if next_input:
                next_input.setFocus()
