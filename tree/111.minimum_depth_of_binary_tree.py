'''
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if not root.left:
            return self.minDepth(root.right) + 1
            
        if not root.right:
            return self.minDepth(root.left) + 1
            
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


# Solution 2: iterative
from collections import deque

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        q, res = deque([root]), 0
        
        while q:
            res += 1

            for _ in range(len(q)):
                node = q.popleft()
                # Found a leaf node, return the current depth
                if not node.left and not node.right:
                    return res
                
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return res
        