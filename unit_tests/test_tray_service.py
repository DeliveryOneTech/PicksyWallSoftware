import unittest
# from unittest.mock import patch
from app.data.entities.tray import Tray
from app.services.tray_service import TrayService


class TrayServiceTest(unittest.TestCase):

    def setUp(self):
        self.tray_service = TrayService()

    def test_get_all_trays(self):
        result = self.tray_service.get_all_trays()
        result_is_list = isinstance(result, list)
        result_all_elements_are_tray = all(isinstance(tray, Tray) for tray in result)
        self.assertTrue(result_is_list)
        self.assertTrue(result_all_elements_are_tray)

    def test_create_tray(self):
        result = self.tray_service.create_tray('A1', False)
        result_is_integer = isinstance(result, int)
        self.assertTrue(result_is_integer)

    def test_update_tray(self):
        all_trays = self.tray_service.get_all_trays()
        tray = all_trays[0]
        result = self.tray_service.update_tray(tray.id, 'UPDATED_A1', True)
        result_is_integer = isinstance(result, int)
        self.assertTrue(result_is_integer)
