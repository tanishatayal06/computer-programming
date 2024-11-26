# Problem: Given two strings, check if one is a rotation of the other.
str1 = input()
str2 = input()
if len(str1) == len(str2) and str2 in str1 + str1:
    print("Rotations")
else:
    print("Not rotations")
