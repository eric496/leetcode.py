"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

# Solution 1
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if None in (l1, l2):
            return l1 or l2

        rev1, rev2 = self.reverseList(l1), self.reverseList(l2)
        carry = 0
        sentinel = walk = ListNode(None)

        while rev1 or rev2:
            if rev1 and rev2:
                walk.next = ListNode((rev1.val+rev2.val+carry)%10)
                carry = (rev1.val+rev2.val+carry) // 10
                walk, rev1, rev2 = walk.next, rev1.next, rev2.next
            elif rev1:
                walk.next = ListNode((rev1.val+carry)%10)
                carry = (rev1.val+carry) // 10
                walk, rev1 = walk.next, rev1.next
            elif rev2:
                walk.next = ListNode((rev2.val+carry)%10)
                carry = (rev2.val+carry) // 10
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

# Follow up
