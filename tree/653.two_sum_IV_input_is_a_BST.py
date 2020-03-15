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
    def findTarget(self, root: TreeNode, target: int) -> bool:
        seen = set()
        
        return self.dfs(root, target, seen)
    
        
    def dfs(self, node: TreeNode, target: int, seen: set) -> bool:
        if not node:
            return False
        
        if node.val in seen:
            return True
        else:
            seen.add(target-node.val)
            
        return self.dfs(node.left, target, seen) or self.dfs(node.right, target, seen)
