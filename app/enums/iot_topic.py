import enum
from app.lib.utils.utils import Utils


class IoTTopic(enum.Enum):
    __base_topic = f"picksywall/{Utils.get_value_from_app_config('DeviceId')}"
    TEST_TOPIC = f"{__base_topic}/test"
    ACK_TOPIC = f"{__base_topic}/ack"
