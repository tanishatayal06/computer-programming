# Problem: Write a function to check if two strings are anagrams
string1 = input()
string2 = input()
if sorted(string1) == sorted(string2):
    print("Anagrams")
else:
    print("Not anagrams")
