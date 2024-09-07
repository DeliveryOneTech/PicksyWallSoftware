from abc import abstractmethod


class MqttMessageRoute:
    @property
    @abstractmethod
    def topic(self):
        pass

    @abstractmethod
    def handle(self, payload):
        pass
