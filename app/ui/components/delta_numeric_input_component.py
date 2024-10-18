from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout

from app.ui.styles import Styles


class DeltaNumericInputComponent(QWidget):
    down_button_clicked = pyqtSignal()
    up_button_clicked = pyqtSignal()
    max_down_button_clicked = pyqtSignal()
    max_up_button_clicked = pyqtSignal()

    def __init__(self, label: str, initial_value: int = None):
        super().__init__()

        '''
        
        v_box = QVBoxLayout()

        self.label = QLabel(label)
        self.label.setStyleSheet(Styles.label())
        v_box.addWidget(self.label)

        inputs_h_box = QHBoxLayout()

        self.disable_input = QLineEdit()
        self.disable_input.setStyleSheet(Styles.bg_gray_input(40))
        self.disable_input.setReadOnly(True)
        inputs_h_box.addWidget(self.disable_input)

        self.input = QLineEdit()
        self.input.setStyleSheet(Styles.bg_gray_input(40))
        if initial_value:
            self.input.setText(str(initial_value))
        # only numeric value allowed
        self.input.setValidator(QtGui.QIntValidator())
        inputs_h_box.addWidget(self.input)

        v_box.addLayout(inputs_h_box)

        v_box.addSpacing(25)

        h_box = QHBoxLayout()
        # icon buttons
        self.down_button = QPushButton()
        self.down_button.setStyleSheet(Styles.btn_danger())
        self.down_button.setText('▼')
        self.up_button = QPushButton()
        self.up_button.setStyleSheet(Styles.btn_success())
        self.up_button.setText('▲')
        self.max_down_button = QPushButton()
        self.max_down_button.setStyleSheet(Styles.btn_danger())
        self.max_down_button.setText('▼▼')
        self.max_up_button = QPushButton()
        self.max_up_button.setStyleSheet(Styles.btn_success())
        self.max_up_button.setText('▲▲')

        self.down_button.clicked.connect(self.down_button_clicked.emit)
        self.up_button.clicked.connect(self.up_button_clicked.emit)
        self.max_down_button.clicked.connect(self.max_down_button_clicked.emit)
        self.max_up_button.clicked.connect(self.max_up_button_clicked.emit)

        h_box.addWidget(self.down_button)
        h_box.addWidget(self.up_button)
        h_box.addWidget(self.max_down_button)
        h_box.addWidget(self.max_up_button)

        v_box.addLayout(h_box)

        self.setLayout(v_box)

'''

        main_layout = QGridLayout()

        self.label = QLabel(label)
        self.label.setStyleSheet(Styles.label())
        main_layout.addWidget(self.label, 0, 0, 1, 2)

        self.disable_input = QLineEdit()
        self.disable_input.setStyleSheet(Styles.bg_gray_input(5))
        self.disable_input.setReadOnly(True)
        main_layout.addWidget(self.disable_input, 1, 0)

        self.input = QLineEdit()
        self.input.setStyleSheet(Styles.bg_gray_input(5))
        if initial_value:
            self.input.setText(str(initial_value))
        # only numeric value allowed
        self.input.setValidator(QtGui.QIntValidator())
        main_layout.addWidget(self.input, 1, 1)

        self.down_button = QPushButton()
        self.down_button.setStyleSheet(Styles.btn_danger(padding="5px"))
        self.down_button.setText('▼')
        self.up_button = QPushButton()
        self.up_button.setStyleSheet(Styles.btn_success(padding="5px"))
        self.up_button.setText('▲')
        self.max_down_button = QPushButton()
        self.max_down_button.setStyleSheet(Styles.btn_danger(padding="5px"))
        self.max_down_button.setText('▼▼')
        self.max_up_button = QPushButton()
        self.max_up_button.setStyleSheet(Styles.btn_success(padding="5px"))
        self.max_up_button.setText('▲▲')

        self.down_button.clicked.connect(self.down_button_clicked.emit)
        self.up_button.clicked.connect(self.up_button_clicked.emit)
        self.max_down_button.clicked.connect(self.max_down_button_clicked.emit)
        self.max_up_button.clicked.connect(self.max_up_button_clicked.emit)

        main_layout.addWidget(self.down_button, 2, 0)
        main_layout.addWidget(self.up_button, 2, 1)
        main_layout.addWidget(self.max_down_button, 3, 0)
        main_layout.addWidget(self.max_up_button, 3, 1)

        self.setLayout(main_layout)



    def get_input_value(self):
        return int(self.input.text())

    def set_input_value(self, value: int):
        self.input.setText(str(value))

    def get_disable_input_value(self):
        return int(self.disable_input.text())

    def set_disable_input_value(self, value: int):
        self.disable_input.setText(str(value))
