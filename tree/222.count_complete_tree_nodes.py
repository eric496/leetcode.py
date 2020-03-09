"""
Given a complete binary tree, count the number of nodes.

Note:
Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:
Input: 
    1
   / \
  2   3
 / \  /
4  5 6
Output: 6
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1


# Solution 1: improved
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left_depth = right_depth = 0
        cur = root
        
        while cur:
            left_depth += 1
            cur = cur.left
            
        cur = root
        
        while cur:
            right_depth += 1
            cur = cur.right
            
        if left_depth == right_depth:
            return 2**left_depth - 1
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1


# Solution 1: Optimized
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left_depth = self.getLeftDepth(root)
        right_depth = self.getRightDepth(root)
        
        if left_depth == right_depth:
            return 2**left_depth - 1
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
    
    
    def getLeftDepth(self, node: TreeNode) -> int:
        depth = 0
        
        while node:
            depth += 1
            node = node.left
            
        return depth
    
    
    def getRightDepth(self, node: TreeNode) -> int:
        depth = 0
        
        while node:
            depth += 1
            node = node.right
            
        return depth


# Solution 2: level order traversal - O(n) solution
from collections import deque

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        res = 0
        q = deque([root])

        while q:
            res += len(q)
            
            for _ in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
        return res


# Solution 2: 