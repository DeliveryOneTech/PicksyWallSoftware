import json
from app.communication.iot.mqtt_context import MqttContext
from app.communication.iot.mqtt_message_router import MqttMessageRouter
from app.lib.decorators.singleton_decorator import Singleton
from app.lib.utils import Utils
from app.lib.console_logger import ConsoleLogger


@Singleton
class MqttSubscriber:
    def __init__(self):
        self.mqtt_client = MqttContext()
        self.console_logger = ConsoleLogger()

        device_id = Utils.get_value_from_app_config('DeviceId')

        self.topic_list_for_subscribe = [
            f'picksywall/{device_id}/test',
        ]

        self.subscribe_all()

    def subscribe_all(self):
        for topic_name in self.topic_list_for_subscribe:
            self.mqtt_client.subscribe(topic_name, self.__callback)
            self.console_logger.log(f'Subscribed to {topic_name}')

    def __callback(self, payload, **kwargs):
        topic = kwargs['topic']
        payload = json.loads(payload)
        MqttMessageRouter().route(topic, payload)

    def unsubscribe_all(self):
        self.mqtt_client.un_subscribe_all(self.topic_list_for_subscribe)
        self.console_logger.log('Unsubscribed from all topics')
