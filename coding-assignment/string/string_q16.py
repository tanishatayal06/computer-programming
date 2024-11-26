# Problem: Given a string s and an integer k, rotate the string by k positions.
input_string = input()
k = int(input())
rotated_string = input_string[k % len(input_string):] + input_string[:k % len(input_string)]
print(rotated_string)
