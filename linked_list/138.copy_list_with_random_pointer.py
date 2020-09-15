"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.

Example 1:
Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.

Note:
You must return the copy of the given head as a reference to the cloned list.
"""

"""
Thought process:
    Use a hash map and two-pass 
        1. Create copy of node in the first pass, original node as key, copy of node as value
        2. Create next and random pointers for the copy list
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        cp = {}
        cur = head
        
        while cur:
            cp[cur] = Node(cur.val)
            cur = cur.next
            
        cur = head
        
        while cur:
            cp[cur].next = cp.get(cur.next)
            cp[cur].random = cp.get(cur.random)
            cur = cur.next
        
        return cp[head]
