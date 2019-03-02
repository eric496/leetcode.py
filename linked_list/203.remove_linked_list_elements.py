'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        
        sentinel = pt = ListNode(-1)
        pt.next = head
        while pt and pt.next:
            if pt.next.val == val:
                pt.next = pt.next.next
            else:
                pt = pt.next
                
        return sentinel.next