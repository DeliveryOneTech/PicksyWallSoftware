import json
from app.communication.iot.mqtt_context import SingletonMqttContext
from app.lib.utils import Utils
from app.lib.console_logger import SingletonConsoleLogger


class InitSubscribers:
    def __init__(self):
        self.mqtt_client = SingletonMqttContext.getInstance()
        self.console_logger = SingletonConsoleLogger()

        device_id = Utils.get_value_from_app_config('DeviceId')

        self.subscribers = [
            f'picksywall/{device_id}/#'
        ]

        for subscriber in self.subscribers:
            self.mqtt_client.subscribe(subscriber, self.__callback)
            self.console_logger.log(f'Subscribed to {subscriber}')

    def __callback(self, payload, **kwargs):
        topic = kwargs['topic']
        payload = json.loads(payload)
        self.console_logger.log(f'Received message from topic {topic}: {payload}')

    def unsubscribe_all(self):
        self.mqtt_client.un_subscribe_all(self.subscribers)
        self.console_logger.log('Unsubscribed from all topics')
