"""
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example,
if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some
number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.
"""


A = "abcde"
B = "cdeab"
def rotateString(A,B):
    return len(A) == len(B) and B in A+A

def rotateString1(A,B):
    if len(A) != len(B):
        return False
    if A == B:
        return True
    for i in range(len(B)):
        if A[i:] + A[0:i] == B:
            return True
    return False


print(rotateString(A,B))
print(rotateString1(A,B))
