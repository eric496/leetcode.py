"""
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

"""
Thought process:
    Draw a graph and walk it over. 
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        sentinel = prev = ListNode(-1)
        sentinel.next = head
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            first.next = second.next
            second.next = first
            prev.next = second
            prev = prev.next.next
            
        return sentinel.next
