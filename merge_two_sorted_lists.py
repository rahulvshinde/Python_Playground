"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
l1, l2 = [1, 2, 4], [1, 3, 4]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#
#
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if l1 and l2:
#             if l1.val > l2.val:
#                 l1, l2 = l2, l1
#             l1.next = self.mergeTwoLists(l1.next, l2)
#         return l1 or l2


class Solution:
    def mergeTwoLists(self, l1,l2):
        head  = ListNode(0)
        ptr = head
        while l1 or l2:
            if l1 and l2:
                smallVal = 0
                if l1.val <=l2.val:
                    smallVal = l1.val
                    l1 = l1.next
                else:
                    smallVal = l2.val
                    l2 = l2.next
                newNode = ListNode(smallVal)
                ptr.next = newNode
                ptr = ptr.next
        return head.next