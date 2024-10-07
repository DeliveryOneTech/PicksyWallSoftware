from enum import Enum

# sonu page ile bitsin
class PageNumber(Enum):
    HOME = 0
    SEND_TO_CARGO_IDENTITY_NUMBER_INPUT = 1 # sender identification page
    SEND_TO_REJECT_IDENTITY_NUMBER_INPUT = 2 # rejection id page
    RECEIVE_PACKAGE_AUTHENTICATION = 3 # receiver authentication page
    SERVICE_USER_AUTHENTICATION = 4
    APPLICATION_LOADING = 5 # initialaztion page
    OTHERS_MAIN = 6 # other services page
    COURIER_USER_AUTHENTICATION = 7 # courier authentication page
    SERVICE_MAIN = 8 # service main page
    LEFT_ROBOT_MANAGEMENT = 9 # left robot management page
    RIGHT_ROBOT_MANAGEMENT = 10 # right robot management page
    SEND_TO_CARGO_CUSTOMER_INFO = 11 # sender information page
    SEND_TO_CARGO_CUSTOMER_ADDRESS = 12 # sender address page
    SEND_TO_CARGO_RECEIVER_INFO = 13 # receiver information page
    SEND_TO_CARGO_RECEIVER_ADDRESS = 14 # receiver address page

    # MAINTENANCE =
    # CLEANING =
