"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""

"""
Thought process:
    1. Create two linked lists. Traverse the input linked list, append smaller values to the first linked list, greater or equal values to the second.
    2. Stitch the two linked lists. 
    3. VERY IMPORTANT: terminate the second linked list with a null pointer to avoid loitering (because the new tail node might not be the original tail node.)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Solution 1: O(n) TC; O(n) SC
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head
        
        sentinel1 = cur1 = ListNode(-1)
        sentinel2 = cur2 = ListNode(-1)
        cur = head
        
        while cur:
            if cur.val < x:
                cur1.next = cur
                cur1 = cur1.next
            else:
                cur2.next = cur
                cur2 = cur2.next
            
            cur = cur.next
            
        cur1.next = sentinel2.next
        # Terminate the linked list to avoid loitering
        cur2.next = None
        
        return sentinel1.next
