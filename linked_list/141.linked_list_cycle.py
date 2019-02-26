'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# two pointers
# tortoise and hare
class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            if slow is fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

# more concise
class Solution(object):
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

