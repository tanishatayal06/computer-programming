# Problem: Given an unsorted list of integers, find the length of the longest increasing subsequence.
import bisect

def length_of_lis(nums):
    if not nums:
        return 0
    
    subsequence = []
    
    for num in nums:
        pos = bisect.bisect_left(subsequence, num)
        if pos == len(subsequence):
            subsequence.append(num)
        else:
            subsequence[pos] = num
    
    return len(subsequence)

# Test case
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_lis(nums))  # Output: 4
