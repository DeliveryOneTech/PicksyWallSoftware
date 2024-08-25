from datetime import datetime
from app.data.models.DbModel import DbModel
from app.data.enums.log_level import LogLevel
from app.data.enums.log_type import LogType


class SystemLog(DbModel):
    def __init__(self, _id: int, logLevel: LogLevel, logType: LogType, message: str, createdDateTime: datetime):
        super().__init__("SystemLog", _id)
        self.logLevel = logLevel
        self.logType = logType
        self.message = message
        self.createdDateTime = createdDateTime
