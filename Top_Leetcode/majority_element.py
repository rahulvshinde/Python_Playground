"""Given an array of size n, find the majority element. The majority element is the element that appears more
than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2"""

import collections
a = [2,2,1,1,1,2,1,1,2]


def majorityElement(nums):
    return sorted(nums)[len(nums)//2]

def majorityElement1(nums):
    return collections.Counter(nums).most_common()[0][0]

#two pass + dictionary
def majorityElement2(nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num,0) + 1
    for num in nums:
        if dic[num] > len(nums)//2:
            return num

def majorityElement3(nums):
    return next(num for num in nums if nums.count(num) > len(nums) // 2)

def majorityElement4(nums):
    mnum,count = None, 0
    for num in nums:
        if num == mnum:
            count +=1
        else:
            if count == 0:
                mnum = num
            else:
                count -= 1
    return mnum

def majorityElement5(nums):
    for key, value in collections.Counter(nums).items():
        if value > len(nums)//2:
            return key

print(majorityElement(a))
print(majorityElement1(a))
print(majorityElement2(a))
print(majorityElement3(a))
print(majorityElement4(a))
print(majorityElement5(a))
