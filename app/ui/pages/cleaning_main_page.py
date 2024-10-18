from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel
from app.enums.page_number import PageNumber
from app.lib.utils.console_logger import ConsoleLogger
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.components.main_button_component import MainButtonComponent
from app.ui.components.picksy_wall_date_time_header_component import PicksyWallDateTimeHeaderComponent
from app.ui.components.picksy_wall_footer_component import PicksyWallFooterComponent
from app.ui.styles import Styles


class CleaningMainPage(QWidget):
    def __init__(self, stacked_widget: BaseQStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget

        header = PicksyWallDateTimeHeaderComponent()
        footer = PicksyWallFooterComponent()

        main_layout = QGridLayout(self)
        v_box = QVBoxLayout()

        if header:
            v_box.addWidget(header)

        tray_information_label = QLabel("Tepsi Bilgisi: 4 Temiz / 2 Kirli")
        tray_information_label.setStyleSheet(Styles.header())
        tray_information_label.setAlignment(Qt.AlignCenter)

        v_box.addWidget(tray_information_label)

        v_box.addSpacing(20)

        h_box = QHBoxLayout()

        self.get_tray_button = MainButtonComponent(
            title_html="<h1>Tepsi Getir</h1>",
            icon_path='',
            tooltip="Bu buton aracılığı ile barkod yazıcının kilidini açabilirsiniz."
        )
        self.tray_cleaned_button = MainButtonComponent(
            title_html="<h1>Temizlendi</h1>",
            icon_path='',
            tooltip="Bu buton aracılığı ile barkod yazıcının kilidini açabilirsiniz."
        )

        h_box.addWidget(self.get_tray_button)
        h_box.addWidget(self.tray_cleaned_button)

        v_box.addLayout(h_box)

        if footer:
            footer.set_service_and_other_button_width(self.get_tray_button.width())
            footer.hide_other_button()
            footer.picksy_wall_footer_service_button.setText("Geri Dön")
            footer.on_click_service_button.connect(lambda: stacked_widget.go_by_page_number(
                PageNumber.CLEANING_MAIN_PAGE, PageNumber.HOME_PAGE
            ))
            v_box.addWidget(footer)

        main_layout.addLayout(v_box, 0, 0)

        self.__define_events()

    def __define_events(self):
        self.get_tray_button.mousePressEvent = lambda event: self.__get_tray()
        self.tray_cleaned_button.mousePressEvent = lambda event: self.__tray_cleaned()

    def __get_tray(self):
        ConsoleLogger().log("Get Tray")

    def __tray_cleaned(self):
        ConsoleLogger().log("Tray Cleaned")
