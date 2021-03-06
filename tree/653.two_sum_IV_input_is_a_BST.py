"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9
Output: True
 

Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28
Output: False
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1:
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        target = set()

        return self.dfs(root, k, target)

    def dfs(self, root: TreeNode, k: int, target: int) -> bool:
        if not root:
            return False

        if root.val in target:
            return True
        else:
            target.add(k - root.val)

        return self.dfs(root.left, k, target) or self.dfs(root.right, k, target)
