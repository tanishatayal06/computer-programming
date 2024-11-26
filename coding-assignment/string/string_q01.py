# Problem: Write a function to check if a given string is a palindrome.
str = input()
if str == str[::-1]:
    print("Palindrome")
else:
    print("Not Palidrome")
