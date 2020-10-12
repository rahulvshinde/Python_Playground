"""Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?"""

a = [1,2,3,4,5]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(ListNode):
    def __init__(self):
        super().__init__()

    def reverseList(self, head: ListNode) -> ListNode:
# def reverseLL(head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        print(prev)

# def reverseLL1(node,prev=None):
#     if not node:
#         return prev
#     n = node.next
#     node.next = prev
#     return reverseLL1(n,node)
#
# print(reverseLL(a))
# print(reverseLL1(a))
ax = Solution()
ax.reverseList(a)