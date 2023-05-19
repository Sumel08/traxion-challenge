from unittest import TestCase

from src.util.utilities import Utilities


class TestUtilities(TestCase):
    def test_create_unique_code(self):
        code = Utilities.create_unique_code(4)
        self.assertEqual(len(code), 4)
        code = Utilities.create_unique_code(6)
        self.assertEqual(len(code), 6)
        code = Utilities.create_unique_code(200)
        self.assertEqual(len(code), 200)

    def test_100000_unique_codes_6_length(self):
        amount_of_codes = 100000
        unique_codes = [Utilities.create_unique_code(6) for x in range(amount_of_codes)]
        self.assertEqual(len(set(unique_codes)), amount_of_codes)
