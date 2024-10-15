from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout
from app.enums.page_number import PageNumber
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.components.main_button_component import MainButtonComponent
from app.ui.components.picksy_wall_date_time_header_component import PicksyWallDateTimeHeaderComponent
from app.ui.components.picksy_wall_footer_component import PicksyWallFooterComponent


class CourierMainPage(QWidget):
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

        self.deliver_cargo_button = MainButtonComponent(
            title_html="<h1>Teslim Et</h1>",
            icon_path=':/icons/assets/send-icon.png',
            tooltip="Bu buton aracılığı ile cihaza kargo teslim edebilirsiniz."
        )

        self.receive_cargo_button = MainButtonComponent(
            title_html="<h1>Teslim Al</h1>",
            icon_path=':/icons/assets/receive-icon.png',
            tooltip="Bu buton aracılığı ile cihazdan 'İade' durumunda olan kargoları teslim alabilirsiniz."
        )

        h_box.addWidget(self.deliver_cargo_button)
        h_box.addWidget(self.receive_cargo_button)

        v_box.addLayout(h_box)

        if footer:
            footer.set_service_and_other_button_width(self.receive_cargo_button.width())
            footer.hide_other_button()
            footer.picksy_wall_footer_service_button.setText("Geri Dön")
            footer.on_click_service_button.connect(lambda: stacked_widget.go_by_page_number(
                PageNumber.COURIER_MAIN_PAGE, PageNumber.HOME_PAGE
            ))
            v_box.addWidget(footer)

        main_layout.addLayout(v_box, 0, 0)

        self.__define_events()

    def __define_events(self):
        self.deliver_cargo_button.mousePressEvent = lambda event: self.stacked_widget.go_by_page_number(
            PageNumber.COURIER_MAIN_PAGE,
            PageNumber.PACKAGE_AUTHENTICATION_PAGE
        )

        self.receive_cargo_button.mousePressEvent = lambda event: self.stacked_widget.go_by_page_number(
            PageNumber.COURIER_MAIN_PAGE,
            PageNumber.OTHER_SERVICES_PAGE
        )
