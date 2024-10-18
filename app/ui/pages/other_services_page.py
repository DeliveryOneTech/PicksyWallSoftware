import logging
from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QVBoxLayout
from app.lib.utils.console_logger import ConsoleLogger
from app.ui.components.main_button_component import MainButtonComponent
from app.ui.components.picksy_wall_date_time_header_component import PicksyWallDateTimeHeaderComponent
from app.ui.components.picksy_wall_footer_component import PicksyWallFooterComponent
from app.enums.page_number import PageNumber
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget


class OtherServicesPage(QWidget):
    def __init__(self, stacked_widget: BaseQStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.console_logger = ConsoleLogger()
        self.console_logger.log()

        header = PicksyWallDateTimeHeaderComponent()
        footer = PicksyWallFooterComponent()

        main_layout = QGridLayout(self)
        v_box = QVBoxLayout()

        # begin header
        if header:
            v_box.addWidget(header)
        # end header

        '''
        begin-content
        '''
        h_box = QHBoxLayout()

        # Main Button 1
        self.courier_login_button = MainButtonComponent(
            title_html="<h1>Kurye</h1>",
            icon_path=':/icons/assets/send-icon.png',
            tooltip="Eğer bir kurye iseniz bu buton aracılığı ile Picksy Wall 'Kurye' işlemlerini gerçekleştirebilirsiniz."
        )

        # Main Button 2
        self.maintenance_button = MainButtonComponent(
            title_html="<h1>Bakım</h1>",
            icon_path=':/icons/assets/maintenance.svg',
            tooltip="Bu buton aracılığı ile Picksy Wall cihazının bakım işlemlerini gerçekleştirebilirsiniz."
        )

        # Main Button 3
        self.cleaning_button = MainButtonComponent(
            title_html="<h1>Temizlik</h1>",
            icon_path=':/icons/assets/seedling.svg',
            tooltip="Bu buton aracılığı ile Picksy Wall cihazının temizlik işlemlerini gerçekleştirebilirsiniz."
        )

        h_box.addWidget(self.courier_login_button)
        h_box.addWidget(self.maintenance_button)
        h_box.addWidget(self.cleaning_button)

        v_box.addLayout(h_box)
        '''
        end-content
        '''

        # begin footer
        if footer:
            footer.set_service_and_other_button_width(self.courier_login_button.width())
            footer.picksy_wall_footer_service_button.setText("Geri Dön")
            footer.hide_other_button()
            footer.on_click_service_button.connect(
                lambda: self.stacked_widget.go_by_page_number(PageNumber.OTHER_SERVICES_PAGE,
                                                              PageNumber.HOME_PAGE)
            )
            footer.on_click_other_button.connect(
                lambda: self.console_logger.log("Other button clicked but not implemented yet.", logging.WARNING)
            )
            v_box.addWidget(footer)
        # end footer

        main_layout.addLayout(v_box, 0, 0)

        self.__define_events()

    def __define_events(self):
        self.courier_login_button.mousePressEvent = lambda event: self.stacked_widget.go_by_page_number(
            PageNumber.OTHER_SERVICES_PAGE,
            PageNumber.COURIER_AUTHENTICATION_PAGE
        )
        self.maintenance_button.mousePressEvent = lambda event: self.stacked_widget.go_by_page_number(
            PageNumber.OTHER_SERVICES_PAGE,
            PageNumber.MAINTENANCE_AUTHENTICATION_PAGE
        )
        self.cleaning_button.mousePressEvent = lambda event: self.stacked_widget.go_by_page_number(
            PageNumber.HOME_PAGE,
            PageNumber.CLEANING_AUTHENTICATION_PAGE
        )
