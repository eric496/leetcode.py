"""
You need to find the largest value in each row of a binary tree.

Example:
Input: 
          1
         / \
        3   2
       / \   \  
      5   3   9 
Output: [1, 3, 9]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        self.dfs(root, 0, res)

        return res

    def dfs(self, node: TreeNode, depth: int, res: List[int]) -> None:
        if not node:
            return

        if depth == len(res):
            res.append(node.val)
        else:
            res[depth] = max(res[depth], node.val)

        self.dfs(node.left, depth + 1, res)
        self.dfs(node.right, depth + 1, res)


# Solution 2: iterative
from collections import deque


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            level_max = float("-inf")

            for _ in range(len(q)):
                node = q.popleft()
                level_max = max(level_max, node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(level_max)

        return res
