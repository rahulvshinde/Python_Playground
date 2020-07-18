"""Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in
sorted non-decreasing order.
Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
Note:
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order."""

a = [-4, -1, 0, 3, 10]


def squareArray(a):
    return sorted([x ** 2 for x in a])


def squareArray1(a):
    return [x * x for x in sorted(a, key=lambda y: y * y)]

def squareArray2(a):
    list2 = []
    for i in a:
        list2.append(i*i)
    return sorted(list2, reverse=False)

#2 pointers solution
def squareArray3(a):
    result = []
    l = 0
    r = len(a) -1
    while l<=r:
        left = a[l] **2
        right = a[r] **2
        if left >right:
            result.insert(0,left)
            l+=1
        else:
            result.insert(0,right)
            r-=1
    return result


print(squareArray(a))
print(squareArray1(a))
print(squareArray2(a))
print(squareArray3(a))
