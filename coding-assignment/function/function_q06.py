# Problem: Given an unsorted list of integers, find the length of the longest consecutive elements sequence.
def longest_consecutive(nums):
    num_set = set(nums)
    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)
    
    return max_length

nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))  

