"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
Input: [3,2,3,null,3,null,1]
     3
    / \
   2   3
    \   \ 
     3   1
Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: [3,4,5,1,3,null,1]
     3
    / \
   4   5
  / \   \ 
 1   3   1
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# DFS with memoization
class Solution:
    def rob(self, root: TreeNode) -> int:
        return self.dfs(root, {})
        
    def dfs(self, node: TreeNode, memo: dict) -> int:
        if not node:
            return 0
        
        if node in memo:
            return memo[node]
        
        val = 0
        
        if node.left:
            val += self.dfs(node.left.left, memo) + self.dfs(node.left.right, memo)
            
        if node.right:
            val += self.dfs(node.right.left, memo) + self.dfs(node.right.right, memo)
            
        val = max(val+node.val, self.dfs(node.left, memo)+self.dfs(node.right, memo))
        memo[node] = val
        
        return val


# DP solution: TODO
