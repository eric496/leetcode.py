"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.

Example:
Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        res = [float('inf')]
        self.dfs(root, target, res)
        
        return res[0]
    
        
    def dfs(self, node: TreeNode, target: float, res: List[int]) -> None:
        if not node:
            return
        
        if abs(node.val-target) < abs(res[0]-target):
            res[0] = node.val
            
        if node.val > target:
            self.dfs(node.left, target, res)
            
        if node.val < target:
            self.dfs(node.right, target, res)


# Solution 2: iterative
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        res = float('inf')

        while root:
            if abs(root.val-target) < abs(res-target):
                res = root.val
            
            if root.val > target:
                root = root.left
            else:
                root = root.right

        return res
