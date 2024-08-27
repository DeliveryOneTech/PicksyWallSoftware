class ActionResultModel:
    success: bool = False
    message: str = None
    data: object = None

    def __init__(self, success: bool = False, message: str = None, data: object = None):
        self.success = success
        self.message = message
        self.data = data
