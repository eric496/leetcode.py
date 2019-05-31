"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""

"""
Thought process:
    1. Create two linked lists. Traverse the input linked list, append smaller values to the first linked list, greater or equal values to the second.
    2. Stitch the two linked lists. 
    3. VERY IMPORTANT: terminate the second linked list with a null pointer to avoid loitering. 
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Solution 1: O(n) TC; O(n) SC
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        first_half_sentinel, second_half_sentinel = ListNode(0), ListNode(0)
        first_walk, second_walk = first_half_sentinel, second_half_sentinel
        
        while head:
            if head.val < x:
                first_walk.next = head
                first_walk = first_walk.next
            else:
                second_walk.next = head
                second_walk = second_walk.next
            head = head.next
        
        first_walk.next = second_half_sentinel.next
        # End the linked list with a null pointer
        second_walk.next = None
        
        return first_half_sentinel.next
