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
from collections import deque


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = deque([(root, 0)])
        res = 0

        while q:
            for _ in range(len(q)):
                node, left = q.popleft()

                if left and not node.left and not node.right:
                    res += node.val

                if node.left:
                    q.append((node.left, 1))

                if node.right:
                    q.append((node.right, 0))

        return res
