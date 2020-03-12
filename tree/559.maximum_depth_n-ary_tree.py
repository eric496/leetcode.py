"""
Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note:
The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


# Solution 1: iterative
from collections import deque

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        q, depth = deque([root]), 0
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                
                for child in node.children:
                    q.append(child)
                
            depth += 1
            
        return depth

