"""
Sort a linked list using insertion sort.

Algorithm of Insertion Sort:
Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Solution 1: TLE        
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        sentinel = ListNode(None)
        sentinel.next = head
        prev = sentinel
        cur = head
        
        while cur:
            nxt = cur.next
            
            while prev.next and prev.next.val < cur.val:
                prev = prev.next
            
            cur.next = prev.next
            prev.next = cur
            prev = sentinel
            cur = nxt

        return sentinel.next


# Solution 2: TLE           
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        sentinel = ListNode(float('-inf'))
        sentinel.next = head
        cur = sentinel
        
        while cur:
            nxt = cur.next 
            walk = sentinel 
            
            while walk and walk.next:
                if cur is walk.next:
                    break
                elif walk.val < cur.val <= walk.next.val:
                    second = walk.next
                    walk.next = cur 
                    cur.next = second
                    break
                else:
                    walk = walk.next
            
            cur = nxt
            
        return sentinel.next       
        