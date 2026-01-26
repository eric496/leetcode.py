"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

"""
Thought process:
    Reverse the input lists, add up each place, and reverse the result list.
    Follow up: use 2 stacks to store input list nodes, pop the stacks and add up node values.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Solution 1
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Reverse two linked lists
        rev1, rev2 = self.reverseList(l1), self.reverseList(l2)
        sentinel = walk = ListNode(None)
        carry = 0

        while rev1 or rev2:
            if rev1 and rev2:
                sum_ = rev1.val + rev2.val + carry
                walk.next = ListNode(sum_ % 10)
                carry = sum_ // 10
                walk, rev1, rev2 = walk.next, rev1.next, rev2.next
            elif rev1:
                walk.next = ListNode((rev1.val + carry) % 10)
                carry = (rev1.val + carry) // 10
                walk, rev1 = walk.next, rev1.next
            elif rev2:
                walk.next = ListNode((rev2.val + carry) % 10)
                carry = (rev2.val + carry) // 10
                walk, rev2 = walk.next, rev2.next

        if carry:
            walk.next = ListNode(carry)

        return self.reverseList(sentinel.next)

    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev


# Solution 2: More concise
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rev1, rev2 = self.reverse(l1), self.reverse(l2)
        sentinel = walk = ListNode(None)
        sum_ = 0

        while rev1 or rev2 or sum_:
            if rev1:
                sum_ += rev1.val
                rev1 = rev1.next

            if rev2:
                sum_ += rev2.val
                rev2 = rev2.next

            walk.next = ListNode(sum_ % 10)
            sum_ //= 10
            walk = walk.next

        return self.reverse(sentinel.next)

    def reverse(self, head: ListNode) -> ListNode:
        prev, cur = None, head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev


# Follow up: Use stack
# Solution 1
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2

        s1 = []
        s2 = []

        while l1:
            s1.append(l1.val)
            l1 = l1.next
        
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        head = None
        carry = 0

        while s1 or s2:
            res = 0
            res += s1.pop() if s1 else 0
            res += s2.pop() if s2 else 0
            res += carry
            carry = res // 10     

            node = ListNode(res%10)
            node.next = head
            head = node       

        if carry:
            node = ListNode(carry)
            node.next = head
            head = node

        return head


# Solution 2: More concise
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stk1, stk2 = [], []
        
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
            
        while l2:
            stk2.append(l2.val)
            l2 = l2.next
        
        cur = 0
        head = nxt = None
        
        while stk1 or stk2 or cur:
            cur += stk1.pop() if stk1 else 0
            cur += stk2.pop() if stk2 else 0
            head = ListNode(cur % 10)
            head.next = nxt
            nxt = head
            cur //= 10
            
        return head
