"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Solution 1: three-step reversal
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k < 1:
            return head
        
        cur = head
        n = 0
        
        while cur:
            n += 1
            cur = cur.next
            
        cur = head
        
        for _ in range(n - k%n - 1):
            cur = cur.next
         
        nxt = cur.next
        cur.next = None
        rev1 = self.reverse(head)
        rev2 = self.reverse(nxt)
        head.next = rev2
        
        return self.reverse(cur)
    
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
            
        return prev


# Solution 2
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head

        walk, n = head, 0

        while walk:
            walk = walk.next
            n += 1

        k %= n
        walk = head

        for _ in range(n - k - 1):
            walk = walk.next

        new_head = new_walk = walk.next
        walk.next = None

        while new_walk and new_walk.next:
            new_walk = new_walk.next

        new_walk.next = head

        return new_head
