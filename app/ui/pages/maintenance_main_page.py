from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout
from app.enums.page_number import PageNumber
from app.lib.utils.console_logger import ConsoleLogger
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.components.main_button_component import MainButtonComponent
from app.ui.components.picksy_wall_date_time_header_component import PicksyWallDateTimeHeaderComponent
from app.ui.components.picksy_wall_footer_component import PicksyWallFooterComponent


class MaintenanceMainPage(QWidget):
    def __init__(self, stacked_widget: BaseQStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget

        header = PicksyWallDateTimeHeaderComponent()
        footer = PicksyWallFooterComponent()

        main_layout = QGridLayout(self)
        v_box = QVBoxLayout()

        if header:
            v_box.addWidget(header)

        h_box = QHBoxLayout()

        self.unlock_barcode_printer_button = MainButtonComponent(
            title_html="<h1>Barkod Yazıcı<br/>Kilidini Aç</h1>",
            icon_path='',
            tooltip="Bu buton aracılığı ile barkod yazıcının kilidini açabilirsiniz."
        )

        h_box.addWidget(self.unlock_barcode_printer_button)

        v_box.addLayout(h_box)

        if footer:
            footer.set_service_and_other_button_width(self.unlock_barcode_printer_button.width())
            footer.hide_other_button()
            footer.picksy_wall_footer_service_button.setText("Geri Dön")
            footer.on_click_service_button.connect(lambda: stacked_widget.go_by_page_number(
                PageNumber.MAINTENANCE_MAIN_PAGE, PageNumber.HOME_PAGE
            ))
            v_box.addWidget(footer)

        main_layout.addLayout(v_box, 0, 0)

        self.__define_events()

    def __define_events(self):
        self.unlock_barcode_printer_button.mousePressEvent = lambda event: ConsoleLogger().log("Unlock Barcode Printer")
