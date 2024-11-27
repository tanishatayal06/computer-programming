# Problem: Write a function that counts the number of vowels in a given string.
def count_vowels(s):
    vowels = set("aeiouAEIOU")
    return sum(1 for char in s if char in vowels)

# Test case
print(count_vowels("hello world"))  # Output: 3
