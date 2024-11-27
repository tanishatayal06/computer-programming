# Problem: Write a recursive function that checks if a string is a palindrome. A palindrome is a word, phrase, or number that reads the same forward and backward.
def is_palindrome(s):
    # Base case: if the string has one or zero characters, it's a palindrome
    if len(s) <= 1:
        return True
    # Compare the first and last characters
    if s[0] != s[-1]:
        return False
    # Recursively check the middle part of the string
    return is_palindrome(s[1:-1])

# Test case
print(is_palindrome("racecar"))  # Output: True
