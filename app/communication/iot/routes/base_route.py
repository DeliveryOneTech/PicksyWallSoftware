from abc import abstractmethod
from app.enums.iot_topic import IoTTopic


class MqttMessageRoute:
    @property
    @abstractmethod
    def topic(self) -> IoTTopic:
        pass

    @abstractmethod
    def handle(self, payload):
        pass
