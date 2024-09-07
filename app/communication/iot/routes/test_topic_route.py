from app.communication.iot.routes.base_route import MqttMessageRoute
from app.lib.utils import Utils


class TestTopicRoute(MqttMessageRoute):
    topic = f'picksywall/{Utils.get_value_from_app_config("DeviceId")}/test'

    def __init__(self):
        super().__init__()

    def handle(self, payload):
        print('HashRoute', payload)
        return payload
