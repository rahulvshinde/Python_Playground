"""
Find the contiguous subarray within an array, A of
length N which has the largest sum.
"""
# import math
nums = [-4, -2, -1, -7, -8, -1, -2, -8, -1, 0]
size = 3


def maxSubarray(nums, size):
    # maxSum = float('inf')
    # i, j = 0,2
    totSum = -float('inf')  # -math.inf
    for i, num in enumerate(nums):
        j = i + size
        if totSum <= sum(nums[i:j]) and j <= len(nums):
            totSum = sum(nums[i:j])
            i += 1
    return totSum


print(maxSubarray(nums, size))
