"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""
from collections import Counter
s= "abab"
p= "ab"

def find_anagrams(s,p):
    res = []
    pCounter = Counter(p)
    sCounter = Counter(s[:len(p)])
    output = []
    i = 0
    j = len(p)
    while j<= len(s):
        if sCounter == pCounter:
            output.append(i)
        sCounter[s[i]] -=1
        if sCounter[s[i]] <=0:
            sCounter.pop(s[i])
        if j<len(s):
            sCounter[s[j]] += 1
        j +=1
        i +=1
    return output
print(find_anagrams(s,p))


