"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.dfs(root, False)

    def dfs(self, node: TreeNode, is_left: bool) -> int:
        if not node:
            return 0

        if not node.left and not node.right and is_left:
            return node.val

        return self.dfs(node.left, True) + self.dfs(node.right, False)


# Solution 2: iterative
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        stk = [root]
        res = 0

        while stk:
            node = stk.pop()

            if node.left and not node.left.left and not node.left.right:
                res += node.left.val

            if node.left:
                stk.append(node.left)

            if node.right:
                stk.append(node.right)

        return res
