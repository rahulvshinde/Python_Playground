"""Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:
Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4"""

inp = [4,1,2,1,2]

def singleNumber(n):
    res = 0
    for num in n:
        res ^= num
    return res

def singleNumber1(nums):
    return 2*sum(set(nums))-sum(nums)

print(singleNumber(inp))
print(singleNumber1(inp))