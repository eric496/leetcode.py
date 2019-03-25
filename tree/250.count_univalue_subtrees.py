"""
Given a binary tree, count the number of uni-value subtrees.
A Uni-value subtree means all nodes of the subtree have the same value.

Example :
Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.cnt = 0
        
        def dfs(root: TreeNode, parent_val: int) -> bool:
            if not root:
                return True

            left = dfs(root.left, root.val)
            right = dfs(root.right, root.val)
            
            if left and right:
                self.cnt += 1
                if root.val == parent_val:
                    return True
            return False
        
        if root:
            dfs(root, root.val)
            
        return self.cnt
