"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(n) TC and O(n) SC
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before, after = ListNode(0), ListNode(0)
        walk_before, walk_after = before, after
        walk = head
        
        while walk:
            if walk.val < x:
                walk_before.next = walk
                walk_before = walk_before.next
            else:
                walk_after.next = walk
                walk_after = walk_after.next
            walk = walk.next
        
        walk_before.next = after.next
        walk_after.next = None
        
        return before.next

# In-place solution

