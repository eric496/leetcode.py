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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution 1: Merge sort
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]
            
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        
        return self.mergeSort(left, right)
        

    def mergeSort(self, ls1: List[ListNode], ls2: List[ListNode]) -> ListNode:
        if None in (ls1, ls2):
            return ls1 or ls2
        
        sentinel = walk = ListNode(None)

        while ls1 and ls2:
            if ls1.val < ls2.val:
                walk.next = ls1
                ls1 = ls1.next
            else:
                walk.next = ls2
                ls2 = ls2.next
            walk = walk.next
        
        walk.next = ls1 or ls2
        
        return sentinel.next


# Solution 2: Heap
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        pq = [(n.val, n) for n in lists if n]
        heapq.heapify(pq)
        sentinel = walk = ListNode(-1)
        
        while pq:
            walk.next = heapq.heappop(pq)[1]
            walk = walk.next
            if walk.next:
                heapq.heappush(pq, (walk.next.val, walk.next))
        
        return sentinel.next
