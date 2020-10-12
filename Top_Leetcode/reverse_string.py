"""Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra
memory.
You may assume all the characters consist of printable ascii characters.
Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]"""

s = ["h", "e", "l", "l", "o"]


# recursive
def reverseString1(s):
    l = len(s)
    if l < 2:
        return s
    return reverseString1(s[l // 2:]) + reverseString1(s[:l // 2])


# # Classic-using two pointers
# def reverseString2(s):
#     i, j = 0, len(s) - 1
#     while i < j:
#         s[i], s[j] = s[j], s[i]
#         i += 1
#         j -= 1
#     return "".join(s)

#
# # pythonic
# def reverseString3(s):
#     return s[::-1]
#
#
# # Mirror image
# def reverseString4(s):
#     l = len(s)
#     for i in range(l // 2):
#         s[i], s[-i - 1] = s[-i - 1], s[i]
#     return s


print(s, "Recursive ---->", reverseString1(s))
# print(s, "Two Pointer ---->", reverseString2(s))
# print(s, "Pythonic ---->", reverseString3(s))
# print(s, "Mirror Image ---->", reverseString4(s))
