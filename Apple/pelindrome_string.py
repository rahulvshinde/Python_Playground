"""Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true"""
import collections

a = "code"


def palindromePermutation(a):
    counter = collections.Counter(a)
    print(counter)
    odd = 0
    for count in counter.values():
        print(count)
        if count % 2:
            print(odd)
            odd += 1
            if odd > 1:
                return False
    return True

def palindromePermutation1(a):
    return len(list(filter(lambda item:item[1]%2, collections.Counter(a).items()))) <=1

print(palindromePermutation(a))
print(palindromePermutation1(a))


























