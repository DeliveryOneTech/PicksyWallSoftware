import json
from app.communication.iot.mqtt_context import SingletonMqttContext
from app.lib.utils import Utils
from app.lib.console_logger import SingletonConsoleLogger


class InitSubscribers:
    def __init__(self):
        self.mqtt_client = SingletonMqttContext()
        self.console_logger = SingletonConsoleLogger()

        device_id = Utils.get_value_from_app_config('DeviceId')

        self.topic_list_for_subscribe = [
            f'picksywall/{device_id}/#'
        ]

        for topic_name in self.topic_list_for_subscribe:
            self.mqtt_client.subscribe(topic_name, self.__callback)
            self.console_logger.log(f'Subscribed to {topic_name}')

    def __callback(self, payload, **kwargs):
        topic = kwargs['topic']
        payload = json.loads(payload)
        self.console_logger.log(f'Received message from topic {topic}: {payload}')

    def unsubscribe_all(self):
        self.mqtt_client.un_subscribe_all(self.topic_list_for_subscribe)
        self.console_logger.log('Unsubscribed from all topics')


class SingletonInitSubscribers(InitSubscribers):
    __instance = None

    def __new__(cls):
        if SingletonInitSubscribers.__instance is None:
            SingletonInitSubscribers.__instance = InitSubscribers()
        return SingletonInitSubscribers.__instance
