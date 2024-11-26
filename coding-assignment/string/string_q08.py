# Problem: Write a function to find the first non-repeating character in a string
from collections import Counter
input_string = input()
count = Counter(input_string)
for char in input_string:
    if count[char] == 1:
        print(char)
        break
