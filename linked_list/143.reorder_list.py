"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

Note: Do not use extra space, modify linked list in place.
"""

"""
Thought process:
    1. Partition the linked list by middle node, reverse the second partition
    2. Swap the nodes iteratively (draw a graph to understand this, walk through an example helps)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return head

        slow = fast = ListNode(None)
        slow.next = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = self.reverse(slow.next)
        walk1 = head
        walk2 = slow.next
        
        while walk1 != slow:
            slow.next = walk2.next
            walk2.next = walk1.next
            walk1.next = walk2
            walk1 = walk2.next
            walk2 = slow.next


    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        
        while head:
            nxt = head.next
            head.next= prev
            prev = head
            head = nxt
        
        return prev
