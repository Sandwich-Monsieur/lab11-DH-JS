#https://github.com/Sandwich-Monsieur/lab11-DH-JS.git
#Partner 1: Dominic Hung
#Partner 2: Jose Serrano

import math
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    #Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(5, 0), 5)
        self.assertEqual(calculator.add(-1, -1), -2)

    def test_subtract(self): # 3 assertions
        self.assertEqual(calculator.sub(5, 3), 2)
        self.assertEqual(calculator.sub(10, 0), 10)
        self.assertEqual(calculator.sub(0, 5), -5)
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    #Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    with self.assertRaises(ZeroDivisionError):
        calculator.div(0, 10)  # a=0, b=10
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(calculator.log(10, 100), 2.0)  # log_a(b)
        self.assertAlmostEqual(calculator.log(math.e, math.e), 1.0)
        self.assertAlmostEqual(calculator.log(4, 2), 0.5)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.log(0, 5)
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch thi
if __name__ == "__main__":
    unittest.main()