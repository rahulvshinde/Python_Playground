"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

"""
import collections
strs = ["eat","tea","tan","ate","nat","bat"]
def groupAnagrams(strs):
    hashmap = {}
    for st in strs:
        key = "".join(sorted(st))
        if key not in hashmap:
            hashmap[key] = [st]
        else:
            hashmap[key] += [st]
    return list(hashmap.values())

def groupAnagrams1(strs):
    hashmap = collections.defaultdict(list)
    for st in strs:
        hashkey = "".join(sorted(st))
        hashmap[hashkey].append(st)
    return list(hashmap.values())


print(groupAnagrams(strs))
print(groupAnagrams1(strs))