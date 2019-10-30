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
    Use a hash map: 
        1. Loop through the list, use nodes as keys, corresponding values are new nodes with same value but null pointers for next and random.
        2. At second iteration, copy next and random pointers.
"""

# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

 
class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return head
        
        cp = {}
        walk = head
        
        while walk:
            cp[walk] = Node(walk.val, None, None)
            walk = walk.next
        
        walk = head
        
        while walk:
            cp[walk].next = cp.get(walk.next)
            cp[walk].random = cp.get(walk.random)
            walk = walk.next
        
        return cp[head]
