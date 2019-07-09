'''
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

'''
Thought process:
    Use three pointers prev, cur, and nxt.
    Explanations: https://www.geeksforgeeks.org/reverse-a-linked-list/
    Draw a graph will help a lot.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Solution 1: Iterative (Explanations: https://www.geeksforgeeks.org/reverse-a-linked-list/)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt
        
        return prev


# Solution 2: Recursive 
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        ptr = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return ptr


# Solution 3: Another iterative approach
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = prev = None

        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
            
        return cur
