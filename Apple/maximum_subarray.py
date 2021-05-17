"""Given an integer array nums, find the contiguous subarray (containing at least one number) which has the
largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle."""


a = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubarray(nums,):
    if not nums:
        return 0
    curSum = maxSum = nums[0]
    for num in nums[1:]:
        curSum = max(num,curSum+num)
        maxSum = max(curSum, maxSum)
    return maxSum

print(maxSubarray(a))
#
# def maxSubarrayFixedSize(nums,subsize):
#     if not nums:
#         return 0
#     curSum = maxSum = nums[0]
#     for num in nums[1:]:
#
#
#
# print(maxSubarrayFixedSize(a, 2))


