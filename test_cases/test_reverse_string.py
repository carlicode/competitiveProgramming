import unittest
from reverse_string import reverse_string

class TestStringReversal(unittest.TestCase):
    
    def test_regular_string(self):
        self.assertEqual(reverse_string("Python"), "nohtyP")
    
    def test_string_with_spaces(self):
        self.assertEqual(reverse_string("Hello World"), "dlroW olleH")
    
    def test_string_with_numbers(self):
        self.assertEqual(reverse_string("12345"), "54321")
    
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")
    
    def test_string_with_special_characters(self):
        self.assertEqual(reverse_string("!@#$"), "$#@!")
    
    def test_palindrome_string(self):
        self.assertEqual(reverse_string("radar"), "radar")
    
if __name__ == "__main__":
    unittest.main()
