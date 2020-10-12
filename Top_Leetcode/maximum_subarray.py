"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [0]
Output: 0

Example 4:

Input: nums = [-1]
Output: -1

Example 5:

Input: nums = [-2147483647]
Output: -2147483647
"""

nums = [-2,1,-3,4,-1,2,1,-5,4]
def maximumSubarray(nums):
    curSum = maxSum = nums[0]
    for num in nums[1:]:
        curSum = max(num,curSum+num)
        maxSum = max(maxSum,curSum)
    return maxSum


def maximum_subarray(nums):
    for i in range(1,len(nums)):
        nums[i]=max(nums[i], nums[i]+nums[i-1])
    return max(nums)

print(maximumSubarray(nums))
print(maximum_subarray(nums))