#https://github.com/Sandwich-Monsieur/lab11-DH-JS.git
#Partner 1: Dominic Hung
#Partner 2: Jose Serrano


import unittest
from calculator

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,3), 6)
        self.assertEqual(mul(-2,3), -6)
        self.assertEqual(mul(0, 3), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(4,2), 0.5)
        self.assertEqual(div(-4,2), -0.5)
        self.assertRaises(ZeroDivisionError, div, 0, 0)

#     # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, -5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(-3,4), 5)
        self.assertEqual(hypotenuse(0, 2), 2)

    def test_sqrt(self): # 3 assertions
        self.assertRaises(ValueError, square_root, -1)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(4), 2)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()