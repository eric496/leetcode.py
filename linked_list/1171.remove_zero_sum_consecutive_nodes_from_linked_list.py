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


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = walk = ListNode(0)
        dummy.next = head
        accsum = 0
        order = [accsum]
        seen = {}
        
        while walk:
            accsum += walk.val
            order.append(accsum)
            if accsum not in seen:
                seen[accsum] = walk
            else:
                seen[accsum].next = walk.next
                order.pop()
                while order[-1] != accsum:
                    seen.pop(order.pop())
            walk = walk.next
        
        return dummy.next
        