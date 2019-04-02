"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        sentinel = walk1 = walk2 = ListNode(-1)
        sentinel.next = head
        walk1.next = head
        walk2.next = head

        for _ in range(n+1):
            walk1 = walk1.next

        while walk1:
            walk1 = walk1.next
            walk2 = walk2.next

        walk2.next = walk2.next.next

        return sentinel.next

