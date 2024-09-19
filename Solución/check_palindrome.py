import re

def check_palindrome(s: str) -> bool:
    # Remove all non-alphanumeric characters and convert to lowercase
    clean_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    # Check if the cleaned string is the same forwards and backwards
    return clean_s == clean_s[::-1]
