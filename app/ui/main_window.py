from PyQt5.QtCore import pyqtSignal
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.pages.application_loading_page import ApplicationLoadingPage
from app.ui.pages.courier_user_authentication_page import CourierUserAuthenticationPage
from app.ui.pages.home_page import HomePage
from app.enums.page_number import PageNumber
from PyQt5.QtWidgets import QMainWindow
from app.ui.pages.left_robot_management_page import LeftRobotManagementPage
from app.ui.pages.others_main_page import OthersMainPage
from app.ui.pages.receive_package_authentication_page import ReceivePackageAuthenticationPage
from app.ui.pages.right_robot_management_page import RightRobotManagementPage
from app.ui.pages.send_to_cargo_customer_address_page import SendToCargoCustomerAddressPage
from app.ui.pages.send_to_cargo_customer_info_page import SendToCargoCustomerInfoPage
from app.ui.pages.send_to_cargo_identity_number_input_page import SendToCargoIdentityNumberInputPage
from app.ui.pages.send_to_cargo_receiver_address_page import SendToCargoReceiverAddressPage
from app.ui.pages.send_to_cargo_receiver_info_page import SendToCargoReceiverInfoPage
from app.ui.pages.send_to_reject_identity_number_input_page import SendToRejectIdentityNumberInputPage
from app.ui.pages.service_main_page import ServiceMainPage
from app.ui.pages.service_user_authentication_page import ServiceUserAuthenticationPage
from app.ui.utils import resource


class MainWindow(QMainWindow):
    app_ready = pyqtSignal()

    def __init__(self):
        try:
            super(MainWindow, self).__init__()
            stacked_widget = BaseQStackedWidget()

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
            stacked_widget.addWidget(
                OthersMainPage(stacked_widget)
            )
            stacked_widget.addWidget(
                CourierUserAuthenticationPage(stacked_widget)
            )
            stacked_widget.addWidget(
                ServiceMainPage(stacked_widget)
            )
            stacked_widget.addWidget(
                LeftRobotManagementPage(stacked_widget)
            )
            stacked_widget.addWidget(
                RightRobotManagementPage(stacked_widget)
            )
            stacked_widget.addWidget(
                SendToCargoCustomerInfoPage(stacked_widget)
            )
            stacked_widget.addWidget(
                SendToCargoCustomerAddressPage(stacked_widget)
            )
            stacked_widget.addWidget(
                SendToCargoReceiverInfoPage(stacked_widget)
            )
            stacked_widget.addWidget(
                SendToCargoReceiverAddressPage(stacked_widget)
            )

            stacked_widget.go_by_page_number(PageNumber.APPLICATION_LOADING,
                                             PageNumber.APPLICATION_LOADING)

            self.setCentralWidget(stacked_widget)

            self.app_ready.emit()

        except Exception as e:
            print(e)
            raise e
