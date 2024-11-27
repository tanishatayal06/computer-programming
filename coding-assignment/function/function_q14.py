# Problem: Given an array of integers and a target value, return the sum of three integers such that the sum is closest to the target
def three_sum_closest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return closest_sum

    return closest_sum

# Test case
nums = [-1, 2, 1, -4]
target = 1
print(three_sum_closest(nums, target))  # Output: 2
