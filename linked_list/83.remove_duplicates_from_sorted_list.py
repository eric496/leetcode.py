'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        walk = head
        while walk:
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