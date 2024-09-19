import unittest
from find_second_largest import find_second_largest

class TestSecondLargestFinder(unittest.TestCase):
    
    def test_regular_case(self):
        self.assertEqual(find_second_largest([3, 1, 4, 4, 2]), 3)
    
    def test_two_elements(self):
        self.assertEqual(find_second_largest([10, 5]), 5)
    
    def test_all_same_elements(self):
        self.assertEqual(find_second_largest([1, 1, 1]), None)
    
    def test_negative_numbers(self):
        self.assertEqual(find_second_largest([-1, -2, -3, -4]), -2)
    
    def test_large_list(self):
        self.assertEqual(find_second_largest(list(range(1000))), 998)

if __name__ == "__main__":
    unittest.main()
