from app.communication.iot.routes.base_route import MqttMessageRoute
from app.lib.utils.console_logger import ConsoleLogger
from app.lib.utils.utils import Utils


class TestTopicRoute(MqttMessageRoute):
    topic = f'picksywall/{Utils.get_value_from_app_config("DeviceId")}/test'
    # TODO : ENUMERABLE NAME EKLENECEK.
    # TODO : ENUMS'A NAME EKLEMEK YENİ EKLENECEKLER İÇİN ZORUNLU..

    def __init__(self):
        super().__init__()

    def handle(self, payload):
        ConsoleLogger.log(payload)
        return payload
