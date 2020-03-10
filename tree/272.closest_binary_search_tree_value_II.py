"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

Example:
Input: root = [4,2,5,1,3], target = 3.714286, and k = 2
    4
   / \
  2   5
 / \
1   3
Output: [4,3]

Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: O(n) time complexity - a variation of inorder traversal
from collections import deque

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        res = deque([])
        self.dfs(root, target, k, res)
        
        return res
        
        
    def dfs(self, node: TreeNode, target: float, k: int, res: deque) -> None:
        if not node:
            return
        
        self.dfs(node.left, target, k, res)
        
        if len(res) == k:
            if abs(node.val-target) < abs(res[0]-target):
                res.popleft()
            else:
                return
            
        res.append(node.val)
        self.dfs(node.right, target, k, res)
        