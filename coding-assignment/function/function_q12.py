# Problem: An element is called a peak if it is greater than or equal to its neighbors. Find a peak element in the list and return its index. You may assume that the list is non-empty.
def find_peak_element(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left

# Test case
nums = [1, 2, 3, 1]
print(find_peak_element(nums))  # Output: 2 (index of peak element 3)

