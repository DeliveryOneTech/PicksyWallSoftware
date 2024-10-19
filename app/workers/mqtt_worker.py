import json
import logging
from app.lib.utils.utils import Utils
from app.enums.thread_name import ThreadName
from app.workers.thread_manager import ThreadManager
from PyQt5.QtCore import QObject, pyqtSignal, QThread
from app.lib.utils.console_logger import ConsoleLogger
from app.communication.iot.mqtt_context import MqttContext
from app.communication.iot.mqtt_message_router import MqttMessageRouter


class MqttWorker(QObject):
    message_received_signal = pyqtSignal(object)
    subscription_result_signal = pyqtSignal(bool)
    is_thread_executed = False

    def __init__(self, thread_name=ThreadName.MQTT_WORKER_ACTION.value):
        super().__init__()
        self.thread_name = thread_name
        self.mqtt_client = None
        self.console_logger = ConsoleLogger()
        self.device_id = Utils.get_value_from_app_config('DeviceId')

        self.topic_list_for_subscribe = [
            f'picksywall/{self.device_id}/test',
        ]

    def subscribe_all(self):
        self.__create_mqtt_client_if_is_none()
        for topic_name in self.topic_list_for_subscribe:
            self.mqtt_client.subscribe(topic_name, self.__callback)
            self.console_logger.log(f'Subscribed to {topic_name}')
        self.subscription_result_signal.emit(True)

    def __callback(self, payload, **kwargs):
        topic = kwargs['topic']
        self.console_logger.log(f'Topic: {topic}, Payload: {payload}')
        try:
            json_payload = json.loads(payload)
        except json.JSONDecodeError:
            ConsoleLogger().log(f'Error while parsing JSON payload: {payload}', logging.ERROR)
            json_payload = payload
        self.message_received_signal.emit({
            'topic': topic,
            'payload': json_payload
        })
        MqttMessageRouter().route(topic, json_payload)

    def unsubscribe_all(self):
        self.__create_mqtt_client_if_is_none()
        self.mqtt_client.un_subscribe_all(self.topic_list_for_subscribe)
        self.console_logger.log('Unsubscribed from all topics')

    def reconnect(self):
        self.__create_mqtt_client_if_is_none()
        self.mqtt_client.reconnect()
        self.subscribe_all()

    def publish(self, topic, payload):
        self.__create_mqtt_client_if_is_none()
        self.mqtt_client.publish(topic, payload)

    def stop(self):
        self.__create_mqtt_client_if_is_none()
        self.unsubscribe_all()
        self.mqtt_client.disconnect()
        self.console_logger.log('Stopped MQTT worker')

    # private methods
    def __create_mqtt_client_if_is_none(self):
        if self.mqtt_client is None:
            self.mqtt_client = MqttContext()

    @staticmethod
    def run_in_thread(auto_start=False, run_with_thread_manager=True):
        action = MqttWorker()
        thread = QThread()
        thread.setObjectName(action.thread_name)

        action.moveToThread(thread)
        thread.started.connect(action.subscribe_all)
        action.is_thread_executed = run_with_thread_manager

        if auto_start:
            thread.start()

        if run_with_thread_manager:
            thread_manager = ThreadManager()
            thread.finished.connect(lambda: thread_manager.remove_redundant_thread_action_pairs())
            thread_manager.add_thread_action_pair(action, thread)

        return action, thread
