from PyQt5.QtWidgets import QStackedWidget
from app.enums.page_number import PageNumber
from app.services.log_service import LogService


class BaseQStackedWidget(QStackedWidget):
    def __init__(self):
        super().__init__()

    def go_by_page_number(self,
                          caller_page_number: PageNumber,
                          target_page_number: PageNumber,
                          custom_method=None) -> None:
        LogService().create_ui_log(
            f"Page transition from {caller_page_number.name} to {target_page_number.name}"
        )

        super().setCurrentIndex(target_page_number.value)

        caller_widget = self.widget(caller_page_number.value)
        if hasattr(caller_widget, "on_exit"):
            caller_widget.on_exit()

        target_widget = self.widget(target_page_number.value)
        if hasattr(target_widget, "on_shown"):
            target_widget.on_shown()

        if custom_method is not None:
            custom_method()
