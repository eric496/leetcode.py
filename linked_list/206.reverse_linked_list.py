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
    Draw a graph helps to understand the process.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Solution 1: Iterative (Explanations: https://www.geeksforgeeks.org/reverse-a-linked-list/)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None

        while head:
            nxt = head.next
            head.next = prev
            prev = head 
            head = nxt
        
        return prev


# Solution 2: Recursive 
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head, None)
        
        
    def reverse(self, cur: ListNode, prev: ListNode) -> ListNode:
        if not cur:
            return prev
        
        nxt = cur.next
        cur.next = prev
        
        return self.reverse(nxt, cur)
