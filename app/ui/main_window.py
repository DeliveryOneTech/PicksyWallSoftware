from PyQt5.QtCore import pyqtSignal
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.pages.application_loading_page import ApplicationLoadingPage
from app.ui.pages.home_page import HomePage
from app.enums.page_number import PageNumber
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from app.ui.pages.receive_package_authentication_page import ReceivePackageAuthenticationPage
from app.ui.pages.send_to_cargo_identity_number_input_page import SendToCargoIdentityNumberInputPage
from app.ui.pages.send_to_reject_identity_number_input_page import SendToRejectIdentityNumberInputPage
from app.ui.pages.service_user_authentication_page import ServiceUserAuthenticationPage


class MainWindow(QMainWindow):
    app_ready = pyqtSignal()

    def __init__(self):
        try:
            super(MainWindow, self).__init__()
            central_widget = QWidget()
            stacked_widget = BaseQStackedWidget()

            self.setCentralWidget(central_widget)
            layout = QVBoxLayout(central_widget)
            layout.addWidget(stacked_widget)

            stacked_widget.addWidget(
                HomePage(stacked_widget)
            )
            stacked_widget.addWidget(
                SendToCargoIdentityNumberInputPage(stacked_widget)
            )
            stacked_widget.addWidget(
                SendToRejectIdentityNumberInputPage(stacked_widget)
            )
            stacked_widget.addWidget(
                ReceivePackageAuthenticationPage(stacked_widget)
            )
            stacked_widget.addWidget(
                ServiceUserAuthenticationPage(stacked_widget)
            )
            stacked_widget.addWidget(
                ApplicationLoadingPage(stacked_widget)
            )

            stacked_widget.go_by_page_number(PageNumber.APPLICATION_LOADING,
                                             PageNumber.APPLICATION_LOADING)

            self.app_ready.emit()

        except Exception as e:
            print(e)
            raise e
