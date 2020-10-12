"""Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:
Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4"""
from functools import reduce
from collections import Counter

inp = [4,1,2,1,2]

def singleNumber(n):
    res = 0
    for num in n:
        res ^= num
    return res

def singleNumber1(nums):
    return 2*sum(set(nums))-sum(nums)

def singleNumber2(nums):
    mydict = {}
    for num in nums:
        if num in mydict:
            mydict[num] += 1
        else:
            mydict[num] = 1
    for key,value in mydict.items():
        if value == 1:
            return key

def singleNumber3(nums):
    return reduce(lambda x,y: x^y, nums)

def singleNumber4(nums):
    elements = Counter(nums)
    for key, value in elements.items():
        if value ==1:
            return key

def singleNumber5(nums):
    for i in [k for k,v in Counter(nums).items() if v == 1]:
        return i

print(singleNumber(inp))
print(singleNumber1(inp))
print(singleNumber2(inp))
print(singleNumber3(inp))
print(singleNumber4(inp))
print(singleNumber5(inp))