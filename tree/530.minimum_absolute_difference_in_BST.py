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


# Solution 1: recursive - inorder traversal
class Solution:
    def __init__(self):
        self.prev = float('-inf')
        self.min_diff = float('inf')
    
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return
        
        self.getMinimumDifference(root.left)
        self.min_diff = min(self.min_diff, abs(root.val-self.prev))
        self.prev = root.val
        self.getMinimumDifference(root.right)
        
        return self.min_diff


# Solution 2: iterative - inorder traversal
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        min_diff = float('inf')
        stk = []
        prev = float('-inf')
        
        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            
            node = stk.pop()
            # Actually no need to use abs() since it is already inorder traversal
            min_diff = min(min_diff, abs(node.val-prev))
            prev = node.val
            root = node.right
            
        return min_diff
        