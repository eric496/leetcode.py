"""
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.
You may assume the integer do not contain any leading zero, except the number 0 itself.
The digits are stored such that the most significant digit is at the head of the list.

Example :
Input: [1,2,3]
Output: [1,2,4]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Solution 1: Use stack
# O(n) TC; O(n) SC
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        stk1 = []

        while head:
            stk1.append(head.val)
            head = head.next

        carry = 1
        stk2 = []

        while stk1:
            cur_digit = stk1.pop()
            stk2.append((cur_digit + carry) % 10)
            carry = (cur_digit + carry) // 10

        if carry:
            stk2.append(carry)

        sentinel = ListNode(-1)
        walk = sentinel

        while stk2:
            walk.next = ListNode(stk2.pop())
            walk = walk.next

        return sentinel.next


# Solution 2: Linked list reversal
# O(n) TC; O(1) SC
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        rev = self.reverse(head)
        sentinel = walk = ListNode(None)
        carry = 1

        while rev:
            sum_ = carry + rev.val
            walk.next = ListNode(sum_ % 10)
            carry = sum_ // 10
            walk, rev = walk.next, rev.next

        if carry:
            walk.next = ListNode(carry)

        return self.reverse(sentinel.next)

    def reverse(self, head: ListNode) -> ListNode:
        prev, cur = None, head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev


# Solution 3: Check if the last digit is 9
# O(n) TC; O(1) SC
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        sentinel = ListNode(None)
        sentinel.next = head
        last_not_nine = sentinel
        walk = head

        while walk:
            if walk.val != 9:
                last_not_nine = walk
            walk = walk.next

        last_not_nine.val += 1
        walk = last_not_nine.next

        while walk:
            walk.val = 0
            walk = walk.next

        return sentinel if sentinel.val == 1 else sentinel.next
