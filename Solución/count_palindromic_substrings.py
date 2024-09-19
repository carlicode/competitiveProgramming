def count_palindromic_substrings(s: str) -> int:
    n = len(s)
    count = 0
    
    # Helper function to count palindromes centered at (left, right)
    def expand_around_center(left: int, right: int) -> int:
        total = 0
        while left >= 0 and right < n and s[left] == s[right]:
            total += 1
            left -= 1
            right += 1
        return total
    
    # Consider each index as the center of a palindrome
    for i in range(n):
        count += expand_around_center(i, i)       # Odd-length palindromes
        count += expand_around_center(i, i + 1)   # Even-length palindromes
    
   
