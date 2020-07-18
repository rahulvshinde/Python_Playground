"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

def isSubtree(s, t):
    def isMatch(s,t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val == t.val:
            if isMatch(s.left, t.left) and isMatch(s.right,t.right):
                return True
            else:
                return False
    if isMatch(s,t):
        return True
    if s is None:
        return False
    return isSubtree(s.left,t) or isSubtree(s.right,t)

isSubtree(s,t)
