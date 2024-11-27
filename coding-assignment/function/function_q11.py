# Problem: Given a list of distinct integers, return all possible subsets (the power set). The solution set must not contain duplicate subsets
def subsets(nums):
    result = []
    
    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])
    return result

# Test case
nums = [1, 2, 3]
print(subsets(nums))  # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
