# Problem: Write a function that accepts any number of arguments and returns the sum of the squares of the arguments.
def sum_of_squares(*args):
    return sum(x**2 for x in args)

# Test case
print(sum_of_squares(1, 2, 3))  # Output: 14
