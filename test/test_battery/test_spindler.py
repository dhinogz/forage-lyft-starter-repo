import unittest
from datetime import datetime

from src.battery import Spindler


class TestSpindler(unittest.TestCase):

    def test_does_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = Spindler(last_service_date=last_service_date)

        self.assertFalse(battery.needs_service())

    def test_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        battery = Spindler(last_service_date=last_service_date)

        self.assertTrue(battery.needs_service())

