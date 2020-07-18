"""Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome."""


def permNumber(num):
    return str(num)== str(num)[::-1]

def permNumber1(num):
    if num < 0:
        return False
    a,b = num, 0
    while num:
        b *= 10
        b += num % 10
        num //= 10
    return a == b


print(permNumber(1212))
print(permNumber1(121))