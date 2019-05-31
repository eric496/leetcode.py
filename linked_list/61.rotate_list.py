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
        if not head or not head.next or not k:
            return head
        
        sentinel = walk = ListNode(None)
        sentinel.next = head
        len_ = 0
        
        while walk and walk.next:
            walk = walk.next
            len_ += 1
        
        offset = len_ - k%len_
        walk = sentinel
        
        for _ in range(offset):
            walk = walk.next
            
        second_half_head = walk.next
        walk.next = None
        first_half_rev = self.reverse(sentinel.next)
        second_half_rev = self.reverse(second_half_head)
        sentinel.next.next = second_half_rev
        
        return self.reverse(first_half_rev)
    
    
    def reverse(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        return prev


# Solution 2
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # If the length of linked list is 0 or 1 or k == 0, directly return head
        if not head or not head.next or not k:
            return head
            
        sentinel = walk = ListNode(0)
        sentinel.next = head
        # Length of the linked list
        n = 0
        
        # Don't miss walk.next, or it will overcount by 1
        while walk and walk.next:
            walk = walk.next
            n += 1
        
        # The length of the first half
        offset = n - k%n
        
        # The old head is the new head, no need to rotate
        if offset == n:
            return head
        
        walk = sentinel
        
        for _ in range(offset):
            walk = walk.next

        tail = walk 

        # New tail's next node is the new head
        if walk and walk.next:
            walk = walk.next
        
        new_head = walk

        # Set tail node's next to null
        tail.next = None
        
        # Keep going until reaching the last node
        while walk and walk.next:
            walk = walk.next
        
        # The last node's next is the old head 
        walk.next = sentinel.next
        
        return new_head
