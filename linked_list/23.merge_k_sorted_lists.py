"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

"""
Thought process:
    Divide and Conquer - same as merge sort
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution 1: Merge sort
class Solution(object):
    def mergeKLists(self, lists) -> ListNode:
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.merge(left, right)

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        if not left or not right:
            return left or right

        sentinel = walk = ListNode(-1)

        while left and right:
            if left.val < right.val:
                walk.next = left
                left = left.next
            else:
                walk.next = right
                right = right.next

            walk = walk.next

        walk.next = left or right

        return sentinel.next


# Solution 2: Heap
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        pq = [(n.val, i, n) for i, n in enumerate(lists) if n]
        heapq.heapify(pq)
        sentinel = walk = ListNode(-1)

        while pq:
            _, i, node = heapq.heappop(pq)
            walk.next = node
            walk = walk.next
            
            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))

        return sentinel.next
