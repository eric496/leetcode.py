"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
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
        fast.next = head
        
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
        prev, cur = None, head
        
        while cur:
            nxt = cur.next
            cur.next= prev
            prev = cur
            cur = nxt
        
        return prev
        