# Problem: Write a recursive function to calculate the factorial of a number n.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Test case
print(factorial(5))  # Output: 120
