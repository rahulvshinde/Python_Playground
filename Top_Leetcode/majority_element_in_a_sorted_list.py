"""
Given an array nums sorted in non-decreasing order, and a number target, return True if and only if target is a majority element.

A majority element is an element that appears more than N/2 times in an array of length N.



Example 1:

Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
Output: true
Explanation:
The value 5 appears 5 times and the length of the array is 9.
Thus, 5 is a majority element because 5 > 9/2 is true.

Example 2:

Input: nums = [10,100,101,101], target = 101
Output: false
Explanation:
The value 101 appears 2 times and the length of the array is 4.
Thus, 101 is not a majority element because 2 > 4/2 is false.
"""
from collections import Counter
def majorityElement(nums, target):
    res = Counter(nums)
    return res[target] > len(nums)//2

def majorityElement2(nums, target):
    size = len(nums)
    cnt = 0
    for num in nums:
        if num == target:
            cnt +=1
    if cnt > size //2:
        return True

print(majorityElement([2,5,5],5))
print(majorityElement2([2,5,5],5))