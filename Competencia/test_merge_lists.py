import unittest
from merge_lists import merge_lists

class TestMergeLists(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual(merge_lists([1, 2, 3], [3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_case_2(self):
        self.assertEqual(merge_lists([5, 10, 15], [1, 5, 20]), [1, 5, 10, 15, 20])
    
    def test_case_3(self):
        self.assertEqual(merge_lists([7, 8, 9], [8, 9, 10]), [7, 8, 9, 10])
    
    def test_empty_lists(self):
        self.assertEqual(merge_lists([], []), [])
    
    def test_one_empty_list(self):
        self.assertEqual(merge_lists([1, 2, 3], []), [1, 2, 3])
    
    def test_identical_lists(self):
        self.assertEqual(merge_lists([1, 2, 3], [1, 2, 3]), [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
