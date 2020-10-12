"""You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

#O(n)
from functools import reduce


def climbstairs(n):
    a = b = 1
    for _ in range(n):
        a , b = b, a+b
    return a

def climbstairs1(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbstairs1(n-1)+ climbstairs1(n-2)

print(climbstairs(43))
print(climbstairs1(43))