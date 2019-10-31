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

'''
Thought process:
    1. Use a slow and fast pointers to find the middle node of the linked list
    2. Reverse the second half of the linked list 
    3. Compare the node values one by one
    Note: the middle node should be skipped (neither include in the first nor second half of the linked list)
          if the number of nodes is odd.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution 1
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        slow = fast = head 
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        if fast:
            slow = slow.next
            
        new_head = self.reverse(slow)
        
        while head and new_head:
            if head.val != new_head.val:
                return False
            else:
                head = head.next
                new_head = new_head.next
            
        return True
        
        
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
        return prev
        