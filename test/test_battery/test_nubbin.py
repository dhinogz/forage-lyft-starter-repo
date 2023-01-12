import unittest
from datetime import datetime

from src.battery import Nubbin


class TestNubbin(unittest.TestCase):

    def test_does_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = Nubbin(last_service_date=last_service_date)

        self.assertFalse(battery.needs_service())

    def test_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = Nubbin(last_service_date=last_service_date)

        self.assertTrue(battery.needs_service())
