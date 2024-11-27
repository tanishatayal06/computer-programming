# Problem: Write a decorator function to memoize results for a function that calculates the Fibonacci number. This will improve the performance of repeated calls.
def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test case
print(fibonacci(10))  # Output: 55

