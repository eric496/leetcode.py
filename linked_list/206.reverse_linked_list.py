'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Recursive 
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        ptr = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return ptr

# Iterative 1
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return cur

# Iterative 2: https://www.geeksforgeeks.org/reverse-a-linked-list/
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt
        return prev


