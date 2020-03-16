"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:
Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:
2

Example 2:
Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:
2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution: recursive
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        res = [0]
        self.dfs(root, res)
        
        return res[0]
        
        
    def dfs(self, node: TreeNode, res: List[int]) -> int:
        if not node:
            return 0
        
        left = self.dfs(node.left, res)
        right = self.dfs(node.right, res)
        
        if node.left and node.left.val == node.val:
            left += 1
        else:
            left = 0
            
        if node.right and node.right.val == node.val:
            right += 1
        else:
            right = 0
            
        res[0] = max(res[0], left+right)
        
        return max(left, right)
        