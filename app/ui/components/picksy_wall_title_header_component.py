from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QSizePolicy
from app.ui.utils import ui_utils
from app.styles import Styles


class PicksyWallTitleHeaderComponent(QtWidgets.QWidget):
    back_button_clicked = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, picksy_wall_title_header):
        picksy_wall_title_header.setObjectName("picksy_wall_title_header")
        self.header_layout = QtWidgets.QHBoxLayout(picksy_wall_title_header)
        self.header_layout.setObjectName("gridLayout")

        self.picksy_wall_header_back_button = QtWidgets.QPushButton(picksy_wall_title_header)
        self.picksy_wall_header_back_button.setObjectName("picksy_wall_header_back_button")

        self.picksy_wall_header_title_label = QtWidgets.QLabel(picksy_wall_title_header)
        self.picksy_wall_header_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.picksy_wall_header_title_label.setObjectName("picksy_wall_header_brand_image_label")
        self.picksy_wall_header_title_label.setStyleSheet(Styles.header())

        self.header_layout.addWidget(self.picksy_wall_header_back_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.header_layout.addItem(spacerItem1)
        self.header_layout.addWidget(self.picksy_wall_header_title_label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.header_layout.addItem(spacerItem2)
        back_button_width = self.picksy_wall_header_back_button.width()
        spacerItem3 = QtWidgets.QSpacerItem(back_button_width, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.header_layout.addItem(spacerItem3)

        self.setContentsMargins(0, 0, 0, 0)

        self.picksy_wall_header_back_button.mousePressEvent = lambda event: self.back_button_clicked.emit()

        self.retranslateUi()

    def retranslateUi(self):
        self.picksy_wall_header_back_button.setIcon(ui_utils.get_icon(":/icons/assets/arrow-left.svg"))
        self.picksy_wall_header_back_button.setIconSize(QtCore.QSize(64, 64))
        self.picksy_wall_header_back_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.picksy_wall_header_back_button.setStyleSheet(Styles.btn_back())

        self.picksy_wall_header_title_label.setScaledContents(True)
        self.picksy_wall_header_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.picksy_wall_header_title_label.setText("Picksy Wall")

    def hide_back_button(self):
        self.picksy_wall_header_back_button.hide()

    def set_title(self, title):
        self.picksy_wall_header_title_label.setText(title)


