"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        sentinel = ListNode(None)
        sentinel.next = head
        prev = sentinel
        walk = head

        while walk:
            while walk.next and walk.val == walk.next.val:
                walk = walk.next

            if prev.next == walk:
                prev = prev.next
            else:
                prev.next = walk.next

            walk = walk.next

        return sentinel.next

