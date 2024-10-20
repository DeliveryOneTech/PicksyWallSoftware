from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QSizePolicy
from app.lib.utils import ui_utils
from app.ui.styles import Styles


class PicksyWallFooterComponent(QtWidgets.QWidget):
    on_click_service_button = QtCore.pyqtSignal()
    on_click_other_button = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, picksy_wall_footer):
        picksy_wall_footer.setObjectName("picksy_wall_footer")
        self.footer_layout = QtWidgets.QHBoxLayout(picksy_wall_footer)
        self.footer_layout.setObjectName("gridLayout")

        spacer_start = QtWidgets.QSpacerItem(5, 0, QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.footer_layout.addItem(spacer_start)

        self.picksy_wall_footer_service_button = QtWidgets.QPushButton(picksy_wall_footer)
        self.picksy_wall_footer_service_button.setObjectName("picksy_wall_footer_other_button")

        self.picksy_wall_footer_brand_image_label = QtWidgets.QLabel(picksy_wall_footer)
        self.picksy_wall_footer_brand_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.picksy_wall_footer_brand_image_label.setObjectName("picksy_wall_footer_brand_image_label")

        self.picksy_wall_footer_other_button = QtWidgets.QPushButton(picksy_wall_footer)
        self.picksy_wall_footer_other_button.setObjectName("picksy_wall_footer_other_button")

        self.footer_layout.addWidget(self.picksy_wall_footer_service_button)
        spacer = QtWidgets.QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.footer_layout.addItem(spacer)
        self.footer_layout.addWidget(self.picksy_wall_footer_brand_image_label)
        spacer = QtWidgets.QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.footer_layout.addItem(spacer)
        self.footer_layout.addWidget(self.picksy_wall_footer_other_button)

        spacer_end = QtWidgets.QSpacerItem(5, 0, QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.footer_layout.addItem(spacer_end)

        self.picksy_wall_footer_service_button.mousePressEvent = lambda event: self.on_click_service_button.emit()
        self.picksy_wall_footer_other_button.mousePressEvent = lambda event: self.on_click_other_button.emit()

        self.retranslateUi()

    def retranslateUi(self):
        self.picksy_wall_footer_service_button.setText("Servis")
        self.picksy_wall_footer_service_button.setMinimumHeight(64)
        self.picksy_wall_footer_service_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.picksy_wall_footer_service_button.setStyleSheet(Styles.home_secondary_button())

        self.picksy_wall_footer_other_button.setText("Diğer")
        self.picksy_wall_footer_other_button.setMinimumHeight(64)
        self.picksy_wall_footer_other_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.picksy_wall_footer_other_button.setStyleSheet(Styles.home_secondary_button())

        self.picksy_wall_footer_brand_image_label.setPixmap(ui_utils.get_pixmap(":/logos/assets/gray-d1-logo.png"))
        self.picksy_wall_footer_brand_image_label.setScaledContents(True)
        self.picksy_wall_footer_brand_image_label.setFixedHeight(100)

    def set_service_and_other_button_width(self, width):
        width -= 255
        self.picksy_wall_footer_service_button.setFixedWidth(width)
        self.picksy_wall_footer_other_button.setFixedWidth(width)
        self.picksy_wall_footer_brand_image_label.setFixedWidth(width)


    def hide_other_button(self):
        self.picksy_wall_footer_other_button.setDisabled(True)
        self.picksy_wall_footer_other_button.setStyleSheet(
            "background-color: transparent; border: none; color: transparent;")

    def hide_service_button(self):
        self.picksy_wall_footer_service_button.setDisabled(True)
        self.picksy_wall_footer_service_button.setStyleSheet(
            "background-color: transparent; border: none; color: transparent;")
