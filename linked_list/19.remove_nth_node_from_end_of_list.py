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
        fast = slow = sentinel = ListNode(None)
        sentinel.next = head
        
        for _ in range(n+1):
            fast = fast.next
            
        while fast:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        
        return sentinel.next
