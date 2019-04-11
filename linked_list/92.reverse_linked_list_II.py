"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        sentinel = ListNode(-1)
        sentinel.next = head
        prev = sentinel
        
        for _ in range(m-1):
            prev = prev.next
        
        first, cur = None, prev.next
        
        for _ in range(n-m+1):
            nxt = cur.next
            cur.next = first
            first = cur
            cur = nxt
        
        prev.next.next = cur
        prev.next = first
        
        return sentinel.next
        