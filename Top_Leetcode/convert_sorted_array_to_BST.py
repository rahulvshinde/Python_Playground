"""Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5"""


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param num, a list of integers
    # @return a tree node
    # 12:37
    def sortedArrayToBST(self, nums):
        # continue while this branch has values to process
        if len(nums) > 0:
            # create node from center point of nums
            i = len(nums) // 2
            root = TreeNode(nums[i])

            # the left node becomes the recursive sorted BST of the items
            # to the left of the center point, and the right node becomes
            # the recursive sorted BST of the items to right of center point
            root.left = self.sortedArrayToBST(nums[:i])
            root.right = self.sortedArrayToBST(nums[i + 1:])

            # return the root, whose children will be properly set
            return root

        # notice that Python functions implicitly return None, so children
        # that call sortedArrayToBST recursively but with no values remaining
        # will be set to None, as desired
