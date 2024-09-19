def count_vowels(s: str) -> int:
    # Define a set of vowels for easy lookup
    vowels = set("aeiouAEIOU")
    # Count the number of vowels in the string
    return sum(1 for char in s if char in vowels)
