"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in
sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

"""

def sortedSquares(A):
    B = []
    for i in A:
        B.append(i * i)
    return sorted(B)

print(sortedSquares([-4,-1,0,3,10]))
#     def sortedSquares(self, A: List[int]) -> List[int]:
#         for i in range(len(A)):
#             A[i] *= A[i]
#         A.sort()
#         return A

#     def sortedSquares(self, A: List[int]) -> List[int]:
#         return sorted([x**2 for x in A])
