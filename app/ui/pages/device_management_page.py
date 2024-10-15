from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QSpacerItem
from app.enums.page_number import PageNumber
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.components.service_main_header_component import HeaderComponentWithDeviceStatus
from app.ui.utils.styles import Styles


class DeviceManagementPage(QWidget):
    def __init__(self, stacked_widget: BaseQStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setStyleSheet("QPushButton {font: 16pt 'MS Shell Dlg 2';}")

        header = HeaderComponentWithDeviceStatus('Cihaz Yönetimi')
        grid_layout = QGridLayout()

        if header:
            header.back_button_clicked.connect(lambda: self.stacked_widget.go_by_page_number(
                PageNumber.DEVICE_MANAGEMENT_PAGE, PageNumber.SERVICE_MAIN_PAGE
            ))
            grid_layout.addWidget(header, 0, 0, 1, 3)

        # add margin to top
        grid_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum), 1, 0, 1, 3)

        self.restart_button = QPushButton('Cihazı Yeniden Başlat')
        self.restart_button.setStyleSheet(Styles.btn_danger(padding="10px"))
        grid_layout.addWidget(self.restart_button, 2, 0, 1, 3)

        grid_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 3, 0, 1, 3)

        self.setLayout(grid_layout)
