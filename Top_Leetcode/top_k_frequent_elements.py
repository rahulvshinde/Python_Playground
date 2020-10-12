"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

from collections import Counter
def topFrequent(nums, k):
    most_common = Counter(nums).most_common()
    print(most_common)
    fin = []
    for l in range(0, k):
        fin.append(most_common[l][0])

    return fin

print(topFrequent([1,1,1,2,2,3], 2))