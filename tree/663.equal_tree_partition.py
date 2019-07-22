"""
Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees which have the equal sum of values after removing exactly one edge on the original tree.

Example 1:
Input:     
    5
   / \
  10 10
    /  \
   2   3
Output: True
Explanation: 
    5
   / 
  10
Sum: 15
   10
  /  \
 2    3
Sum: 15

Example 2:
Input:     
    1
   / \
  2  10
    /  \
   2   20
Output: False
Explanation: You can't split the tree into two trees with equal sum after removing exactly one edge on the tree.

Note:
The range of tree node value is in the range of [-100000, 100000].
1 <= n <= 10000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:    
    
    def checkEqualTree(self, root):
        
        def dfs(root):
            if not root:
                return 0
            sums.append(root.val + dfs(root.left) + dfs(root.right))
            return sums[-1]
        
        sums = []
        dfs(root)
        
        return sums.pop() / 2 in sums
        