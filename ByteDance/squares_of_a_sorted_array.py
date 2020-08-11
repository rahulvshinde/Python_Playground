"""Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number,
also in sorted non-decreasing order.
Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]"""






inp = [-7,-3,2,3,11]

class Solution(object):
#O(n)
    def sortedSquares(self, A):
        answer = []
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                answer.append(left * left)
                l += 1
            else:
                answer.append(right * right)
                r -= 1
        return (answer[::-1])

#O(n log n)
    def sortedSquares1(self, A):
        return sorted(x**2 for x in A)

if __name__ == "__main__":
    check = Solution()
    print(check.sortedSquares(inp))
    print(check.sortedSquares1(inp))
