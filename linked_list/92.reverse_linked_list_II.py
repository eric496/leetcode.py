"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

"""
Thought process:
    1. Move the prev pointer to the node right before the m-th node.
    2. Reverse the list of length (n-m+1): walk over an example it should be more clear.
    3. Keep track of the prev node before reversion and the tail node after the reversion.
    4. Stitch the forehead + reversed list + tail of the linked list to get the result.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Solution 1
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        sentinel = ListNode(None)
        sentinel.next = head
        prev = sentinel
        
        for _ in range(m-1):
            prev = prev.next
        
        cur = prev.next
        before, after = prev, cur
        
        for _ in range(n-m+1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            
        before.next = prev
        after.next = cur
        
        return sentinel.next


# Solution 2
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
        