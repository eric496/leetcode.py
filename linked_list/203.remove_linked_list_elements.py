"""
Remove all elements from a linked list of integers that have value val.

Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

"""
Thought process:
    Loop through the list. If the next node value equals to the target value, skip it. 
    Otherwise, move the walking pointer by one node forward.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution 1
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = walk = ListNode(None)
        sentinel.next = head

        while walk and walk.next:
            if walk.next.val == val:
                walk.next = walk.next.next
            else:
                walk = walk.next

        return sentinel.next


# Solution 2
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = walk = ListNode(None)
        sentinel.next = head

        while walk:
            while walk.next and walk.next.val == val:
                walk.next = walk.next.next

            walk = walk.next

        return sentinel.next


# Solution 3
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = walk = ListNode(None)
        sentinel.next = head

        while walk:
            prev = walk

            while walk.next and walk.next.val == val:
                walk = walk.next

            prev.next = walk.next
            walk = walk.next

        return sentinel.next
