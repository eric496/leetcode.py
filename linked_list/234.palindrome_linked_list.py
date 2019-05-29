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
    1. Use a slow and fast pointers to find the mid node of the linked list
    2. Reverse the second half of the linked list 
    3. Compare the node values one by one
    Note: the mid node should be skipped (neither include in the first nor second half of the linked list)
          if there is an odd number of nodes.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution 1
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # If there is an odd number of nodes, 
        # then the second half needs to skip the mid node of the list 
        if fast:
            slow = slow.next
        
        second_half = self.reverse(slow)
        
        while head and second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next
        
        return True
        
            
    def reverse(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        return prev
        