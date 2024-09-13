from app.enums.page_number import PageNumber
from app.lib.console_logger import ConsoleLogger
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QGridLayout, QSpacerItem, QSizePolicy
from app.styles import Styles
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.components.delta_numeric_input_component import DeltaNumericInputComponent
from app.ui.components.service_main_header_component import ServiceMainHeaderComponent


class ServiceMainPage(QWidget):
    def __init__(self, stacked_widget: BaseQStackedWidget):
        super().__init__()
        self.setStyleSheet("QPushButton {font: 16pt 'MS Shell Dlg 2';}")
        self.console_logger = ConsoleLogger()
        self.console_logger.log()

        self.v_box = QVBoxLayout()

        self.header = ServiceMainHeaderComponent()
        footer = None

        if self.header:
            self.header.back_button_clicked.connect(lambda: stacked_widget.go_by_page_number(
                PageNumber.SERVICE_MAIN, PageNumber.HOME
            ))
            self.v_box.addWidget(self.header)

        '''
        begin - content
        '''
        self.v_box.addSpacing(50)

        connection_check_button = QPushButton('Bağlantı Kontrolü')
        connection_check_button.clicked.connect(lambda: self.console_logger.log('connection check'))
        connection_check_button.setStyleSheet(Styles.btn_success(padding="25px 40px"))

        robot_check_button = QPushButton('Robot Kontrolü')
        robot_check_button.clicked.connect(lambda: self.console_logger.log('robot check'))
        robot_check_button.setStyleSheet(Styles.btn_success(padding="25px 40px"))

        lighting_check_button = QPushButton('Aydınlatma Kontrolü')
        lighting_check_button.clicked.connect(lambda: self.console_logger.log('lighting check'))
        lighting_check_button.setStyleSheet(Styles.btn_success(padding="25px 40px"))

        relay_check_button = QPushButton('Röle Kontrolü')
        relay_check_button.clicked.connect(lambda: self.console_logger.log('relay check'))
        relay_check_button.setStyleSheet(Styles.btn_success(padding="25px 40px"))

        package_measuring_system_button = QPushButton('Paket Ölçüm Sistemi')
        package_measuring_system_button.clicked.connect(lambda: self.console_logger.log('package measuring system'))
        package_measuring_system_button.setStyleSheet(Styles.btn_success(padding="25px 40px"))

        restart_button = QPushButton('Cihazı Yeniden Başlat')
        restart_button.clicked.connect(lambda: self.console_logger.log('restart'))
        restart_button.setStyleSheet(Styles.btn_danger(padding="25px 40px"))

        x1_axis = DeltaNumericInputComponent('X1 Ekseni')
        x1_axis.down_button_clicked.connect(lambda: self.console_logger.log('x1 down'))
        x1_axis.up_button_clicked.connect(lambda: self.console_logger.log('x1 up'))
        x1_axis.max_down_button_clicked.connect(lambda: self.console_logger.log('x1 max down'))
        x1_axis.max_up_button_clicked.connect(lambda: self.console_logger.log('x1 max up'))

        z_axis = DeltaNumericInputComponent('Z Ekseni')
        z_axis.down_button_clicked.connect(lambda: self.console_logger.log('z down'))
        z_axis.up_button_clicked.connect(lambda: self.console_logger.log('z up'))
        z_axis.max_down_button_clicked.connect(lambda: self.console_logger.log('z max down'))
        z_axis.max_up_button_clicked.connect(lambda: self.console_logger.log('z max up'))

        delivery_cover = DeltaNumericInputComponent('Teslimat Kapağı')
        delivery_cover.down_button_clicked.connect(lambda: self.console_logger.log('delivery down'))
        delivery_cover.up_button_clicked.connect(lambda: self.console_logger.log('delivery up'))
        delivery_cover.max_down_button_clicked.connect(lambda: self.console_logger.log('delivery max down'))
        delivery_cover.max_up_button_clicked.connect(lambda: self.console_logger.log('delivery max up'))

        x2_axis = DeltaNumericInputComponent('X2 Ekseni')
        x2_axis.down_button_clicked.connect(lambda: self.console_logger.log('x2 down'))
        x2_axis.up_button_clicked.connect(lambda: self.console_logger.log('x2 up'))
        x2_axis.max_down_button_clicked.connect(lambda: self.console_logger.log('x2 max down'))
        x2_axis.max_up_button_clicked.connect(lambda: self.console_logger.log('x2 max up'))

        y_axis = DeltaNumericInputComponent('Y Ekseni')
        y_axis.down_button_clicked.connect(lambda: self.console_logger.log('y down'))
        y_axis.up_button_clicked.connect(lambda: self.console_logger.log('y up'))
        y_axis.max_down_button_clicked.connect(lambda: self.console_logger.log('y max down'))
        y_axis.max_up_button_clicked.connect(lambda: self.console_logger.log('y max up'))

        hide_cover = DeltaNumericInputComponent('Gizleme Kapağı')
        hide_cover.down_button_clicked.connect(lambda: self.console_logger.log('hide down'))
        hide_cover.up_button_clicked.connect(lambda: self.console_logger.log('hide up'))
        hide_cover.max_down_button_clicked.connect(lambda: self.console_logger.log('hide max down'))
        hide_cover.max_up_button_clicked.connect(lambda: self.console_logger.log('hide max up'))

        grid_layout = QGridLayout()
        grid_layout.addWidget(connection_check_button, 0, 0)
        grid_layout.addWidget(robot_check_button, 0, 1)
        grid_layout.addWidget(lighting_check_button, 0, 2)
        grid_layout.addWidget(relay_check_button, 1, 0)
        grid_layout.addWidget(package_measuring_system_button, 1, 1)
        grid_layout.addWidget(restart_button, 1, 2)

        grid_layout.addItem(QSpacerItem(20, 75, QSizePolicy.Minimum, QSizePolicy.Expanding), 2, 0)

        grid_layout.addWidget(x1_axis, 3, 0)
        grid_layout.addWidget(z_axis, 3, 1)
        grid_layout.addWidget(delivery_cover, 3, 2)
        grid_layout.addWidget(x2_axis, 4, 0)
        grid_layout.addWidget(y_axis, 4, 1)
        grid_layout.addWidget(hide_cover, 4, 2)

        grid_layout.setHorizontalSpacing(75)
        grid_layout.setVerticalSpacing(45)

        self.v_box.addLayout(grid_layout)

        self.v_box.addStretch()

        '''
        end - content
        '''

        if footer:
            self.v_box.addWidget(footer)

        self.setLayout(self.v_box)
