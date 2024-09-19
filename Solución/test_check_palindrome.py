import unittest
from check_palindrome import check_palindrome

class TestPalindromeChecker(unittest.TestCase):
    
    def test_regular_palindrome(self):
        self.assertTrue(check_palindrome("Anita lava la tina"))
    
    def test_non_palindrome(self):
        self.assertFalse(check_palindrome("Python no es palíndromo"))
    
    def test_palindrome_with_spaces_and_punctuation(self):
        self.assertTrue(check_palindrome("A Santa at NASA"))
    
    def test_empty_string(self):
        self.assertTrue(check_palindrome(""))
    
    def test_palindrome_with_numbers(self):
        self.assertTrue(check_palindrome("12321"))
    
    def test_non_palindrome_with_numbers(self):
        self.assertFalse(check_palindrome("12345"))

if __name__ == "__main__":
    unittest.main()
