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
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k:
            return head
        
        sentinel = ListNode(0)
        sentinel.next = head
        walk = sentinel
        n = 0
        
        while walk and walk.next:
            walk = walk.next
            n += 1
                    
        offset = n - k%n
        
        if offset == n:
            return head
        
        walk = sentinel
        
        while offset:
            walk = walk.next
            offset -= 1
        
        tail = walk 

        if walk and walk.next:
            walk = walk.next
        
        tail.next = None
        new_head = walk
        
        while walk and walk.next:
            walk = walk.next
        
        walk.next = sentinel.next
        
        return new_head
