"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res)

        return res

    def dfs(self, root: TreeNode, res) -> None:
        if not root:
            return

        self.dfs(root.left, res)
        self.dfs(root.right, res)
        res.append(root.val)


# Solution 2: iterative
from collections import deque

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        stk, res = [], deque()
        
        while stk or root:
            if root:
                stk.append(root)
                res.appendleft(root.val)
                root = root.right
            else:
                root = stk.pop()
                root = root.left
                
        return res
        

# Solution 2: iterative
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        stk = [root]
        res = []
        
        while stk:
            node = stk.pop()
            res.append(node.val)
            
            if node.left:
                stk.append(node.left)
                
            if node.right:
                stk.append(node.right)
                
        return res[::-1]
