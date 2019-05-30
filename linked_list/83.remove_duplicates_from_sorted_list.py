'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
'''

'''
Thought process:
    1. Compare the current node value with the next node value, skip the next node if their values are equal.
    2. No need to use sentinel, because the head node will never be changed.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        walk = head

        while walk:
            # Check if walk.next is null because walk.next.next is used in the while
            while walk.next and walk.val == walk.next.val:
                walk.next = walk.next.next
            
            walk = walk.next
        
        return head


# Solution 2
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        walk = head
        
        while walk and walk.next:
            if walk.val == walk.next.val:
                walk.next = walk.next.next
            else:
                walk = walk.next
        
        return head
