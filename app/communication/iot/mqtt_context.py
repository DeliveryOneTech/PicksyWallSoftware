from awscrt import io, mqtt
from awsiot import mqtt_connection_builder
import json
from app.lib.utils import Utils
from app.data.enums.log_level import LogLevel
from app.services.log_service import LogService
from app.lib.console_logger import SingletonConsoleLogger

data = Utils.read_all_app_config()["IoTConfiguration"]
ENDPOINT = data['Endpoint']
CLIENT_ID = data['ClientId']
PATH_TO_CERTIFICATE = data['PathToCertificate']
PATH_TO_PRIVATE_KEY = data['PathToPrivateKey']
PATH_TO_AMAZON_ROOT_CA_1 = data['PathToAmazonRootCA']


class MqttContext:
    def __init__(self):
        self.logService = LogService()
        self.subscribedTopics = []
        self.event_loop_group = io.EventLoopGroup(1)
        self.host_resolver = io.DefaultHostResolver(self.event_loop_group)
        self.client_bootstrap = io.ClientBootstrap(self.event_loop_group, self.host_resolver)
        self.mqtt_connection = self.create_connection()
        self.mqtt_connection.on_publish = self.on_publish
        
        self.console_logger = SingletonConsoleLogger()

        self.console_logger.log("Connecting to {} with client ID '{}'...".format(
            ENDPOINT, CLIENT_ID))

        # Make the connect() call

        self.connect_future = self.mqtt_connection.connect()
        self.connect_future.result()

        self.logService.create_mqtt_log(LogLevel.INFO, "MQTT baglantisi baslatildi")
        self.console_logger.log("Mqtt Connected!")

    def create_connection(self):
        try:
            self.logService.create_mqtt_log(LogLevel.INFO,
                                            "MQTT baglantisi kurmak icin create_connection fonksiyonu cagrildi")
            return mqtt_connection_builder.mtls_from_path(
                endpoint=ENDPOINT,
                cert_filepath=PATH_TO_CERTIFICATE,
                pri_key_filepath=PATH_TO_PRIVATE_KEY,
                client_bootstrap=self.client_bootstrap,
                ca_filepath=PATH_TO_AMAZON_ROOT_CA_1,
                client_id=CLIENT_ID,
                clean_session=False,
                keep_alive_secs=6)
        except Exception as e:
            self.console_logger.log(e)
            self.logService.create_mqtt_log(LogLevel.ERROR, f"MQTT baglantisi kurulamadi :: {e}")

    def reconnect(self):
        try:
            self.logService.create_mqtt_log(LogLevel.INFO, "MQTT baglantisi yeniden kuruluyor")
            self.un_subscribe_all(self.subscribedTopics)
            self.mqtt_connection = self.create_connection()
            self.mqtt_connection.on_publish = self.on_publish
            self.connect_future = self.mqtt_connection.connect()
            self.connect_future.result()
            self.logService.create_mqtt_log(LogLevel.INFO, "MQTT baglantisi yeniden kuruldu")
            self.console_logger.log("Mqtt Reconnected!")
        except Exception as e:
            self.console_logger.log(e)
            self.logService.create_mqtt_log(LogLevel.ERROR, f"MQTT baglantisi yeniden kurulamadi :: {e}")

    def publish(self, topic, message):
        try:
            self.mqtt_connection.publish(
                topic=topic,
                payload=json.dumps(message),
                qos=mqtt.QoS.AT_LEAST_ONCE)
            self.on_publish(topic, message)
        except Exception as e:
            self.console_logger.log("Error : {}".format(e))
            self.logService.create_mqtt_log(LogLevel.ERROR, f"MQTT publish islemi basarisiz :: {e}")
            return

    def on_publish(self, topic, payload, **kwargs):
        self.console_logger.log("Published message from topic '{}': {}".format(topic, payload))
        self.logService.create_mqtt_log(LogLevel.INFO,
                                        "Published Message To Topic : {} , Payload : {}".format(topic, payload))

    def subscribe(self, topic, callback):
        # if topic is subscribed exisiting, unsubscribe it
        if self.isSubscribed(topic) is False:
            self.subscribedTopics.append(topic)
            # subscribe to topic
            self.console_logger.log("Subscribing to topic '{}'...".format(topic))
            subscribe_future, packet_id = self.mqtt_connection.subscribe(
                topic=topic,
                qos=mqtt.QoS.AT_LEAST_ONCE,
                callback=callback)
            subscribe_result = subscribe_future.result()
            self.logService.create_mqtt_log(LogLevel.INFO, "Abone olunan topic : {}".format(topic))
            return packet_id
        else:
            return None

    def isSubscribed(self, topic):
        return topic in self.subscribedTopics

    def on_message_received(self, topic, payload, **kwargs):
        # called when a message is received
        # self.console_logger.log but background color is yellow
        self.console_logger.log("\033[33mReceived message from topic '{}': {}".format(topic, payload))

    def disconnect(self):
        disconnect_future = self.mqtt_connection.disconnect()
        disconnect_future.result()
        self.subscribedTopics = []
        self.logService.create_mqtt_log(LogLevel.INFO, "MQTT baglantisi kapatildi")
        self.console_logger.log("Mqtt Disconnected!")

    def unSubscribe(self, topic):
        # if topic in subscribedTopics, unsubscribe it
        if self.isSubscribed(topic) is True:
            self.subscribedTopics.remove(topic)
            self.console_logger.log("Unsubscribing from topic '{}'...".format(topic))
            unsubscribe_future, packet_id = self.mqtt_connection.unsubscribe(
                topic=topic)
            unsubscribe_result = unsubscribe_future.result()
            self.console_logger.log("Unsubscribed: {}".format(unsubscribe_result))
            self.logService.create_mqtt_log(LogLevel.INFO, "Aboneligi sonlanan topic : {}".format(topic))
        else:
            self.console_logger.log("Topic '{}' is not subscribed".format(topic))

    def un_subscribe_all(self, topics):
        unsubscribe_futures = []
        for topic in topics:
            unsubscribe_future, _ = self.mqtt_connection.unsubscribe(topic)
            unsubscribe_futures.append(unsubscribe_future)
        for unsubscribe_future in unsubscribe_futures:
            unsubscribe_future.result()
        self.logService.create_mqtt_log(LogLevel.INFO, "Tum abonelikler sonlandirildi")
        self.subscribedTopics = []


class SingletonMqttContext:
    __instance = None

    @staticmethod
    def getInstance():
        try:
            if SingletonMqttContext.__instance is None:
                SingletonMqttContext()
            return SingletonMqttContext.__instance
        except Exception as e:
            self.console_logger.log(e)

    def __init__(self):
        try:
            if SingletonMqttContext.__instance is not None:
                raise Exception("This class is a singleton!")
            else:
                SingletonMqttContext.__instance = MqttContext()
        except Exception as e:
            self.console_logger.log(e)
