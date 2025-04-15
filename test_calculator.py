# https://github.com/joshuaking18/lab10-JK

import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.subtract(-3, -1), -2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(10, 100), 2)
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)  # base can't be 1
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)  # base can't be negative
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -10)  # argument can't be negative
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 10)  # base can't be zero


    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-2, 5), -10)
        self.assertEqual(calculator.mul(0, 99), 0)

    def test_divide(self):
        self.assertEqual(calculator.div(2, 10), 5)
        self.assertEqual(calculator.div(5, 25), 5)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 10)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -10)
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)
        self.assertAlmostEqual(calculator.hypotenuse(-3, -4), 5)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(16), 4)
        self.assertEqual(calculator.square_root(0), 0)
        with self.assertRaises(ValueError):
            calculator.square_root(-1)

if __name__ == '__main__':
    unittest.main()