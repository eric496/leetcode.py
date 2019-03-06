'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        
        return True