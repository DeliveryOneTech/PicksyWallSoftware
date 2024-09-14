from app.enums.page_number import PageNumber
from app.lib.console_logger import ConsoleLogger
from app.ui.pages.robot_management_main_page import RobotManagementMainPage


class RightRobotManagementPage(RobotManagementMainPage):
    def __init__(self, stacked_widget):
        super().__init__(stacked_widget, PageNumber.RIGHT_ROBOT_MANAGEMENT)
        self.console_logger = ConsoleLogger()
        self.console_logger.log()
