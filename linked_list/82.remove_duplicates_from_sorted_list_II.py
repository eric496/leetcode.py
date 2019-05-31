"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3
"""

"""
Thought process:
    1. Use a pointer to track the previous node of the current node.
    2. Traverse the linked list, there are 2 possible conditions:
            1) The node value is unique, then the inner walking pointer does not move. We just move prev and walk pointers one step forward.
            2) There are duplicate values, and the inner walking pointer will skip all the duplicate values and only keep the first node with duplicate value. 
               In thi case, we need to prev pointer's next to point to walking pointer's next so that the first node with duplicate value will be skpped as well.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        sentinel = walk = ListNode(None)
        sentinel.next = head
        prev = sentinel
        
        while walk:
            # Don't forget to check walk.next
            while walk.next and walk.val == walk.next.val:
                walk = walk.next
            
            if prev.next is walk:
                prev = prev.next
            else:
                prev.next = walk.next
                
            walk = walk.next
        
        return sentinel.next
