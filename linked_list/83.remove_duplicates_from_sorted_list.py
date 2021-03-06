"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
"""

"""
Thought process:
    1. Compare the current node value with the next node value, skip the next node if their values are equal.
    2. No need to use sentinel, because the head node will never be modified or removed.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        walk = head

        while walk:
            # Skip next node if its value equals to the value of the current node
            while walk.next and walk.val == walk.next.val:
                walk.next = walk.next.next

            walk = walk.next

        return head


# Solution 2
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        walk = head

        while walk:
            if walk.next and walk.val == walk.next.val:
                walk.next = walk.next.next
            else:
                walk = walk.next

        return head
