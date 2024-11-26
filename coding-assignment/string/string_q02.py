# Problem: Write a function to count the number of vowels in a string.
string = input()
vowels = "aeiouAEIOU"
vowel_count = 0
for char in string:
    if char in vowels:
        vowel_count += 1
print(vowel_count)
