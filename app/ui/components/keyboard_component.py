from PyQt5 import QtWidgets, QtCore
import pyautogui
import pyperclip
from app.ui.utils.styles import Styles


class KeyboardComponent(QtWidgets.QWidget):
    return_pressed = QtCore.pyqtSignal()

    def __init__(self, submit_button_is_visible=True):
        super().__init__()

        self.setStyleSheet(Styles.btn_keyboard())

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.row1_layout = QtWidgets.QHBoxLayout()
        self.row1_layout.setObjectName("row1_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.row1_layout.addItem(spacerItem)

        self.addKeys("1234567890", self.row1_layout)

        # Backspace button
        self.backspaceButton = QtWidgets.QPushButton()
        self.backspaceButton.setObjectName("backspaceButton")
        self.backspaceButton.setText("Sil")
        self.backspaceButton.setStyleSheet(Styles.btn_keyboard("#f44336"))
        self.backspaceButton.clicked.connect(self.on_click_back_space_button)
        self.backspaceButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.row1_layout.addWidget(self.backspaceButton)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.row1_layout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.row1_layout, 0, 0, 1, 1)

        self.row2_layout = QtWidgets.QHBoxLayout()
        self.row2_layout.setObjectName("row2_layout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.row2_layout.addItem(spacerItem2)

        self.addKeys("QWERTYUIOPĞÜ", self.row2_layout)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.row2_layout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.row2_layout, 1, 0, 1, 1)

        self.row3_layout = QtWidgets.QHBoxLayout()
        self.row3_layout.setObjectName("row3_layout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.row3_layout.addItem(spacerItem4)

        self.addKeys("ASDFGHJKLŞİ", self.row3_layout)

        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.row3_layout.addItem(spacerItem5)
        self.gridLayout.addLayout(self.row3_layout, 2, 0, 1, 1)

        self.row4_layout = QtWidgets.QHBoxLayout()
        self.row4_layout.setObjectName("row4_layout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.row4_layout.addItem(spacerItem6)

        self.addKeys("ZXCVBNMÖÇ", self.row4_layout)

        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.row4_layout.addItem(spacerItem7)
        self.gridLayout.addLayout(self.row4_layout, 3, 0, 1, 1)

        # Row 5 - Space, ., /, Enter buttons
        self.row5_layout = QtWidgets.QHBoxLayout()
        self.row5_layout.setObjectName("row5_layout")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.row5_layout.addItem(spacerItem8)

        # Space button
        self.spaceButton = QtWidgets.QPushButton()
        self.spaceButton.setObjectName("space")
        self.spaceButton.setText("")
        self.spaceButton.setMinimumWidth(300)
        self.spaceButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spaceButton.clicked.connect(self.on_click_space_button)
        self.spaceButton.enterEvent = lambda event, value='space': self.on_enter_event(value)
        self.spaceButton.leaveEvent = lambda event, value='space': self.on_leave_event(value)
        self.spaceButton.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.row5_layout.addWidget(self.spaceButton)

        # . button
        self.dotButton = QtWidgets.QPushButton()
        self.dotButton.setObjectName(".")
        self.dotButton.setText(".")
        self.dotButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dotButton.clicked.connect(lambda: self.on_click_key_button('.'))
        self.dotButton.enterEvent = lambda event, value='.': self.on_enter_event(value)
        self.dotButton.leaveEvent = lambda event, value='.': self.on_leave_event(value)
        self.row5_layout.addWidget(self.dotButton)

        # / button
        self.slashButton = QtWidgets.QPushButton()
        self.slashButton.setObjectName("/")
        self.slashButton.setText("/")
        self.slashButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slashButton.clicked.connect(lambda: self.on_click_key_button('/'))
        self.slashButton.enterEvent = lambda event, value='/': self.on_enter_event(value)
        self.slashButton.leaveEvent = lambda event, value='/': self.on_leave_event(value)
        self.row5_layout.addWidget(self.slashButton)

        # Enter button
        self.enterButton = QtWidgets.QPushButton()
        self.enterButton.setObjectName("enterButton")
        self.enterButton.setText("Giriş")
        self.enterButton.setStyleSheet(Styles.btn_keyboard("#4CAF50"))
        self.enterButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.enterButton.clicked.connect(self.on_click_enter_button)
        self.enterButton.setFixedWidth(150)
        self.row5_layout.addWidget(self.enterButton)
        if not submit_button_is_visible:
            self.enterButton.hide()

        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.row5_layout.addItem(spacerItem9)

        self.gridLayout.addLayout(self.row5_layout, 4, 0, 1, 1)

        self.setLayout(self.gridLayout)

    def addKeys(self, keys, layout):
        for key in keys:
            button = QtWidgets.QPushButton()
            button.setObjectName(key)
            button.setText(key)
            button.setFocusPolicy(QtCore.Qt.NoFocus)
            button.mousePressEvent = lambda event, value=key: self.on_click_key_button(value)
            button.enterEvent = lambda event, value=key: self.on_enter_event(value)
            button.leaveEvent = lambda event, value=key: self.on_leave_event(value)
            layout.addWidget(button)

    def on_click_key_button(self, value):
        if value is False:
            self.__trigger_delete()
            return
        elif value is True:
            self.__trigger_enter()
            return

        value_for_clipboard = str(value).replace(" ", "")
        pyperclip.copy(value_for_clipboard)
        pyautogui.hotkey('ctrl', 'v')

    def on_click_space_button(self):
        pyautogui.press('space')

    def on_click_back_space_button(self):
        pyautogui.press('backspace')

    def on_click_enter_button(self):
        self.return_pressed.emit()

    def on_enter_event(self, btn_name):
        button = self.findChild(QtWidgets.QPushButton, btn_name)
        button.setStyleSheet(Styles.btn_keyboard_hover())

    def on_leave_event(self, btn_name):
        button = self.findChild(QtWidgets.QPushButton, btn_name)
        button.setStyleSheet(Styles.btn_keyboard())
