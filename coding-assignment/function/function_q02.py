# Problem: Given a list of integers, write a function to find all subarrays that sum up to zero.
def find_subarrays_with_zero_sum(nums):
    subarrays = []
    sum_dict = {0: [-1]}  # Sum: List of indices where this sum occurs
    cumulative_sum = 0

    for i, num in enumerate(nums):
        cumulative_sum += num
        if cumulative_sum in sum_dict:
            for index in sum_dict[cumulative_sum]:
                subarrays.append(nums[index + 1:i + 1])
        if cumulative_sum not in sum_dict:
            sum_dict[cumulative_sum] = []
        sum_dict[cumulative_sum].append(i)
    
    return subarrays

nums = [1, -1, 2, -2, 3, -3]
print(find_subarrays_with_zero_sum(nums))
