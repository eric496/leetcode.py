"""
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
After doing so, return the head of the final linked list.  You may return any such answer.
(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.

Example 2:
Input: head = [1,2,3,-3,4]
Output: [1,2,4]

Example 3:
Input: head = [1,2,3,-3,-2]
Output: [1]

Constraints:
The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution 1: two passes
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head
        seen = {0: sentinel}
        cumsum = 0

        while head:
            cumsum += head.val
            seen[cumsum] = head
            head = head.next

        head = sentinel
        cumsum = 0

        while head:
            cumsum += head.val

            if cumsum in seen:
                head.next = seen[cumsum].next

            head = head.next

        return sentinel.next


# Solution 2: one pass
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        sentinel = cur = ListNode(0)
        sentinel.next = head
        cumsum = 0
        cumsums = [0]
        seen = {}

        while cur:
            cumsum += cur.val
            cumsums.append(cumsum)

            if cumsum not in seen:
                seen[cumsum] = cur
            else:
                seen[cumsum].next = cur.next
                cumsums.pop()

                while cumsums[-1] != cumsum:
                    seen.pop(cumsums.pop())
                    
            cur = cur.next

        return sentinel.next
