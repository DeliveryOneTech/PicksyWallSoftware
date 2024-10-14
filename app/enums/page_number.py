from enum import Enum


class PageNumber(Enum):
    HOME_PAGE = 0

    SENDER_IDENTIFICATION_PAGE = 1  # sender identification page
    SENDER_INFORMATION_PAGE = 11  # sender information page
    SENDER_ADDRESS_PAGE = 12  # sender address page
    RECEIVER_INFORMATION_PAGE = 13  # receiver information page
    RECEIVER_ADDRESS_PAGE = 14  # receiver address page

    REJECTION_ID_PAGE = 2  # rejection id page

    INITIALIZATION_PAGE = 5  # initialaztion page
    RECEIVER_AUTHENTICATION_PAGE = 3  # receiver authentication page

    OTHER_SERVICES_PAGE = 6  # other services page
    COURIER_AUTHENTICATION_PAGE = 7  # courier authentication page

    SERVICE_USER_AUTHENTICATION_PAGE = 4
    SERVICE_MAIN_PAGE = 8  # service main page
    LEFT_ROBOT_MANAGEMENT_PAGE = 9  # left robot management page
    RIGHT_ROBOT_MANAGEMENT_PAGE = 10  # right robot management page

    # MAINTENANCE =
    # CLEANING =
