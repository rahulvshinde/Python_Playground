"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

num1 = "100"
num2 = "999"
def addStrings(num1,num2):
    """
            :type num1: str
            :type num2: str
            :rtype: str
            """
    res, i, j, s = [], len(num1) - 1, len(num2) - 1, 0
    while i >= 0 or j >= 0 or s:
        if i >= 0:
            s += int(num1[i])
            i -= 1
        if j >= 0:
            s += int(num2[j])
            j -= 1
        res.append(str(s % 10))
        s /= 10
    res_str = ''.join(res[::-1])
    return res_str

def addStrings1(num1,num2):
    return int(num1)+int(num2)

# print(addStrings(num1,num2))
# print(addStrings1(num1,num2))
