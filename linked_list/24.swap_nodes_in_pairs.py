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


# Solution 1
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


# Solution 2: use the reverse node in k group template
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        cur = head
        cnt = 0
        
        while cnt < 2:
            if not cur:
                return head
            
            cur = cur.next
            cnt += 1
            
        prev = self.swapPairs(cur)
        
        while cnt:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt 
            cnt -= 1
            
        return prev
