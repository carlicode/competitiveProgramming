import unittest
from find_lcm import find_lcm

class TestLCMCalculator(unittest.TestCase):
    
    def test_case_6_4(self):
        self.assertEqual(find_lcm(6, 4), 12)
    
    def test_case_15_20(self):
        self.assertEqual(find_lcm(15, 20), 60)
    
    def test_case_7_5(self):
        self.assertEqual(find_lcm(7, 5), 35)
    
    def test_case_same_number(self):
        self.assertEqual(find_lcm(10, 10), 10)
    
    def test_case_large_numbers(self):
        self.assertEqual(find_lcm(100000, 100000), 100000)

if __name__ == "__main__":
    unittest.main()
