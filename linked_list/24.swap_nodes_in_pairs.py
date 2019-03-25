"""
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Iterative
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        sentinel = ListNode(-1)
        sentinel.next = head
        walk = sentinel
        
        while walk.next and walk.next.next:
            first = walk.next
            second = walk.next.next
            walk.next = second
            first.next = second.next
            second.next = first
            walk = walk.next.next
            
        return sentinel.next
