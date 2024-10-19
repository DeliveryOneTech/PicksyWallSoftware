import logging
from app.lib.models.d1_result_data_model import D1Result
from app.lib.utils.console_logger import ConsoleLogger
from app.ui.abstracts.BaseQStackedWidget import BaseQStackedWidget
from app.ui.pages.cleaning_authentication_page import CleaningAuthenticationPage
from app.ui.pages.cleaning_main_page import CleaningMainPage
from app.ui.pages.courier_main_page import CourierMainPage
from app.ui.pages.device_management_page import DeviceManagementPage
from app.ui.pages.initialization_page import InitializationPage
from app.ui.pages.courier_authentication_page import CourierAuthenticationPage
from app.ui.pages.home_page import HomePage
from app.enums.page_number import PageNumber
from PyQt5.QtWidgets import QMainWindow
from app.ui.pages.left_robot_management_page import LeftRobotManagementPage
from app.ui.pages.maintenance_authentication_page import MaintenanceAuthenticationPage
from app.ui.pages.maintenance_main_page import MaintenanceMainPage
from app.ui.pages.other_services_page import OtherServicesPage
from app.ui.pages.package_authentication_page import PackageAuthenticationPage
from app.ui.pages.receiver_authentication_page import ReceiverAuthenticationPage
from app.ui.pages.right_robot_management_page import RightRobotManagementPage
from app.ui.pages.sender_address_page import SenderAddressPage
from app.ui.pages.sender_information_page import SenderInformationPage
from app.ui.pages.sender_identification_page import SenderIdentificationPage
from app.ui.pages.receiver_address_page import ReceiverAddressPage
from app.ui.pages.receiver_information_page import ReceiverInformationPage
from app.ui.pages.rejection_id_page import RejectionIdPage
from app.ui.pages.service_main_page import ServiceMainPage
from app.ui.pages.service_user_authentication_page import ServiceUserAuthenticationPage
from app.workers.loops.check_internet_connection_loop import CheckInternetConnectionLoop
from app.ui import resource


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
                SenderIdentificationPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                RejectionIdPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                ReceiverAuthenticationPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                ServiceUserAuthenticationPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                InitializationPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                OtherServicesPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                CourierAuthenticationPage(self.stacked_widget)
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
                SenderInformationPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                SenderAddressPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                ReceiverInformationPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                ReceiverAddressPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                DeviceManagementPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                MaintenanceAuthenticationPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                CleaningAuthenticationPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                CourierMainPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                PackageAuthenticationPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                MaintenanceMainPage(self.stacked_widget)
            )
            self.stacked_widget.addWidget(
                CleaningMainPage(self.stacked_widget)
            )

            self.stacked_widget.go_by_page_number(PageNumber.INITIALIZATION_PAGE,
                                                  PageNumber.INITIALIZATION_PAGE)

            self.setCentralWidget(self.stacked_widget)

        except Exception as e:
            ConsoleLogger().log(f"{e}", logging.ERROR)
            raise e

    __last_internet_state = CheckInternetConnectionLoop.get_internet_connection_state()

    def __handle_check_internet_connection_loop_result_signal(self, result: D1Result):
        if not result.success:
            self.stacked_widget.go_by_page_number(PageNumber.HOME_PAGE, PageNumber.INITIALIZATION_PAGE)
        elif self.__last_internet_state is False and result.success:
            self.stacked_widget.mqtt_worker.reconnect()
            self.stacked_widget.go_by_page_number(PageNumber.INITIALIZATION_PAGE, PageNumber.HOME_PAGE)

        self.__last_internet_state = result.success

    def showEvent(self, event):
        super().showEvent(event)
        self.check_internet_connection_loop_thread.start()
        self.check_internet_connection_loop_action.result_signal.connect(
            self.__handle_check_internet_connection_loop_result_signal
        )
