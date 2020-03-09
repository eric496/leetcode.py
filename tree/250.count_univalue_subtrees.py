"""
Given a binary tree, count the number of uni-value subtrees.
A Uni-value subtree means all nodes of the subtree have the same value.

Example :
Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        res = [0]
        self.dfs(root, res)
        
        return res[0]
        
        
    def dfs(self, node: TreeNode, res: List[int]) -> bool:
        if not node:
            return True
        
        left = self.dfs(node.left, res)
        right = self.dfs(node.right, res)
        
        if left and right:
            if node.left and node.val != node.left.val:
                return False
            
            if node.right and node.val != node.right.val:
                return False
            
            res[0] = res[0] + 1
            
            return True
        
        return False
