# Problem: Given a list of numbers containing n distinct numbers taken from the range 1 to n+1, find the missing number in the list.
def find_missing_number(nums):
    n = len(nums)
    total = (n + 1) * (n + 2) // 2
    return total - sum(nums)

# Test case
nums = [1

