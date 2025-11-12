#https://github.com/Sandwich-Monsieur/lab11-DH-JS.git
#Partner 1: Dominic Hung
#Partner 2: Jose Serrano

import calculator
import math
import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-2, 2), 0)
        self.assertEqual(calculator.add(4, 0), 4)
        self.assertEqual(calculator.add(15, 10), 25)
        self.assertEqual(calculator.add(1.3, 5.2), 6.5)
    def test_subtract(self):
        self.assertEqual(calculator.sub(2, 1), 1)
        self.assertEqual(calculator.sub(5, 0), 5)
        self.assertEqual(calculator.sub(-5, -3), -2)
        self.assertEqual(calculator.sub(17, 7), 10)
    def test_multiply(self):
        self.assertEqual(calculator.mul(1, 1), 1)
        self.assertEqual(calculator.mul(2, 2), 4)
        self.assertEqual(calculator.mul(-4, 2), -8)
        self.assertEqual(calculator.mul(10, 2), 20)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 10) # a=0, b=10
    def test_logarithm(self):
        self.assertAlmostEqual(calculator.log(10, 100), 2.0)
        self.assertAlmostEqual(calculator.log(math.e, math.e), 1.0)
        self.assertAlmostEqual(calculator.log(4, 2), 0.5)
    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.log(0, 5)
        with self.assertRaises(ValueError):
            calculator.log(1, 5)
        with self.assertRaises(ValueError):
            calculator.log(-2, 5)


# Do not touch this
if __name__ == "__main__":
    unittest.main()