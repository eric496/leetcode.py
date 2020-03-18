"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
The binary search tree is guaranteed to have unique values.

Example 1:
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23

Note:
The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        res = [0]
        self.dfs(root, L, R, res)
        
        return res[0]
        
        
    def dfs(self, root: TreeNode, L: int, R: int, res: List[int]) -> None:
        if not root:
            return
        
        if L <= root.val <= R:
            res[0] += root.val
        
        self.dfs(root.left, L, R, res)
        self.dfs(root.right, L, R, res)


# Solution 2: iterative
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        
        stk, res = [root], 0
        
        while stk:
            node = stk.pop()
            
            if L <= node.val <= R:
                res += node.val
                
            if node.val > L and node.left:
                stk.append(node.left)
                
            if node.val < R and node.right:
                stk.append(node.right)
                
        return res
        