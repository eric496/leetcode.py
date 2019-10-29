'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

'''
Thought process:
    1. Use a sentinel node to keep track of the head of the result linked list;
       Use a moving pointer to build the result linked list;
       Use a carry variable to store the value carried over from the previous place.
    2. Traverse list nodes in l1 and l2 simultaneously, there are 3 possible cases:
            1) l1 and l2 are of the same length
            2) l1 is longer than l2, we need to traverse the rest of l1 after we traversed the part of the same length
            3) l2 is longer than l1, we need to traverse the rest of l2 after we traversed the part of the same length
    3. Based on the 3 cases above, follow the rules to calculate the digit at each place of the result linked list by:
            1) Sum the current node values of l1 and l2 and the carry value
            2) Take mod of 10 of the sum (using %10) as the current node value of the result linked list
            3) Update carry by taking integer division of the sum (using //10)
    4. Outside the loop at the the end of the program, we need to double check if carry is non-zero. 
       If so, we need to append it to the result linked list.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Solution 1
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = walk = ListNode(None)
        carry = 0
        
        while l1 or l2:
            if l1 and l2:
                sum_ = l1.val + l2.val + carry
                walk.next = ListNode(sum_%10)
                carry = sum_ // 10
                walk, l1, l2 = walk.next, l1.next, l2.next
            elif l1:
                sum_ = l1.val + carry
                walk.next = ListNode(sum_%10)
                carry = sum_ // 10
                walk, l1 = walk.next, l1.next
            elif l2:
                sum_ = l2.val + carry
                walk.next = ListNode(sum_%10)
                carry = sum_ // 10
                walk, l2 = walk.next, l2.next
                
        if carry:
            walk.next = ListNode(carry)
            
        return sentinel.next
                

# Solution 2: 
# The same idea as Solution 1, but more concise. 
# Sequentially add up node values of l1 and l2 if they exist.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = walk = ListNode(None)
        sum_ = 0
        
        while l1 or l2 or sum_:
            if l1:
                sum_ += l1.val
                l1 = l1.next
            
            if l2:
                sum_ += l2.val
                l2 = l2.next
            
            walk.next = ListNode(sum_%10)
            sum_ //= 10
            walk = walk.next
        
        return sentinel.next
