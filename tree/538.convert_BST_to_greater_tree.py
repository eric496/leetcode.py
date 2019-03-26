"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:
Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.dfs(root, 0)
        return root
        
    def dfs(self, root: TreeNode, val: int) -> int:
        if not root:
            return val
        
        val = self.dfs(root.right, val)
        root.val += val
        
        return self.dfs(root.left, root.val)
