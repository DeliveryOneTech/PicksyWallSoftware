from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QVBoxLayout
from app.lib.system_logger import SingletonSystemLogger
from app.styles import Styles
from app.ui.components.main_button_component import MainButtonComponent
from app.ui.components.picksy_wall_date_time_header_component import PicksyWallDateTimeHeaderComponent
from app.ui.components.picksy_wall_footer_component import PicksyWallFooterComponent
from app.ui.enums.page_number import PageNumber
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget


class HomePage(QWidget):
    def __init__(self, stacked_widget: BaseQStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.singleton_system_logger = SingletonSystemLogger()
        self.singleton_system_logger.log()

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
            footer.hide_back_button()
            v_box.addWidget(footer)
        # end footer

        main_layout.addLayout(v_box, 0, 0)

        self.define_events()

    def define_events(self):
        self.send_button.mousePressEvent = lambda event: self.stacked_widget.go_by_page_number(PageNumber.HOME,
                                                                                               PageNumber.SEND_TO_CARGO_IDENTITY_NUMBER_INPUT)
        self.receive_button.mousePressEvent = lambda event: self.stacked_widget.go_by_page_number(PageNumber.HOME,
                                                                                                  PageNumber.RECEIVE_PACKAGE_AUTHENTICATION)
        self.send_to_reject_button.mousePressEvent = lambda event: self.stacked_widget.go_by_page_number(
            PageNumber.HOME, PageNumber.SEND_TO_REJECT_IDENTITY_NUMBER_INPUT)

    def on_click_main_button(self, button, func=None):
        button.setStyleSheet(Styles.btn_main_clicked())
        QTimer.singleShot(1000, lambda: button.setStyleSheet(Styles.btn_main()))
        if func:
            func()
