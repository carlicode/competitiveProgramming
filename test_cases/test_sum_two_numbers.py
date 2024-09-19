import unittest
from sum_two_numbers import sum_two_numbers

class TestSumTwoNumbers(unittest.TestCase):
    
    def test_positive_numbers(self):
        self.assertEqual(sum_two_numbers(3, 5), 8)
    
    def test_negative_and_positive(self):
        self.assertEqual(sum_two_numbers(-2, 4), 2)
    
    def test_large_numbers(self):
        self.assertEqual(sum_two_numbers(1000, -1000), 0)
    
    def test_both_negative(self):
        self.assertEqual(sum_two_numbers(-3, -7), -10)
    
    def test_zero_sum(self):
        self.assertEqual(sum_two_numbers(0, 0), 0)
    
    def test_zero_and_positive(self):
        self.assertEqual(sum_two_numbers(0, 10), 10)

if __name__ == "__main__":
    unittest.main()