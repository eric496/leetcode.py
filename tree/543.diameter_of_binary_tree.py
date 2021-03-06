"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = [0]
        self.dfs(root, res)

        return res[0]

    def dfs(self, root: TreeNode, res: List[int]) -> int:
        if not root:
            return 0

        left = self.dfs(root.left, res)
        right = self.dfs(root.right, res)
        res[0] = max(res[0], left + right)

        return max(left, right) + 1
