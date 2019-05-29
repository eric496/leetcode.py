"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

"""
Thought process:
    Merge sort 
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        prev, slow, fast = None, head, head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        
        return self.merge(l1, l2)
    
    
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:        
        sentinel = walk = ListNode(None)
        
        while l1 and l2:
            if l1.val < l2.val:
                walk.next = l1
                l1 = l1.next
            else:
                walk.next = l2
                l2 = l2.next
                  
        walk.next = l1 or l2
        
        return sentinel.next
