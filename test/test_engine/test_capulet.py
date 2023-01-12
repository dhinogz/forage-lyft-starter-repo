import unittest

from src.engine import Capulet


class TestNubbin(unittest.TestCase):

    def test_does_not_need_service(self):
        current_mileage = 29999
        last_service_mileage = 0

        engine = Capulet(
            current_mileage=current_mileage, 
            last_service_mileage=last_service_mileage
        )

        self.assertFalse(engine.needs_service())

    def test_needs_service(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = Capulet(
            current_mileage=current_mileage, 
            last_service_mileage=last_service_mileage
        )

        self.assertTrue(engine.needs_service())