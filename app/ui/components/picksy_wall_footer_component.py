from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QSizePolicy
from app.ui.utils import ui_utils
from app.styles import Styles


class PicksyWallFooterComponent(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, picksy_wall_footer):
        picksy_wall_footer.setObjectName("picksy_wall_footer")
        self.footer_layout = QtWidgets.QHBoxLayout(picksy_wall_footer)
        self.footer_layout.setObjectName("gridLayout")

        self.picksy_wall_footer_back_button = QtWidgets.QPushButton(picksy_wall_footer)
        self.picksy_wall_footer_back_button.setObjectName("picksy_wall_footer_back_button")

        self.picksy_wall_footer_brand_image_label = QtWidgets.QLabel(picksy_wall_footer)
        self.picksy_wall_footer_brand_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.picksy_wall_footer_brand_image_label.setObjectName("picksy_wall_footer_brand_image_label")

        self.picksy_wall_footer_other_button = QtWidgets.QPushButton(picksy_wall_footer)
        self.picksy_wall_footer_other_button.setObjectName("picksy_wall_footer_other_button")

        self.footer_layout.addWidget(self.picksy_wall_footer_back_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.footer_layout.addItem(spacerItem1)
        self.footer_layout.addWidget(self.picksy_wall_footer_brand_image_label)
        self.footer_layout.addWidget(self.picksy_wall_footer_other_button)

        self.retranslateUi()

    def retranslateUi(self):
        self.picksy_wall_footer_back_button.setIcon(ui_utils.get_icon(":/icons/assets/arrow-left.svg"))
        self.picksy_wall_footer_back_button.setIconSize(QtCore.QSize(64, 64))
        self.picksy_wall_footer_back_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.picksy_wall_footer_back_button.setStyleSheet(Styles.btn_back())

        self.picksy_wall_footer_other_button.setText("Diğer")
        self.picksy_wall_footer_other_button.setMinimumHeight(64)
        self.picksy_wall_footer_other_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.picksy_wall_footer_other_button.setStyleSheet(Styles.home_page_others_button())

        self.picksy_wall_footer_brand_image_label.setPixmap(ui_utils.get_pixmap(":/logos/assets/gray-d1-logo.png"))
        self.picksy_wall_footer_brand_image_label.setScaledContents(True)
        self.picksy_wall_footer_brand_image_label.setFixedSize(500, 100)

    def hide_back_button(self):
        self.picksy_wall_footer_back_button.hide()

    def hide_other_button(self):
        self.picksy_wall_footer_other_button.hide()
        spacer = QtWidgets.QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.footer_layout.addItem(spacer)
