"""Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra
space complexity?"""
from functools import reduce

# inp = [9,6,4,2,3,5,7,0,1]
inp = [0,1]
def missingNumber(nums):
    n = len(nums)
    return int(n * (n+1) //2 - sum(nums))

def missingNumber1(nums):
    n = len(nums)
    nums.sort()
    for idx, value in enumerate(nums):
        print(idx, value)
        if idx != value:
            return idx
    return nums[-1]+1
print(missingNumber(inp))
print(missingNumber1(inp))