"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
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


# Solution 1: merge sort O(NlogN) TC and O(logN) SC
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
        
        # Cut the list to avoid loitering
        prev.next = None
        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merge(left, right)


    def merge(self, l1: ListNode, l2: ListNode) -> None:
        sentinel = cur = ListNode(None)

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
                
            cur = cur.next

        cur.next = l1 or l2

        return sentinel.next
