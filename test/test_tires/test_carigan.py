import unittest

from src.tires import Carigan


class TestCarigan(unittest.TestCase):

    def test_does_not_need_service(self):
        
        tires_wear = [0.6, 0.7, 0.4, 0.5]

        tires = Carigan(
            tires_wear=tires_wear,
        )

        self.assertFalse(tires.needs_service())

    def test_needs_service(self):

        tires_wear = [0.9, 0.8, 0.6, 0.7]

        tires = Carigan(
            tires_wear=tires_wear,
        )

        self.assertTrue(tires.needs_service())

    def test_invalid_tires_wear_input(self):

        tires_wear = [1.1, 0.8, 0.6, 0.5]

        with self.assertRaises(ValueError):
            tires = Carigan(
                tires_wear=tires_wear,
            )
            