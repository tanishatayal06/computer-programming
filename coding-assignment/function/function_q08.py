# Problem: Given a list of integers, find all elements that appear more than once in the list.
def find_duplicates(nums):
    seen = set()
    duplicates = set()
    
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

# Test case
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates(nums))  # Output: [2, 3]
