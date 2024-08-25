from PyQt5.QtWidgets import QStackedWidget
from app.ui.enums.page_number import PageNumber


class BaseQStackedWidget(QStackedWidget):
    def __init__(self):
        super().__init__()

    def go_by_page_number(self,
                          caller_page_number: PageNumber,
                          target_page_number: PageNumber,
                          custom_method=None) -> None:
        super().setCurrentIndex(target_page_number.value)

        caller_widget = self.widget(caller_page_number.value)
        if hasattr(caller_widget, "on_exit"):
            caller_widget.on_exit()

        target_widget = self.widget(target_page_number.value)
        if hasattr(target_widget, "on_shown"):
            target_widget.on_shown()

        if custom_method is not None:
            custom_method()
