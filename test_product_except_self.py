import unittest
from product_except_self import product_except_self

class TestProductExceptSelf(unittest.TestCase):
    
    def test_regular_case(self):
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
    
    def test_case_with_zero(self):
        self.assertEqual(product_except_self([0, 2, 3]), [6, 0, 0])
    
    def test_two_elements(self):
        self.assertEqual(product_except_self([2, 5]), [5, 2])
    
    def test_all_ones(self):
        self.assertEqual(product_except_self([1, 1, 1, 1]), [1, 1, 1, 1])
    
    def test_negative_numbers(self):
        self.assertEqual(product_except_self([-1, -2, -3, -4]), [-24, -12, -8, -6])

if __name__ == "__main__":
    unittest.main()
