"""
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each
letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.

https://leetcode.com/problems/partition-labels/discuss/193371/Python-solution-28ms
"""


s = "ababcbacadefegdehijhklij"
def partitionLabels(s):
    hashmap = {}
    for ind, char in enumerate(s):
        hashmap[char] = ind
    cur_max = 0
    counter = 0
    result = []

    for ind, char in enumerate(s):
        counter +=1
        print('Index {}, Char {}, hashmap[char] {}, cur_max {}, counter {}'.format(ind, char, hashmap[char], cur_max, counter))
        cur_max = max(cur_max,hashmap[char])
        if cur_max == ind:
            result.append(counter)
            counter = 0
    print(result)

partitionLabels(s)