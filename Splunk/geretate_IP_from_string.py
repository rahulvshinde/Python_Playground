#Program to generate all possible valid IP addresses from given string

# class Solution:
#     def restoreIpAddresses(self, s: str) -> List[str]:
#         self.res = []
#         self.backtrack(s, [], 0)
#         return self.res
#
#     def backtrack(self, s, current, start):
#         if len(current) == 4 and start == len(s):
#             self.res.append(".".join(current))
#             return
#         if len(current) > 4:
#             return
#         for i in range(start, min(start + 3, len(s))):
#             if s[start] == '0' and i > start:
#                 continue
#             if int(s[start:i + 1]) <= 255:
#                 self.backtrack(s, current + [s[start:i + 1]], i + 1)

s = "25525511135"
res = []
def restore_ip_addr(s):
    backtrack(s,[],0)
    return res
def backtrack(s, current, start):
    if len(current) == 4 and start == len(s):
        res.append(".".join(current))
        print(current)
        return
    if len(current) > 4:
        return
    for i in range(start, min(start+3, len(s))):
        if s[start] == '0' and i>start:
            continue
        if int(s[start:i+1])<=255:
            backtrack(s,current+[s[start:i+1]], i+1)
print(restore_ip_addr(s))