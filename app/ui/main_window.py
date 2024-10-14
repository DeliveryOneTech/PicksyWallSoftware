from app.lib.models.d1_result_data_model import D1Result
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
from app.workers.loops.check_internet_connection_loop import CheckInternetConnectionLoop
from app.ui.utils import resource


class MainWindow(QMainWindow):

    def __init__(self):
        (self.check_internet_connection_loop_action,
         self.check_internet_connection_loop_thread) = CheckInternetConnectionLoop().run_in_thread(
            auto_start=False, run_with_thread_manager=False
        )

        try:
            super(MainWindow, self).__init__()

            self.stacked_widget = BaseQStackedWidget()
            self.setFixedSize(1280, 800)

            self.stacked_widget.addWidget(
                HomePage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                SendToCargoIdentityNumberInputPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                SendToRejectIdentityNumberInputPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                ReceivePackageAuthenticationPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                ServiceUserAuthenticationPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                ApplicationLoadingPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                OthersMainPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                CourierUserAuthenticationPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                ServiceMainPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                LeftRobotManagementPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                RightRobotManagementPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                SendToCargoCustomerInfoPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                SendToCargoCustomerAddressPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                SendToCargoReceiverInfoPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                SendToCargoReceiverAddressPage(self.stacked_widget)
            )

            self.stacked_widget.go_by_page_number(PageNumber.APPLICATION_LOADING,
                                                  PageNumber.APPLICATION_LOADING)

            self.setCentralWidget(self.stacked_widget)

        except Exception as e:
            print(e)
            raise e

    def handle_check_internet_connection_loop_result_signal(self, result: D1Result):
        if not result.success:
            self.stacked_widget.go_by_page_number(PageNumber.HOME, PageNumber.APPLICATION_LOADING)
            return

        current_page_number = PageNumber(self.stacked_widget.currentIndex())
        if current_page_number == PageNumber.APPLICATION_LOADING:
            self.stacked_widget.go_by_page_number(PageNumber.APPLICATION_LOADING, PageNumber.HOME)

    def showEvent(self, event):
        super().showEvent(event)
        self.check_internet_connection_loop_thread.start()
        self.check_internet_connection_loop_action.result_signal.connect(
            self.handle_check_internet_connection_loop_result_signal
        )
