"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.

Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:
Input: head = [0]
Output: 0

Example 3:
Input: head = [1]
Output: 1

Example 4:
Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880

Example 5:
Input: head = [0,0]
Output: 0
 
Constraints:
The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution 1: reverse the linked list and add up bit by bit
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        head = self.reverse(head)
        res = power = 0
        
        while head:
            res += head.val * 2**power
            head = head.next
            power += 1
        
        return res
        
        
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
        return prev
    

# Solution 2: no need to reverse the linked list, add up bit by bit
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        
        while head:
            res = res*2 + head.val
            head = head.next
        
        return res


# Solution 3: bit manipulation
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        
        while head:
            res <<= 1
            res |= head.val
            head = head.next
            
        return res
