import unittest
from count_vowels import count_vowels

class TestVowelCounter(unittest.TestCase):
    
    def test_regular_string(self):
        self.assertEqual(count_vowels("Python"), 1)
    
    def test_string_with_spaces(self):
        self.assertEqual(count_vowels("Hello World"), 3)
    
    def test_string_with_numbers_and_special_characters(self):
        self.assertEqual(count_vowels("123 @Home!"), 2)
    
    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)
    
    def test_all_vowels(self):
        self.assertEqual(count_vowels("aeiouAEIOU"), 10)
    
    def test_no_vowels(self):
        self.assertEqual(count_vowels("bcdfgh"), 0)

if __name__ == "__main__":
    unittest.main()
