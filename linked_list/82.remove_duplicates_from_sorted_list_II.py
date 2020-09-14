"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3
"""

"""
Thought process:
    1. Use a pointer to track the predecessor of the current node.
    2. Traverse the linked list, there are 2 possible conditions for each node:
            1) The node value is unique, then the inner while loop does not execute. We just move prev and walk pointers one step forward.
            2) There are duplicate values, and the inner while loop will skip all the duplicate values and only keep the first node with duplicate value. 
               In this case, we need to prev pointer's next to point to walking pointer's next so that the first node with duplicate value will be skpped as well.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        sentinel = prev = ListNode(None)
        sentinel.next = cur = head

        while cur:
            # Don't forget to check walk.next
            while cur.next and cur.val == cur.next.val:
                cur = cur.next

            # Walking pointer didn't move which means it is a unique node
            # So just move prev pointer to point to this unique node
            if prev.next is cur:
                prev = prev.next
            # Walking pointer actually moved which means there are duplicate nodes
            # Let the prev pointer's next pointer point to walking pointer's next node (skip all duplicates)
            else:
                prev.next = cur.next

            cur = cur.next

        return sentinel.next
