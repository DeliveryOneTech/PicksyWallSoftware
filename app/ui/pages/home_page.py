import logging
from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QVBoxLayout
from app.lib.console_logger import ConsoleLogger
from app.ui.components.main_button_component import MainButtonComponent
from app.ui.components.picksy_wall_date_time_header_component import PicksyWallDateTimeHeaderComponent
from app.ui.components.picksy_wall_footer_component import PicksyWallFooterComponent
from app.enums.page_number import PageNumber
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget


class HomePage(QWidget):
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
        self.send_button = MainButtonComponent(
            title_html="<h1>Gönder</h1>",
            icon_path=':/icons/assets/send-icon.png',
            tooltip="Bu buton aracılığı ile kargo gönderimi yapabilirsiniz."
        )

        # Main Button 2
        self.receive_button = MainButtonComponent(
            title_html="<h1>Teslim Al</h1>",
            icon_path=':/icons/assets/receive-icon.png',
            tooltip="Bu buton aracılığı ile Picksy Wall'da bulunan kargonuzu teslim alabilirsiniz."
        )

        # Main Button 3
        self.send_to_reject_button = MainButtonComponent(
            title_html="<h1>İade Et</h1>",
            icon_path=':/icons/assets/reject-icon.png',
            tooltip="Bu buton aracılığı ile kargonuzu iade edilmek üzere gönderebilirsiniz."
        )

        h_box.addWidget(self.send_button)
        h_box.addWidget(self.receive_button)
        h_box.addWidget(self.send_to_reject_button)

        v_box.addLayout(h_box)
        '''
        end-content
        '''

        # begin footer
        if footer:
            footer.set_service_and_other_button_width(self.send_button.width())
            footer.on_click_service_button.connect(
                lambda: self.stacked_widget.go_by_page_number(PageNumber.HOME_PAGE,
                                                              PageNumber.SERVICE_USER_AUTHENTICATION_PAGE)
            )
            footer.on_click_other_button.connect(
                lambda: self.stacked_widget.go_by_page_number(PageNumber.HOME_PAGE,
                                                              PageNumber.OTHER_SERVICES_PAGE)
            )
            v_box.addWidget(footer)
        # end footer

        main_layout.addLayout(v_box, 0, 0)

        self.__define_events()

    def __define_events(self):
        self.send_button.mousePressEvent = lambda event: self.stacked_widget.go_by_page_number(
            PageNumber.HOME_PAGE,
            PageNumber.SENDER_IDENTIFICATION_PAGE
        )
        self.receive_button.mousePressEvent = lambda event: self.stacked_widget.go_by_page_number(
            PageNumber.HOME_PAGE,
            PageNumber.RECEIVER_AUTHENTICATION_PAGE
        )
        self.send_to_reject_button.mousePressEvent = lambda event: self.stacked_widget.go_by_page_number(
            PageNumber.HOME_PAGE,
            PageNumber.REJECTION_ID_PAGE
        )
