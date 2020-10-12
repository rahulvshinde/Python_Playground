"""Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of
the non-zero elements.
Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

a = [0, 1, 0, 3, 12]

def moveZeros(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums

def moveZeros1(nums):
    for num in nums:
        if num == 0:
            nums.remove(num)
            nums.append(num)
    return nums

print("Original List: {old}\nMoved Zeros: {new}".format(old=a, new=moveZeros(a)))
print("Original List: {old}\nMoved Zeros: {new}".format(old=a, new=moveZeros1(a)))
