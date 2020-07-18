"""Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]"""

nums = [1,2,3]
def subsets(nums):
    subset = [[]]
    for num in nums:
        print(subset)
        subset += [ele + [num] for ele in subset]
    return subset

print(subsets(nums))
