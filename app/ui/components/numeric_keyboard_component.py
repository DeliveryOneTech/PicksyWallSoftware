from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from app.styles import Styles
from app.ui.utils.ui_utils import *
import pyautogui
import pyperclip


class NumericKeyboardComponent(QtWidgets.QWidget):
    return_pressed = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        btn_width = 150
        btn_height = 110

        layout = QtWidgets.QGridLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignCenter)

        for i in range(1, 10):
            button = QtWidgets.QPushButton(str(i))
            button.setObjectName(str(i))
            button.setFixedSize(btn_width, btn_height)
            button.setStyleSheet(Styles.btn_numeric_keyboard())
            button.setFocusPolicy(Qt.NoFocus)
            layout.addWidget(button, (i - 1) // 3, (i - 1) % 3)
            button.mousePressEvent = lambda event, value=i: self.__on_click(value)
            button.enterEvent = lambda event, value=i: self.on_enter_event(value)
            button.leaveEvent = lambda event, value=i: self.on_leave_event(value)

        button = QtWidgets.QPushButton("0")
        button.setObjectName("0")
        button.setFixedSize(btn_width, btn_height)
        button.setStyleSheet(Styles.btn_numeric_keyboard())
        button.setFocusPolicy(Qt.NoFocus)
        button.mousePressEvent = lambda event, value=0: self.__on_click(value)
        button.enterEvent = lambda event, value=0: self.on_enter_event(value)
        button.leaveEvent = lambda event, value=0: self.on_leave_event(value)
        layout.addWidget(button, 3, 1)

        delete_button = QtWidgets.QPushButton()
        delete_button.setIcon(get_icon(":/icons/assets/white-arrow-left.svg"))
        delete_button.setIconSize(QtCore.QSize(48, 48))
        delete_button.setFixedSize(btn_width, btn_height)
        delete_button.setStyleSheet(Styles.btn_danger())
        delete_button.setFocusPolicy(Qt.NoFocus)
        layout.addWidget(delete_button, 3, 0)
        delete_button.mousePressEvent = lambda event, value=False: self.__on_click(value)

        enter_button = QtWidgets.QPushButton()
        enter_button.setIcon(get_icon(":/icons/assets/check-lg.svg"))
        enter_button.setIconSize(QtCore.QSize(48, 48))
        enter_button.setFixedSize(btn_width, btn_height)
        enter_button.setStyleSheet(Styles.btn_success())
        enter_button.setFocusPolicy(Qt.NoFocus)
        layout.addWidget(enter_button, 3, 2)
        enter_button.mousePressEvent = lambda event, value=True: self.__on_click(value)

        layout.setHorizontalSpacing(0)
        layout.setVerticalSpacing(0)

        self.setLayout(layout)

    def __on_click(self, value):
        if value is False:
            self.__trigger_delete()
            return
        elif value is True:
            self.__trigger_enter()
            return

        value_for_clipboard = str(value).replace(" ", "")
        pyperclip.copy(value_for_clipboard)
        pyautogui.hotkey('ctrl', 'v')

    def __trigger_delete(self):
        pyautogui.press('backspace')

    def __trigger_enter(self):
        self.return_pressed.emit()

    def on_enter_event(self, value):
        button = self.findChild(QtWidgets.QPushButton, str(value))
        button.setStyleSheet(Styles.btn_numeric_keyboard_hover())

    def on_leave_event(self, value):
        button = self.findChild(QtWidgets.QPushButton, str(value))
        button.setStyleSheet(Styles.btn_numeric_keyboard())
