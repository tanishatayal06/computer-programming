# Problem: Write a Python program to generate all permutations of a list in Python. (itertools)
import itertools
numbers = [1, 2, 3]
permutations = itertools.permutations(numbers)
for perm in permutations:
    print(perm)

