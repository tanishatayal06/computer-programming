# Given a list of numbers and a target sum, write a function to find all unique combinations of numbers that add up to the target.
def combination_sum(nums, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(nums)):
            if nums[i] > target:
                continue
            backtrack(i, target - nums[i], path + [nums[i]])
    result = []
    nums.sort()
    backtrack(0, target, [])
    return result

nums = [2, 3, 6, 7]
target = 7
print(combination_sum(nums, target))  # Output: [[2, 2, 3], [7]]

