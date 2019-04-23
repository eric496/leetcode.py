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
        # If the length of linked list is 0 or 1 or k == 0, directly return head
        if not head or not head.next or not k:
            return head
            
        sentinel = ListNode(0)
        sentinel.next = head
        walk = sentinel
        # Length of the linked list
        n = 0
        
        while walk and walk.next:
            walk = walk.next
            n += 1
                    
        offset = n - k%n
        
        # The old head is the new head, no need to rotate
        if offset == n:
            return head
        
        walk = sentinel
        
        while offset:
            walk = walk.next
            offset -= 1
        
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
