class MqttMessageEvent:
    sample_time: object = None
    cmd: int = None
    data: object = None

    def __init__(self, sample_time: object, cmd: int, data: object):
        self.sample_time = sample_time
        self.cmd = cmd
        self.data = data
