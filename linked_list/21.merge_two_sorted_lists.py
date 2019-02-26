'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

'''
Thought:
    Use a sentinel node to track the head of the new linked list. Use a runner to append new nodes to the linked list.
    Loop through two linked lists and append the smaller value of the current two nodes. 
    Append what is left in the longer linked list (suppose two linked list have different length) to the new linked list after the loop.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Pythonic way to check the empty linked lists
        if None in (l1, l2):
            return l1 or l2
        cur = sentinel = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        # This is pythonic! 
        cur.next = l1 or l2
        return sentinel.next
