from enum import Enum


class ThreadName(Enum):
    CHECK_INTERNET_CONNECTION_LOOP = "CheckInternetConnectionLoop"
    SUBSCRIBE_TO_ALL_TOPICS_ACTION = "SubscribeToAllTopicsAction"
    SERVICE_USER_LOGIN_ACTION = "ServiceUserLoginAction"
    CHECK_USER_IDENTITY_NUMBER_ACTION = "CheckUserIdentityNumberAction"
    MQTT_WORKER_ACTION = "MqttWorkerAction"
