"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.



Note: You may assume the string contains only lowercase English letters.

"""
import collections
s = "leetcode"
def uniqueCharacter(s):
    if not s:
        return -1
    d = collections.defaultdict(int)
    for char in s:
        d[char] +=1

    for i,c in enumerate(s):
        if d[c] < 2:
            return i
    return -1


def uniqueCharacter1(s):
    if not s:
        return -1

    myMap = {}
    for i, ch in enumerate(s):
        if ch in myMap:
            myMap[ch] = -1
        else:
            myMap[ch] = i

    for key, value in myMap.items():
        if value != -1:
            return value
    return -1


print(uniqueCharacter(s))
print(uniqueCharacter1(s))





