import arithmetic_arrager as arithmetic
from unittest import TestCase


class ArithmeticTest(TestCase):
    def test_too_many_problems(self):
        result = arithmetic.arithmetic_arranger(['1 + 2', '31 + 4', '123 + 321', '5 + 3', '1 + 4', '5 + 2'])
        self.assertEqual(result, 'Error: Too many problems.')

    def test_operator_error(self):
        result = arithmetic.arithmetic_arranger(['1 / 4'])
        self.assertEqual(result, "Error: Operator must be '+' or '-'.")

    def test_number_of_digits(self):
        result = arithmetic.arithmetic_arranger(['12345 + 312'])
        self.assertEqual(result, 'Error: Numbers cannot be more than four digits.')
