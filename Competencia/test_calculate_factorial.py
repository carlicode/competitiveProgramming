import unittest
from calculate_factorial import calculate_factorial

class TestFactorialCalculator(unittest.TestCase):
    
    def test_factorial_of_five(self):
        self.assertEqual(calculate_factorial(5), 120)
    
    def test_factorial_of_zero(self):
        self.assertEqual(calculate_factorial(0), 1)
    
    def test_factorial_of_seven(self):
        self.assertEqual(calculate_factorial(7), 5040)
    
    def test_factorial_of_one(self):
        self.assertEqual(calculate_factorial(1), 1)
    
    def test_factorial_of_twelve(self):
        self.assertEqual(calculate_factorial(12), 479001600)

if __name__ == "__main__":
    unittest.main()
