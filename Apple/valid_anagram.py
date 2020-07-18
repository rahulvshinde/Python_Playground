"""Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?"""

import collections

def anagramCheck(s,t):
    return collections.Counter(s) == collections.Counter(t)

def anagramCheck1(s,t):
    dic = {}
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    for j in t:
        if j not in dic:
            return False
        else:
            dic[j] -= 1

    for val in dic.values():
        if val != 0:
            return False
    return True


s = "anagram"
t = "gramana"
print(anagramCheck(s,t))
print(anagramCheck1(s,t))
