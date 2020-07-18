"""Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?"""


def reverseLL(head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev

def revrseLL1(node,prev=None):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return reverseLL1(n,node)

print(reverseLL(a))
print(reverseLL1(a))