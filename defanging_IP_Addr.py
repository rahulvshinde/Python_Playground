# """
# Given a valid (IPv4) IP address, return a defanged version of that IP address.
#
# A defanged IP address replaces every period "." with "[.]".
#
# Example 1:
#
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# Example 2:
#
# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"
# """
#
# import re
# ipstr="1.1.1.1"
# def defangIPAddr(ipstr):
#     return ipstr.replace('.', '[.]')
#
# def defangIPAddr1(ipstr):
#     return '[.]'.join(ipstr.split('.'))
#
# def defangIPAddr2(ipstr):
#     return re.sub('\.','[.]', ipstr)
#
# def defangIPAddr3(ipstr):
#     if i in ipstr:
#         if i == ".":
#             print(i)
#
# print("Original IP Addr: {} \nDefanged IP Addr: {}".format(ipstr, defangIPAddr(ipstr)))
# print("Original IP Addr: {} \nDefanged IP Addr: {}".format(ipstr, defangIPAddr1(ipstr)))
# print("Original IP Addr: {} \nDefanged IP Addr: {}".format(ipstr, defangIPAddr2(ipstr)))
# print("Original IP Addr: {} \nDefanged IP Addr: {}".format(ipstr, defangIPAddr3(ipstr)))



def dtob(num):
    if num >1:
        dtob(num//2)
        print(num % 2, end = '')
dtob(7)