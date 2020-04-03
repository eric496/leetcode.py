"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

"""
Thought process:
    Classic tortoise and hare problem: use two pointers a slow and a fast. 
        The slow pointer moves one step at each iteration, while the fast moves two.
        There are two conditions: 
            1) The fast pointer meets the slow pointer -> there is a cycle
            2) The fast pointer reaches the end of the linked list before meeting the slow pointer -> there is no cycle
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # slow and fast both point at the head node, so compare equality after they move.
            if slow is fast:
                return True

        return False
