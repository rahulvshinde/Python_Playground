"""Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if
every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true"""

# a = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
a = [1,2,3,4,5]

def dupOrNot(a):
    return len(set(a)) != len(a)

def dupOrNot1(a):
    mydict= {}
    for i, num in enumerate(a):
        if num not in mydict:
            mydict[num] = 1
        else:
            return True
    return False

print(dupOrNot(a))
print(dupOrNot1(a))
