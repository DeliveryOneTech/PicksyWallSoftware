from app.enums.page_number import PageNumber
from app.lib.console_logger import ConsoleLogger
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QGridLayout
from app.styles import Styles
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
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
        connection_check_button.setStyleSheet(Styles.btn_success(padding="25px 40px"))
        robot_check_button = QPushButton('Robot Kontrolü')
        robot_check_button.setStyleSheet(Styles.btn_success(padding="25px 40px"))
        lighting_check_button = QPushButton('Aydınlatma Kontrolü')
        lighting_check_button.setStyleSheet(Styles.btn_success(padding="25px 40px"))

        relay_check_button = QPushButton('Röle Kontrolü')
        relay_check_button.setStyleSheet(Styles.btn_success(padding="25px 40px"))
        package_measuring_system_button = QPushButton('Paket Ölçüm Sistemi')
        package_measuring_system_button.setStyleSheet(Styles.btn_success(padding="25px 40px"))
        restart_button = QPushButton('Yeniden Başlat')
        restart_button.setStyleSheet(Styles.btn_danger(padding="25px 40px"))

        buttons_grid = QGridLayout()
        buttons_grid.addWidget(connection_check_button, 0, 0)
        buttons_grid.addWidget(robot_check_button, 0, 1)
        buttons_grid.addWidget(lighting_check_button, 0, 2)
        buttons_grid.addWidget(relay_check_button, 1, 0)
        buttons_grid.addWidget(package_measuring_system_button, 1, 1)
        buttons_grid.addWidget(restart_button, 1, 2)
        buttons_grid.setHorizontalSpacing(75)
        buttons_grid.setVerticalSpacing(45)

        self.v_box.addLayout(buttons_grid)

        self.v_box.addStretch()

        '''
        end - content
        '''

        if footer:
            self.v_box.addWidget(footer)

        self.setLayout(self.v_box)
