from app.communication.iot.routes.base_route import MqttMessageRoute
from app.enums.iot_topic import IoTTopic
from app.lib.utils.console_logger import ConsoleLogger


class TestTopicRoute(MqttMessageRoute):
    topic = IoTTopic.TEST_TOPIC

    def __init__(self):
        super().__init__()

    def handle(self, payload):
        ConsoleLogger().log(payload)
        return payload
