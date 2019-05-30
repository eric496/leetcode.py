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

"""
Thought process:
    One-pass approach: use two pointers, let the first move forward by n+1 nodes, then let both move simultaneouly. 
                       When the first pointer reach the tail, the second is at the node right before the n-th from the end. 
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        sentinel = walk1 = walk2 = ListNode(-1)
        sentinel.next = head
        walk1.next = walk2.next = sentinel

        for _ in range(n+1):
            walk1 = walk1.next

        while walk1:
            walk1, walk2 = walk1.next, walk2.next

        walk2.next = walk2.next.next

        return sentinel.next
