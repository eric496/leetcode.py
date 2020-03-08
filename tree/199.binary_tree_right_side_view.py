"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: iterative - a variation of level order traversal
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res = []
        q = deque([root])
        
        while q:
            size = len(q)
            
            for i in range(size):
                node = q.popleft()
                
                # Only need to store the last node val of each level
                if i == size-1: 
                    res.append(node.val)    
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
        return res


# Solution 2: recursive
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, 0, res)
        
        return res
        
        
    def dfs(self, node: TreeNode, depth: int, res: List[int]) -> None:
        if not node:
            return
        
        if depth == len(res):
            res.append(node.val)
            
        self.dfs(node.right, depth+1, res)
        self.dfs(node.left, depth+1, res)
