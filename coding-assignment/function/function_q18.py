# Problem: Write a recursive function to find whether a given number is prime.
def is_prime(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)

# Test case
print(is_prime(17))  # Output: True
