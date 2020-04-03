"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res)

        return res

    def dfs(self, root: TreeNode, res: List[int]) -> None:
        if not root:
            return

        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)


# Solution 2: iterative
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stk, res = [], []

        while stk or root:
            while root:
                stk.append(root)
                root = root.left

            root = stk.pop()
            res.append(root.val)
            root = root.right

        return res


# Solution 2: iterative - a variation
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stk, res = [], []

        while stk or root:
            if root:
                stk.append(root)
                root = root.left
            else:
                root = stk.pop()
                res.append(root.val)
                root = root.right

        return res
