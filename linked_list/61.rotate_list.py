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
        if not head or not head.next:
            return head
        
        sentinel = walk = ListNode(None)
        sentinel.next = head
        length = 0
        
        while walk and walk.next:
            walk = walk.next
            length += 1
        
        if k % length == 0:
            return head

        walk = sentinel
        offset = length - k%length

        for _ in range(offset):
            walk = walk.next
            
        new_head = walk.next
        walk.next = None
        first_partition_rev = self.reverse(sentinel.next)
        second_partition_rev = self.reverse(new_head)
        sentinel.next.next = second_partition_rev

        return self.reverse(first_partition_rev)
    
    
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
        # Directly return head node if head is null or head is the only node
        if not head or not head.next:
            return head
            
        sentinel = walk = ListNode(None)
        sentinel.next = head
        length = 0
        
        # Count the length of the linked list
        # Start from the dummy head, so count stops at the node previous to the last node
        while walk.next:
            length += 1
            walk = walk.next
        
        # No rotation occurs if k is multiples of the length of the linked list
        if k % length == 0:
            return head

        # Reset the walking pointer to dummyhead for another round of traversal to find the new tail
        walk = sentinel
        # Offset is the steps that needs to traverse to find the new tail
        offset = length - k%length
        
        # Walking pointer is now the new tail
        for _ in range(offset):
            walk = walk.next
    
        # New tail's next node is the new head
        # Initialize a new walking pointer to traverse the remaining nodes
        new_head = new_walk = walk.next
        # Set new tail's next to be null
        walk.next = None
        
        # Traverse the remaining nodes 
        while new_walk.next:
            new_walk = new_walk.next
            
        # Connect the old tail to the old head
        new_walk.next = sentinel.next
        
        return new_head
