# Problem: Write a function to find all permutations of a string
from itertools import permutations

input_string = input()
perms = set(permutations(input_string))
for perm in perms:
    print(''.join(perm))
