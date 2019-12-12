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
        
        slow = fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        
        return self.merge(left, right)
    
    def merge(self, left: ListNode, right: ListNode) -> None:
        sentinel = walk = ListNode(-1)
        
        while left and right:
            if left.val < right.val:
                walk.next = left
                left = left.next
            else:
                walk.next = right
                right = right.next
            walk = walk.next
            
        walk.next = left or right
        
        return sentinel.next
