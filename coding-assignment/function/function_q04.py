# Problem: Write a function to rotate a list by k positions to the right, where k is non-negative.
def rotate_list(nums, k):
    n = len(nums)
    k = k % n 
    return nums[-k:] + nums[:-k]
  
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate_list(nums, k))  # Output: [5, 6, 7, 1, 2, 3, 4]
