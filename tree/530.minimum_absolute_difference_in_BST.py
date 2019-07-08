"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:
Input:
   1
    \
     3
    /
   2
Output:
1
Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

Note: There are at least two nodes in this BST.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    prev = float('-inf')
    res = float('inf')
    
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return
        
        self.getMinimumDifference(root.left)
        self.res = min(self.res, abs(root.val-self.prev))
        self.prev = root.val
        self.getMinimumDifference(root.right)
        
        return self.res
        