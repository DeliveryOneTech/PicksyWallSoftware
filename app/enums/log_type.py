import enum


class LogType(enum.Enum):
    SYSTEM_LOG = 0
    MQTT_LOG = 1
    UI_LOG = 2
    EXCEPTION_LOG = 3 # try-except block
