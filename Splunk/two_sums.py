"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def twoSum(nums, target):
    mydict = {}
    for i, num in enumerate(nums):
        if num in mydict:
            return [mydict[num], i]
        else:
            mydict[target - num] = i
print(twoSum([2, 7, 11, 15], 9))


def twoSum1(nums, target):
    myhash={}
    for idx, num in enumerate(nums):
        if target-num in myhash:
            return [myhash[target-num],idx]
        myhash[num] = idx
print(twoSum1([2, 7, 11, 15], 9))

