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
    def insert(self, head: 'Node', val: int) -> 'Node':
        insert_node = Node(val, head)
        
        if not head:
            # Given an empty list, the inserted node's next pointer should point to itself
            insert_node.next = insert_node
            return insert_node
        
        cur = head
        
        while 1:
            if cur.val <= val <= cur.next.val:
                break
            elif cur.val>cur.next.val and (val>=cur.val or val<=cur.next.val):
                break
            elif cur.next is head:
                break        
            cur = cur.next
            
        insert_node.next = cur.next
        cur.next = insert_node
        
        return head
