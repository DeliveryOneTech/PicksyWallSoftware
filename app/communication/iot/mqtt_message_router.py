from app.communication.iot.routes.base_route import MqttMessageRoute
from app.lib.decorators.singleton_decorator import Singleton
from app.communication.iot.routes.test_topic_route import TestTopicRoute


@Singleton
class MqttMessageRouter:
    def __init__(self):
        # get all MqttMessageRoute inherited classes
        self.routes = [cls() for cls in MqttMessageRoute.__subclasses__()]

    def route(self, topic, payload):
        for route in self.routes:
            if route.topic == topic:
                return route.handle(payload)
        return None
