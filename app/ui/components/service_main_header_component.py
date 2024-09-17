from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QSizePolicy
from app.ui.components.status_circle_component import StatusCircleComponent
from app.ui.utils import ui_utils
from app.styles import Styles


class ServiceMainHeaderComponent(QtWidgets.QWidget):
    back_button_clicked = QtCore.pyqtSignal()

    def __init__(self, label_text: str, system_status='gray', internet_status='gray', temperature_status='gray',
                 electricity_status='gray'):
        super().__init__()
        self.label_text = label_text
        self.system_status = system_status
        self.internet_status = internet_status
        self.temperature_status = temperature_status
        self.electricity_status = electricity_status
        self.setupUi(self)

    def setupUi(self, picksy_wall_title_header):
        picksy_wall_title_header.setObjectName("picksy_wall_title_header")
        self.header_layout = QtWidgets.QHBoxLayout(picksy_wall_title_header)
        self.header_layout.setObjectName("gridLayout")

        self.picksy_wall_header_back_button = QtWidgets.QPushButton(picksy_wall_title_header)
        self.picksy_wall_header_back_button.setObjectName("picksy_wall_header_back_button")

        self.header_layout.addWidget(self.picksy_wall_header_back_button)

        spacerItem0 = QtWidgets.QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.header_layout.addItem(spacerItem0)

        label = QtWidgets.QLabel(self.label_text)
        label.setStyleSheet(Styles.label())
        label.setObjectName("label")
        label.setFixedWidth(500)
        self.header_layout.addWidget(label)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.header_layout.addItem(spacerItem1)

        self.system_status_circle = StatusCircleComponent('Sistem', self.system_status)
        self.header_layout.addWidget(self.system_status_circle)
        self.internet_status_circle = StatusCircleComponent('İnternet', self.internet_status)
        self.header_layout.addWidget(self.internet_status_circle)
        self.temperature_status_circle = StatusCircleComponent('Sıcaklık', self.temperature_status)
        self.header_layout.addWidget(self.temperature_status_circle)
        self.electricity_status_circle = StatusCircleComponent('Elektrik', self.electricity_status)
        self.header_layout.addWidget(self.electricity_status_circle)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.header_layout.addItem(spacerItem2)

        back_button_width = self.picksy_wall_header_back_button.width()
        label_width = label.width()
        spacerItem3 = QtWidgets.QSpacerItem(back_button_width + label_width, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.header_layout.addItem(spacerItem3)

        self.setContentsMargins(0, 0, 0, 0)

        self.picksy_wall_header_back_button.mousePressEvent = lambda event: self.back_button_clicked.emit()

        self.retranslateUi()

    def retranslateUi(self):
        self.picksy_wall_header_back_button.setIcon(ui_utils.get_icon(":/icons/assets/arrow-left.svg"))
        self.picksy_wall_header_back_button.setIconSize(QtCore.QSize(48, 48))
        self.picksy_wall_header_back_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.picksy_wall_header_back_button.setStyleSheet(Styles.btn_back())

    def hide_back_button(self):
        self.picksy_wall_header_back_button.hide()
