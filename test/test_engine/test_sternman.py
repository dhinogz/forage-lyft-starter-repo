import unittest

from src.engine import Sternman


class TestSternman(unittest.TestCase):

    def test_does_not_need_service(self):
        is_warning_light_on = False
        engine = Sternman(
            is_warning_light_on=is_warning_light_on
        )

        self.assertFalse(engine.needs_service())

    def test_needs_service(self):
        is_warning_light_on = True

        engine = Sternman(
            is_warning_light_on=is_warning_light_on
        )

        self.assertTrue(engine.needs_service())