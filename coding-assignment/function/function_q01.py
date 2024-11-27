# Problem: Write a function that finds the Kth largest element in a list of numbers. You are not allowed to sort the list
import heapq
def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]
nums = [3, 1, 4, 1, 5, 9, 2, 6]
k = 3
print(kth_largest(nums, k))  
