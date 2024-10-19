import unittest
from app.data.entities.log import Log
from app.services.log_service import LogService


class TestLogService(unittest.TestCase):
    def setUp(self):
        self.log_service = LogService()

    def test_create_system_log(self):
        result = self.log_service.create_system_log('Test system log')
        result_is_integer = isinstance(result, int)
        self.assertTrue(result_is_integer)

    def test_create_mqtt_log(self):
        result = self.log_service.create_mqtt_log('Test mqtt log')
        result_is_integer = isinstance(result, int)
        self.assertTrue(result_is_integer)

    def test_create_ui_log(self):
        result = self.log_service.create_ui_log('Test ui log')
        result_is_integer = isinstance(result, int)
        self.assertTrue(result_is_integer)

    def test_create_exception_log(self):
        result = self.log_service.create_exception_log('Test exception log')
        result_is_integer = isinstance(result, int)
        self.assertTrue(result_is_integer)

    def test_get_all_logs(self):
        result = self.log_service.get_all_logs()
        result_is_list = isinstance(result, list)
        result_all_elements_are_log = all(isinstance(log_item, Log) for log_item in result)
        self.assertTrue(result_is_list)
        self.assertTrue(result_all_elements_are_log)

    def test_get_log(self):
        result = self.log_service.get_log(1)
        result_is_log = isinstance(result, Log)
        self.assertTrue(result_is_log)
