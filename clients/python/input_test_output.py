import unittest
from unittest.mock import patch

from input_output import read_input_data, read_many_inputs_times


class InputTest(unittest.TestCase):

    VALID_NUMBER: float = 42.00

    @patch('builtins.input', lambda *args: '42.0')
    def test_read_input(self):
        """ :: it should read the input from user """
        input_values = read_input_data()

        name, purchase = input_values

        self.assertIsInstance(name, str)
        self.assertIsInstance(purchase, float)
        self.assertIsInstance(input_values, tuple)

    @patch('builtins.input', lambda *args: '42.0')
    def test_read_many_inputs(self):
        """ :: it should read the input many times """
        TIMES = 2
        values_list: list = read_many_inputs_times(times=TIMES)

        self.assertEqual(len(values_list), TIMES)
        self.assertIsInstance(values_list, list)

        self.assertEqual(values_list, [
            (str(self.VALID_NUMBER), self.VALID_NUMBER),
            (str(self.VALID_NUMBER), self.VALID_NUMBER)
        ])

    @patch('builtins.input', lambda *args: '42.0')
    def test_read_many_inputs_default(self):
        """ :: it should read the input 1 time by default """
        values_list: list = read_many_inputs_times()

        self.assertEqual(len(values_list), 1)
        self.assertIsInstance(values_list, list)

        self.assertEqual(values_list, [
            (str(self.VALID_NUMBER), self.VALID_NUMBER)
        ])
