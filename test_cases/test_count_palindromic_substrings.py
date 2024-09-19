import unittest
from count_palindromic_substrings import count_palindromic_substrings

class TestCountPalindromicSubstrings(unittest.TestCase):
    
    def test_case_aaa(self):
        self.assertEqual(count_palindromic_substrings("aaa"), 6)
    
    def test_case_abc(self):
        self.assertEqual(count_palindromic_substrings("abc"), 3)
    
    def test_case_abba(self):
        self.assertEqual(count_palindromic_substrings("abba"), 6)
    
    def test_single_character(self):
        self.assertEqual(count_palindromic_substrings("a"), 1)
    
    def test_empty_string(self):
        self.assertEqual(count_palindromic_substrings(""), 0)

if __name__ == "__main__":
    unittest.main()
