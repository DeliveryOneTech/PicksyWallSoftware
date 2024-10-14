from app.enums.page_number import PageNumber
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QSpacerItem, QSizePolicy
from app.ui.utils.styles import Styles
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.components.delta_numeric_input_component import DeltaNumericInputComponent
from app.ui.components.service_main_header_component import ServiceMainHeaderComponent


class RobotManagementMainPage(QWidget):
    def __init__(self, stacked_widget: BaseQStackedWidget, caller_page_number: PageNumber):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.caller_page_number = caller_page_number

        self.setStyleSheet("QPushButton {font: 16pt 'MS Shell Dlg 2';}")
        grid_layout = QGridLayout()

        label = 'Sol' if caller_page_number == PageNumber.LEFT_ROBOT_MANAGEMENT else 'Sağ'

        header = ServiceMainHeaderComponent(label + ' Robot')

        if header:
            header.back_button_clicked.connect(lambda: self.stacked_widget.go_by_page_number(
                self.caller_page_number, PageNumber.SERVICE_MAIN
            ))
            grid_layout.addWidget(header, 0, 0, 1, 3)

        '''
        begin - content
        '''

        self.connection_check_button = QPushButton('Bağlantı Kontrolü')
        self.connection_check_button.setStyleSheet(Styles.btn_success(padding="10px"))

        self.robot_check_button = QPushButton('Senaryo Kontrolü')
        self.robot_check_button.setStyleSheet(Styles.btn_success(padding="10px"))

        self.lighting_check_button = QPushButton('Aydınlatma Kontrolü')
        self.lighting_check_button.setStyleSheet(Styles.btn_success(padding="10px"))

        self.relay_check_button = QPushButton('Röle Kontrolü')
        self.relay_check_button.setStyleSheet(Styles.btn_success(padding="10px"))

        self.package_measuring_system_button = QPushButton('Paket Ölçüm Sistemi')
        self.package_measuring_system_button.setStyleSheet(Styles.btn_success(padding="10px"))

        self.restart_button = QPushButton('Cihazı Yeniden Başlat')
        self.restart_button.setStyleSheet(Styles.btn_danger(padding="10px"))

        self.x1_axis = DeltaNumericInputComponent('X1 Ekseni')

        self.z_axis = DeltaNumericInputComponent('Z Ekseni')

        self.delivery_cover = DeltaNumericInputComponent('Teslimat Kapağı')

        self.x2_axis = DeltaNumericInputComponent('X2 Ekseni')

        self.y_axis = DeltaNumericInputComponent('Y Ekseni')

        self.hide_cover = DeltaNumericInputComponent('Gizleme Kapağı')

        grid_layout.addWidget(self.connection_check_button, 1, 0)
        grid_layout.addWidget(self.robot_check_button, 1, 1)
        grid_layout.addWidget(self.lighting_check_button, 1, 2)
        grid_layout.addWidget(self.relay_check_button, 2, 0)
        grid_layout.addWidget(self.package_measuring_system_button, 2, 1)
        grid_layout.addWidget(self.restart_button, 2, 2)
        grid_layout.addWidget(self.x1_axis, 3, 0)
        grid_layout.addWidget(self.z_axis, 3, 1)
        grid_layout.addWidget(self.delivery_cover, 3, 2)
        grid_layout.addWidget(self.x2_axis, 4, 0)
        grid_layout.addWidget(self.y_axis, 4, 1)
        grid_layout.addWidget(self.hide_cover, 4, 2)

        grid_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding), 5, 0, 1, 3)

        '''
        end - content
        '''
        self.setLayout(grid_layout)
