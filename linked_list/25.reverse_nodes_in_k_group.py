"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:
Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

Note:
Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution1: Iteration
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 1:
            return head

        n = 0
        sentinel = ListNode()
        sentinel.next = cur = head

        while cur:
            n += 1
            cur = cur.next
        
        prev = sentinel
        cur = head
        for _ in range(n // k):
            for _ in range(k - 1):
                nxt = cur.next
                cur.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
            
            prev = cur
            cur = cur.next
        
        return sentinel.next


# Solution 2: Recursion
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Step 1: count k nodes
        if not head:
            return head
        
        cur = head
        cnt = 0
        
        while cnt < k:
            if not cur:
                return head
            
            cur = cur.next
            cnt += 1

        # Step 2: reverse k nodes   
        prev = self.reverseKGroup(cur, k)
        
        while cnt:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt 
            cnt -= 1
            
        return prev


# Solution 3
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        
        sentinel = prev = ListNode()
        sentinel.next = head
        
        while prev:
            prev = self.reverse(prev, k)
            
        return sentinel.next
    
    def reverse(self, prev: ListNode, k: int) -> ListNode:
        last = prev
        
        for i in range(k+1):
            last = last.next
            
            if i != k and not last:
                return None
            
        tail = prev.next
        cur = prev.next.next
        
        while cur != last:
            nxt = cur.next
            cur.next = prev.next
            prev.next = cur 
            tail.next = nxt
            cur = nxt
        
        return tail
