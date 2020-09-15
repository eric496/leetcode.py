"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

"""
Thought process:
    1. Traverse the linked list to find the node before the m-th node.
    2. Reverse the linked list from the m-th to the n-th node (total of n-m+1 nodes).
    4. Stitch the forehead + reversed part + tail of the linked list to get outcome.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Solution 1
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        sentinel = prev = ListNode(None)
        sentinel.next = head

        for _ in range(m - 1):
            prev = prev.next

        # cur will be the tail node after reversal
        # The linked list is divided into three parts: before m, m to n, and after n.
        # prev_tail is the tail node of the first part, rev_tail is the tail of the second part.
        # We keep track of these two tails to stitch the linked list after reversal.
        prev_tail, rev_tail, cur = prev, prev.next, prev.next

        # Reverse from m-th to n-th nodes (a total of n-m+1 nodes)
        for _ in range(n - m + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # After the reversal, prev is pointing at the head of second part, and cur is pointing at the head of the third part
        # Stitch the linked list in the correct order: sentinel.next -> prev_tail -> prev -> rev_tail -> cur -> the original tail
        prev_tail.next = prev
        rev_tail.next = cur

        return sentinel.next


# Solution 2
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        sentinel = prev = ListNode(None)
        sentinel.next = head

        for _ in range(m - 1):
            prev = prev.next

        new_head, cur = None, prev.next

        for _ in range(n - m + 1):
            nxt = cur.next
            cur.next = new_head
            new_head = cur
            cur = nxt

        prev.next.next = cur
        prev.next = new_head

        return sentinel.next


# Solution 3:
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        sentinel = cur = ListNode(-1)
        sentinel.next = head
        h = t = prev = None
        
        for i in range(n):
            if i + 1 == m:
                h = cur.next
                cur.next = None
                prev = cur
                cur = h
            else:
                cur = cur.next
            
        t = cur
        cur = cur.next
        t.next = None
        newh = self.reverse(h)
        prev.next = newh
        h.next = cur
        
        return sentinel.next
        
    
    def reverse(self, node: ListNode) -> ListNode:
        prev = None
        
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
            
        return prev
        