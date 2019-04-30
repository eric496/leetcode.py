"""
Sort a linked list using insertion sort.

Algorithm of Insertion Sort:
Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        sentinel = ListNode(-1)
        prev = sentinel
        
        while head:
            nxt = head.next
            
            if prev.val >= head.val:
                prev = sentinel
            
            while prev.next and prev.next.val < head.val:
                prev = prev.next
            
            head.next = prev.next
            prev.next = head
            head = nxt
            
        return sentinel.next
        