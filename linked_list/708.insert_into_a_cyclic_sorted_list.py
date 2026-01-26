"""
Given a node from a cyclic linked list which is sorted in ascending order, write a function to insert a value into the list such that it remains a cyclic sorted list. The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the cyclic list.
If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the cyclic list should remain sorted.
If the list is empty (i.e., given node is null), you should create a new single cyclic list and return the reference to that single node. Otherwise, you should return the original given node.
"""


# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal, head) 
        
        if not head:
            # Point to itself so it is circular
            node.next = node
            return node
        
        cur = head
        
        while cur:
            # Case 1: insert in the middle of the climbing
            if cur.val <= node.val <= cur.next.val:
                break
            
            # Case 2: insert val is either min or max - at the tail of the list
            if cur.val > cur.next.val:
                if node.val >= cur.val or node.val <= cur.next.val:
                    break
            
            # Case 3: all values are flat, insert into either head or tail
            if cur.next is head:
                break
            
            cur = cur.next
        
        node.next = cur.next
        cur.next = node
                
        return head
