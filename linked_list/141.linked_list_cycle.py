'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''

'''
Thought process:
    Classic tortoise and hare problem: use two pointers slow and fast. 
    Slow pointer moves one step at each iteration, while fast moves two.
    If there is a cycle, the fast pointer will inevitably surpass the slow when they've both entered the cycle.
    Otherwise the fast will reach the end of the linked list and we should return False.
'''

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
            if slow is fast:
                return True
        
        return False
